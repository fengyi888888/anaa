import requests
from lxml import html
#定义url
target_url="https://www.tiobe.com/tiobe-index/"

#发送请求
response=requests.get(target_url)

# #打印响应内容
# print(response.text)


document=html.fromstring(response.text)

#解析表头_xpath语法
# th_list=document.xpath("//table[@id='top20']/thead/tr/th/text()")
# th_list=document.xpath("/html/body/section/div/article/table[1]/thead/tr/th/text()")
th_list=document.xpath("//*[@id='top20']/thead/tr/th/text()")
print(th_list)


# 解析表格数据
td_list=document.xpath("//table[@id='top20']/tbody/tr")
for td in td_list:
    td=td.xpath("./td/text()")
    print(td)