#异常处理


# try:
#         print("------------------------")
#         # print(my_name)
#         # print(1/0)
#         # print("ABC"[10])
#         print("aABC".hell)
#         print("------------------------")
# except NameError as e:  #捕获的是 NameError 类型异常
#     print("名字不存在!异常信息是:",e)
# except ZeroDivisionError as e:
#     print("0不能作为除数!异常信息是:", e)
# except IndexError as e:
#     print("索引错误!异常信息是:", e)
# except Exception as e:#捕获所有异常
#     print("程序运行出错了!")
# finally: #无论程序是否正常运行都会运行
#     print("资源释放-")

def fun1():
    print("fun1......running...")
    fun2()

def fun2():
    print("fun2......running...")
    fun3()

def fun3():
    print("fun3......running...")
    print(my_color)

if __name__ == "__main__":
    try:
        fun1()
    except Exception as e:
        print("程序运行出错了请联系管理员!错误信息是:",e)


