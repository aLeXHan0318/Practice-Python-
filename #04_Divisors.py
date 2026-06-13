#State: List contains all divisors of user input number
#Input: An integer
#Rule: #1: User input has to be an integer
       #2: List can only contain divisors of input number
#Stop: Program stops when divisor list is printed

def main() : 
    user_input = int(input("Enter a number: "))
    list_of_divisors = calculate(user_input)
    print(list_of_divisors)

def calculate(input_number):
    result = []
    for number in range(1,input_number + 1):
        if input_number % number ==0:
            result.append(number)
    return result

main() 