# if条件判断
# score = 681
# if score>=680:
#     print("欢迎您")
#     print("你好")
    # 案例
# ok_account="123456"
# ok_password="123456"
# account=input("账号")cd/////////////////////////
# password=input("密码")
# if  account==ok_account and password==ok_password:
#     print("登入成功")
# if account!=ok_account or password!=ok_password:
#     print("请重新输入")
# ok_account = "123456"
# ok_password = "123456"
# account = input("账号")
# password = input("密码")
# if account == ok_account and password == ok_password:
#     print("登入成功")
# else:
#     print("请重新输入")


    # 案例
# year=int(input("请输入年份"))
# if year%4==0 and year%100!=0 or year%400==0:
#     print("是闰年")
# else:
#     print("平年")


#if-->elif-->else
# num=int(input("请输入"))
# if num>0:
#     print(f"{num}是正数")
# elif num<0:
#     print(f"{num}是负数")
# else:
#     print(f"{num}是0")


# 案例
ok_account1="123456"
ok_account2="12345"
ok_account3="1234"
ok_password1="123456"
ok_password2="12345"
ok_password3="1234"
account=input("账号")
password=input("密码")
if account==ok_account1 and password==ok_password1:
    print("登入成功")
elif account==ok_account2 and password==ok_password2:
    print("登入成功")
elif account==ok_account3 and password==ok_password3:
    print("登入成功")
else:
    print("登入失败")















