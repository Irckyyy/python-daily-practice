# day03_mini_CLI_calculator

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
    
    print(numbers)

def main():

    print("------------------------------\nHello there! Welcome to CLI Calculator tool that offer basic operations.\n------------------------------\n")
    get_operation()
    get_numbers_until_equals()
    


        


while True:
    
    
    
    break

if __name__ == "__main__":
    main()