Cideth Oliva Consolidation 2: Word Guessing Game
=====================================================

Thought process/ Instructions: 
------------------------------

For this word game,  as stated in the directions for this project: the game may have one or more players. 
To implement this rule, I didn’t put a minimum or maximum number of players. To do that, I would've done 
if num_players > 4:  print("Max number of players allowed is 4."). I wanted this game to be played with
however many players the player wanted. The object of the game is to guess a secret word from a bank of words
while players take turns. On each turn, the player gets to guess a possible letter that might be the word.
After guessing a letter, the program tells the player how many occurrences of that letter are in the secret 
word. As the directions state, the game DOES NOT tell the player the position of letters in the word but it does keep 
count of the previous guesses inputted. On the same turn, the player can also try to guess the word. The program
will give them a prompt asking if they'd like to guess the word and the player inputs a yes (y) or no (n). If they say yes
but guess incorrectly, a statement will show up saying "You did not guess the correct word" and continue with the other 
player's turn. However, if they guess correctly, the game will be over and winner will be stated. A player's final 
score is the number of turns (letter guesses) they made before guessing the correct word, so lower score are better. I couldn't
exactly figure out how to make the program state the winner with minimum amount of guesses AND the correct word but when the 
player guesses the right word, it states "You guesses the right word!" underneath. Each player only has three word guesses, 
and they lose the game if they get their third guess wrong.
---------------------------------------------------------------------

How to play step by step:
==========================
1. Begin by running import random, num_players = int(input("How many Players?")). STOP HERE!
2. When prompted, "How many players," enter the number of players. Then press enter, and begin running the next line
(including the for loop) until it states player 1, turn 1: , previous guesses [], and what is your letter guess? [].
3. After guessing a letter, it will tell you how many times that letter occurs in the word and if you'd like to guess the word.
You can either input a y for yes or an n for no. 
4. If you say yes to guessing the word but it's incorrect, it will tell you it's not the correct word and move on to the next player's
turn. If you state no, it will move on to the next player's turn.
5. As the game goes on, the program will continue storing the previous letter guesses and you may continue guessing letters until 
you have enough correct letter occurrences to guess the word. However, you only 3 word guesses and if you incorrect on the third 
guess, the game is over. 
6. Whichever player guesses the word correctly wins. Ideally, the player with the least amount of guesses and the correct word guess wins but 
I couldn't figure out how to display that yet. It'll state the winner as the player with the least amount of guesses only.  
7. After winner is stated, run the line that starts with winner = word_guess.index(min(word_guess)) until it states winner (althought it may be incorrect),
and the players amount of letter guesses and word guesses will also be stated.  


MIT License
============

Copyright <2024> <Cideth Oliva>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.