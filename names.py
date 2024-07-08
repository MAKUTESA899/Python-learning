from name_function import get_formatted_name
print("enter 'q' at ant time to quit.")
while True:
    first = input("\n please give me a first name: ")
    if first == 'q':
        break
    last = input("please give me last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first,last)
    print(f"\t neatly formatted name: {formatted_name}. ")