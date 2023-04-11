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
def Rxyz(r,b,a):#XYZ固定角
    return(np.mat([[cos(a)*cos(b),cos(a)*sin(b)*sin(r)-sin(a)*cos(r),cos(a)*sin(b)*cos(r)+sin(a)*sin(r)],
                     [sin(a)*cos(b),sin(a)*sin(b)*sin(r)+cos(a)*cos(r),sin(a)*sin(b)*cos(r)-cos(a)*sin(r)],
                     [-sin(b),cos(b)*sin(r),cos(b)*cos(r)]]))
def Rzyz(r,b,a):#ZYZ歐拉角
    return(np.mat([[cos(a)*cos(b)*cos(r)-sin(a)*sin(r),-cos(a)*cos(b)*sin(r)-sin(a)*cos(r),cos(a)*sin(b)],
                     [sin(a)*cos(b)*cos(r)+cos(a)*sin(r),-sin(a)*cos(b)*sin(r)+cos(a)*cos(r),sin(a)*sin(b)],
                     [-sin(b)*cos(r),sin(b)*sin(r),cos(b)]]))                     
mat=Rzyz(15,25,20)
print(mat)
b=atan2((mat[2,0]**2+mat[2,1]**2)**(1/2),mat[2,2])
a=atan2(mat[1,2]/sin(b),mat[0,2]/sin(b))    
r=atan2(mat[2,1]/sin(b),-mat[2,0]/sin(b))
print('r=',r,'b=',b,'a=',a)