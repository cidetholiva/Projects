import random

def correct_word(secret_word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '-' for letter in secret_word) # hidden hypens _ for word

def hangman_game():
    words_bank = ["computer", "python", "chocolate", "code", "snake"]
    secret_word = random.choice(words_bank).lower()  # chooses a random word and converts to lowercase
    guessed_letters = []
    strikes = 0
    max_strikes = 5
    
    print("Welcome to Hangman!")
    print(f"The word has {len(secret_word)} letters.")
    
    while strikes < max_strikes and not all(letter in guessed_letters for letter in secret_word): #runs loop until player runs out of strikes
        print("\n" +  correct_word(secret_word, guessed_letters))
        print(f"Letter guesses: {' '.join(guessed_letters)}")
        print(f"Strikes: {strikes}/{max_strikes}")
        
        guess = input("Enter a letter or type 'quit' to exit: ").lower()
        
        if guess == 'quit': #exits game if player types quit
            print(f"The word was: {secret_word}")
            print("Quitting the game...Thanks for playing!")
            return
        
        if len(guess) != 1 or not guess.isalpha(): #checks if input is one single letter / alphabetical
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess not in secret_word:
            strikes += 1
            print("Incorrect guess!")
    
    if all(letter in guessed_letters for letter in secret_word):
        print("\n" + correct_word(secret_word, guessed_letters))
        print("Congratulations! You guessed the word!")
    else:
        print(f"\nSorry, you've run out of strikes! The word was: {secret_word}")

hangman_game()
