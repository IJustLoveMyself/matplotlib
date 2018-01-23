#**************coding:utf-8****************
import matplotlib.pyplot as plt

#图例、标题和标签

# 例1、

# 方法A
# x1 = [1,2,3]
# y1 = [4,5,6]
# x2 = [7,8,9]
# y2 = [10,11,12]
# plt.plot(x1,y1,label = "line1") # 线1
# plt.plot(x2,y2,label = "line2") # 线2
# plt.xlabel("x_axis") # x轴的名字
# plt.ylabel("y_axis") # y轴的名字
# plt.title("line_test") #生成的图的标题
# plt.legend(loc = 0) #
# plt.show()

# 方法B
# x1 = [1,2,3]
# y1 = [4,5,6]
# x2 = [7,8,9]
# y2 = [10,11,12]
# line1, = plt.plot(x1,y1) # 线1
# line2,= plt.plot(x2,y2) # 线2
# plt.xlabel("x_axis") # x轴的名字
# plt.ylabel("y_axis") # y轴的名字
# plt.title("line_test") #生成的图的标题
# plt.legend([line1,line2],["line1","line2"],loc = 0) # 显示图例,前两个参数是序列
# plt.show()

# 方法A和方法B最终的效果相同
# 关于plt.legend
# 参数loc的取值
# 'best'         : 0, (only implemented for axes legends)(自适应方式)
# 'upper right'  : 1,
# 'upper left'   : 2,
# 'lower left'   : 3,
# 'lower right'  : 4,
# 'right'        : 5,
# 'center left'  : 6,
# 'center right' : 7,
# 'lower center' : 8,
# 'upper center' : 9,
# 'center'       : 10,

