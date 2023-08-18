# guarda nombre y oferta
# loop pidiendo nombre y oferta hasta que dicen que no hay mas
# arroja el nombre de la persona con la oferta de mayor valor
import os
def main():
    print("Welcome to the secret auction program.")
    
    name_bid = {}
    
    while True:
        while True:
            name = input("What is your name?: ")
            if name not in name_bid:
                bid = int(input("What is your bid?: $"))
                name_bid[name] = bid
                break
            else:
                print("Name already taken, please provide other name.")
        
        another = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        if another == 'no':
            os.system('clear')
            break
        os.system('clear')
    
    max_val_name = max(name_bid, key=name_bid.get)
    print(f"The winner is {max_val_name} with a bid of ${name_bid[max_val_name]}.")


main()