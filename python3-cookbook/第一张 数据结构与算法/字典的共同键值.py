a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# 移除指定值 并返回一个新的字典
res = {k: a[k] for k in a.keys()-{"x"}}
print(res)

#字典的键视图可以进行集合操作 比如集合并、交、差运算
res1 = a.keys()-b.keys()
print(res1)
