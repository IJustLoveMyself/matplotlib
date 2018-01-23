#**************coding:utf-8****************
import matplotlib.pyplot as plt
import numpy as np
#plot的属性

# 例1、
# plt.plot([1,4,3,7])
# plt.ylabel("number_test")
# plt.show()
# 如果你向plot()命令提供单个列表或数组，则matplotlib假定它是一个y	值序列，并自动为
# 你生成x值。由于python范围从	0开始，默认x向量具有与y	相同的长度，但从0开始,因此x数据是[0,1,2,3]
# plot()是一个通用命令，并且可接受任意数量的参数。plot（x1,y1,"属性",x2,y2,"属性"...）,
# print type(plt.plot([1,4,3,7])) #<type 'list'>

# plt.plot()对于每个	x,y	参数对（x,y都有，没有少），有一个可选的第三个参数，
# 它是指示图形颜色和线条类型的格式字符串

# 例2、
# x = np.arange(10)
# y = np.arange(10)
# plt.plot(x,y,"rD")
# plt.show()
#画出来的是红色的圆点，r表示红色，o表示实心的圆圈，如果不不加参数，默认格式字符串为"b-"，表示蓝色的线。
# 例3、
# x1 = np.arange(10)
# y1 = np.arange(10)
# x2 = np.arange(10)
# y2 = np.arange(10,20)
# plt.plot(x1,y1,"r-",x2,y2,'b-') #画两条线，可以画三条....但是每对x和y后面只能跟一个指示图形颜色和线条类型的字符串参数
# plt.show()

# character	description
# ‘-‘	        solid line style  实线 ——
# ‘--’	        dashed line style 由短线构成的虚线 ----
# ‘-.’	        dash-dot line style 短线+点 -.-. (点和短线在一条线上)
# ‘:’	        dotted line style 由点构成的线 ....
# ‘.’	        point marker 用点来标记数据点
# ',’	        pixel marker
# ‘o’	        circle marker
# ‘v’	        triangle_down marker
# ‘^’	        triangle_up marker
# ‘<’	        triangle_left marker
# ‘>’	        triangle_right marker
# ‘1’	        tri_down marker
# ‘2’	        tri_up marker
# ‘3’	        tri_left marker
# ‘4’	        tri_right marker
# ’s’	        square marker
# ‘p’	        pentagon marker
# ‘*’	        star marker
# ‘h’	        hexagon1 marker
# ‘H’	        hexagon2 marker
# ‘+’	        plus marker
# ‘x’	        x marker
# ‘D’	        diamond marker
# ‘d’	        thin_diamond marker 菱形
# ‘|‘           vlint marker
# ‘_’	        hline marker
#
# character	color
# ‘b’	        blue
# ‘g’	        green
# ‘r’	        red
# ‘c’	        cyan
# ‘m’	        magenta
# ‘y’	        yellow
# ‘k’	        black
# ‘w’	        white

# 例2只是简单的属性设置
# 属性的设置有三种方式：
# 方式1 直接在plot()函数中设置
# 例3、
# x = np.arange(10)
# y = np.arange(10)
# plt.plot(x,y,color = "r",linewidth = 3) #这样设置属性的画plot（）中只能设置一对xy的值
# plt.show()

# 通过获取plt.plot()创建的对象，通过对象来设置属性。
# 例4、
# x1 = np.arange(5)
# y1 = np.arange(5)
# x2 = np.arange(6,10)
# y2 = np.arange(6,10)
# x3 = np.arange(11,15)
# y3 = np.arange(11,15)
# line1,line2,line3 = plt.plot(x1,y1,x2,y2,x3,y3)
# line1.color = 'r'
# line2.color = 'c'
# line3.color = 'k'
# line1.linewidth = 2
# line2.linewidth = 4
# line3.linewidth = 6
# plt.show()


# 使用setp（）函数设置属性
# 例5、
# x1 = np.arange(5)
# y1 = np.arange(5)
# x2 = np.arange(6,10)
# y2 = np.arange(6,10)
# x3 = np.arange(11,15)
# y3 = np.arange(11,15)
# line1,line2,line3 = plt.plot(x1,y1,x2,y2,x3,y3)
# plt.setp(line1,color = 'r',linewidth = 3)
# plt.setp(line1,color = 'y',linewidth = 3)
# plt.setp(line1,color = 'k',linewidth = 3)
# plt.show()


# plt.plot()的参数
#
# Property	                     Value Type
# alpha	                         控制透明度，0为完全透明，1为不透明
# animated	                     [True False]
# antialiased or aa	             [True False]
# clip_box	                     a matplotlib.transform.Bbox instance
# clip_on	                     [True False]
# clip_path	                     a Path instance and a Transform instance, a Patch
# color or c	                 颜色设置
# contains	                     the hit testing function
# dash_capstyle	                 [‘butt’ ‘round’ ‘projecting’]
# dash_joinstyle	             [‘miter’ ‘round’ ‘bevel’]
# dashes	                     sequence of on/off ink in points
# data	                         数据(np.array xdata, np.array ydata)
# figure	                     画板对象a matplotlib.figure.Figure instance
# label	                         图示
# linestyle or ls	             线型风格[‘-’ ‘–’ ‘-.’ ‘:’ ‘steps’ …]
# linewidth or lw	             宽度float value in points
# lod	                         [True False]
# marker	                     数据点的设置[‘+’ ‘,’ ‘.’ ‘1’ ‘2’ ‘3’ ‘4’]
# markeredgecolor or mec	     any matplotlib color
# markeredgewidth or mew	     float value in points
# markerfacecolor or mfc	     any matplotlib color
# markersize or ms	             float
# markevery	                     [ None integer (startind, stride) ]
# picker	                     used in interactive line selection
# pickradius	                 the line pick selection radius
# solid_capstyle	             [‘butt’ ‘round’ ‘projecting’]
# solid_joinstyle	             [‘miter’ ‘round’ ‘bevel’]
# transform	                     a matplotlib.transforms.Transform instance
# visible	                     [True False]
# xdata	                         np.array
# ydata	                         np.array
# zorder	                     any number


