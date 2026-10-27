# 猜数字游戏
# import random
# radom_num=random.randint(1,100)#(生成随机数)
# while True:
#     num=int((input("请输入一个数字:")))
#     if num==radom_num:
#         print("恭喜你猜对了")
#         break
#     elif num>radom_num:
#         print("猜大了")
#         continue
#     elif num<radom_num:
#         print("猜小了")
        # 练习1
total=0
for i in range(1,1001):
    if i%5==0:
        total+=i
print(total)
# 练习2
n=0
m=0
msg="akiwksjakdiklowiqaamnbav"
for i in msg:
    if i=="a":
        n+=1
    elif i=="k":
        m+=1
print(f"一共有那{n}个a")
print(f"一共有那{m}个k")







