
filename='guest.txt'


while True:
    name = input("what is your name: ")
    print('To exit the program enter q')
    if name == 'q':
        break
    with open(filename, 'a') as file_object:
        file_object.write(f"{name}\n")
        print(f'Hello {name}')