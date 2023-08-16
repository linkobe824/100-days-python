import random

def main():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q',
               'r','s','t','u','v','w','x','y','z', 'A','B','C','D','E','F','G',
               'H','I','J','K','L','M','N','Ñ','O','P','Q','R','T','S','U','V',
               'W','X','Y','Z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','#','$','%','&','(',')','*','+']
    
    characters = [letters, numbers, symbols]
    
    print("Welcome to the PyPassword Generator!")
    size_letters = int(input("How many letters would you like in your password\n"))
    size_symbols = int(input("How many symbols would you like?\n"))
    size_numbers = int(input("How many numbers would you like?\n"))
    
    total_char = size_letters + size_symbols + size_numbers
    # se agrega un contador al final de cada lista para tener una referencia
    # de cuantas restan por usar
    letters.append(size_letters)
    numbers.append(size_numbers)
    symbols.append(size_symbols)
    
    password = ''
    
    for c in range(total_char):
        i = 0
        while True:
            i = random.randint(0,2)
            if characters[i][-1] > 0:
                characters[i][-1] -= 1
                break
        #se resta dos al final para no incluir tampoco el restante anexado
        password += characters[i][random.randint(0, len(characters[i])-2)]
    
    print(f"Here is your password: {password}")
    
    # se pueden utilizar 3 loops separados para crear un password lista de 
    # las letras, numeros y simbolos aleatorios pero en orden 
    # por ejemplo 3letras 2numerso y 2 simbolos: aFc53&$
    # entonces, utilizamos random.shuffle en la lista para mezclar los elementos
    
main()

