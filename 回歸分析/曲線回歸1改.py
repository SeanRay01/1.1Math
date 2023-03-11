import matplotlib.pyplot as plt
import pandas as pd
import math
#原始資料一
odata={'x':[1,2,3,4,5,6,7,8,9,10,17],
       'y':[16,17,18.8,21.1,24,27.1,30.6,34.5,38.6,43,80]}
odata1=pd.DataFrame(odata)
n=int(len(odata['x']))
#自然指數處理
odata2=pd.DataFrame({'lnx':[],'lny':[]})
for i in range(n):
    content1=math.log(odata1['x'][i])
    content2=math.log(odata1['y'][i])
    series=pd.Series([content1,content2],index=['lnx','lny'])
    odata2=odata2.append(series,ignore_index=True)  
#統計原始資料一、二
odata0=pd.concat([odata1,odata2],axis=1)
odata0_des=odata0.describe().loc[['mean']]
mean_add1=[odata0_des['x']['mean'],odata0_des['y']['mean']]
mean_add2=[odata0_des['lnx']['mean'],odata0_des['lny']['mean']]
#內容計算
ndata1=pd.DataFrame({'lny':[],'(x-x)':[],'(x-x)^':[],"(y'-y')":[],"(x-x)(y'-y')":[]})
ndata2=pd.DataFrame({"(x'-x')":[],"(x'-x')^":[],"(y'-y')":[],"(y'-y')^":[],"(x'-x')(y'-y')":[]})
for i in range(n):
    content1=float(odata2['lnx'][i])
    content2=float(odata2['lny'][i])
    content3=(float(odata1['x'][i])-float(odata0_des['x']['mean']))
    content4=(content3**2)
    content5=(float(odata2['lnx'][i])-float(odata0_des['lnx']['mean']))
    content6=(content5**2)
    content7=(float(odata2['lny'][i])-float(odata0_des['lny']['mean']))
    content8=(content7**2)
    content9=(content3*content7)
    content10=(content5*content7)
    series1=pd.Series([content2,content3,content4,content7,content9]
                     ,index=['lny','(x-x)','(x-x)^',"(y'-y')","(x-x)(y'-y')"])
    ndata1=ndata1.append(series1,ignore_index=True)    
    series2=pd.Series([content5,content6,content7,content8,content10]
                     ,index=["(x'-x')","(x'-x')^","(y'-y')","(y'-y')^","(x'-x')(y'-y')"])
    ndata2=ndata2.append(series2,ignore_index=True)  
#統計新資料一、二
ndata1_des=ndata1.describe().loc[['mean']]
ndata2_des=ndata2.describe().loc[['mean']]
mean_add1+=[float(ndata1_des['lny']['mean'])
           ,0,float(ndata1_des['(x-x)^']['mean'])*n
           ,0,float(ndata1_des["(x-x)(y'-y')"]['mean'])*n]
mean_add2+=[0,float(ndata2_des["(x'-x')^"]['mean'])*n
           ,0,float(ndata2_des["(y'-y')^"]['mean'])*n
           ,float(ndata2_des["(x'-x')(y'-y')"]['mean'])*n]
#新舊資料合併
edata1=pd.concat([odata1,ndata1],axis=1)
edata2=pd.concat([odata2,ndata2],axis=1)
series1=pd.Series(mean_add1,index=['x','y','lny','(x-x)','(x-x)^',"(y'-y')","(x-x)(y'-y')"])
edata1=edata1.append(series1,ignore_index=True)    
series2=pd.Series(mean_add2,index=['lnx','lny',"(x'-x')","(x'-x')^","(y'-y')","(y'-y')^","(x'-x')(y'-y')"])
edata2=edata2.append(series2,ignore_index=True) 
#計算a&b
b1=edata1["(x-x)(y'-y')"][n]/edata1['(x-x)^'][n]
B = math.exp(b1)
a1=edata1['lny'][n]-b1*edata1['x'][n]
A = math.exp(a1)
b2=edata2["(x'-x')(y'-y')"][n]/edata2["(x'-x')^"][n]
a2=edata2['lny'][n]-b2*edata2['lnx'][n]
#計算標準誤差s、相關係數r
ndata3=pd.DataFrame({"y'(x)":[],"y'-y'^":[],"(y'-y'^)^":[]})
for i in range(n):
    content1=a2+b2*edata2['lnx'][i]
    content2=edata1['lny'][i]-content1
    content3=content2**2
    series3=pd.Series([content1,content2,content3],index=["y'(x)","y'-y'^","(y'-y'^)^"])
    ndata3=ndata3.append(series3,ignore_index=True) 
ndata0_des=ndata3.describe().loc[['mean']]
series3=pd.Series([float(ndata0_des["y'(x)"]['mean'])*n
                 ,float(ndata0_des["y'-y'^"]['mean'])*n
                 ,float(ndata0_des["(y'-y'^)^"]['mean'])*n],index=["y'(x)","y'-y'^","(y'-y'^)^"])
ndata3=ndata3.append(series3,ignore_index=True) 
edata2=pd.concat([edata2,ndata3],axis=1)
r=edata2["(x'-x')(y'-y')"][n]/((edata2["(x'-x')^"][n]**0.5)*(edata2["(y'-y'^)^"][n]**0.5))
s=(edata2["(y'-y'^)^"][n]/(n-2))**0.5
edata3=pd.DataFrame({'a':[a1],'b':[b1],'A':[A],'B':[B],'r':[r],'s':[s]})
print(edata1)
print(edata3)
print('Y=%.3f*%.3f^'%(A,B))
# print(edata2)
#畫圖
xmean=float(edata1['x'][n])
x = list()
y = list()
xs = xb = odata1['x'][0]
xs2 = xb2 = odata2['lnx'][0]
ys = yb = odata1['y'][0]
for i in range(1, n):
    if odata1['x'][i] < xs:
        xs = odata1['x'][i]
    if odata1['x'][i] > xb:
        xb = odata1['x'][i]
    if odata2['lnx'][i] < xs2:
        xs2 = odata2['lnx'][i]
    if odata2['lnx'][i] > xb2:
        xb2 = odata2['lnx'][i]
    if odata1['y'][i] < ys:
        ys = odata1['y'][i]
    if odata1['y'][i] > yb:
        yb = odata1['y'][i]
for i in range(int(xs*0.9)*10, int((xb+1)*1.2)*10):
    x.append(i/10)
    y.append(A*(B**(i/10)))
fig=plt.figure(figsize=(8,6))
ax1=fig.add_subplot(1,2,1)
ax1.axis([xs*0.1, xb*1.2, ys*0.1, yb*1.2])  # 範圍設定
ax1.grid(True)
ax1.plot(odata1['x'],odata1['y'],'ro')
ax1.plot(x,y,color='blue',label='Y=A*B^')
ax1.legend()
x = [xs2,xb2*1.5]
y = [0,0]
for i in range(0, 2):
    y[i]=a2+b2*x[i]
ax2=fig.add_subplot(1,2,2)
ax2.grid(True)
ax2.plot(odata2['lnx'],odata2['lny'],'ro')
ax2.plot(x,y,color='blue',label='lnY=a+bX')
ax2.legend()
plt.show()