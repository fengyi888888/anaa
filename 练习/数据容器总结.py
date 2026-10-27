# 开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
#
# 1. 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
# 2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
# 3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
# 4. 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
# 5. 列出所有学生：遍历所有学生信息并输出。
# 6. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
# 7. 退出系统。
# from traceback import print_tb
# from unittest import case
students=[]
menu="""
#################################################################################################
#  1.添加学生信息  2.修改学生信息  3.删除学生信息  4.查询学生信息  5.列出所有学生  6.统计班级成绩  7.退出系统  #
#################################################################################################
"""
while True:
    print(menu)
    choice=input("请选择你的操作(1-7):")
    match choice:
        case "1":
            student_name=input("请添加学生名字")
            student_chinese=float(input("请添加语文成绩"))
            student_english=float(input("请添英语成绩"))
            student_math=float(input("请添加数学成绩"))
            student={"学生姓名":student_name,"语文成绩":student_chinese,"英语成绩":student_english,"数学成绩":student_math}
            students.append(student)
            print("添加成功")
        case "2":
            if not students:
                print("还没有学生信息,请添加")
                continue
            name = input("请修改学生名字")
            for stu in students:
                if stu["学生姓名"]==name:
                    stu["语文成绩"] = input("请修改语文成绩")
                    stu["英语成绩"]= input("请修改英语成绩")
                    stu["数学成绩"] = input("请修改数学成绩")
                    print("修改成功")
                    continue
            else:
                print("该学生不存在,请重新操作")
        case "3":
            if not students:
                print("还没有学生信息,请添加")
                continue
            name = input("请修改学生名字")
            for stu in students:
                    if stu["学生姓名"]==name:
                        del stu["name"]
                    else:
                        print("该学生不存在,请重新操作")
        case "4":
            if not students:
                print("还没有学生信息,请添加")
                continue
            name = input("请输入查询的学生")
            for stu in students:
                  if  stu["学生姓名"]==name:
                          print(
                                 f"学生的姓名为{stu["学生姓名"]},语文成绩:{stu["语文成绩"]},英语成绩:{stu["英语成绩"]},数学成绩:{stu["数学成绩"]}")
                  else:
                    print("该学生不存在")
        case "5":
            if not students:
                print("还没有录用")
                continue
            for stu in students:
               i=stu["学生姓名"]
               score=stu
               print(f"该学生的姓名为{i},语文成绩:{score["语文成绩"]},英语成绩:{score["英语成绩"]},数学成绩:{score["数学成绩"]}")
        case "6":
             if not students:
                 print("还没有学生信息,请添加")
                 continue
             elif students:
                  chinese_score=[stu["语文成绩"] for  stu in students]
                  english_score=[stu["英语成绩"] for  stu in students]
                  math_score=[stu["数学成绩"] for  stu in students]
                  max_chinese=[stu["学生姓名"] for stu in students if stu["语文成绩"]==max(chinese_score)]
                  min_chinese=[stu["学生姓名"] for stu in students if stu["语文成绩"]==min(chinese_score)]
                  max_english=[stu["学生姓名"] for stu in students if stu["英语成绩"]==max(english_score)]
                  min_english=[stu["学生姓名"] for stu in students if stu["英语成绩"]==min(english_score)]
                  max_math=[stu["学生姓名"] for stu in students if stu["数学成绩"]==max(math_score)]
                  min_math=[stu["学生姓名"] for stu in students if stu["数学成绩"]==min(math_score)]
                  for i in max_english:
                      e=i
                  for i in min_chinese:
                      c=i
                  for i in max_math:
                      m=i
                  for i in min_math:
                      m_m=i
                  for i in min_english:
                      m_e=i
                  for i in min_chinese:
                      m_c=i
                  age1=sum(chinese_score) / len(chinese_score)
                  age2=sum(english_score) / len(english_score)
                  age3=sum(math_score) / len(math_score)
                  print(
                      f"语文最高分为{max(chinese_score)},最高分人是{c},英语最高分为{max(english_score)},最高分人是{e},数学最高分为{max(math_score)},最高分数学是{m}")
                  print(
                      f"语文最低分为{min(chinese_score)},最低分人是{m_c},英语最低分为{min(english_score)},最低分人是{m_e},数学最低分为{min(math_score)},最低分人是{m_m}")
                  print( f"语文平均分为{age1:.2f},英语平均分为{age2:.2f},数学平均分为{age3:.2f}")


        case "7":
              print("Bey~")
              break
        case _:

              print("操作错误,请重新输入!!!")

# for i in student:
#     score = student[i]
#     chinese_score = []
#     english_score = []
#     mash_score = []
#     chinese_score.append(score["语文成绩"])
#     english_score.append(score["英语成绩"])
            #     mash_score.append(score["数学成绩"])
            #     print(
            #         f"语文最高分为{max(chinese_score)},英语最高分为{max(english_score)},数学最高分为{max(mash_score)}")
            #     print(
            #         f"语文最低分为{min(chinese_score)},英语最低分为{min(english_score)},数学最低分为{min(mash_score)}")
            #     print(
            #         f"语文平均分为{sum(chinese_score) / len(chinese_score)},英语最低分为{sum(english_score) / len(english_score)},数学最低分为{sum(mash_score) / len(mash_score)}")
            #     ")
# max1={"最高分":max_chinese}
#                   max2={"最高分":max_english}
#                   max3={"最高分":max_math}
#                   min1={"最低分":min_chinese}
#                   min2={"最低分":min_english}
#                   min3={"最低分":min_math}