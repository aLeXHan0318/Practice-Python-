#State: The boolean value indicating whether the input string is palindrome or not
#Input: A string entered by user
#Rule: #1: User input must be a string
       #2: Output has to be a boolean value
#Stop: Program ends when a boolean value is displayed

def main() :
    user_input = input("Enter a word: ")
    validity = is_palindrome(user_input)
    print(validity)

def is_palindrome(word) :
    return word == word[::-1]
main() 