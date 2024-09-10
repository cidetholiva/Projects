from spaceship import Spaceship
from missions import NumberGuessingMission, RockPaperScissorsMission, AnimalGuessingMission, WordScrambleMission
from utils import validate_input

def main(): #used list to store different missions & conditional statements
    spaceship = Spaceship(fuel=300, supplies={})
    missions = [
        NumberGuessingMission(name="Cosmic Codebreaker", reward=1000, spaceship=spaceship),
        RockPaperScissorsMission(name="Celestial Clash", reward=500, spaceship=spaceship),
        AnimalGuessingMission(name="Space Safari", reward=800, spaceship=spaceship),
        WordScrambleMission(name="Stellar Scramble", reward=600, spaceship=spaceship)
    ]

    print("Welcome to the Space Exploration Adventure Game!")
    
    while True:
        if spaceship._all_planets_won():
            print("Congratulations! You have successfully helped all three planets and completed your mission!")
            break

        print(f"\nCurrent Fuel: {spaceship.fuel}, Points: {spaceship.points}")
        command = input("Enter a command (travel, refuel, buy supplies, missions, quit): ").strip().lower()
        if command == "travel":
            distance = input("Enter distance to travel (50-800 million kilometers): ")
            if validate_input(distance):
                spaceship.travel(int(distance))
        elif command == "refuel":
            amount = input("Enter amount to refuel: ")
            if validate_input(amount):
                spaceship.refuel(int(amount))
        elif command == "buy supplies":
            item = input("Enter item to buy (e.g., water, food, transportation, repairs, technology): ").strip().lower()
            amount = input(f"Enter amount of {item} to buy: ")
            if validate_input(amount):
                spaceship.buy_supplies(item, int(amount))
        elif command == "missions":
            for i, mission in enumerate(missions):
                print(f"{i + 1}. {mission.name} - Reward: {mission.reward} points")
            
            mission_choice = input("Choose a mission by number: ")
            if validate_input(mission_choice):
                mission_index = int(mission_choice) - 1
                if 0 <= mission_index < len(missions):
                    mission = missions[mission_index]
                    print(f"Starting mission: {mission.name}")
                    mission.complete()
                else:
                    print("Invalid mission number. Please choose a valid number.")
        elif command == "quit":
            print("Thank you for playing the Space Exploration Adventure Game!")
            break
        else:
            print("Invalid command. Please enter 'travel', 'refuel', 'buy supplies', 'missions', or 'quit'.")

if __name__ == "__main__":
    main()
