Cideth Oliva Consolidation 1: "Tuple Out" Dice Game
=====================================================

Thought process/ Instructions: 
------------------------------

For the tuple game,  as stated in the directions for this project: the game may have one or more players. 
To implement this rule, I didn’t put a minimum or maximum number of players. To do that, I would've done 
if num_players > 4:  print("Max number of players allowed is 4."). I wanted this game to be played with
however many players the player wanted. The second rule for the game is how to win and to win the game, the 
player with the most points wins. However, for each turn, the active player rolls three dice: if all three dice 
are rolled with the same number, the player has “tupled out.” To implement this, I first had to think about 
how tupling out works. Basically, if roll1=roll2, roll2=roll3 and all die numbers are the same, then the player 
has tupled out and their turn ends with zero points. (For example, rolling three “4”s at the same time means 
zero points for that turn). On the other hand, the player may continue playing and increase their score if they 
haven’t tupled out. If two dice have the same value, they are “fixed”, and they cannot be re-rolled.The player 
can re-roll any dice that are not “fixed”, as often as they would like, until they decide to stop, or until they 
“tuple out” (get three of the same number). To implement this, I used a while statement and gave the player a 
choice to continue or stop. The risk with continuing is that they may tuple out and in addition to that, whenever they
get a fixed number, it is subtracted from their score so that only the die that was unique is added. When all players 
have finished their four turns, the total score appears and the winner is declared. I couldn't figure out how to keep the game 
playing if only one player tuples out because if I change the rolls to equal 3,3,3 for example, it would make ALL rolls equal that num.
Tupling is rare though, so everything else works and at the end, the player with the highest score is displayed. 

---------------------------------------------------------------------

How to play step by step:
==========================
1. Begin by running import random, num_players = int(input("How many Players?")). STOP HERE!
2. When prompted, "How many players," enter the number of players. Then press enter, and begin running the next line
(including the for loop) until it states player 1, turn 1: and dice numbers. 
3. After receiving die numbers, it will tell you whether you got fixed die, tupled, or neither. If die are fixed, it will 
also state which numbers were fixed.
4. Then, it prompts whethere player 1 would like to keep rerolling (type "r") or stop (type "s"). The player can keep rerolling for however
long they'd like but there's always the chance of being tupled out and anytime they get fixed numbers, it subtracts them.
In addition, I haven't figured out how to keep other players playing if one player tuples out. So if tuple, it is likely that the 
whole game exits. 
5. After player decides to type "s" for stop, the next player goes and so on until four rounds are played (4 turns in total).
6. Scores are calculated after each turn but to find out who won, run the line that starts with final_score = max(player_scores) and continue running each line
until it states player blank wins with a score of blank, or if tied it will state which player tied and their score. 

MIT License
============
In folder, "consolidation_projects," attached is MIT License. Here it is again, just in case. 

Copyright <2024> <Cideth Oliva>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.