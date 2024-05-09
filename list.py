thislist =["apple", "banana", "mango"]

print (thislist)

#length of a list

thislist =["apple", "banana", "mango"]
print(len(thislist))

#type

thislist =["apple", "banana", "mango"]
print(type(thislist))

#access item
thislist =["apple", "banana", "mango"]
print(thislist[2])

#change item value
thislist =["apple", "banana", "mango"]
thislist [1]= "cherry"
print (thislist)
thislist =["apple", "banana", "mango"]
thislist[0]="watermelon"
print(thislist)
thislist =["apple", "banana", "mango"]
thislist[2]="kiwi"

print(thislist)
 
#insert  in a list
thislist =["apple", "banana", "mango"]
thislist.insert(2 , "cherry")
print(thislist)
thislist =["apple", "banana", "mango"]
thislist.insert(3,"watermelon")
print(thislist)
thislist =["apple", "banana", "mango"]
thislist.insert(0,"orange")
print(thislist)

#append list
thislist =["apple", "banana", "mango"]
thislist.append("oranges")
print(thislist)

#remove
thislist =["apple", "banana", "mango"]
thislist.remove("apple")
print(thislist)
thislist =["apple", "banana", "mango"]
thislist.pop()
print(thislist)

#delete a list
thislist =["apple", "banana", "mango"]
del thislist 
print(thislist)
thislist =["apple", "banana", "mango"]
thislist.clear()
print(thislist)


#loop through a list
this =["apple", "banana", "mango"]
for m in this:
    print(m)