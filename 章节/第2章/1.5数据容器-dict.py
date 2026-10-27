#  字典：使用键值对（key: value）来存储数据，每一个键都对应一个值，通过键（key）可以快速找到对应的值（value）。
# • 特点：键值对（key: value）存储、键（key）不能重复、可修改.  value可以任何类型的数据,key不能为可变数据类型(如不能为 list set dict)
# 字典---key不能重复如果重复后面覆盖前面的值
# dict1 = {"王林":670,"李慕婉":680,"徐立国":580,"韩立":688}
# print(dict1)
# print(type(dict1))
# # 访问
# print(dict1["王林"])#获取
# dict1["王林"] =688#修改
# print(dict1)
dict1 = {"王林":670,"李慕婉":680,"徐立国":580,"韩立":688}
#
# # 添加-key不存在
# dict1["帅哥"]=600
# print(dict1)
#
# # 修改-key存在
# dict1["帅哥"]=699
# print(dict1)
#
# # 查询
# print(dict1["帅哥"])
# print(dict1.get("帅哥"))
#
# print(dict1.keys())#获取所有的key
# print(dict1.values())#获取所有的value
# print(dict1.items())#获取所有的key和value
#
# # 删除
# score=dict1.pop("徐立国")
# print(score)
# print(dict1)
#
#
# del dict1["韩立"]
# print(dict1)
#
# # 遍历
for k in dict1.keys():
    print(f"{k}: {dict1[k]}")
#
# for item in dict1.items():
#     print(f"{item[0]} : {item[1]}")
# for k,v in dict1.items():
#     print(f"{k} : {v}")



#案例
# 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，通过控制台菜单与用户交互。具体功能如下：
#
# 1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
# 5. 退出购物车

shopping_cart = {}

#1.制作菜单
print("欢迎使用购物车管理系统")
# menu="""
# ########  购物车系统  ########
# #        1.添加购物车s_name=       #
# #        2.修改购物车        #
# #        3.删除购物车        #
# #        4.查询购物车        #
# #        5.退出购物车        #
# ############################
# """
#
#
# while True:
#     # 2.执行的具体操
#     print(menu)
#     choice = input("请选择要选择的操作(1-5):")
#     match choice:
#         case "1":  # 添加购物车的操作
#             good_name = input("请输入商品名称:")
#             good_price = float(input("请输入商品价格:"))
#             good_num = int(input("请输入商品数量:"))
#             # 如果商品存在则不添加,提示信息
#             if good_name in shopping_cart:
#                 print("该商品已存在请重新选择")
#             else:
#                 shopping_cart[good_name] = {"price": good_price, "num": good_num}
#                 print("商品添加完毕")
#         case "2":  # 修改购物车
#             change_good_name = input("请输入修改的商品")
#             if change_good_name in shopping_cart:
#                 change_good_price = float(input("请输入修改的商品价格"))
#                 change_good_num = int(input("请输入修改的商品数量"))
#                 shopping_cart[change_good_name] = {"price": change_good_price, "num": change_good_num}
#                 print("修改完毕")
#             else:
#                 print("该商品不存在")
#
#         case "3":  # 删除购物车
#             good_name = input("请输入商品名称:")
#             if good_name not in shopping_cart:
#                 print("该商品不存在")
#             else:
#                 shopping_cart.pop(good_name)
#                 print("删除完毕")
#         case "4":  # 查询购物车
#             for good_name in shopping_cart:
#                 good = shopping_cart[good_name]
#                 print(f"商品名称:{good_name},商品价格:{good["price"]},商品数量:{good["num"]}")
#         case "5": # 提出购物车
#             print("Bey ~ ")
#             break
#         case _:  # 匹配其他情况
#             print("非法操作,不支持!!!")
#
#

