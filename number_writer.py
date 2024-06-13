import json
number =[2,3,4,5,6,11,13]
filename= 'number.json'

with open(filename, 'w') as f:
    json.dump(number,f)