#__all__指定from....import*导入的哪些功能
__all__ = ["log_separator1", "log_separator2", "log_separator3", "log_separator4","PI"]
#常量(名称全部大写:命名规范)
PI=3.14
NAME="帅哥"


#函数
def log_separator1():
    print("-" * 30)#"-"重复输出30次

def log_separator2():
    print("+" * 30)
def log_separator3():
    print("#" * 30)
def log_separator4():
    print("*" * 30)

#测试代码
#__name__ :Python中的内置变量,表示的是当前模块的名字(直接运行当前模块,__name__的值为"__main__",当该模块导入时,__name__的值就是该模块的名称)
#执行当前文件则会执行如下代码;如果被当做模块导入则不执行
if __name__ == '__main__':
       log_separator1()
