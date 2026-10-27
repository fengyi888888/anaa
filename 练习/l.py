students=[]
menu="""
########################################################################
#  1.添加学生信息  2.修改学生信息  3.删除学生信息  4.查询学生信息  5.列出所有学生  #
########################################################################
"""
while True:
    choice=input("请操作")
    match choice:
        case "1":
           student= Student(input("请输入学生姓名"),float(input("请输入语文成绩")),float(input("请输入数学成绩")),float(input("请输入英语成绩")))
           students.append(student)
        case "2":
           if not students:
                 print("还没有学生信息,请添加")
                 continue
           name = input("请修改学生名字")
           for stu in students:
                if stu["学生姓名"] == name:
                        stu["语文成绩"] = input("请修改语文成绩")
                        stu["英语成绩"] = input("请修改英语成绩")
                        stu["数学成绩"] = input("请修改数学成绩")
                        print("修改成功")
                        continue
           else:
                     print("该学生不存在,请重新操作")