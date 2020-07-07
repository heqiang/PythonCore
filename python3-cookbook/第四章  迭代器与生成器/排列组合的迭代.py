# permutations() 接受一个集合并产生一个元组序列，每个元组由集合中所有的一个可能排列组成  顺序不同 (a,b) 和(b,a)都会输出
# combinations() 得到输入集合中所有元素的组合 (a,b) 和(b,a)只会输出一个
# 上面两种都可指定输出序列的长度
from itertools import permutations,combinations

list = [1,2,3,5,86,8]

for x in permutations(list,2):
        print(x)
for x in combinations(list,2):
    print(x)