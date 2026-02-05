# day03_mini_CLI_calculator

def get_operation():
    while True:
        
        operand = input("Please choose the operation(+, -, *, /): ").strip()
        if operand not in ["+", "-", "*", "/"]: 
            print("Please enter a correct operation")
            continue
        
        return operand


def main():

    print("------------------------------\nHello there! Welcome to CLI Calculator tool that offer basic operations.\n------------------------------\n")
    get_operation()


        


while True:
    
    
    
    break

if __name__ == "__main__":
    main()