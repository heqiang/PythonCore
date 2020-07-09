from collections  import defaultdict

d = defaultdict(list)
d["a"].append(1)
d['a'].append(2)
d['b'].append(4)

a = {}
a.setdefault("a" ,[]).append(1)
a.setdefault("b",())
print(a)