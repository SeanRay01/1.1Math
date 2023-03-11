import matplotlib.pyplot as plt
import pandas as pd
#原始資料一
odata0={'x':[65,59,55,65,30,33,45,55,46,67,75,67,69,50,53],
        'y':[94,85,76,85,47,57,62,81,69,90,98,87,90,74,76]}
odata1=pd.DataFrame(odata0)
n=int(len(odata0['x']))
#統計原始資料一
odata1_des=odata1.describe().loc[['mean']]
mean_add=[odata1_des['x']['mean'],odata1_des['y']['mean']]
#內容計算
ndata1=pd.DataFrame({'(x-x)':[],'(x-x)^':[],'(y-y)':[],'(y-y)^':[],'(x-x)(y-y)':[]})
for i in range(n):
    content1=(float(odata0['x'][i])-float(odata1_des['x']['mean']))
    content2=(content1**2)
    content3=(float(odata0['y'][i])-float(odata1_des['y']['mean']))
    content4=(content3**2)
    content5=(content1*content3)
    series=pd.Series([content1,content2,content3,content4,content5]
                     ,index=['(x-x)','(x-x)^','(y-y)','(y-y)^','(x-x)(y-y)'])
    ndata1=ndata1.append(series,ignore_index=True)    
#統計新資料一
ndata1_des=ndata1.describe().loc[['mean']]
mean_add+=[0,float(ndata1_des['(x-x)^']['mean'])*n
          ,0,float(ndata1_des['(y-y)^']['mean'])*n
          ,float(ndata1_des['(x-x)(y-y)']['mean'])*n]
#新舊資料合併
edata1=pd.concat([odata1,ndata1],axis=1)
series=pd.Series(mean_add,index=['x','y','(x-x)','(x-x)^','(y-y)','(y-y)^','(x-x)(y-y)'])
edata1=edata1.append(series,ignore_index=True)
#計算a&b
b=edata1['(x-x)(y-y)'][n]/edata1['(x-x)^'][n]
a=edata1['y'][n]-b*edata1['x'][n]
#計算標準誤差s、相關係數r
ndata2=pd.DataFrame({'y(x)':[],'y-y^':[],'(y-y^)^':[]})
for i in range(n):
    content1=a+b*edata1['x'][i]
    content2=edata1['y'][i]-content1
    content3=content2**2
    series=pd.Series([content1,content2,content3],index=['y(x)','y-y^','(y-y^)^'])
    ndata2=ndata2.append(series,ignore_index=True) 
ndata2_des=ndata2.describe().loc[['mean']]
series=pd.Series([float(ndata2_des['y(x)']['mean'])*n
                 ,float(ndata2_des['y-y^']['mean'])*n
                 ,float(ndata2_des['(y-y^)^']['mean'])*n],index=['y(x)','y-y^','(y-y^)^'])
ndata2=ndata2.append(series,ignore_index=True) 
edata1=pd.concat([edata1,ndata2],axis=1)
print(edata1)
r=edata1['(x-x)(y-y)'][n]/((edata1['(x-x)^'][n]**0.5)*(edata1['(y-y)^'][n]**0.5))
s=(edata1['(y-y^)^'][n]/(n-2))**0.5
edata2=pd.DataFrame({'a':[a],'b':[b],'r':[r],'s':[s]})
print(edata2)
print('Y=%.3f+%.3fX'%(a,b))
#畫圖
plt.title('Y = a + bX')
plt.xlabel('X axis')  # X軸
plt.ylabel('Y axis')  # Y軸
xmean=float(odata1_des['x']['mean'])
x = [xmean*0.4,xmean*1.6]
y = [0,0]
for i in range(0, 2):
    y[i]=a+b*x[i]
plt.grid(True)
plt.plot(odata0['x'],odata0['y'],'ro')
plt.plot(x,y,color='blue',label='Y=a+bX')
plt.legend()
plt.show()