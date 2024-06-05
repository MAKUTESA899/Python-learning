def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

x = "peter"
def name():
  x="kamau"
  print(x)
name()
print(x)
