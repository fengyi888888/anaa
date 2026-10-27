from lxml import html

#读入html文件
with open("resources/凡人修仙传.html","r",encoding="utf-8") as f:
    html_doc=f.read()

    #解析html文件,将其转换为一个文档
    tree=html.fromstring(html_doc)

    #解析表头_xpath语法
    title=tree.xpath("//title/text()")
    print(title)
