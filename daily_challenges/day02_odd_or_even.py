# daily_challenges/day02_odd_or_even.py
# Day 2 —  Even / odd number checker

print("---------------\nHello there! Welcome to a short tool that recognizes whether a number is Odd or Even. \n ---------------\n---------------\n RULES:\n 1.) Please only type a positive number.\n 2. Do not put negative numbers or decimals.\n 3. Have fun in this basic tool! 😊\n\n ")

while True:
    
    number = input("Please pick a number: ")
    
    if not (number.isdigit()):
        print("Characters, negative numbers, and irrational numbers are not allowed. Please pick a number. ")
        continue

    num_int = int(number)
    
    if num_int == 0:
        print("Zero is not allowed. Please pick again.")
        continue
        
    if num_int % 2 == 0:
        print(f"The number is Even. This is because {num_int} is divisible by 2.\n")
    
    else:
        remainder = num_int % 2
        print(f"The number is Odd. This is because {num_int} divided by 2 has a remainder of {remainder}.\n")

    while True:
        
        again = input("Do you want to test again? (Yes/No): ").strip().lower()
        
        if again == "yes":
            break
            
        elif again == "no":
            print("Thank you so much for using the program! 😊 \nNote that this program is bound for future upgrades! Maybe adding a GUI through Tkinter 😉\nExiting....\n.....\n....")
            exit()
        else:
            print("Please enter Yes to continue or No to terminate the program.")
            continue
        
    

