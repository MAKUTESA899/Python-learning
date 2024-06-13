
try:
     num1 = input("Enter the first number: ")
     num2 = input("Enter the second number: ")
     sum = int(num1) + int(num2)
     print (f"{num1} + {num2} = {sum}")
except ValueError: 
    print("Kindly enter a number")
else:
    print("thanks")
    
