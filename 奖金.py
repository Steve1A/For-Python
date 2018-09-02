while True:
    I=input('输入利润（单位：万元）:')
    while True:
        try:
            I=int(I)
            break
        except:
            print('这不是一个数字')
    break
if I<=10:
    jiang=I/10
elif I>10 and I<=20:
    I2=I-10
    I3=I-I2
    jiang=I3/10+I2/100*7.5
elif I>20 and I<=40:
    jiang=I/100*5
elif I>40 and I<=60:
    jiang=I/100*3
elif I>60 and I<=100:
    jiang=I/100*1.5
elif I>100:
    jiang=I/100
print('%s万元'%(jiang))
