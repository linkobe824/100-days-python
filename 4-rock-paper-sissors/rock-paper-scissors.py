import random

def main():
    options = ["Rock", "Paper", "Scissors"]
    #validate input
    while True:
        choice = int(input("Whad do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
        if choice < 0 or choice > 2:
            print("Invalid input, try again.")
        else:
            break
    
    computer_choice = random.randint(0, 2)
    print(f"You choose {options[choice]}")
    print(f"Computer chose {options[computer_choice]}")
    
    
    if (choice == 0 and computer_choice == 1) or (choice == 1 and computer_choice == 2) or (choice == 2 and computer_choice == 0):
        print("You Lose")
    elif choice == computer_choice:
        print("Draw")
    else:
        print("You Win")
    
    
main()