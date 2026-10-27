#读文件
"""
路径：
    相对路径：从当前目录开始查找(推荐)
    . :当前目录  --->./resources/静夜思.txt ./可以省略
    .. :上一级目录 --->  ../第2章./file/寻隐者不遇.txt----../../第2章./file/寻隐者不遇.txt
    绝对路径：从盘符开始查找,文件位置的的完整路径  (注意: \在字符串中表示的是转义字符,\n,\t)
    D:\\pythonproject\\章节\\第3章\\resources\\望庐山瀑布.txt 或者使用/

      注意：
        相对路径不能跨目录
        相对路径不能跳出当前目录
        相对路径不能跳出当前盘符
"""
with open('D:\\pythonproject\\章节\\第3章\\resources\\望庐山瀑布.txt', 'r', encoding='utf-8') as f:
    content=f.read()
    print(content)



#写文件
with open('D:\\pythonproject\\章节\\第3章\\resources\\望庐山瀑布.txt', 'a', encoding='utf-8') as f:
    f.write("\n\n望庐山瀑布(李白)\n\n")
    f.write("日照香炉生紫烟，\n")
    f.write("遥看瀑布挂前川。\n")
    f.write("飞流直下三千尺，\n")
    f.write("疑是银河落九天。\n")