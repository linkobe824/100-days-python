def main():
    operations = {
        '+':  add,
        '-': substract,
        '*': mult,
        '/': div
    }
    

            
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