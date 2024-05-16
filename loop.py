#while loops
#x = 1
#while x < 11:
    #print(x)
  #  x +=1

#the continue statement

x = 2
while x <=20:
    y = 2
    while y <= 20:
        if (x % y) == 0:
            break
        y+=1
        if (x == y): 
            print(x)
    x +=1

x= (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for y in range(2,11):
    if (y%2 == 0):
        print(y)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
