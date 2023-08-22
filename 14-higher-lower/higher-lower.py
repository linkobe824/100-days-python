from data import data
from art import logo, vs
import random
import os

def main():   
    score = 0
    
    character_a = get_random_character()
    character_b = get_random_character()
    
    while True:
        print(logo)
        
        if score > 0:
            print(f"Correct, Score: {score}")
            
        print(f"Compare A: {character_a['name']}, a {character_a['description']}, from {character_a['country']}.")
        print(vs)
        print(f"Against B: {character_b['name']}, a {character_b['description']}, from {character_b['country']}.")
        
        answer = input("Who has more followers? Type 'A' or 'B': ")
        
        if answer == 'A' and character_a['follower_count'] > character_b['follower_count']:
            character_b = get_random_character()
        elif answer == 'B' and character_b['follower_count'] > character_a['follower_count']:
            character_a = character_b
            character_b = get_random_character()
        else:
            os.system('clear')
            print(f"Sorry, it's wrong. Score: {score}")
            break

        score += 1
        os.system('clear')
            
    
def get_random_character():
    """Return a random character object from the data array"""
    size = len(data)
    return data[random.randint(0, size - 1)]
    
if __name__ == '__main__':
    main()