# # 列表操作
# #定义
# s=[50,33,62,90,"a",True]
# # print(type(s))
# # # 访问列表元素
# # # 获取
# # print(s[0])#正向,0开始
# # print(s[-6])#反向,-1开始
# # #修改
# # s[4]="asd"
# print(s)
# # #删除
# # del s[5]
# # print(s)
# # #遍历
# # for i in s:
# #     print(i)
#     #切片
# # s=["a","b","c","d","e","f","g"]
# #     # 语法:[开始索引:结束索引:步长(默认1)]
# # print(s[0:5])
# # print(s[:5:2])
# # print(s[0:-2])
#
# #列表定义
s=[10,50,30,40,20,60,50,34,54]
# #在尾端加入元素append
# s.append(80)
# print(s)
#
# #插入元素insert
# s.insert(2,15)
# print(s)
#
# #remove删除第一个匹配的元素
# s.remove(50)
# print(s)
#
# #pop删除索引位置的元素并返回(如果未索引则默认最后一个)
# a=s.pop(1)
# print(a)
#
# #排序sort
s.sort()
# print(s)
#
# #reverse(倒序)
# s.reverse()
# print(s)

# 案例
#1定义列表
# num_list=[]
# # #2输入10个数字
# for i in range(0,10):
#     num=int(input("请输入10个数字"))
#     num_list.append(num)
# # #3排序
# num_list.sort()
# print(num_list)

#3求平均值最小值和最大值  -->sum(求和函数)--->len(获取元素个数)--min()获取最小值--max--获取最大值
# print("最小值", num_list[0])
# print("最大值", num_list[-1])
# print("平均值", sum(num_list) / len(num_list))
# 案例
# num_list1=[19,23,54,64,875,20,109,232,123,54]
# num_list2=[55,80,72,35,60,123,54,29,91]
# #1.合并列表
# for i in num_list2:
#     num_list1.append(i)
# print(num_list1)
#
# # 去除重复元素
# new_list=[]#去重后的列表
# for i in num_list1:
#     #(判断是否有相同元素)
#     if  i not in new_list :#in:判断元素是否存在列表中,如果存在返回True,不存在返回False
#         new_list.append(i)
# print(new_list)
# num_list1=[19,23,54,64,875,20,109,232,123,54]
# num_list2=[55,80,72,35,60,123,54,29,91]
# #1.合并列表
# #解包:将列表这一类容器解开一个一个独立的元素(*)
# #组包:将多个值合并到一个容器
# num_list=[*num_list1,*num_list2]
# print(num_list)
# # 去除重复元素
# new_list=[]
# #去重后的列表
# for i in num_list:
#     #(判断是否有相同元素)
#     if  i not in new_list :#in:判断元素是否存在列表中,如果存在返回True,不存在返回False
#         new_list.append(i)
# print(new_list)

# num_list1=[19,23,54,64,875,20,109,232,123,54]
# num_list2=[55,80,72,35,60,123,54,29,91]
#1.合并列表
#解包:将列表这一类容器解开一个一个独立的元素(*)
#组包:将多个值合并到一个容器
# num_list=num_list1+num_list2
# print(num_list)
# # 去除重复元素
# new_list=[]
# #去重后的列表
# for i in num_list:
#     #(判断是否有相同元素)
#     if  i not in new_list :#in:判断元素是否存在列表中,如果存在返回True,不存在返回False
#         new_list.append(i)
# print(new_list)


# 案例方法一
# new_list=[]
# for i in range(1,21):
#     i=i*i
#     new_list.append(i)
# print(new_list)
#
# # 方法二列表退倒式-->就是按照一定的规则快速生成一个列表的方法-->语法格式1:[要插入的值for i in 序列/列表]-->语法格式2:[要插入的值for i in 序列/列表 if条件]
# num_list2=[i**2 for i in range(1,21)]
# print(num_list2)

num_list=[19,23,54,64,87,20,109,232,123,43,26,55,72]
num_list1=[]
for num in num_list:
    if num%2==0:
        num=num*num
        num_list1.append(num)
print(num_list1)

um_list2=[19,23,54,64,87,20,109,232,123,43,26,55,72]
num_list3=[ i**2  for i in um_list2 if i%2==0]
print(num_list3)








