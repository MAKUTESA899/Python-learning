x = 10
# greater than or equal to
print(x>=20)
x+=5
print(f"the result of x+=5 if x is 10 = {x}")

y=3
y-=7
print(f"the result of y-=7 if y is 3 = {y}")

q = 10
q*= 5
print(f"the result of q*=5 if q is 10 = {q}")

w = 2
w%= 4
print(f"the result of w%=4 if w is 2 = {w}")

e = 5
e/= 3
print(f"the result of e/=3 if e is 5 = {e}")

r = 5
r//= 10
print(f"the result of r//=10 if r is 5 = {r}")

t = 6
t**= 8
print(f"the result of t**=8 if t is 6 = {t}")

u =  4
u&= 6
print(f"yhe result of u&= 6 if u is 4 = {u}")

i = 6
i|= 7
print(f"the result of i|= 7 if i is 6 = {i}")

o = 2
o^= 3
print(f"the result of o^= 3 if o is 2 = {o}")

p = 8
p>>=19
print(f"the result of p>>=19 if p is 8 = {p}")

a = 14
a<<= 20
print(f"the result of a<<= 20 if a is 14 = {a}")

#python logical operators
f = 6
print(f>10 and f<2)

g = 10
print(g<4 or g>5)

h = 1
print(not(h<4 and h<3))

#python identity operators
j= ["apple", "mango"]
k= ["apple tree", "mango tree"]
l = j
print(l is j)
print(l is k)

z= ["apple", "mango"]
x= ["apple tree", "mango tree"]
c = z
print(c is not x)
print(c is not z)

#python membership operators
v= ["apple", "mango"]
print ("apple"in v)

v= ["apple", "mango"]
print("apple"not in v)
print(len(v))