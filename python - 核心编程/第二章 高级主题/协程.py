import gevent,time
from gevent import monkey
monkey.patch_all()


def test1():
    for x in range(10):
        time.sleep(1)
        print("test",str(1))


def test2():
    for x in range(10):
        time.sleep(2)
        print("test",str(2))

g1 = gevent.spawn(test1)
g2 = gevent.spawn(test2)

g1.join()
g2.join()