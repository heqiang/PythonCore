import  redis


r = redis.Redis(host="127.0.0.1",port=6379)

res = r.bitcount("stu")
# 01110011
# 01110100
# 1110101
print(res)