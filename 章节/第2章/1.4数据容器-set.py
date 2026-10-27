# set集合是无序的,不可重复的,可修改的数据容器
s10={"c","d","e","f"}
# 定义空集合
s=set()

s1={100,200,300,400,500,600,700,800}
print(s1)

s1.add(1200)
print(s1)

#remove删除集合中的指定元素(没有将报错)
s1.remove(200)
print(s1)


#随机删除集合中的元素并返回
e=s1.pop()
print(e)
print(s1)

#clear()清空集合
s1.clear()
print(s1)

s2={"A","B","C","D","E","X","Y"}
s3={"C","E","Y","Z"}

#differrnt(存在于第一个集合不存在第二个)
print(s3.difference(s2))
print(s2.difference(s3))

#union()两个集合的并集
print(s2.union(s3))

#intersection():求两个集合的交集
print(s2.intersection(s3))

# 案例
# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = {"遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

# 1.找出同时修法学和艺术的
# 方式一
print(f"同时修 法学 和 艺术 的有{french_set.intersection(art_set)}")

# 方式二& -->交集
fa=french_set & art_set
print(f"同时修 法学 和 艺术 的有{fa}")

#2.找出同时修四门学科的人
# 方法一
teg1=french_set.intersection(art_set)
teg2=football_set.intersection(basketball_set)
teg=teg1.intersection(teg2)
print(f"共同修四门的人有{teg}")

# 方法二
all_set=french_set & football_set & basketball_set & art_set
print(f"共同修四门的人有{all_set}")

#3.找出选了足球但是没有选择没有选择篮球的学生-->差集
# 方式一
print(f"选了足球但是没有选择没有选择篮球的学生{football_set.difference(basketball_set)}")

# 方式二 -  --->差集
print(f"选了足球但是没有选择没有选择篮球的学生{football_set -basketball_set}")

# 方式三:集合推导式--->快速构建集合,语法:{要往集合中添加的元素  for s in set1}
fb_set={ s  for s in football_set if s not in basketball_set}
print(f"选了足球但是没有选择没有选择篮球的学生{fb_set}")

#4.统计每一个学生的选修的课程数量
#4.1获取到学生名单--并集(|)
# allset=football_set.union(basketball_set).union(french_set).union(art_set)
allset=football_set | basketball_set | art_set |french_set
print(allset)

#4.2获取每一个学生选修的的课程数量
all_list=[*football_set,*basketball_set,*art_set,*french_set]
for s in allset:
     print(f"{s}选修{all_list.count(s)}了课程")


