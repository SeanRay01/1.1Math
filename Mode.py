import numpy as np
pi=np.pi
def P3(x,y,z):#位置矢量
    return(np.mat([[x],[y],[z]]))
def sin(t):
    return(np.round(np.sin(t/180*pi),9))
def cos(t):
    return(np.round(np.cos(t/180*pi),9))
def ten(t):
    return(np.round(np.tan(t/180*pi),9))
def atan2(x,y):
    return(round(np.arctan2(x,y)*180/pi,5))
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
def DQ(x,y,z):#平移算式
    return(np.mat([[1,0,0,x],
                     [0,1,0,y],
                     [0,0,1,z],
                     [0,0,0,1]],dtype='float'))
def T(r,dq):#一般變換!!!
    dq[0:3,0:3]=r
    return(dq)
def Rxyz(r,b,a):#XYZ固定角
    return(np.mat([[cos(a)*cos(b),cos(a)*sin(b)*sin(r)-sin(a)*cos(r),cos(a)*sin(b)*cos(r)+sin(a)*sin(r)],
                     [sin(a)*cos(b),sin(a)*sin(b)*sin(r)+cos(a)*cos(r),sin(a)*sin(b)*cos(r)-cos(a)*sin(r)],
                     [-sin(b),cos(b)*sin(r),cos(b)*cos(r)]]))
def Rzyz(r,b,a):#ZYZ歐拉角
    return(np.mat([[cos(a)*cos(b)*cos(r)-sin(a)*sin(r),-cos(a)*cos(b)*sin(r)-sin(a)*cos(r),cos(a)*sin(b)],
                     [sin(a)*cos(b)*cos(r)+cos(a)*sin(r),-sin(a)*cos(b)*sin(r)+cos(a)*cos(r),sin(a)*sin(b)],
                     [-sin(b)*cos(r),sin(b)*sin(r),cos(b)]]))                     
def Rk(th,x,y,z):#等效角
    return(np.mat([[x*x*(1-cos(th))+cos(th),y*x*(1-cos(th))-z*sin(th),z*x*(1-cos(th))+y*sin(th)],
                     [x*y*(1-cos(th))+z*sin(th),y*y*(1-cos(th))+cos(th),z*y*(1-cos(th))-x*sin(th)],
                     [x*z*(1-cos(th))-y*sin(th),y*z*(1-cos(th))+x*sin(th),z*z*(1-cos(th))+cos(th)]]))
def DH(i,a,alpha,d,theta):
    i-=1
    return(np.mat([[cos(theta[i]),-sin(theta[i])*cos(alpha[i]),sin(theta[i])*sin(alpha[i]),a[i]*cos(theta[i])],
                     [sin(theta[i]),cos(theta[i])*cos(alpha[i]),-cos(theta[i])*sin(alpha[i]),a[i]*sin(alpha[i])],
                     [0,sin(alpha[i]),cos(alpha[i]),d[i]],
                     [0,0,0,1]]))
#位移
print('====================\n\t位移')
p1=P3(0,0,0)
p2=P3(50,0,0)
p3=P3(30,0,0)
degree=[0,30,45]
o00=p1
print(o00)
o01=p1+Rz(-degree[1]).T*p2
print(o01)
o02=o01+Rz(-degree[2]).T*p3
print(o02)
#ZYZ歐拉角
print('=========================\n\tZYZ歐拉角')
mat=Rzyz(15,25,20)#參數
print(mat)
b=atan2((mat[2,0]**2+mat[2,1]**2)**(1/2),mat[2,2])
a=atan2(mat[1,2]/sin(b),mat[0,2]/sin(b))    
r=atan2(mat[2,1]/sin(b),-mat[2,0]/sin(b))
print('r=',r,'b=',b,'a=',a)
#DH model
print('=========================\n\tDH model')
a_list = [0,0,0]#參數:a
alpha =  [0,-90,0]#參數:阿法
d_list = [10,20,30]#參數:d
theta =  [45,0,0]#參數:西達
t01=DH(1,a_list,alpha,d_list,theta)
t12=DH(2,a_list,alpha,d_list,theta)
t23=DH(3,a_list,alpha,d_list,theta)
t03=t01*t12*t23
print(t01)
print(t12)
print(t23)
print(t03)
#位移
print('====================\n\t位移')
h01=DQ(0,100,0)*DQ(0,0,100)
h12=DQ(-50,0,0)*DQ(0,50,0)
h23=DQ(0,0,200)*T(Rz(90),DQ(0,0,0))*T(Rx(180),DQ(0,0,0))
h03=h01*h12*h23
print(h01)
print(h12)
print(h23)
print(h03)