#ignores duplicate values
#thislist = {"apple", "banana", "cherry", "apple"}

#
#thislist = {"apple", "banana", "cherry", "apple", True, 1, 2}

#print (thislist)

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print (set1)
print (set2)
print (set3)

#data type
myset = {"apple", "banana", "cherry"}
print(type(myset))

#double (( ))
thisset = set(("apple", "banana", "cherry"))
print (thisset)

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print (x)