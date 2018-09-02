Hlong=100
long=100
for p in range(0,10):
    Hlong+=long/2
    long/=2
print('第十次弹了：%s米，共经过：%s米'%(long,Hlong))
