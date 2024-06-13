print("welcome to division world")
print("to quit press 'q' ")

while True:
    first_number=input("first ;")
    if first_number=='q':
        break
    second_number=input("second ;")
    
    if second_number=='q':
        break
    try:
        answer = int(first_number) / int (second_number)
    except ZeroDivisionError:
        print("you can divide  a number with a zero")

    else:
         print(answer)

filename='main.py'
with open(filename) as file_object:
    try:
        x=(filename)
    except FileNotFoundError:
        pass
    else:
        print(x)