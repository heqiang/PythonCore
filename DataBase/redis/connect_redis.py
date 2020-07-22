import  redis


r = redis.Redis(host="127.0.0.1",port=6379)

r.set("py",123)
res = r.keys("*")
print(res)

r.hset("Stu","name","hq")





