def cheng3(be):
    be=be*be*be
    return be
for x in range(100,100001):
    if x>999:
        x2=[int(x/1000),int(x%1000/100),int(x%1000%100/10),int(x%1000%100%10)]
        y=x2[0]
        y2=x2[1]
        y3=x2[2]
        y4=x2[3]
        y=cheng3(y)
        y2=cheng3(y2)
        y3=cheng3(y3)
        y4=cheng3(y4)
        zho=y+y2+y3+y4
        if zho==x:
            print(x)
    else:
        x2=[int(x/100),int(x%100/10),int(x%100%10)]
        y=x2[0]
        y2=x2[1]
        y3=x2[2]
        y=cheng3(y)
        y2=cheng3(y2)
        y3=cheng3(y3)
        zho=y+y2+y3
        if zho==x:
            print(x)