import random

num_players = int(input("How many players?"))
letter_guess= [0] * num_players #array to store player score
word_guess= [0] * num_players #array to store num of word guesses
words_bank= ["computer", "python", "chocolate", "code", "snake"]

secret_word = random.choice(words_bank)
#print(secret_word) # just for testing 
guessed = False
# optional: player_status = [False] * num_players
turn = 1
previous_guesses = [] # list to store all previous guesses
# while there is at least one False value in player_status
while guessed == False: # tab for getting it all in for loop
    for player in range(num_players):
        if word_guess[player] < 3:
            print(f"\nPlayer{player + 1}, Turn {turn}:")
            print("Previous guesses:", previous_guesses) #stores previous guesses
            player_letter_guess = input("What is your letter guess?")
            letter_count= secret_word.count(player_letter_guess)
            print(f"The letter {player_letter_guess} occurs {letter_count} times")
            letter_guess[player] =  letter_guess[player] + 1 # players, guessing letter

            previous_guesses.append(player_letter_guess) #each time a player makes a guess, it's added to the list
        

            choice = input("Would you like to guess the word? y/n")
            if choice == 'y':
                word_guess[player] =  word_guess[player] + 1
                player_guess = input("What is your guess?")
                if player_guess == secret_word:
                    print("You guessed the right word!")
                    guessed = True
                    # player_status[player] = True
                    break
                else:
                    print("You did not guess the correct word")
        
    turn += 1

winner = word_guess.index(min(word_guess)) #announces winner (the player with the least amount of tries to guess word), need to fix it to state winner with the least amount of tries and correct guess
print(f"\nPlayer {winner + 1} is the winner!")

for player in range(num_players):
    print(f"\nPlayer{player + 1}, letter guess: {letter_guess[player]}, word guess: { word_guess[player]} ") #states players letter guess and word guess

   

    