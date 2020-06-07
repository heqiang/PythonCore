x = 10
a= lambda y,x=x:x+y
x = 20
b = lambda y,x=x:x+y
print(a(10))
print(b(10))