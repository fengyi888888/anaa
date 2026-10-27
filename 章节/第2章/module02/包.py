# import utils.my_fun
#
# utils.my_fun.log_separator1()

# from utils import my_fun
# my_fun.log_separator1()


#注意如果要这种方式导入的所有模块,要在__init__中添加__all__[]
# from utils import *
#
# my_fun.log_separator1()
#
# print(my_var.PI)
# print(my_var.NAME)

#绝对路径
from  章节.第2章.utils.my_fun import log_separator1,log_separator3

log_separator1()
log_separator3()


