import numpy as np
import math
pi=np.pi
def sin(t):
    return(round(np.sin(t/180*pi),9))
def cos(t):
    return(round(np.cos(t/180*pi),9))
def ten(t):
    return(round(np.tan(t/180*pi),9))
def atan2(x,y):
    return(round(np.arctan2(x,y)*180/pi,9))
def DH(i,a,alpha,d,theta):
    i-=1
    return(np.mat([[cos(theta[i]),-sin(theta[i]),0,a[i]],
                     [sin(theta[i])*cos(alpha[i]),cos(theta[i])*cos(alpha[i]),-sin(alpha[i]),-sin(alpha[i])*d[i]],
                     [sin(theta[i])*sin(alpha[i]),cos(theta[i])*sin(alpha[i]),cos(alpha[i]),cos(alpha[i])*d[i]],
                     [0,0,0,1]]))
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