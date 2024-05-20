def add(a,c):
    return a+c
def subtract(a,c):
    return a-c
def multiply(a,c):
    return a*c
def divide(a,c):
    return a/c



def calculator():
    while True:
        print("welcome to my calculator")
        print("1. add")
        print("2. subtract")
        print("3. multiply")
        print("4. divide")
        print("5 exit")

        choice = int(input("your choice"))
        if choice ==5:
            print("thank you")
            break
        print("input you value")
        a = int(input("a ;"))
        c = int(input("b ;"))

        if choice in [1, 2, 3, 4, 5]:
            if choice ==1:
                print(f"the sum of {a} and {c} is {add(a,c)}")
            elif choice ==2:
                print(f"the difference of {a} and {c} is {subtract(a,c)}")
            elif choice ==3:
                print(f"the product of {a} and {c} is {multiply(a,c)}")
            else:
                print(f"the division of {a} and {c} is {divide(a,c)}")
        else:
            print("choose a number that exist in the list")
        continue
calculator()       
        



        

