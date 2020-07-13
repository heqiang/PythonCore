# 就是在一个类中实现了 __enter__ 和__exit__方法 这个类的实例就是衣蛾上下文管理器
# 使用上下文管理器的三个好处：
    # 提高代码的复用率；
    # 提高代码的优雅度；
    # 提高代码的可读性；

# 使用类来生成一个上下文管理器
import contextlib


class Resource():
    def __enter__(self):
        print("connect to source")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        :param exc_type: 异常类型
        :param exc_val: 异常值
        :param exc_tb: 异常的错误栈信息
        :return:
        """
        print("Close Source connection")

    def Operate(self):
        print("in operate")



# contextlib 简化上下文管理器的构建
@contextlib.contextmanager
def open_func(file_name):
    # enter方法
    print("open file:",file_name,"in enter")
    file_handler = open(file_name,"r")
    # 重点 yield
    try:
        yield file_handler
    except Exception as exc:
        # deal with  exception
        print("the exception is throw")
    finally:
        # exit 方法
        print("close file:",file_name,"in exit")
        file_handler.close()
        return

with open_func("ceshi.txt") as  f:
    for x in f:
        print(x)