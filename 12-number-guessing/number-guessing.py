import random
import os

def main():
    print("Welcome to the Number Guessing Game!")
    
    while True:
        
        print("I'm thinking of a number between 1 and 100.")
        number = random.randint(1,100)
        dificulty = input("Choose a dificulty. Type 'easy' or 'hard': ")
        
        if dificulty == 'hard':
            attempts = 5
        else:
            attempts = 10
            
        while attempts > 0:
            print(f"You have {attempts} atempts reaming to guess the number.")
            attempts -= 1
            guess = int(input("Make a guess: "))
            
            if guess > number:
                os.system('clear')
                print(f"Too High - Guess again - Last Guess: {guess}")
            elif guess < number:
                os.system('clear')
                print(f"Too Low - Guess again - Last Guess: {guess}")
            else:
                print("Correct!!")
                break
            
        if attempts == 0:
            print(f"The number was: {number}")
        
        if input("Type 'y' to play again: ") != 'y':
            break
        else:
            os.system('clear')

main()