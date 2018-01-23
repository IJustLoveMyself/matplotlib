#***********coding:utf-8***********************
import matplotlib.pyplot as plt
import numpy as np

# 创建多图
# plt.subplot(fignum,numcols,numrows)
# fignum总共的子图的个数
# numcols 子图所在的列数
# numrows 子图所在的行数
# 例1、
x1 = np.arange(0,360)
y1 = np.sin(np.pi*x1/180)
y2 = np.cos(np.pi*x1/180)
y3 = x1
plt.figure(1)

plt.subplot(3,1,1)
line1, = plt.plot(x1,y1,"r:")
plt.legend([line1],["sin"])

plt.subplot(3,1,2)
line2, = plt.plot(x1,y2)
plt.legend([line2],["cos"])

plt.subplot(3,1,3)
line3, = plt.plot(x1,y3)
plt.legend([line3],["y=x"])
plt.show()

