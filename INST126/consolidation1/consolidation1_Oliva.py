import random 
#int for intergers
num_players = int(input("How many Players?")) #declares scores for players, no specific amount of players
player_scores = [0] * num_players #score starts at zero
dice = (1, 2, 3, 4, 5, 6)

for turn in range(4):  # four turns each player
    for player in range(num_players):
        #player_roll1 = random.choice(dice)
        #player_roll2 = random.choice(dice)
        #player_roll3 = random.choice(dice)
        #easier way- assign a variable to rolls and have it roll 3 times randomly
        print(f"\nPlayer {player + 1}, Turn {turn + 1}:") #states current player and turn num
        rolls = [random.choice(dice) for _ in range(3)]  # rolls 3 dice for player, using _ as a placeholder
        #rolls= [3,3,3], check to see if tuple works
        print("Dice:", rolls) 

        while True: #while statement, checks to see if rolls have tupled out or been fixed and continues to loop until break
            #if player_roll1 == player_roll2 and player_roll1 == player_roll3<--too complicated, using len and set makes it easier to detect if tupled 
            if len(set(rolls)) == 1:  # tupled out, set converts rolls list into a set that removes duplicate nums so when a duplicate occurs 3 times, it tupled. the 1 indicates that there's only one unique num
                print(f"You have tupled out! Your score for turn {turn + 1} is {player_scores[player]}")
                break
            else:
                #player_roll1 == player_roll2 or player_roll1 == player_roll3 or player_roll2 == player_roll3, basically what rolls in rolls if rolls means. if two rolls equal the same number, it's fixed
                fixed_dice = [roll for roll in rolls if rolls.count(roll) == 2] #if two nums are same, it goes under fixed die
                if fixed_dice:  # fixed dice (2 same num)
                    fixed_numbers = ", ".join(str(num) for num in fixed_dice) #showing fixed nums
                    print("Your dice are fixed! Fixed numbers:", fixed_numbers)
                else:
                    print("Your dice are not fixed or tupled, keep going!") #if dice aren't fixed or tupled, can continue as normal

                choice = input("Enter 'r' to re-roll or 's' to Stop: ") #giving player choice to stop game or reroll

                if choice.lower() == 's': #if statement, lower converts string to lowercase
                    total_score = sum(rolls) - sum(fixed_dice) #anytime player rolls a fixed die, it is subtracted from score
                    print(f"{player_scores[player]} scored {total_score} points this turn.")
                    player_scores[player] += total_score
                    break
                elif choice.lower() == 'r': #if player doesn't choose s, then r rerolls 
                    roll_to_reroll = random.randint(0, 2)  # randomly choose a die to re-roll, starts at 0 so 0,1,2, means 3 dice
                    rolls[roll_to_reroll] = random.choice(dice)
                    print("Dice after re-roll:", rolls)
                else:
                    print("Invalid choice. Please enter 'r' or 's'.") #if player inputs something other than r or s, invalid appears


final_score = max(player_scores) #finds highest score among all players  
winners = [i + 1 for i in range(len(player_scores)) if player_scores[i] == final_score] #checks if scores of players match to highest score determining who won
if len(winners) == 1:
    print(f"\nPlayer {winners[0]} wins with a score of {final_score}!")
else: #if there are multiple winners aka a tie, then this checks who has the same highest score (winners)
    winners_str = "" #empty string to store tied players
    for winner in winners:
        winners_str += str(winner) + ", " #
    winners_str = winners_str[:-2]  # removes the comma and space since loop adds extra comma/space
    print(f"\nPlayers {winners_str} tie with a score of {final_score}!")
