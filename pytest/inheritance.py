class parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class child(parent):
    def __init__(self,name,age):
      super().__init__(name,age)
      self.work= 2

x = child ("mike",12)
print(x.name)

