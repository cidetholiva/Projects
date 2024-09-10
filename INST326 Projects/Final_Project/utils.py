import re

def validate_input(user_input):
    pattern = r"^\d+$"  # regex for positive integers
    if re.match(pattern, user_input):
        return True
    else:
        print("Invalid input. Please enter a positive number.")
        return False
