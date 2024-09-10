import random
from matplotlib import pyplot as plt

num_players = int(input("How many players? "))
letter_guess = [0] * num_players  # array to store player score
word_guess = [0] * num_players  # array to store num of word guesses
correct_guesses = [False] * num_players  # array to track if a player has guessed the word correctly
words_bank = ["computer", "python", "chocolate", "code", "snake"]

secret_word = random.choice(words_bank)
#print(secret_word)  # just for testing
guessed = False
turn = 1
previous_guesses = []  # list to store all previous guesses

while not guessed:
    for player in range(num_players):
        if word_guess[player] < 3:
            print(f"\nPlayer {player + 1}, Turn {turn}:")
            print("Previous guesses:", previous_guesses)  # stores previous guesses
            player_letter_guess = input("What is your letter guess? ")
            letter_count = secret_word.count(player_letter_guess)
            print(f"The letter {player_letter_guess} occurs {letter_count} times")
            letter_guess[player] += 1  # players, guessing letter

            previous_guesses.append(player_letter_guess)  # each time a player makes a guess, it's added to the list

            choice = input("Would you like to guess the word? y/n ")
            if choice == 'y':
                word_guess[player] += 1
                player_guess = input("What is your guess? ")
                if player_guess == secret_word:
                    print("You guessed the right word!")
                    correct_guesses[player] = True
                    guessed = True
                    break
                else:
                    print("You did not guess the correct word")
        
    turn += 1

# initializes min_word_guesses with a value larger than the maximum possible word_guess value
max_possible_guesses = 3
min_word_guesses = max_possible_guesses + 1
winner = -1
for i in range(num_players):
    if correct_guesses[i] and word_guess[i] < min_word_guesses:
        min_word_guesses = word_guess[i]
        winner = i

if winner != -1:
    print(f"\nPlayer {winner + 1} is the winner!")
else:
    print("\nNo player guessed the word correctly.")

for player in range(num_players):
    print(f"\nPlayer {player + 1}, letter guess: {letter_guess[player]}, word guess: {word_guess[player]}")  # states players letter guess and word guess

x_axis = list(range(1, num_players + 1))  #matplotlib to show bar graph of how many letter guesses each player took
my_graph = plt.bar(x_axis, letter_guess)
plt.xlabel("Player")
plt.ylabel("Letter Guesses")
plt.xticks(x_axis)
plt.yticks(range(0, max(letter_guess) + 1))
plt.show()