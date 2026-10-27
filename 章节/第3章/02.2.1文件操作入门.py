# #读取文件
# 1. 打开文件
f= open("./resources/望庐山瀑布.txt","r",encoding="utf-8")


# 2. 读取文件

# content=f.read()#读取全部内容
# print(content)

content_list=f.readlines()#读取所有行
for line in content_list:
    print(line)
    print(line.strip())#去除换行符
# 3. 关闭文件
f.close()





#写文件
# # 1. 打开文件
# f= open("./resources/静夜思.txt","w",encoding="utf-8")
#
# #2.书写内容
# f.write("静夜思(李白)\n\n")
# f.write("床前明月光，\n")
# f.write("疑是地上霜。\n")
# f.write("举头望明月，\n")
# f.write("低头思故乡。\n")
#
#
#
# # 3. 关闭文件
# f.close()



#######################====================释放资源=======================================

# =============================================================方式一=================================================
# 1. 打开文件
# f= open("./resources/静夜思.txt","w",encoding="utf-8")
#
# #2.书写内容
# try:
#         i=1/0
#         f.write("静夜思(李白)\n\n")
#         f.write("床前明月光，\n")
#         f.write("疑是地上霜。\n")
#         f.write("举头望明月，\n")
#         f.write("低头思故乡。\n")
#
#
# finally:
# # 3. 关闭文件
#         print("文件关闭")
#         f.close()





# =============================================================方式二(最佳方式)=================================================


# with 语句(上下文管理器)的核心作用是确保资源总能正确的获取和释放(即使发生异常,也会被正确释放),也是项目开发中的推荐方式

# with open("./resources/静夜思.txt","w",encoding="utf-8") as f:
#         f.write("静夜思(李白)\n\n")
#         f.write("床前明月光，\n")
#         f.write("疑是地上霜。\n")
#         f.write("举头望明月，\n")
#         f.write("低头思故乡。\n")
#         f.close()
