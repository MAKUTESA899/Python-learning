print("if you want to exit press 'q'")
while True:
    filename='guest.txt'
    with open(filename, 'w') as file_object:
        file_object = input("why do you like programing; ")
        if file_object== 'q':
            break

print(file_object)