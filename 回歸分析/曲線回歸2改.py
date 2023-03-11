import matplotlib.pyplot as plt
import pandas as pd
import math
#原始資料一
odata={'x':[0.5,1.3,2.4,3.6,4.4,5.1,5.6,6.2,7.3,8.1],
       'y':[1.5,3.9,6.4,10.8,16.9,27.8,35.5,59.7,148.6,215.4]}
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
mean_add1=[odata0_des['x']['mean'],odata0_des['y']['mean'],odata0_des['lnx']['mean'],odata0_des['lny']['mean']]
mean_add2=[odata0_des['lnx']['mean'],odata0_des['lny']['mean']]
#內容計算
ndata1=pd.DataFrame({"(x'-x')":[],"(x'-x')^":[],"(y'-y')":[],"(x'-x')(y'-y')":[]})
ndata2=pd.DataFrame({"(x'-x')":[],"(x'-x')^":[],"(y'-y')":[],"(y'-y')^":[],"(x'-x')(y'-y')":[]})
for i in range(n):
    content5=(float(odata2['lnx'][i])-float(odata0_des['lnx']['mean']))
    content6=(content5**2)
    content7=(float(odata2['lny'][i])-float(odata0_des['lny']['mean']))
    content8=(content7**2)
    content9=(content5*content7)
    series1=pd.Series([content5,content6,content7,content9]
                     ,index=["(x'-x')","(x'-x')^","(y'-y')","(x'-x')(y'-y')"])
    ndata1=ndata1.append(series1,ignore_index=True)    
    series2=pd.Series([content5,content6,content7,content8,content9]
                     ,index=["(x'-x')","(x'-x')^","(y'-y')","(y'-y')^","(x'-x')(y'-y')"])
    ndata2=ndata2.append(series2,ignore_index=True)  
#統計新資料一、二
ndata0_des=ndata2.describe().loc[['mean']]
mean_add1+=[0,float(ndata0_des["(x'-x')^"]['mean'])*n,0,float(ndata0_des["(x'-x')(y'-y')"]['mean'])*n]
mean_add2+=[0,float(ndata0_des["(x'-x')^"]['mean'])*n,0,float(ndata0_des["(y'-y')^"]['mean'])*n
             ,float(ndata0_des["(x'-x')(y'-y')"]['mean'])*n]
#新舊資料合併
edata1=pd.concat([odata0,ndata1],axis=1)
edata2=pd.concat([odata2,ndata2],axis=1)
series1=pd.Series(mean_add1,index=['x','y','lnx','lny',"(x'-x')","(x'-x')^","(y'-y')","(x'-x')(y'-y')"])
edata1=edata1.append(series1,ignore_index=True)    
series2=pd.Series(mean_add2,index=['lnx','lny',"(x'-x')","(x'-x')^","(y'-y')","(y'-y')^","(x'-x')(y'-y')"])
edata2=edata2.append(series2,ignore_index=True) 

#計算a&b
B=edata1["(x'-x')(y'-y')"][n]/edata1["(x'-x')^"][n]
a=edata1['lny'][n]-B*edata1['lnx'][n]
A = math.exp(a)
#計算標準誤差s、相關係數r
ndata3=pd.DataFrame({"y'(x)":[],"y'-y'^":[],"(y'-y'^)^":[]})
for i in range(n):
    content1=a+B*edata2['lnx'][i]
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
edata3=pd.DataFrame({'a':[a],'A':[A],'B':[B],'r':[r],'s':[s]})
print(edata1)
print(edata3)
print('Y=%.3f*X**%.3f'%(A,B))
print(edata2)
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
    y.append(A*((i/10)**B))
fig=plt.figure(figsize=(8,6))
ax1=fig.add_subplot(1,2,1)
ax1.axis([xs*0.1, xb*1.2, ys*0.1, yb*1.2])  # 範圍設定
ax1.grid(True)
ax1.plot(odata1['x'],odata1['y'],'ro')
ax1.plot(x,y,color='blue',label='Y=A*X**B')
ax1.legend()
x = [xs2,xb2*1.5]
y = [0,0]
for i in range(0, 2):
    y[i]=a+B*x[i]
ax2=fig.add_subplot(1,2,2)
ax2.grid(True)
ax2.plot(odata2['lnx'],odata2['lny'],'ro')
ax2.plot(x,y,color='blue',label='lnY=a+bX')
ax2.legend()
plt.show()