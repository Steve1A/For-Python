def find(x1):
    lis=[2]
    for x in range(0,x1):
        coun=0
        if x%2==0:
            continue
        for y in range(2,x):
            if x%y!=0:
                coun+=1
                if coun==x-2:
                    lis.append(x)
    return lis

while True:
    print('请输入一个数字')
    while True:
        try:
            x=int(input())
            break
        except:
            print('这不是一个数字')
    y=find(x)
    y2=[]
    TorF=True
    while TorF==True:
        for z in y:
            if x%z==0:
                y2.append(z)
                x/=z
            elif x==z:
                y2.append(z)
                TorF=False
    print(y2)