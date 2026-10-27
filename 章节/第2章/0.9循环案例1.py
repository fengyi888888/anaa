# account=input("请输入你的账号")
# password=input("请输入你的密码")
# while (account!="123456"and password!="123456") and (account!="12345" and password!="12345") and (account!="1234" and password!="1234")and(account=="" or password==""):
#     account=input("请重新输入账号")
#     password=input("请重新输入密码")
# else:
#     print("登入成功")

# break 只能在循环里出现(结束循环  break跳出循环while的else不会执行)
# continue(只能出现在循环里表示直接进入下一次循环)
while True:
    account=input("请输入账号")
    password=input("请输入密码")
    if account=="123456"and password=="123456":
        print("登入成功")
        break
    elif account==""or password=="":
        print("账号密码不能为空请重新输入")
        continue #(直接进入下一次循环)
    elif account=="1234"and password=="1234":
        print("登入成功")
        break
    elif account=="12345"and password=="12345":
        print("登入成功")
        break
    else:
        print("请重新输入")
