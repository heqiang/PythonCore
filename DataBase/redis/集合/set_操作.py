
import  redis


r = redis.Redis(host="127.0.0.1",port=6379)

# r.sadd("stu","xiaoming","xiaohei")
# res = r.sunion("stu","stu1")
r.smove("stu","stu1","xiaohei")
