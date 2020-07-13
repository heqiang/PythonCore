# 你写了很多仅仅用作数据结构的类，不想写太多烦人的 __init__() 函数

class Structure():
    _fields = []

    def __init__(self,*args):
        if len(args) != len(self._fields):
            raise  TypeError("Expected {} arguments ".format(len(self._fields)))

        for name,value in zip(self._fields,args):
            print(name +" "+ value)
            setattr(self,name,value)

class Stock(Structure):
    _fields = ["name","sex"]

a = Stock("hq","man")
print(dir(a))