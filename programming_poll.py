filename = 'poll.txt'
while True:
    responses = []
    print('To exit the program enter q')
    answer = input("Why do you like programming: ")
    if answer == 'q':
        for response in responses:
            print(response)
        break
    with open(filename, 'a') as file_object:
        responses.append(answer)
        file_object.write(f"{answer}\n")
