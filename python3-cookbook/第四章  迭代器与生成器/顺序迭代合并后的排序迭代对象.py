#也不会对输入做任何的排序检测。在遍历的时候它仅仅是检查所有序列的开始部分并返回最小的那个，
# 这个过程一直会持续直到所有输入序列中的元素都被遍历完
import  heapq

a = [5, 4, 3, 10]
b = [3, 5, 6, 11]
heapq.heapify(a)
heapq.heapify(b)
res = heapq.heappop(a)
print("弹出来的最小值为："+str(res))
print(a)
heapq.heappush(a,555)
print(a)
# 先吧item放入堆中 然后在弹出最小的元素并返回，比先push 在pop效率高
res1 = heapq.heappushpop(a,2)
print("弹出来的最小值为："+str(res1))
print(a)

#先弹出最小值 在推入item 比 先pop  在push效率高
res2 = heapq.heapreplace(b,2)
print("弹出来的最小值为："+str(res2))
print(b)



