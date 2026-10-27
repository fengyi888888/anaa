#全局变量
from operator import truediv

num =100


# 定义函数
def circle_area(r):
    # 局部变量只能在函数内部使用
    pi =3.14
    area = pi * r * r
    global num

    num = 10000
    print("num",1000)
    return  area


c_area = circle_area(10)
print(c_area)

print("num", num)


def reg_stu(name,age,gender,city):
    print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
    return {"name":name,"age":age,"gender":gender,"city":city}

#传参方式一: 位置传参
stu =reg_stu("张三",18,"男","北京")
print(stu)


#传参方式二: 关键字传参
stu =reg_stu(name="张三",age=18,gender="男",city="北京")
print(stu)


#传参方式三: 位置传参+关键字传参
stu =reg_stu("张三",18,gender="男",city="北京")
print(stu)


#--------------------------------------------默认参数-----------------------------------------------------------------
def reg_stu1(name,age,gender,city="北京"):
    print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
    return {"name":name,"age":age,"gender":gender,"city":city}

stu =reg_stu1(name="张三",age=18,gender="男")
print(stu)

stu =reg_stu1(name="李四",age=18,gender="男",city="江西")
print(stu)





#--------------------------------------------不定长参数(位置传递*args--元组)-----------------------------------------------------------------
# 位置传递(*args)-----多个参数会封装到一个元组里
# 需求:根据传入的数据,计算数据的平均值,最大值最小值
def calc_data(*args):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args)/len(args)
    return min_data,max_data,round(avg_data,1)

#调用函数,
data=calc_data(6,5,4,7,9,2)
print(data)

data=calc_data(10,5,7,9,3,7,8,5,2,9,7,8)
print(data)



#--------------------------------------------不定长参数(关键字传递*kwargs--字典)-----------------------------------------------------------------
# 需求:根据传入的数据,计算数据的平均值,最大值最小值
#关键字传递(**kwargs)
def calc_data1(*args,**kwargs):
    """
    # 需求:根据传入的数据,计算数据的平均值,最大值最小值
    :param args:不定长位置参数
    :param kwargs:不定长关键字
      round:保留的小数位个数
    """
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args)/len(args)

    if kwargs.get("round") is not None:
        avg_data = round(avg_data,kwargs.get("round"))

    if kwargs.get("print") :
         print(f"计算出来的最小值:{min_data},最大值:{max_data},平均值:{avg_data}")


    return min_data,max_data,avg_data


#调用函数,
data=calc_data1(6,5,4,7,9,2,round=1,print=True)
print(data)

data=calc_data1(10,5,7,9,3,7,8,5,2,9,7,round=1)
print(data)

data=calc_data1(10,5,7,9,3,7,8,5,2,9,7,round=1,print=False)
print(data)



#
