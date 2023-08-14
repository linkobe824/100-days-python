def main():
    print("Welcome to the tip calculator.")
    bill = float(input("What was the total bill? $")) #124.54
    split = int(input("How many people to split the bill? ")) #5
    percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? ")) #12
    tip = (bill / split) + ((bill/split)*(percentage/100))
    print(f"Each person should pay: ${round(tip,1)}") 
   
main()

