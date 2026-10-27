# 注意:函数定义不会执行,调用才会
# 函数定义:
# def out_line():
#     print("")
#     print("")
#
#
# 函数调用
# out_line()
from ast import Num
from operator import ifloordiv
from urllib.request import AbstractBasicAuthHandler


# 函数的参数与返回值
# 函数1:计算圆的面积----半径
def circle_area(r):
    area = r*r*3.14
    return area

area=circle_area(10)
print(area)


# 函数2:计算长方形面积--长宽
def rectangle_area(l,w):
    """
    计算长方形的面积
    param l:长
    param w:宽
    return :面积
    """
    area = l*w
    return area
print(rectangle_area(5,4))
print(help(rectangle_area))

# 函数3:计算圆的面积和周长---->返回值有多个逗号分隔------>多个返回值会封装在元组类型
def circle_area_len(r):
    """

    """
    area = r*r*3.14
    len =round(2*r*3.14,1)
    return area , len

al=circle_area_len(10)
print(al)
print(type(al))


area,len=circle_area_len(10)#解包
print(area)
print(len)


# 案例1:计算三角形面积
def triangle_area(l,h):
    """
    输入底和高
    """
    area = 1/2 *l*h
    return area
#案例2:计算传入的字符串中元音的个数
def  count_aeiou(s):
    num=0
    for i in s:
        if i in "aeiouAEIOU":
            num+=1
    return num
print(count_aeiou("hello"))
#案例3:计算传入班级的最高分,最低分和平均数\
# def score(scor_list):
#     max_scor=max(scor_list)
#     min_score=min(scor_list)
#     avg_score=round(sum(scor_list)/len(scor_list),1)
#     return max_scor,min_score,avg_score
#1.定义一个函数,根据传入的分数,计算对应的等级
# s>=90--a
# s>=75--b
# s>=60--c
# s<60---d

def  score(s):
    if s>=90:
       return "A"
    elif s>=75:
        return "B"
    elif s>=60:
        return "C"
    else:
        return "D"
    return
print(score(65))
# 2.判断回文
def level_str(s):
    str=s[::-1]
    if str==s:
        return "是回文"
    else:
        return "不是回文"
print(level_str("acd"))

#3.调整时间将秒转换为小时

def   time(t):
     if not isinstance(t,int) or t < 0:
        return "必须是非负整数"
     hours=t//3600
     remain=t%3600
     minute=remain//60
     second=remain%60
     return hours,minute,second
h,m,s=time(9885)
print(f"{h}小时,{m}分钟,{s}秒")

#4.定义一个函数:判断三角形的类型
def side_length(a,b,c):
    if a+b>c and a+c>b and b+c>a:
          if a==b==c:
              return "该三角形是等边三角形"
          elif a==b or a==c or b==c:
              return "该三角形是等腰三角形"
          else:
              return "该三角形是普通三角形"
    else:
        return "这三边不能组成三角形"
print(side_length(14,14,14))









