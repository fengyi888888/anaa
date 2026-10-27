# for循环:遍历输入的字符串
# msg =input("请输入遍历的字符")
# for i in msg:#i表示遍历出来的元素;msg表示需要遍历的元素
#     print(f"元素{i}")
# else:
#     print("循环结束")
    # 案例 range函数(end)0~end-1   (start,end)start~end-1   (start,end.step)-->range(0,10,2)--0,20.4.6.8
# total = 0
# for i in range(101):
#     if i % 2 != 0:
#         total += i
# print(f"100以内的奇数和为:{total}")
# total = 0
# for i in range(100,501):
#     if i % 3 == 0:
#         total += i
# print(f"100到500的3倍数和为:{total}")

# 案例打印长方形
# print("*")默认换行
#print("*",end"":end表示的是每一次输出以什么结束;默认\n,表示换行
# m=int(input("请输入长"))
# n=int(input("请输入宽"))
# for o in range(n):
#     for i in range(m):
#         print("*", end="")
#     print()
# 案例j九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}x{i}={i*j}",end="\t")
#     print()

# a=int(input("请输入边长"))
# for i in range(a):
#     for j in range(i+1):
#        print("*",end=" \t")
#     print()

# a=int(input("请输入数字"))
# for i in range(1,a+1):
#     for j in range(1,i+1):
#        print(f"{j}",end=" \t")
#     print()


for i in range(1,9):
    for j in range(1,9):
        if (i+j)%2!=0:
            print("▢",end="\t")
        else:
            print("▣",end="\t")
    print()




















