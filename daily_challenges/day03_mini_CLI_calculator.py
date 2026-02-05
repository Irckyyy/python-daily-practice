# day03_mini_CLI_calculator
import math
from functools import reduce
import operator

def get_operation():
    while True:
        
        operand = input("Please choose the operation(+, -, *, /): ").strip()
        if operand not in ["+", "-", "*", "/"]: 
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
        except ValueError: 
            print("Invalid input. Please enter a valid number.") 
    return numbers
    
def compute(operand, numbers):
    if operand == "+":
        result = sum(numbers)
    elif operand == "-":
        result = reduce(operator.sub, numbers)  
    elif operand == "*":
        result = math.prod(numbers)
    elif operand == "/":
        try:
            result = reduce(operator.truediv, numbers)
        except ZeroDivisionError:
            return "Error: Cannot divide by zero. Please try again."


    if isinstance(result, (int, float)) and result.is_integer():
        return int(result)
    return result

def choice():
    
    while True:
        again = input("Do you want to try again? (y/n): ").lower().strip()
        if again == "y":
            return True
        elif again == "n":
            return False
        else:
            print("Please enter a valid answer (Y/N)")
            continue
    

def main():

    print("------------------------------\nHello there! Welcome to CLI Calculator tool that offers basic operations.\n------------------------------\n")
    
    while True:
        operand = get_operation()
        numbers = get_numbers_until_equals()
        if operand in ["+", "*"] and len(numbers) >= 1:
            result = compute(operand, numbers)
        elif operand in ["-", "/"] and len(numbers) >= 2:
            result = compute(operand, numbers)
        else:
            print("Not enough numbers for this operation! Try again.")
            continue
    
        clean_numbers = [int(n) if n.is_integer() else n for n in numbers]
        print(f"\nNumbers: {clean_numbers}")
        print(f"Operation: '{operand}'")
        print(f"Result: {result}\n\n")
    
        again = choice()
        if not again:
            print("Thank you for using the program!")
            break        
    

if __name__ == "__main__":
    main()