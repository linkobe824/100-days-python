def main():
    operations = {
        '+':  add,
        '-': substract,
        '*': mult,
        '/': div
    }
    
    def calculator():
        num1 = float(input("What's the first number?: "))
        
        while True:
            for key in operations:
                print(key)
            op = input("Pick operation: ")
            num2 = float(input("What's the next number?: "))
            
            operation =  operations[op]
            result = operation(num1, num2)
            print(f"{num1} {op} {num2} = {result}")

            next_calculation = input(f"Type 'y' to continue with {result} or type 'n' to start new calculation: ")
            
            if next_calculation == 'y':
                num1 =  result
            else:
                calculator()
            
    calculator()
        
def add(x, y):
    """Return the addition of x and y"""
    return x + y

def substract(x,y):
    return x - y

def mult(x,y):
    return x * y

def div(x,y):
    return round(x/y, 5)
    
main()