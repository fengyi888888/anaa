#定义类  --->不推荐动态的添加属性
# class Car:
#     pass
#
# #创建对象
#
# c1=Car()
# #动态的为对象添加属性
# c1.color="red"
# c1.brand="BMW" #brand(品牌)
# c1.name="x5"
# c1.price=500000
#
# print(c1)
# print(c1.brand)
# print(c1.__dict__)#会将对象的所有属性以字典的方式输出

# class Car:
#     #__init__是初始化的方法,会在对象创建时自动调用,可以在改方法中设置对应的属性;
#     #self:是第一个参数,表示当前所创建的第一个实例对象
#     def __init__(self,c_color,c_brand,c_price ):
#         self.color = c_color
#         self.brand = c_brand
#         self.price = c_price
#         print("Car 类型的对象初始化完毕,对象属性已经添加完毕 .")
#
# #创建对象`
# c1= Car("red","BWM",500000)
# print(c1.__dict__)

#------------------------------------------------------ 定义类 实例方法-------------------------------------------------##

# class Car:
#     #__init__是初始化的方法,会在对象创建时自动调用,可以在改方法中设置对应的属性;
#     #self:是第一个参数,表示当前所创建的第一个实例对象
#     def __init__(self,c_color,c_brand,c_price,c_name ):
#         self.color = c_color
#         self.brand = c_brand
#         self.price = c_price
#         self.name = c_name
#         print("Car 类型的对象初始化完毕,对象属性已经添加完毕 .")
# #定义实例方法
#     def running(self):
#          print(f"{self.brand}{self.name}正在高速行驶中....")
#
#     def total_cost(self,discount,rate):
#         """
#         计算提车总费用
#         :param discount:折扣
#         :param rate:税率
#         """
#         total_cost =self.price*discount+self.price*rate
#         return total_cost
#
# #测试
# c1=Car("红色","BWM",500000,"x7")
# #调用对象中的方法
# c1.running()
# c1.total_cost(discount=0.9,rate=0.1)
# print(f"提车的总费用为:{c1.total_cost(discount=0.9,rate=0.1)}")

# class Car:
#     #__init__是初始化的方法,会在对象创建时自动调用,可以在改方法中设置对应的属性;
#     #self:是第一个参数,表示当前所创建的第一个实例对象
#     def __init__(self,c_color,c_brand,c_price,c_name ):
#         self.color = c_color
#         self.brand = c_brand
#         self.price = c_price
#         self.name = c_name
#         print("Car 类型的对象初始化完毕,对象属性已经添加完毕 .")
# #定义实例方法
#     def running(self):
#          print(f"{self.brand}{self.name}正在高速行驶中....")
#
#     def total_cost(self,discount,rate):
#         """
#         计算提车总费用
#         :param discount:折扣
#         :param rate:税率
#         """
#         total_cost =self.price*discount+self.price*rate
#         return total_cost
#     def __str__(self):
#         return f"{self.color} {self.brand} {self.price} {self.name}"
#     def __eq__(self, other):
#         return self.color == other.color and self.brand == other.brand and self.price == other.price and self.name == other.name
#     def __lt__(self, other):
#         return self.price < other.price
# c1=Car("红色","BYD",18000,"秦")
# c2=Car("黄色","BYD",18000,"汉")
# print(c1)
# print(c2)
#
# print(c1==c2)
# print(c1<c2)


#####-------------------实例属性&类属性-----------------------###

# class Car:
#     #类属性  (所以实例对象共享的)
#     wheel=4  #轮胎的数量
#     tax_rate=0.1  #税率
#
#     #__init__是初始化的方法,会在对象创建时自动调用,可以在改方法中设置对应的属性;
#     #self:是第一个参数,表示当前所创建的第一个实例对象
#     def __init__(self,c_color,c_brand,c_price,c_name ):
#         self.color = c_color
#         self.brand = c_brand
#         self.price = c_price
#         self.name = c_name
#         # self.wheel = 2
#
# #定义实例方法
#     def running(self):
#          print(f"{self.brand}{self.name}正在高速行驶中....")
#
#     def total_cost(self,discount,rate):
#         """
#         计算提车总费用
#         :param discount:折扣
#         :param rate:税率
#         """
#         total_cost =self.price*discount+self.price*rate
#         return total_cost
#
# c1=Car("白色","BYD",180000,"汉")
# print(c1.brand)
# print(c1.wheel)   #通过实例对象,会先查找实例属性,~不存在再查找类属性
#
# # 通过类名访问类属性
#
# print(Car.wheel)
# c2=Car("黑色","Tesla",260000,"Model Y")
#学生类
from 练习.数据容器总结 import choice


class Student:
    def __init__(self,name,chinese,math,english):
        self.name=name
        self.chinese=chinese
        self.math=math
        self.english=english
    def __str__(self):
        return f"姓名:{self.name}  | 语文:{self.chinese} | 数学:{self.math} | 英语{self.english} | 总分:{self.chinese+self.math+self.english} "
    def update_score(self,chinese=None,math=None,english=None):
       if chinese is not None:
           self.chinese=chinese
       if math is not None:
           self.math=math
       if english is not None:
           self.english=english
# if __name__=="__main__":
#   s1=Student("王林",98,88,92)
#   print(s1)
#   s1.update_score(english=95)
#   print(s1)

#教务系统的类

class EdManagement:
    system_version=0.1
    system_name ="教务系统"
    def __init__(self):
        self.student_list = [] #记录在校学生的成绩信息
#添加学生成绩
    def add_student(self):
        name=input("请输入学生姓名:")
        for s in self.student_list:
            if s.name==name:
               print("该学生已经添加,添加失败")
               return
        chinese=int(input("请输入学生语文成绩:"))
        math=int(input("请输入学生数学成绩:"))
        english=int(input("请输入学生英语成绩:"))
        #判断分数
        if  0 <= chinese <=100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu=Student(name,chinese,math,english)
            self.student_list.append(stu)
            print("添加成功")
        else:
            print("学生的各科成绩必须在 0 ~ 100 之间")

#修改学生成绩

    def update_student(self):
        name = input("请输入修改的学生姓名:")
        for s in self.student_list:
            if s.name==name:
               print(f"当前成绩是{s}")
               chinese = int(input("请输入修改后的语文成绩:"))
               math = int(input("请输入修改后的数学成绩:"))
               english = int(input("请输入修改后的英语成绩:"))
               if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                   s.update_score(chinese,math,english)
                   print("成绩修改成功")
                   print(f"修改后成绩是{s}")
                   return
            else:
                print("学生的各科成绩必须在 0 ~ 100 之间")
                return
        print("为找到该学生修改失败")

#删除学生成绩\
    def delete_student(self):
        name = input("请输入删除的学生姓名:")
        for s in self.student_list:
            if s.name==name:
                self.student_list.remove(s)
                print("学生信息删除成功")
                return
            else:
                print("未找到该学生信息,删除失败!")

#查询指定学生成绩
    def  query_student(self):
        name = input("请输入要查询的学生姓名:")
        for s in self.student_list:
            if s.name==name:
                print(f"学生信息{s}")
                return
        print("该学生不存在")
#展示全部学生成绩
    def  show_students(self):
        for s in self.student_list:
            print(f"学生信息为{s}")

#运行系统

    def run(self):
        print(f"欢迎使用教务管理系统  V  {EdManagement.system_version}")

        while True:
            print()
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ## # # # #")
            print("#  1.添加学生信息  2.修改学生信息  3.删除学生信息  4.查询学生信息  5.列出所有学生 6.退出菜单 #")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # ## # # # # # ## # # # # # ## # #")
            choice =input("请选择你的操作,输入1~6")
            match choice:
                case "1":
                    self.add_student()
                case "2":
                    self.update_student()
                case "3":
                    self.delete_student()
                case "4":
                    self.query_student()
                case "5":
                    self.show_students()
                case "6":
                    break
                case _:
                    print("请输入1~6")

if __name__=="__main__":
   edmanage = EdManagement()
   edmanage.run()