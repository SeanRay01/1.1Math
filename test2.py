import numpy as np
pi = np.pi
def sin(t):  # sin function
    return(round(np.sin(t/180*pi), 9))
def cos(t):  # cos function
    return(round(np.cos(t/180*pi), 9))
def Rz(t):  # Z旋轉
    return(np.mat([[cos(t), -sin(t)],
                   [sin(t), cos(t) ]]))
# 設定
p0 = np.mat([[0], [0]])
p1 = np.mat([[-50], [0]])
p2 = np.mat([[-30], [0]])
theta = [0, 30, 45]
# 計算
o00 = p0
print('O00=\n', o00)
o01 = o00-Rz(-theta[1]).T*p1
print('O0a=\n', o01)
o02 = o01-Rz(-theta[2]).T*p2
print('O0b=\n', o02)
