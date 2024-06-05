mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

class MyNumber:
    def __iter__(self):
        self.a=1
        return self
    
 