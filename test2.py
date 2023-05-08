import numpy as np
import matplotlib.pyplot as plt
pi=np.pi
# 建立 3D 圖形
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
def sin(t):
    return(np.round(np.sin(t/180*pi),9))
def cos(t):
    return(np.round(np.cos(t/180*pi),9))
def ten(t):
    return(np.round(np.tan(t/180*pi),9))
def atan2(x,y):
    return(round(np.arctan2(y,x)*180/pi,5))
def DQ(x,y,z):#平移算式
    return(np.mat([[1,0,0,x],
                     [0,1,0,y],
                     [0,0,1,z],
                     [0,0,0,1]],dtype='float'))
def Rx(t):#X旋轉
    return(np.mat([[1,0,0],
                     [0,cos(t),-sin(t)],
                     [0,sin(t),cos(t)]]))
def Ry(t):#Y旋轉
    return(np.mat([[cos(t),0,sin(t)],
                     [0,1,0],
                     [-sin(t),0,cos(t)]]))
def Rz(t):#Z旋轉
    return(np.mat([[cos(t),-sin(t),0],
                     [sin(t),cos(t),0],
                     [0,0,1]]))  
def T(r,dq):#一般變換!!!
    dq[0:3,0:3]=r
    return(dq)
def DH(i,a,alpha,d,theta):
    i-=1
    return(np.mat([[cos(theta[i]),-sin(theta[i])*cos(alpha[i]),sin(theta[i])*sin(alpha[i]),a[i]*cos(theta[i])],
                     [sin(theta[i]),cos(theta[i])*cos(alpha[i]),-cos(theta[i])*sin(alpha[i]),a[i]*sin(theta[i])],
                     [0,sin(alpha[i]),cos(alpha[i]),d[i]],
                     [0,0,0,1]]))
def SixAxisModel(a_list,alpha,d_list,theta):
    t1=[]
    t2=[DQ(0,0,0)]
    for i in range(1,7):
        t1.append(DH(i,a_list,alpha,d_list,theta))
    data=np.mat([[1,0,0,0],
                [0,1,0,0],
                [0,0,1,0],
                [0,0,0,1]])
    print('-'*10,'t01','-'*10,'\n',data)
    for i,j in enumerate(t1):
        data=data*j
        print('-'*10,f't0{i+2}','-'*10,'\n',data)
        t2.append(data)
    return(t2)
def inverse_kinematics(a_list,d_list,t06):
    theta=[0,1,2,3,4,5,6]
    o=[0,t06[0,3],t06[1,3],t06[2,3]]
    r=[[0],[0,t06[0,0],t06[0,1],t06[0,2]],[0,t06[1,0],t06[1,1],t06[1,2]],[0,t06[2,0],t06[2,1],t06[2,2]]]
    x=o[1]-d_list[5]*r[1][3]
    y=o[2]-d_list[5]*r[2][3]
    z=o[3]-d_list[5]*r[3][3]
    # print(x,y,z)
    d=round((x**2+y**2+(z-d_list[0])**2-a_list[1]**2-a_list[2]**2)/(2*a_list[1]*a_list[2]),8)
    theta[1]=atan2(x,y)
    theta[3]=(atan2(d,(1-d**2)**0.5))
    theta[2]=atan2((x**2+y**2)**0.5,z-d_list[0])-atan2(a_list[1]+a_list[2]*cos(theta[3]),a_list[2]*sin(theta[3]))
    theta[5]=atan2(r[1][3]*sin(theta[1])-r[2][3]*cos(theta[1]),(1-(r[1][3]*sin(theta[1])-r[2][3]*cos(theta[1]))**2)**0.5)
    theta[4]=atan2(r[1][3]*cos(theta[1])*cos(theta[2]+theta[3])+r[2][3]*sin(theta[1])*cos(theta[2]+theta[3])+r[3][3]*sin(theta[2]+theta[3]),-r[1][3]*cos(theta[1])*cos(theta[2]+theta[3])-r[2][3]*sin(theta[1])*sin(theta[2]+theta[3])+r[3][3]*cos(theta[2]+theta[3]))
    theta[6]=atan2(-r[1][1]*sin(theta[1])+r[2][1]*cos(theta[1]),r[1][2]*sin(theta[1])-r[2][2]*cos(theta[1]))
    return(theta)
def plot_dot(t1,t2):
    x=np.linspace(t1[0,3],t2[0,3], 2)
    y=np.linspace(t1[1,3],t2[1,3], 2)
    z=np.linspace(t1[2,3],t2[2,3], 2)
    ax.plot(x,y,z)
    # print(x,y,z)
    ax.scatter(x,y,z, c=z, cmap='jet')
def plot(t):
    #繪製坐標軸
    x=np.linspace(-2000, 2000, 100)
    y=np.linspace(0,0, 100)
    z=np.linspace(0,3500, 100)
    ax.plot(x,y,y, color='red')   #畫出三軸資料所構成的曲面
    ax.plot(y,x,y, color='red')   #畫出三軸資料所構成的曲面
    ax.plot(y,y,z, color='red',label='coordinate')   #畫出三軸資料所構成的曲面
    #繪製手臂位置
    for i in range(6):
        plot_dot(t[i],t[i+1])
    # 顯示圖例
    ax.legend()
    # 顯示圖形
    plt.show()
# DH_Model
a_list = [0,750,750,0,0,0]#參數
alpha =  [90,0,0,-90,90,0]#參數
d_list = [1500,0,0,0,0,500]#參數
thetas = [0,0,0,0,0,0]#參數
t=SixAxisModel(a_list,alpha,d_list,thetas)#計算DH-Model
theta=inverse_kinematics(a_list,d_list,t[6])#計算逆運動學
print('\n\tinverse_kinematics\n',theta)
plot(t)#繪圖
