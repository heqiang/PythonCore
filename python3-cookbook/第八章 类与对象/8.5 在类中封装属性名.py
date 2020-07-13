# 单下划线开始的成员变量交保护变量，意思是只有类对象和之类对象能访问到
# 双下化线 开始的交私有成员 意思是只有类对象自己能访问 ，子类对象也不能访问到这个数据
    #使用双下划线会导致改变访问名称的形式 ,参考 类B 通过dir(b)可查看
# 结论：
# 1、_xxx 不能用于’from module import *’ 以单下划线开头的表示的是protected类型的变量。 即保护类型只能允许其本身与子类进行访问。
# 2、__xxx 双下划线的表示的是私有类型的变量。只能是允许这个类本身进行访问了。连子类也不可以
# 3、__xxx___ 定义的是特列方法。像__init__之类的

class A():
    def __init__(self):
        self._inter = 0
        self.public = 1

    def public_method(self):
        print(self.public)

    def _inter_method(self):
        print(self._inter)
    def get_private_method(self):
        return self._inter,self._inter_method()
a = A()
a._inter = 5
print(a._inter)

# 双下划线开头
class  B():
    def __init__(self):

        self.__name = "text"
    def __private(self):
        print("私有方法")
b = B()
print(dir(b))
# print(b.__name)#报错
print(b._B__name)
b._B__private()
