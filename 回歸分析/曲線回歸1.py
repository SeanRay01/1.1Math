import matplotlib.pyplot as plt
import math
data0 = 10
j = 0
list0 = [[0], [1, 0,0], [2, 0,0], [3, 0,0], [4, 0,0], [5, 0,0], [6, 0,0], [7, 0,0]
        , [8, 0,0], [9, 0,0], [10, 0,0], [11, 0,0], [12, 0,0], [13, 0,0], [14, 0,0], [15, 0,0]
        , [16, 0,0], [17, 0,0], [18, 0,0], [19, 0,0], [20, 0,0], [21, 0,0], [22, 0,0], [23, 0,0]
        , [24, 0,0], [25, 0,0], [26, 0,0], [27, 0,0], [28, 0,0], [29, 0,0], [30, 0,0], [31, 0,0]]
list2 = [[0], [1, 3,16], [2, 7,34], [3, 8,40], [4, 12,93], [5, 14,125],
         [6, 9,50], [7, 9,48], [8, 4,18], [9, 11,70], [10, 13,110],
         [11,12,85],[12,8,45],[13,7,40],[14,6,33],[15,3,20],[16]]
list1 = [[0], [1, 750, 50], [2, 800, 15], [3, 700, 100], [4, 850, 9], [5, 590, 950],
         [6, 620, 820], [7, 650, 400], [8, 680, 150], [9, 710, 110], [10, 550, 1200],
         [11]]
xs = xb = list1[1][1]
ys = yb = list1[1][2]
xdata = list()
ydata = list()
x = list()
y = list()
for i in range(1, 20):
    list1[data0+1].append(0)
# data0=int(input('數據數量(<=30):'))
for i in range(1, data0+1):
    # print("第%s筆資料:"%i)
    # list1[i][1]=int(input('X值:'))
    # list1[i][2]=int(input('Y值:'))
    list1[i].append(0)
    list1[i][3] = math.log(list1[i][2])
    list1[data0+1][1] += list1[i][1]  # 1
    list1[data0+1][2] += list1[i][2]  # 2
    list1[data0+1][3] += list1[i][3]  # 3
xber = list1[data0+1][1] = list1[data0+1][1]/data0
yber = list1[data0+1][2] = list1[data0+1][2]/data0
ydber = list1[data0+1][3] = list1[data0+1][3]/data0
for i in range(1, data0+1):
    list1[i].append(list1[i][1]-xber)  # 4
    list1[i].append(list1[i][4]*list1[i][4])  # 5
    list1[i].append(list1[i][2]-yber)  # 6
    list1[i].append(list1[i][6]*list1[i][6])  # 7
    list1[i].append(list1[i][3]-ydber)  # 8
    list1[i].append(list1[i][4]*list1[i][8])  # 9
    list1[i].append(list1[i][4]*list1[i][6])  # 10
    list1[i].append(list1[i][8]*list1[i][8])  # 11
    # if (list1[i][9] < 0):
    #     list1[i][9] = list1[i][9]*-1
    # if (list1[i][10] < 0):
    #     list1[i][10] = list1[i][10]*-1
    list1[data0+1][4] += list1[i][4]
    list1[data0+1][5] += list1[i][5]
    list1[data0+1][6] += list1[i][6]
    list1[data0+1][7] += list1[i][7]
    list1[data0+1][8] += list1[i][8]
    list1[data0+1][9] += list1[i][9]
    list1[data0+1][10] += list1[i][10]
    list1[data0+1][11] += list1[i][11]
b = list1[data0+1][9]/list1[data0+1][5]
B = math.exp(b)
a = ydber-xber*b
A = math.exp(a)
for i in range(1, data0+1):
    list1[i].append(A*(B**list1[i][1]))  # 12
    list1[i].append(pow((list1[i][2]-list1[i][12]), 2))  # 13
    list1[data0+1][12] += list1[i][12]
    list1[data0+1][13] += list1[i][13]
r = list1[data0+1][9]/(pow(list1[data0+1][5], 0.5)* pow(list1[data0+1][11], 0.5))
# print("%.5f=%.5f/(%.5f*%.5f)" % (r, list1[data0+1][10], pow(list1[data0+1][5], 0.5), pow(list1[data0+1][7], 0.5)))
s = pow(list1[data0+1][13]/(data0-2), 0.5)
print("%7s,%7s,%7s,%10s,%10s,%10s,%15s,%15s"
    %('number','x','y','lny','(x-x)','(x-x)^','(lny-lny)','(x-x)(lny-lny)'))
for i in range(1, data0+2):
    print("   %.0f.  / %7.2f / %7.2f / %7.5f / %7.5f / %7.5f / %7.5f / %7.5f" % (
        list1[i][0], list1[i][1], list1[i][2], list1[i][3],
        list1[i][4], list1[i][5], list1[i][8], list1[i][9]))
print("b=%.5f\ta=%.5f\tB=%.5f\tA=%.5f\tr=%.5f    s=%.5f" % (b, a, B, A, r, s))
print('y=%.5f*%.5f^x' % (A, B))
for i in range(1, data0+1):
    xdata.append(list1[i][1])
    ydata.append(list1[i][2])
    if list1[i][1] < xs:
        xs = list1[i][1]
    if list1[i][2] < ys:
        ys = list1[i][2]
    if list1[i][1] > xb:
        xb = list1[i][1]
    if list1[i][2] > yb:
        yb = list1[i][2]
for i in range(int(xs*0.9), int(xb*1.1)):
    x.append(i)
    y.append(A*B**i)
plt.axis([xs-10, xb+100, ys-10, yb+100])  # 範圍設定
plt.xlabel('X axis')  # X軸
plt.ylabel('Y axis')  # Y軸
plt.plot(xdata, ydata, 'ro')
# plt.plot(x, y, 'b.')
plt.plot(x, y, color=(100/255, 100/255, 255/255))
plt.show()