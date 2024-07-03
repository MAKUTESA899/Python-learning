import json

fav_num=input("whats your favourite number :")
filename='number.json'
with open(filename)as f:
    my_number=json.load(f)
if my_number == fav_num:
    print(f"your number is {my_number}")
else:
    with open(filename,'w')as f:
        json.dump(fav_num,f)