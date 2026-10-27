class Shopping:
    def __init__(self,name,price,num,):
        self.name=name
        self.price=price
        self.num=num

    def __str__(self):
        return f"商品名字{self.name} | 商品价格 {self.price} | 商品数量 {self.num} |"
    def update_shopping(self,name=None,price=None,num=None):
        input("请输入需要修改的商品名称:")
        if name is not None:
            self.name=name
            self.price=price
            self.num=num
            return
class Shopping_mangage:
    system_version = 0.1
    system_name = "教务系统"

    def __init__(self):
        self.shopping_list = []
    def add_shopping(self):
        name=input("请添加你的商品名称`")
        for s in self.shopping_list:
            if name==s.name:
                print("该商品已经存在,添加失败!")
                return
        price=float(input("请添加你的商品价格"))
        num =int(input("请添加你的商品数量"))
        shoppy=Shopping(name,price,num)
        self.shopping_list.append(shoppy)
    def update_shopping(self):
        name = input("请输入修改的商品名称`")
        for s in self.shopping_list:
            print(f"当前商品信息为{s}")
            if name==s.name:
                name = input("请输入修改的商品名称`")
                price=float(input("请输入修改的商品价格"))
                num=int(input("请输入修改的商品数量"))
                Shopping.update_shopping(name,price,num)
                print("修改后的商品数据为`")
                return
            else:
                 print("未找到该商品信息,修改失败")
                 return
    def delete_shopping(self):
        name = input("请输入删除的商品名称`")
        for s in self.shopping_list:
            if name==s.name:
                self.shopping_list.remove(s)
                print("删除成功")
                return
            else:
                print("未找到该商品信息,删除失败")
                return
    def query_shopping(self):
            name = input("请输入查询的商品名称`")
            for s in self.shopping_list:
                if name==s.name:
                       print(f"当前所有商品信息为{s}")
    def  run(self):
        while True:
            print()
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print("#  1.添加商品信息  2.修改商品信息  3.删除商品信息  4.查询商品信息  5.退出菜单 #")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # ## # # # # # ## # # ")
            choice = input("请选择你的操作,输入1~5")
            match choice:
                case "1":
                    self.add_shopping()
                case "2":
                    self.update_shopping()
                case "3":
                    self.delete_shopping()
                case "4":
                    self.query_shopping()
                case "5":
                    print("退出菜单 Bey~")
                    break
                case _:
                    print("操作错误,请输入1~5")

if __name__ == "__main__":
    shopping = Shopping_mangage()
    shopping.run()






