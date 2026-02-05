# day03_mini_CLI_calculator
import math
from functools import reduce
import operator

def get_operation():
    while True:
        
        operand = input("Please choose the operation(+, -, *, /, =): ").strip()
        if operand not in ["+", "-", "*", "/", "="]: 
            print("Please enter a correct operation.")
            continue
        
        return operand

def get_numbers_until_equals():
        
    numbers = []
    while True:
        val = input("Enter an element (or press Enter to finish): ")
        if val == "":
            break  
        try: 
            num = float(val)  
            numbers.append(num)
        except ValueError: print("Invalid input. Please enter a valid integer.") 
        continue
    return numbers
    
def compute(operand, numbers):
    if operand == "+":
        result = sum(numbers)
    elif operand == "-":
        result = reduce(operator.sub, numbers)  
    elif operand == "*":
        result = math.prod(numbers)

    if result == int(result): 
        result = int(result)
        return result
    else:
        return result

def main():

    print("------------------------------\nHello there! Welcome to CLI Calculator tool that offer basic operations.\n------------------------------\n")
    operand = get_operation()
    numbers = get_numbers_until_equals()
    result = compute(operand, numbers)
    print(result)
    

if __name__ == "__main__":
    main()