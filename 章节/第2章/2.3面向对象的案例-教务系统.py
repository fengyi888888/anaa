#学生类
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

class EduManagement:
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
        print(f"欢迎使用教务管理系统  V  {EduManagement.system_version}")

        while True:
            print()
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ## # # # #")
            print("#  1.添加学生信息  2.修改学生信息  3.删除学生信息  4.查询学生信息  5.列出所有学生 6.退出菜单 #")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # ## # # # # # ## # # # # # ## # #")
            choice =input("请选择你的操作,输入1~6")
            try:
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
            except Exception as e:
                print("程序出错了!错误信息是:",e)

if __name__=="__main__":
   edumanage = EduManagement()
   edumanage.run()