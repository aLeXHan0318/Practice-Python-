#state: Boolean value of user input value
#Input: An integer user enterd
#Rule: If number doesn't match, tell user wether the input value is lower or higher than the right value
#Stop: Program ends when user inputes the correct number

import random

def main() :
    correct_number = random.randint(1,9)
    times = 1
    while True :
        user_input = int(input("Enter an integer: "))
        result = compare(user_input, correct_number)
        times += 1
        print(f"Your guess is {result}. You've tried {times} times.")
        if result == "Correct" :
            user = input("Do you want to play again? (exit / continue) ")
            if user == "continue" :
                times = 1
                correct_number = random.randint(1,9)
                continue
            else:
                print("Thanks for playing!")
                break

def compare(input_number, system_number) :
    if input_number > system_number :
        return "Too High"
    elif input_number < system_number :
        return "Too Low"
    else:
        return "Correct"

main() 