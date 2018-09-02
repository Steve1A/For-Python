yin=[]
v=0
f=0
p2=0
import math
for x in range(1,1001):
    yin=[]
    p2=0
    for a in range(1,1001):
        for b in range(1,1001):
            if a*b==x:
                yin.append(a)
                yin.append(b)
    for p in yin:
        p2=p+p2
    p2=p2/2
    p2=p2-x
    if p2==x:
        print(x)
