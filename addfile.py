filename='pitext'
with open(filename, 'w') as file_object:
    file_object.write("i love math")

print(file_object)

filename='pitext'
with open(filename, 'a') as file_object:
    file_object.write("i love history \n i love english\n but kiswahili is the best")

print(file_object)