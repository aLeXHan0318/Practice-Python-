"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 
100 years old. Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year). 
"""

#State: A message stating the year when the user will turn 100 years old.
#Input: The program receives a user’s name and age.
#Rule: Age must be a valid integer between 0 and 120 (inclusive). Name must not be empty or consist only of spaces. If any condition is not met, the input is considered invalid.
#Stop: Program stops when message comes out 

def main() :
    current_year = 2026 
    usr_name = input("Enter your name: ")
    usr_age = int(input("Enter your age"))
    usr_future_age = calculation(usr_age, current_year)
    print(f"Year {usr_future_age} you will be 100 years old")

def calculation(usr_age, current_year) :
    years_left = current_year - usr_age + 100
    return years_left


main() 
