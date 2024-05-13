#update a tuple
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print (green)
print (tropic)
print (red)

#access a tuple
thistuple = ("apple", "banana", "cherry")

print(thistuple[1])

thistuple = ("apple", "banana", "cherry")

print (thistuple[-1])

thistuple = ("apple", "banana", "cherry")

if "apple" in thistuple:
    print("yes, if 'apple' is in the fruits tuple")


#remove a tuple
    thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#loop a tuple

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print (x)

thistuple = ("apple", "banana", "cherry")

for i in this range(len(thistuple)):
    print(thistuple[i])