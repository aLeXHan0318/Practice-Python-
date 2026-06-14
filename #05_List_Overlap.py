#State: A list that contains numbers that are contained in both list a & b
#Input: There is no user input, because input lists are provided from the practice website
#Rule: Return list contains only the elements are common between the lists
#Stop: Program stops when return list is printed out on terminal

def main() :
    list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    list_common = differentiate(list_a, list_b)
    print(list_common)

def differentiate(list_1, list_2) :
    return [number for number in set(list_1) if number in set(list_2)] 
main()
