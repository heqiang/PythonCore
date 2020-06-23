# 检查类的继承关系

class  A():
    pass

class B(A):
    pass


res = issubclass(B,A)
print(res)