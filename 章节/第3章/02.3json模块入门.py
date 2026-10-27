import json


#写入文件
user={
    "name":"小帅",
    "age" : 18,
    "gender":"男",
    "hobby":["reading","swimming"]
 }
with   open("resources/user.json","w",encoding="utf_8") as f:
    # ensu_ascii:默认为True,确保所有的数据输出都是ascii编码(非Ascii码会转义);False:飞ascii码不转义
    # indent: 会在输出的json文件中缩进(格式化)
    json.dump(user,f,ensure_ascii=False,indent=2)


#读取json文件

with open("resources/user.json","r",encoding="utf-8") as f:
    user=json.load(f)
    print(user)