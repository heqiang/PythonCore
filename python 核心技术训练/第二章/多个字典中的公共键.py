from  random import  randint,sample

s1 = "sfkdl"

a = sample(s1,3)
print(a)

s = {x:randint(1,5) for x in sample(s1,(3,6))}
print(s)