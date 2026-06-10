#State: message addressed to user that tells them When they will turn 100 years old 
#Input: User's age & name 
#Rule: User's input must qualify 
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
