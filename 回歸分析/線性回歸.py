import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data0 = 15
list1 = [[0], [1, 55, 74], [2, 71, 91], [3, 72, 98], [4, 70, 87], [5, 63, 90], [6, 40, 64], [7, 50, 76], [8, 55, 81],
         [9, 65, 94], [10, 59, 85], [11, 45, 70], [12, 61, 85], [13, 30, 54], [14, 21, 44], [15, 17, 4], [16, 0, 0]]
data1 = list()
data2 = list()
xdata = list()
ydata = list()
x = [0,100]
y = [0,0]
for i in range(1, data0+1):
    list1[data0+1][1] += list1[i][1]
    list1[data0+1][2] += list1[i][2]
for i in range(4, 11):
    list1[data0+1].append(0)
xber = list1[data0+1][1] = list1[data0+1][1]/data0
yber = list1[data0+1][2] = list1[data0+1][2]/data0
for i in range(1, data0+1):
    list1[i].append(list1[i][1]-xber)
    list1[i].append(list1[i][3]*list1[i][3])
    list1[i].append(list1[i][2]-yber)
    list1[i].append(list1[i][5]*list1[i][5])
    list1[i].append(list1[i][3]*list1[i][5])
    # if (list1[i][7] < 0):
    #     list1[i][7] = list1[i][7]*-1
    list1[data0+1][3] += list1[i][3]
    list1[data0+1][4] += list1[i][4]
    list1[data0+1][5] += list1[i][5]
    list1[data0+1][6] += list1[i][6]
    list1[data0+1][7] += list1[i][7]
b = list1[data0+1][7]/list1[data0+1][4]
a = yber-b*xber
for i in range(1, data0+1):
    list1[i].append(a+b*list1[i][1])
    list1[i].append((list1[i][2]-list1[i][8])*(list1[i][2]-list1[i][8]))
    list1[16].append(
        list1[16][7]/(pow(list1[16][4], 0.5)*pow(list1[16][6], 0.5)))
    list1[16][8]+=list1[i][8]
    list1[16][9]+=list1[i][9]
r = list1[16][7]/(pow(list1[16][4], 0.5)*pow(list1[16][6], 0.5))
s = pow(list1[16][9]/(data0-2), 0.5)
print("number\tx\ty\t(x-x)\t(x-x)^\t(y-y)\t(y-y)^   (x-x)(y-y)\ta+bx    (y-y^)^")
for i in range(1, data0+2):
    print("%.0f\t%.2f\t%.2f\t%4.1f\t%6.2f\t%.3f\t%8.3f   %6.3f\t%6.3f    %8.3f\t" % (
        list1[i][0], list1[i][1], list1[i][2], list1[i][3], list1[i][4], list1[i][5],
        list1[i][6], list1[i][7], list1[i][8], list1[i][9]))
print("b=%.5f\ta=%.5f\tr=%.5f\ts=%.5f" % (b, a, r, s))
plt.axis([0, 100, 0, 100])  # 範圍設定
plt.xlabel('X axis')  # X軸
plt.ylabel('Y axis')  # Y軸
for i in range(1, data0+1):
    xdata.append(list1[i][1])
    ydata.append(list1[i][2])
for i in range(0, 2):
    y[i]=a+b*x[i]
plt.plot(xdata,ydata,'ro')
plt.plot(x,y,color=(100/255,100/255,255/255))
plt.show()