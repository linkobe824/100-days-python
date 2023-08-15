def main():
    print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
    val = input("You're at a corss road. Where do you want to go? Type 'left' or 'right' ")
    if val == "left":
        val = input("You found yourself infront of a lake. Type 'wait' or 'swim' ")
        if val == "wait":
            val = input("Which door?. Type 'red', 'yellow' or 'blue' ")
            if val == "yellow":
                print("You win")
            else:
                print("You lose.")
        else:
            print("You lose.")
    else:
        print("You lose.")

main()