from datetime import timedelta

a = timedelta(days=2,hours=2.5)
b = timedelta(days=1,hours=3)
c = a + b
print("天数:%d"%c.days)
print("秒:%d"%c.seconds) #计算的是小时转换的秒
print(c.total_seconds())#计算的是天数加小时转换的秒数
print((24*3+5.5)*3600) #计算的是天数
