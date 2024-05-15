#sum
print("this is my calculator")
choice = int(input("to exsit press 0 to continue press 1 \n choose your option: "))
while choice >= 1:
    operation = int(input("1.addition \n2.subtraction \n3.divison \n4.multiplication\n0 exist\noperation ="))
    if (operation ==1):
       a = int(input("a ;"))
       b = int(input("b ;"))
       result = a + b
       print(f"the sum of {a} and {b} is {result}")
    elif (operation ==2):
        a = int(input("a ;"))
        b = int(input("b ;"))
        result = a - b
        print(f"the subtraction of {a} and {b} is {result}")
    elif (operation ==3):
        a = int(input("a ;"))
        b = int(input("b ;"))
        result = a / b
        print(f"the division of {a} and {b} is {result}")
    elif (operation ==2):
        a = int(input("a ;"))
        b = int(input("b ;"))
        result = a * b
        print(f"the division of {a} and {b} is {result}") 
    elif operation ==0:
        choice =0
        print ("HAVE A NICE DAY") 
    else:
        print("the insert does not exist") 