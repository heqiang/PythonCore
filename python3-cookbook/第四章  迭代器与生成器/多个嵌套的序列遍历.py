from collections.abc import Iterable

def flattern(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x,Iterable) and not isinstance(x ,ignore_types):
            yield from flattern(x)
        else:
            yield x


my_list = [[1,6],[2,8],[3,7],[5,9]]

for x in flattern(my_list):
    print(x)


