# program for counting words in a file

import os
# the current directory returns the current working directory as a string and assigns it to a variable
current_directory = os.getcwd()
print("Current directory:", current_directory)

print("Files and folders in my current directory:")
for item in os.listdir(): # returns a list of all the files and directories in my current directory
    print(item)


def main(): #function 
    search_file = input("Enter the file name: ") #this prompts user to enter file name and word
    enter_word = input("Enter word to count: ")
    
    file = open(search_file, 'r') #this opens the file that you searched for and reads it
    words= file.read().lower() 
    number = words.count(enter_word.lower()) # the "lower" makes sure that case doesn't matter because it'll make it all lower case
    print(f"The word '{enter_word}' appears {number} times in the file.")
    file.close()

if __name__ == "__main__": # if condition is true, it will run main
    main()


   