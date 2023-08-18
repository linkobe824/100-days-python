alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
            'q','r','s','t','u','v','w','x','y','z']

def main():
    while True:
        choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if choice == 'encode':
            encode()
        elif choice == 'decode':
            decode()
        else:
            print("Wrong instruction.")
        
        followUp = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
        
        if followUp == 'no':
            break
        

def encode():
    msg = input("Type your message:\n")
    key = int(input("Type the shift number:\n"))
    size = len(alphabet)
    encoded = ""
    for c in msg:
        index = alphabet.index(c)
        encoded_index = (index + key)%size
        encoded += alphabet[encoded_index]
    print(f"Here's the encoded result: {encoded}")
    
def decode():
    msg = input("Type your message:\n")
    key = int(input("Type the shift number:\n"))
    size = len(alphabet)
    decoded = ""
    for c in msg:
        index = alphabet.index(c)
        decoded_index = (index - key)%size
        decoded += alphabet[decoded_index]
    print(f"Here's the decoded result: {decoded}")

        
main()

