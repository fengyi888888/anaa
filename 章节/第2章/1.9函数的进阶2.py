# 函数的参数类型
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b



# 计算
def calc(a,b,oper):
    return oper(a,b)


print(calc(10,50,add))



# ------------------------------------匿名函数--------------------------------------------------------------------------#\
# 需求1:打印一个分割线
out_line=lambda :print ("-------------------------------------------")

out_line()

# 需求2:计算两个数字的和
add_=lambda a,b:a+b

print(add_(10,10))


# 案例
# 一.定义一个函数,计算阶乘
#递归调用,在函数中自己调用自己---一定要有终结点
def jc(n):
    if n==1:
         return 1
    else:
         return n*jc(n-1)


print(jc(10))




# 二.定义一个函数,根据传入的一批商品,优惠,运费信息算总金额
#1.满优惠劵要满5000才可以使用,且优惠金额不能超过商品本身
#2.积分抵扣需要商品金额满5000才能使用,100积分抵扣1元
def calc_order_cost(*kwargs,coupon,score,express):
    """
    :param kwargs:商品信息(名称,价格,数量)---->如:("鼠标",188,2)
    :param coupon: 优惠劵
    :param score: 积分
    :param express: 快递运费
    :return: 订单的总金额
    """
    #订单的总金额=商品总金额 - 优惠劵 - 积分抵扣 +运费
    #1.计算商品总金额
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

















