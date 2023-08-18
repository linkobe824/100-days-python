import random

def main():
    stages = ['''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========
''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========
''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========
''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /    |
        |
        |
    =========
''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========
''', '''
    +---+
    |   |
        |
        |
        |
        |
    =========
''']
    words = ["ardvark", "baboon", "camel"]
    chosen_word = randomWord(words)
    
    display = ["_" for i in range(len(chosen_word))]
    print(" ".join(display))
    
    guesses = 6
    
    
    
    while '_' in display and guesses > 0:
        print(stages[guesses])
        guess = input("Choose a letter: ").lower()
        guessed_state = False
        for i, c in enumerate(chosen_word):
            if guess == c:
                display[i] = guess
                guessed_state = True
        if not guessed_state:
            guesses -= 1
            
        print(" ".join(display))
    
    if '_' not in display:
        print("You Win")
    else:
        print(stages[guesses])
        print("You Lose")
        
def randomWord(list: list) -> str:
    return list[random.randint(0, len(list)-1)]
    
    
main()