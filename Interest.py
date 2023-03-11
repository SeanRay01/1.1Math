import matplotlib.pyplot as plt
month=12*1
x=[0]
y1=[197]
y2=[128]
y3=[325]
for i in range(1,month+1):
    print('month:%s'%(i-1),'總額:%f'%y3[i-1],'U任:%f'%y1[i-1],'我:%f\n'%y2[i-1])
    x.append(i)
    add=y3[i-1]*0.1
    y1_add1=add*(y1[i-1]/y3[i-1])
    y1_add2=(add-y1_add1)*0.05
    y2_add=(add-y1_add1)*0.95
    y1.append(y1[i-1]+y1_add1+y1_add2)
    y2.append(y2[i-1]+y2_add)
    y3.append(y3[i-1]+add)
    print('賺: 總額:%f'%add,'U任:%f'%(y1_add1+y1_add2),'我:%f'%y2_add)
    print('U任:%f%%'%((y1_add1+y1_add2)/add*100),'我:%f%%'%((y2_add)/add*100))
print('month:%s'%i,'總額:%f'%y3[i],'U任:%f'%y1[i],'我:%f'%y2[i])
    
plt.grid(True)
plt.xlabel('Month')  # X軸
plt.ylabel('Interest')  # Y軸
plt.plot(x, y1, 'go')
plt.plot(x, y2, 'go')
plt.plot(x, y3, 'go')
plt.plot(x, y1, color='red',label='U')
plt.plot(x, y2, color='blue',label='S')
plt.plot(x, y3, color='purple',label='ALL')
plt.legend()
plt.show()
