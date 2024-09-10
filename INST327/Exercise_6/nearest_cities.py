""" Find cities near a specified location. """


from argparse import ArgumentParser
import sys

from haversine import haversine


class Cities:
    """
    A class to manage city data and find the nearest cities based on a given point.
    
    Attributes:
    cities (dict): A dictionary where keys are tuples of area and city names, and values are tuples of latitude and longitude.
    """
    
    def __init__(self, filename):
        """
        Initializes the Cities object with data from a specified file.
        
        Args:
        filename (str): The path to the file that has city data. Each line should have: area, city, latitude, longitude.
        """
        self.cities = {}
        with open(filename, 'r') as file: #read contents of file 
            for line in file:
                data = line.strip().split(',')
                if len(data) == 4: #checks area, city, lat, long
                    area, city, latitude, longitude = map(str.strip, data)
                    self.cities[(area, city)] = (float(latitude), float(longitude))
    
    def nearest(self, point):
        """
        Finds the nearest cities to a specified point using the Haversine distance formula.
        
        Args:
        point (tuple): A tuple that has latitude and longitude (float values).
        
        Returns:
        list: A list of tuples representing the nearest cities based on the given point.
        """
        # sorting cities by distance from the given point
        sorted_cities = sorted(self.cities.keys(), key=lambda x: haversine(point, self.cities[x]))
        nearest_cities = sorted_cities[:5]# returning the first five closest cities
        return nearest_cities


def main(filename, arg1, arg2):
    """ Read city data from a file and find the closest cities to a
    specified location (either an area and city from filename or a
    latitude and longitude which may or may not be in the file).
    
    Args:
        filename (str): path to a file containing city data. Each line
            in the file should consist of four values, separated by
            commas: area (e.g., state or country), city, latitude in
            decimal degrees, longitude in decimal degrees.
        arg1 (str): either the name of an area in the file, or a string
            representation of a latitude.
        arg2 (str): either the name of a city in the file, or a string
            representation of a longitude.
    
    Side effects:
        Writes to stdout.
    """
    cities = Cities(filename)
    try:
        lat = float(arg1)
        lon = float(arg2)
        point = (lat, lon)
    except ValueError:
        try:
            point = cities.cities[arg1, arg2]
        except KeyError:
            sys.exit(f"Error: could not look up {arg1}, {arg2}")
    print(f"For {arg1}, {arg2}, the nearest cities from the file are")
    for result in cities.nearest(point):
        print("    " + ", ".join(result))


def parse_args(arglist):
    """ Process command-line arguments and return the parsed values as a
    namespace. """
    parser = ArgumentParser()
    parser.add_argument("filename", help="file containing city data")
    parser.add_argument("arg1",
                        help="a latitude expressed in decimal degrees"
                             " or an area (state, country) from the"
                             " file")
    parser.add_argument("arg2",
                        help="a longitude expressed in decimal degrees"
                             " or a city name from the file")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename, args.arg1, args.arg2)
