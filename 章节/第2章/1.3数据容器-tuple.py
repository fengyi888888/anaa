#元组的基本操作--tuple
#定义
# t1=(80,90,85,52,32,41)
# print(type(t1))
#
#
# #索引访问
# print(t1[0])
# print(t1[-1])
#
# # 切片
# print(t1[0:3:1])
# #count统计元素个数
# print(t1.count(80))
# #index获取索引位置(第一次)
# print(t1.index(80))
#
# #注意:
# t2=()
# print(t2)
# print(type(t2))
#
# t3=(100,)#(d定义单元数要加逗号)
# print(t3)
# print(type(t3))
from pickletools import string1

# 组包:将多个值合并到一个容器里中
# 解包:将容器(元组,列表)解开独立的元素.分别赋值给多个变量

#定义元组,组包
# t1=(5,4,6,7)
# #定义元组,组包
# t2=5,4,6,7
# # 基础解包
# a,b,c,d=t1
# print(a)
# #扩展解包(*)在元组解包时,*收集的所有元素,允许我们处理不确定的元素(生成列表,以便于可以进行进一步的处理)
# x,*y,z=t2#x为5,y为4,6,z为7
# s,*o=t2#s为5,o为4,6,7
# *i,e=t2#i为5,4,6,e为7

# 案例1
# a=10
# b=20
# #组包t=b,a
# #解包a,b=t
# a,b=b,a
# print(a,b)
#
# 案例2
# a=100
# b=200
# c=300
# a,b,c=c,a,b
# print(a,b,c)

# 案例
students =(
    ("s001","王林",85,92,78),
    ("s002","李慕婉",92,88,95),
    ("s003","十三",78,85,82),
    ("s004","曾牛",88,79,91),
    ("s005","周铁",95,96,89),
    ("s006","王卓",76,82,77),
    ("s007","红蝶",89,91,94),
    ("s008","徐立国",75,69,82),
    ("s009","许木",86,89,98),
    ("s0010","遁天",66,59,72),
)
#average:.1f--->保留一位小数
# 方式一
# print("学号\t\t姓名\t\t总分\t\t平均分\t\t")
# for s in students:
#    total=s[2]+s[3]+s[4]
#    average=total/3
#    print(f"{s[0]} \t {s[1]} \t {total} \t {average:.1f}")
print("学号\t\t姓名\t\t总分\t\t平均分\t\t")
for id,name,chinese,math,english in students:
    total = chinese+math+english
    average = total / 3
    print(f"{id} \t\t {name} \t\t {chinese} \t\t {math} \t\t {english} \t\t {total} \t\t {average:.1f} ")

chinese_scores=[ s[2] for s in students ]
math_scores=[ s[3] for s in students ]
english_scores=[ s[4] for s in students ]
print(f"语文最低分:{min(chinese_scores)},最高分{max(chinese_scores)},平均分{sum(chinese_scores)/len(chinese_scores)}")
print(f"数学最低分:{min(math_scores)},最高分{max(math_scores)},平均分{sum(math_scores)/len(math_scores)}")
print(f"英文最低分:{min(english_scores)},最高分{max(english_scores)},平均分{sum(english_scores)/len(english_scores)}")
for s in students:
    total=s[2]+s[3]+s[4]
    average=total/3
    if average>=90:
        print(average)







