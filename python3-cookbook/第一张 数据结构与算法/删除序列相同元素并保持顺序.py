# 序列元素为 hashable 的时候才可以
def dedup(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
de = dedup(a)
print(list(de))

dict_ = {"a":1,"b":2}


# 如果你想消除元素不可哈希（比如dict类型）的序列中重复元素的话

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)