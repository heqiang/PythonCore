# -*- coding:utf-8 -*-
#迭代器(iterator) 和可迭代器对象(iterable)
#凡是可以for循环的，都是Iterable
# 凡是可以next()的，都是Iterator
# 集合数据类型如list，truple，dict，str，都是Itrable不是Iterator，但可以通过iter()函数获得一个Iterator对象
# Python中的for循环就是通过next实现的

# 什么是迭代器
# 满足两个条件 1 有iter方法  2 有next方法
#迭代器对象
class  MyListIterator(object):
        def __init__(self,data):
            self.data = data
            self.index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.index<len(self.data):
                item = self.data[self.index]
                self.index += 1
                return item
            else:
                raise StopIteration

list = [1,3,5,9,7]
a = MyListIterator(list)
while True:
    try:
         res = next(a)
         print(res)
    except:
        break

#可迭代对象
# class MyIterable(object):
#         def __init__(self,data):
#             self.data = data
#
#         def __iter__(self):
#             return MyListIterator(self.data)
# iterable = MyIterable(list)
# for x in iterable:
#       print(x)
