
import random

words = ["Adjective 1" , "Noun 1", "Past Tense Verb 1 ", "Adverb 1", "Adjective 2", "Noun 2", "Noun 3", "Adjective 3", "Past Tense Verb 2", "Adverb 2", " Past Tense Verb 3", "Adjective 4"]
final_words = []
for word in words: # for loop to prompt user for 3 diff words (adj., noun, verb, adverb) and picks random from input
    choice1= input(f"Please enter {word}: ")
    choice2= input(f"Please enter {word}: ")
    choice3= input(f"Please enter {word}: ")
    choices = [choice1, choice2, choice1]
    final_choice = random.choice(choices)
    final_words.append(final_choice)

madlib = f"""
Today I went to Inst126. I saw a(n) {final_words[0]} {final_words[1]} sitting down and taking notes. 
Dr. Jackson {final_words[2]} {final_words[3]} to the computer that showed the {final_words[4]} {final_words[5]}. 
I worked on my assignment with my {final_words[6]} sitting next to me. Working so long made me hungry so I went to Stamp 
to get a {final_words[7]} scoop of ice cream. I got full so afterwards I {final_words[8]} {final_words[9]} 
to catch my bus. When I got home I {final_words[10]} after a {final_words[11]} day at school.
"""

print(madlib.strip())