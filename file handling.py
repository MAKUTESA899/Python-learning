with open ('pitext') as file_object:
    contects =file_object.read()
    print(contects)

find_path='pitext'
with open(find_path) as file_object:
    content=file_object.read()
    print(content)

filename='pitext'

with open(filename) as file_object:
    for line in file_object:
        print(line)

filename='pitext'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
filename='pitext'
with open(filename) as file_object:
    line = file_object.readline()

pi_string='i love math'
for line in line:
    pi_string+=line.rstrip()

print(pi_string)
print(len(pi_string))

filename='pitext'
with open(filename) as file_object:
    line= file_object.readline()
    pi_string+=line.strip()
    print(pi_string)
    print(len(pi_string))



filename='pitext'
with open(filename) as file_object:
    line= file_object.readline()
    pi_string+=line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
 print("Your birthday appears in the first million digits of pi!")
else:
 print("Your birthday does not appear in the first million digits of pi.")