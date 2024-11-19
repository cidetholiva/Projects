# practice with string and string methods

"This is a string"

'This is also a string'

"This isn't a bad idea"

#'This is a bad idea, isn't it'
# when using isn't, it mistakes ' for the string, so just use double quotes

'She told me, "go there"'
# "She told me, "go there""" <--this is bad 

"She told me, \"don't go there\"."
# the backslash tells python that it's just a regular quote, it's not special 

report= "She told me, \"don't go there\"."
print(report)
#this is how it'll print: She told me, "don't go there".

print("Here's\na string\nwith some\nline returns\n\n")
print("\u2660")

##########################################
#find and index 
"here's a short sentence".count(" ") #this counts how many spaces there are 
example_sentence="here's a short sentence"
example_sentence.count(" ")
example_sentence.find(" ")

"here's a short sentence".count("s")
example_sentence="here's a short sentence"
example_sentence.count("s")
example_sentence.find("s")
print(example_sentence[5])
example_sentence.find("s",6) #look for the next s 

#index works the same as find, except find gives you neg and index gives you error

example_sentence.find("z")
example_sentence.index("s",6)
example_sentence.index("z")

# grab surrounding text
search_word = "spam"

with open("spam_song.txt") as fc:
    spam_song = fc.read()

type(spam_song)
len(spam_song)

spam_song.find(search_word)
print(spam_song[400:404])
print(spam_song[380:424])

position = 0
spam_positions = []
while position < len(spam_song):
    found_spam = spam_song.find(search_word, position) # when finding, put big first (so text), then what you're trying to search for
    if found_spam == -1:
        break
    print(spam_song[(found_spam-10):(found_spam+14)])
    spam_positions.append(found_spam) #take the list ur adding to
    position = found_spam + 1
print(spam_positions)
len(spam_positions)

spam_song.count("spam")

#############################
#starting 4/25 lecture with endswith and startswith

import os
files_here= os.listdir
print(files_here)
#type(files_here)
#type(files_here[0])

"file.txt".endswith(".txt")
"README.md".endswith(".txt")

for file in files_here:
   print(f"let's check to see if {file} is a TXT file")
   if file.endswith(".txt"):
       print(f"Here's the first 100 bytes of the file {file}")
       with open(file) as file_connection:
           print(file_connection.read(100)) #endswith is handy for files, looking through files

waitress_lines = []
with open("spam_song.txt", "r") as file_connection: #open file
    for line in file_connection: #looping through the file
        if line.startswith("Waitress"):
            waitress_lines.append(line)
print(waitress_lines)

print("\n".join(waitress_lines)) #the \n is the glue, then join is putting it into a seperate string, then u add what you want joined

example_csv_line= ["name", "email", "gpa", "year"]
print(example_csv_line[0]+ "," +
      example_csv_line[1]+ "," +
      example_csv_line[2]+ "," +
      example_csv_line[3]) #this is too long to do, there's an easier way
print(",".join(example_csv_line)) #this is the easier way, using join

print(",".join([str(1), str(2), str(3), str(4)])) #join will only work with strings 
print(",".join([1,2,3,4])) #this won't work because it only works with strings

#removes

my_courses = ["INST126", "INST314", "462", "STAT100"]
"INST126".removeprefix("INST")
"126".removeprefix("INST")

course_numbers = []
for course in my_courses:
    course_number = course.removeprefix("INST")
    course_numbers.append(course_number)
print(course_numbers)    

#remove suffix works the same way, for the end of the string 
print("filename.txt".removesuffix(".txt"))

#############################

#replace() examples

"spam song, spam spam ".replace("spam", "Treet")
"spam song, spam spam".replace("spam", "Treet", 2)

with open("spam_song.txt") as fc:
    spam_text = fc.read()

treet_text = spam_text.replace("spam", "Treet")
print(treet_text)   