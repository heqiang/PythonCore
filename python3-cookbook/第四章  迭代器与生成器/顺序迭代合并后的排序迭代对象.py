#也不会对输入做任何的排序检测。 它仅仅是检查所有序列的开始部分并返回最小的那个，这个过程一直会持续直到所有输入序列中的元素都被遍历完
import  heapq

a = [1, 4, 3, 10]
b = [0, 5, 6, 11]

res = heapq.merge(a,b)
for x in res:
    print(x)