# num=int(input("输入一个数字"))
# if num%2==0:
#     print(f"{num}是偶数")
# else:
#     print(f"{num}是奇数")
# old=int(input("输入你的年龄"))
# if old>=18:
#     print(f"{old}已经成年")
# else:
#     print(f"{old}未成年")
# 判断三角形边长为正整数
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# if   a==b==c:
#     print("这个三角形是等边三角形")
# elif (a+b>c and a+c>b and b+c>a) and ( b==c or a==b or c==a):
#     print("这个三角形是等腰三角形")
# elif a+b>c and a+c>b and b+c>a :
#     print("这个三角形是普通三角形")
# else:
#     print("不是三角形")
# 案例
elect=int(input("你的电费用度:"))
if elect<=2880:
    elect=elect*0.4883
    print(f"你的电费为{elect}")
elif 2880<=elect<=4800:
    elect=elect*0.5383
    print(f"你的电费为{elect}")
else:
    elect=elect*0.7783
print(f"你的电费为{elect}")

