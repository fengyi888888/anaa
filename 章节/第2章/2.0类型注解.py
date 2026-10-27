

a=596
score1=98.5
hobby="Python"
flag=True
pic=False


name=["A","B","C",100]
phones={"10086","155596","566666"}
options={"count":2,"total":2}
goods=("手机",699,1)


name.append("X")
name.append(1000)
name.append(1.2)
print(name)


name1:int=10
goods1:tuple[str,int]=("手机",100)



###############################################################函数类型注解##############################################################################3

def circle_area(r:float) -> tuple[float,float]:
    area = r*r*3.14
    return round(area,1),round(2*3.14*r,1)

area=circle_area(5.0)
print(area)







def calc_order_cost(*kwargs:tuple[str,float,int],coupon:int=0,score:int=0,express:float =0.0):

    total_price=[i[1]*i[2] for i in kwargs]
    total_cost=sum(total_price)

    #2.扣减优惠劵
    if total_cost>=5000 and coupon<=total_cost:
        total_cost-=coupon

    #3.扣减积分抵扣
    if total_cost>=5000 and  score//100<=total_cost:
        total_cost-=score//100

    #4.添加运费
    total_cost+=express
    return total_cost


total =calc_order_cost(("鼠标",188,2),("手机",5666,1),("键盘",500,1),coupon=50,score=5000,express=9.9)
print(total)














