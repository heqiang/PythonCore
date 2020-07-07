# 随机生成字典
from random import randint
dict_ = {x:randint(60,80) for x in range(1,23)}
print(dict_)

# 筛选分数大于90的
res = {k:v for k,v in dict_.items() if v>78}
print(res)

# 集合
# 为元祖中的每个元素命名，提高可读性
Name,Age,Sex,Email = 0,1,2,3

student = ("jin","18","male","14221270652@qq.com")

Name = student[Name]
Age = student[Age]

