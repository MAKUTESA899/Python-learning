def read(filename):
    try:
        with open(filename) as f:
            contents= f.read()
            print(contents)
    except FileNotFoundError:
        pass
    else:
        print("thank you!")
      
filenames = ['cat.txt', 'dog.txt', 'cow.txt']

for filename in filenames:
    read(filename)