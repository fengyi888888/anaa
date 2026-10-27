import re


s1="17345678909是我的手机号,我的qq号是314319283"
s2="我的手机号是14344211111,我的qq号是314319283,另外一个手机号是1634566666666"


#match-从字符串的开头开始匹配(匹配第一个匹配项)  --->Match对象
result=re.match(r"1[3-9]\d{9}",s1)
print(result.group())  #匹配的结果
print(result.span())   #匹配项的索引
print(result.start())  #匹配项的起始索引
print(result.end())    #匹配项的结束索引


# search-从字符串的任意位置开始匹配(匹配第一个匹配项)  --->Match对象
result=re.search(r"1[3-9]\d{9}",s2)
print(result.group())  #匹配的结果
print(result.span())   #匹配项的索引
print(result.start())  #匹配项的起始索引
print(result.end())    #匹配项的结束索引


# findall-从字符串的任意位置开始匹配(匹配所有匹配项)  --->列表
result=re.findall(r"1[3-9]\d{9}",s2)
print(result)

