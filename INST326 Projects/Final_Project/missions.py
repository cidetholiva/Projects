import random
from utils import validate_input 

class Mission:
    def __init__(self, name, reward, spaceship):
        self.name = name
        self.reward = reward
        self.spaceship = spaceship  

    def complete(self):
        raise NotImplementedError("Subclasses should implement this!")

class NumberGuessingMission(Mission): #Cosmic Codebreaker
    def complete(self):
        print(f"You went on a mission and found a treasure chest! Guess a number between 1 and 10 to open it. There's {self.reward} points inside!")
        correct_number = random.randint(1, 10)
        attempts = 3

        while attempts > 0:
            guess = input(f"Enter your guess (Attempts left: {attempts}): ")
            if validate_input(guess):
                guess = int(guess)
                if guess == correct_number:
                    print(f"Congratulations! You guessed the correct number {correct_number}. You win {self.reward} points!")
                    self.spaceship.adjust_points(self.reward)
                    return
                else:
                    attempts -= 1
                    print("Wrong guess.")
        
        print(f"Out of attempts! The correct number was {correct_number}. Points deducted.")
        self.spaceship.adjust_points(-self.reward)

class RockPaperScissorsMission(Mission): #Celestial Clash
    def complete(self):
        print(f"You encountered a Celestial! Play Rock, Paper, Scissors to win {self.reward} points!")
        choices = ["rock", "paper", "scissors"]
        attempts = 3

        while attempts > 0:
            user_choice = input(f"Enter rock, paper, or scissors (Attempts left: {attempts}): ").strip().lower()
            computer_choice = random.choice(choices)
            if user_choice in choices:
                if user_choice == computer_choice:
                    print(f"It's a tie! The Celestial also chose {computer_choice}.")
                elif (user_choice == "rock" and computer_choice == "scissors") or \
                     (user_choice == "paper" and computer_choice == "rock") or \
                     (user_choice == "scissors" and computer_choice == "paper"):
                    print(f"You win! The Celestial chose {computer_choice}. You win {self.reward} points!")
                    self.spaceship.adjust_points(self.reward)
                    return
                else:
                    print(f"You lose! The Celestial chose {computer_choice}.")
                attempts -= 1
            else:
                print("Invalid choice. Please enter rock, paper, or scissors.")
        
        print(f"Out of attempts! Points deducted.")
        self.spaceship.adjust_points(-self.reward)

class AnimalGuessingMission(Mission): #Space Safari
    def complete(self):
        animals = {
            "cat": "It has whiskers.",
            "dog": "It barks!",
            "cheetah": "It's the fastest land animal.",
            "mouse": "It squeaks!"
        }
        correct_animal = random.choice(list(animals.keys()))
        hint = animals[correct_animal]

        print(f" Woah, there's wild animals loose in space. Guess the animal name to win their bounty. Hint: {hint}")
        attempts = 3

        while attempts > 0:
            guess = input(f"Enter your guess (Attempts left: {attempts}): ").strip().lower()
            if guess == correct_animal:
                print(f"Congratulations! You guessed the correct animal {correct_animal}. You win {self.reward} points!")
                self.spaceship.adjust_points(self.reward)
                return
            else:
                attempts -= 1
                print("Wrong guess.")
        
        print(f"Out of attempts! The correct animal was {correct_animal}. Points deducted.")
        self.spaceship.adjust_points(-self.reward)

class WordScrambleMission(Mission): #Stellar Scramble
    def complete(self):
        word = "planet"
        scrambled_word = ''.join(random.sample(word, len(word)))
        print(f" You came across a hidden message! Unscramble the word to win {self.reward} points! Scrambled word: {scrambled_word}")
        
        attempts = 3
        while attempts > 0:
            guess = input("Enter your guess: ").strip().lower()
            if guess == word:
                print(f"Congratulations! You unscrambled the word correctly. You win {self.reward} points!")
                self.spaceship.adjust_points(self.reward)
                return
            else:
                attempts -= 1
                print(f"Wrong guess. Attempts left: {attempts}")
        
        print(f"Out of attempts! The correct word was {word}. Points deducted.")
        self.spaceship.adjust_points(-self.reward)
