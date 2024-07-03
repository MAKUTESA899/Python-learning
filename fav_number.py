import json

filename='favourite.json'
with open(filename) as f:
    fav_number=json.load(f)
    print(f"i know your favourite number {fav_num}")