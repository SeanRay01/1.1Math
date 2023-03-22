import numpy as np
pi=np.pi
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
    return(np.mat([[cos(t),sin(t),0],
                     [0,1,0],
                     [-sin(t),0,cos(t)]]))
def Rz(t):#Z旋轉
    return(np.mat([[cos(t),-sin(t),0],
                     [sin(t),cos(t),0],
                     [0,0,1]]))
def Rzyz(r,b,a):#ZYZ歐拉角
    return(np.mat([[cos(a)*cos(b)*cos(r)-sin(a)*sin(r),-cos(a)*cos(b)*sin(r)-sin(a)*cos(r),cos(a)*sin(b)],
                     [sin(a)*cos(b)*cos(r)+cos(a)*sin(r),-sin(a)*cos(b)*sin(r)+cos(a)*cos(r),sin(a)*sin(b)],
                     [-sin(b)*cos(r),sin(b)*sin(r),cos(b)]]))  
mat=Rzyz(30,0.00001,10)
print(mat)
b=atan2((mat[2,0]**2+mat[2,1]**2)**(1/2),mat[2,2])
a=atan2(mat[1,2]/sin(b),mat[0,2]/sin(b))
r=atan2(mat[2,1]/sin(b),-mat[2,0]/sin(b))
print('r=',r,'b=',b,'a=',a)