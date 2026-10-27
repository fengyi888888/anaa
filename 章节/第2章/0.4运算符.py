#算数运算符
# print("10-4=",10-4)
# print("10+4=",10+4)
# print("10*4=",10*4)
# print("10**4=",10**4)#幂函数
# print("10/4=",10/4)
# print("10//4=",10//4)#整除

#优先级--> ** --> * / //  -->+ -
# print("0.1+10/4**2=",0.1+10/4**2)
#
# # 案例
# x=input("请输入x=")
# y=input("请输入y=")
# print(f"x+y={float(x)+float(y)},x-y={float(x)-float(y)}")

# 比较运算符-->会计算运算符两边的表达式,然后返回一个布尔作为结果
# print("100等于100吗",100==100) #true


# 逻辑运算符是多个条件(布尔)表达式,并返回一个最终布尔结果运算符
# and or not(取反操作true变成false,false变为true)

# num=int(input("请输入一个整数数"))(and类型)
# print(f"{num}在10到20之间",num>10and num<20)
# print(f"{num}在10到20之间", 10 < num < 20)


num=int(input("请输入一个整数数"))
print(f"{num}在10到20之间",num<=10 or num>=20)


