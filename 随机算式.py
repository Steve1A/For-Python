import random

num=0
num2=0
my_score=0

jc=['+','-','*','/']
print('你要多少道题')
while True:
    try:
        rou=int(input())
        break
    except:
        print('You\'re wrong')
        print('你要多少道题')
for v in range(0,rou):
    wor=random.choice(jc)
    num=random.randrange(100)
    num2=random.randrange(100)
    eval('%s%s%s'%(num,wor,num2))
    i=False
    while i==False:
        if num2==0:
            num2=random.randint(1,100)
        else:
            i=True
    p=False
    while p==False:
        if num%num2!=0:
            num2=random.randint(1,100)
        elif num%num2==0:
            p=True

    ra=eval('%s%s%s'%(num,wor,num2))
    print('%s%s%s'%(num,wor,num2))
    print('请作答')
    my_an=input()

    try:
        my_an=int(my_an)
    except:
        print('这不是一个数字')

    if my_an==ra:
        my_score+=1
        print('正确，你的分数是%s'%(my_score))
    else:
        print('错误')
print('你最终的分数是%s'%(my_score))
