# -*- coding:utf-8 -*-
import re
str_ = '\"/nd.jsp?id=1367#_np=0_641_11\"'
res = re.findall("id=\d+\S+\d+",str_)
print(res)

count = sum([x for x in range(1,101)])
print(count)