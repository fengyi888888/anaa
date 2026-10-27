# print("hello")
# print(type("hello"))
# # type获取变量类型
# print(type(10))
# print(type(10.1))
# print(type(True))
# print(type(None))
#
# #  常用数据类型isinstance(数据，类型 )-->bool值--<判定数据是否指定的类型
num =10
print(type(num))
print(isinstance(num,int))
print(isinstance(num,float))
print(isinstance(num,bool))


# 字符串
# 定义字符串的三种方式
# s1 ="hello"#双引号定义
# s2 ='python'#单引号定义
# s3 ="""
# Hello：
#     我喜欢你
# """#三引号定义（多行字符串）
# print(s1)
# print(s2)
# print(s3)
# print(type(s1))
# print(type(s2))
# print(type(s3))
# 定义字符串0-->it's very good
#转义字符 \',\",\n,\t
# msg ='it\'s very good'
# print(msg)
# print("我喜欢你\n你知道吗")
# print("\t我喜欢你\n\t你知道吗")#\n是换行\t是缩进相当于tap



#字符串的拼接
# s5 ="我喜欢你" "你知道吗"+"?"
# print(s1)
# msg1="我喜欢你"
# msg2="你知道吗？"
# print("我说,"+msg1+"."+msg2)


# 案例--> str(int数字)  --> 将int转为字符串
# name="帅哥"
# age=21
# pro="软件工程"
# hobby ="python、java"
# print("大家好，我是" + name +",今年" + str(age) +"岁，我的专业是" +pro+ "，喜欢的是"+hobby)

#方式一   字符串格式化-->%s 占位符
# name="帅哥"
# age=21
# pro="软件工程"
# hobby ="python、java"
# print("大家好，我是 %s,今年 %s,我的专业是 %s，喜欢的是 %s"%(name,age,pro,hobby))
#方式二  -->f" ...{变量名/表达式}.."   推荐方式
# name="帅哥"
# age=21
# pro="软件工程"
# hobby ="python、java"
# print(f"大家好，我是{name},今年{age}岁，我的专业是{pro}，喜欢的是{hobby}")


