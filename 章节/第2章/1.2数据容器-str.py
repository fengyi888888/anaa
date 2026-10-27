#字符串 基本操作--->不可修改
from traceback import print_tb

s="hello-Python-hello-world "
# print(s[4])
# print(s[-8])
#
# for i in s:
#     print(i)
#
#切片
# print(s[0:5:1])
# print(s[:5])
# print(s[6:12:1])
# print(s[6::1])
print(s[::-1])

#find:查找字符串第一次牵引的位置
# index=s.find("-")
# print(index)
#
# #count统计字符串在指定字符串出现的次数
# a=s.count("o")
# print(a)
#
# #upper转为大写
# su=s.upper()
# print(su)
#
# #lower转为小写
# lo=s.lower()
# print(lo)
#
# #split()将字符串按照指定字符串切割-列表
# slist=s.split()
# print(slist)
#
# #replace将字符串的指定子串替代为新的
# re=s.replace("-",">>")
# print(re)
#
# #startswith()/endswith判断字符串是否是以指定字符串开头/结尾,并返回布尔值
# print(s.startswith("hello"))
# print(s.endswith("Python"))
# print(s)

# 案例


# 判断用户邮箱格式
#方式一
# while True:
#     mail=input("请输入你的邮箱")
#     if mail.count("@")==1 and mail.count(".")>=1:
#         break
#     else:
#         print("格式错误,请重新输入")
# print("邮箱格式正确")


# 方式二:in运算符-->判断是否存在字符串中,存在返回True,不存在返回False
# mail=input("请输入你的邮箱")
# if "@" in mail and mail.count(".")>=1:
#     print("邮箱格式正确")
# else:
#     print("格式错误,请重新输入")

# 案例1.回文
# s=input("请输入一段文字")
# if s==s[::-1]:
#    print(f"{s}是回文")
# else:
#     print(f"{s}不是回文")
 # 2.输入10个数字反转并大写最后遍历出来
s_list=[]
for i in range(10):
    a=input("请输入10个字符串")
    b=a.upper()[::-1]
    s_list.append(b)

print(s_list)
for num in s_list:
    print(num)














