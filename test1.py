import numpy as np
pi=np.pi
def DH(i,a_list,alpha_list,d_list,theta_list):
    """
    function：坐标系{i-1}到坐标系{i}的转换矩阵
    tips：这里的last_i指的是i-1
    """
    i = i  # 下面使用的i-1表示列表的第i-1个数，注意同DH参数里的i-1区别
    T_martix = np.mat(np.zeros((4,4)))
    
    T_martix[0,0] = np.cos(theta_list[i-1])
    T_martix[0,1] = -1*np.sin(theta_list[i-1])
    T_martix[0,2] = 0
    T_martix[0,3] = a_list[i-1]
    
    T_martix[1,0] = np.sin(theta_list[i-1])*np.cos(alpha_list[i-1])
    T_martix[1,1] = np.cos(theta_list[i-1])*np.cos(alpha_list[i-1])
    T_martix[1,2] = -1*np.sin(alpha_list[i-1])
    T_martix[1,3] = -1*np.sin(alpha_list[i-1])*d_list[i-1]
    
    T_martix[2,0] = np.sin(theta_list[i-1])*np.sin(alpha_list[i-1])
    T_martix[2,1] = np.cos(theta_list[i-1])*np.sin(alpha_list[i-1])
    T_martix[2,2] = np.cos(alpha_list[i-1])
    T_martix[2,3] = np.cos(alpha_list[i-1])*d_list[i-1]
    
    T_martix[3,0] = 0
    T_martix[3,1] = 0 
    T_martix[3,2] = 0
    T_martix[3,3] = 1
    
    return T_martix
a_list = [0,0,140,100,0,0]
alpha_list = [0,pi/2,0,0,pi/2,pi/2]
d_list = [180,0,0,90,80,60]
theta_list = [0,pi/2,0,pi/2,-1*pi/2,0]
t01=DH(1,a_list,alpha_list,d_list,theta_list)
t12=DH(2,a_list,alpha_list,d_list,theta_list)
t23=DH(3,a_list,alpha_list,d_list,theta_list)
t34=DH(4,a_list,alpha_list,d_list,theta_list)
t45=DH(5,a_list,alpha_list,d_list,theta_list)
t56=DH(6,a_list,alpha_list,d_list,theta_list)
t06=t01*t12*t23*t34*t45*t56
print(t06)