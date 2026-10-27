a,b,c=100,200,300
e=a
d=b
b=e
e=c
a=e
c=d
print(a,b,c)

# 初始化变量
a = 100
b = 200
c = 300

# 交换变量：将 a,b,c 的值分别赋值给 c,a,b
a, b, c = c, a, b

# 输出结果
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
