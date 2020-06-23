class fib():
    def __init__(self,list):
        self.index = len(list)
        self.list = list

    def __iter__(self):
        return self
    def __next__(self):
        if self.index ==0:
            raise StopIteration("没有了")
        self.index -= 1
        return  self.list[self.index]


a = fib([x for x in range(5)])

print(a)
iter(a)
next(a)
# for x in a :
#     print(x)