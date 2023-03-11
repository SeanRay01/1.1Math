import numpy as np
Service = '玄武:'
def kelly_strategy():
    win=float(input('贏率%:'))
    lose=100-win
    current=float(input('現價:'))
    profit=((1-float(input('止盈:'))/current)**2)**0.5
    loss=((1-float(input('止損:'))/current)**2)**0.5
    principal=float(input('本金:'))
    print('profit:%.2f%%,loss:%.2f%%'%(profit*100,loss*100))
    position=np.round(win-lose/(profit/loss), 3)
    print('倉位:%.3f%%'%position)
    print('投入金額:%.3f'%(principal*position/100))

while True:
    kelly_strategy()
    #_____________________________________________#
    while True:#是否再一次
        q3=input('%s請問是否再一次(y,n):'%Service)
        if q3 == 'Y' or q3 == 'y' or q3 == 'N' or q3 == 'n':
            break
        else:
            print(Service,'輸入錯誤重來')
    if q3 == 'N' or q3 == 'n':
        break