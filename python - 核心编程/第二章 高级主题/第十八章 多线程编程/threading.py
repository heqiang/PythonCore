import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        super(myThread).__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter
    def  run(self):
        print("开始线程："+self.name)
        print_time(self.name,self.counter,2)
        print("退出线程: "+self.name)

def print_time(threadName,delay,counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter-=1

#创建新线程
thread1=myThread(1,"thread1",1)
thread2=myThread(2,'thread2',2)

#开启线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("主线程退出")

