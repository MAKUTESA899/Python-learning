import json

filename='password.json'
try:
    with open(filename) as 


filename='name.json'
try:
    with open(filename) as f:
        name=json.load(f)
except FileNotFoundError:
    name=input("your name is? ")
    with open(filename 'w') as f:
        json.dump(username , f)
        print(f"i will remember you{username}")
else:
    print(f "well come back {username}")