class Spaceship:
    def __init__(self, fuel, supplies):
        self.fuel = fuel
        self.supplies = supplies
        self.points = 0
        self.won_planets = set()

    def travel(self, distance):
        if distance < 50 or distance > 800:
            print("Invalid distance. Please choose a distance between 50 and 800 million kilometers.")
            return

        if 50 <= distance <= 100:
            destination = "Mars"
            fuel_required = 120
            supplies_needed = {"water": 100, "food": 150}
            story = "You traveled to Mars! The Queen of Mars needs water and food to feed her kingdom."
        elif 101 <= distance <= 400:
            destination = "Jupiter"
            fuel_required = 200
            supplies_needed = {"transportation": 250}
            story = "You traveled to Jupiter! A young man needs transportation to save his kidnapped family."
        elif 401 <= distance <= 800:
            destination = "Venus"
            fuel_required = 300
            supplies_needed = {"repairs": 300, "technology": 200}
            story = "You traveled to Venus. An asteroid has hit their planet, and they need repairs and technology to rebuild."

        if self.fuel < fuel_required:
            print(f"Not enough fuel to travel to {destination}. Fuel required: {fuel_required}.")
            return

        self.fuel -= fuel_required
        print(f"Traveled {distance} million kilometers to {destination}. Fuel left: {self.fuel}")
        print(story)
        
        self._help_planet(destination, supplies_needed)
        
    def _help_planet(self, planet, supplies_needed):
        while True:
            action = input(f"Do you want to help {planet}? You need {supplies_needed}. (yes/no): ").strip().lower()
            if action == "yes":
                if self._has_required_supplies(supplies_needed):
                    self._deduct_supplies(supplies_needed)
                    print(f"Helped {planet} successfully! Supplies left: {self.supplies}")
                    self._win_planet(planet)
                    if self._all_planets_won():
                        print("Congratulations! You have successfully helped all three planets and completed your mission!")
                        return
                    break
                else:
                    print(f"Not enough supplies to help {planet}. Go on missions to earn points and buy supplies.")
                    break
            elif action == "no":
                print(f"Decided not to help {planet}. You can choose to go on missions to earn points.")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
    
    def _has_required_supplies(self, supplies_needed):
        return all(self.supplies.get(item, 0) >= amount for item, amount in supplies_needed.items())
    
    def _deduct_supplies(self, supplies_needed):
        for item, amount in supplies_needed.items():
            self.supplies[item] -= amount

    def _win_planet(self, planet):
        if planet not in self.won_planets:
            self.won_planets.add(planet)
            self.adjust_points(100)
            print(f"You have won {planet} and earned 100 points!")

    def _all_planets_won(self):
        return len(self.won_planets) == 3

    def refuel(self, amount):
        if self.points < amount:
            print(f"Not enough points to refuel {amount} units. You have {self.points} points.")
            return
        self.fuel += amount
        self.points -= amount
        print(f"Refueled {amount} units. Fuel now: {self.fuel}. Points now: {self.points}")

    def buy_supplies(self, item, amount):
        cost = amount
        if self.points < cost:
            print(f"Not enough points to buy {amount} units of {item}. You have {self.points} points.")
            return
        self.supplies[item] = self.supplies.get(item, 0) + amount
        self.points -= cost
        print(f"Bought {amount} units of {item}. Supplies now: {self.supplies[item]}. Points now: {self.points}")

    def adjust_points(self, amount):
        self.points += amount
        print(f"Points adjusted by {amount}. Total points: {self.points}")
