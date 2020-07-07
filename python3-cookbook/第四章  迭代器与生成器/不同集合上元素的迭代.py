from itertools import chain
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
c = ['w', 'g', 's']

for x in chain(a,b,c):
    print(x)