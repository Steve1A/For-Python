import random
import time

you_core=0
com_core=0
again=True

print('How many rounds do you want?')
rous=int(input())
for x in range(0,rous):
    print('==========You==========')
    print('选择你射门的方向，1、2、3')
    spa=[1,2,3]
    you_spa=input()
    if you_spa!='1' and you_spa!='2' and you_spa!='3':
        print('没有这个方向')
    else:
        you_spa=int(you_spa)
        com_spa=random.choice(spa)
        if you_spa==com_spa:
            print('Oh，老铁没进哦')
        elif you_spa!=com_spa:
                print('Oh,Goul!!!')
                you_core+=1
                print('%s (you):%s (com)'%(you_core,com_core))
    
    time.sleep(0.5)
    
    print('==========Computer==========')
    print('选择你防守的方向，1、2、3')
    spa=[1,2,3]
    you_spa=input()
    if you_spa!='1' and you_spa!='2' and you_spa!='3':
        print('没有这个方向')
    else:
        you_spa=int(you_spa)
        com_spa=random.choice(spa)
        if you_spa==com_spa:
            print('Oh，守住了！')
        elif you_spa!=com_spa:
                print('Oh,Goul!!!')
                com_core+=1
                print('%s (you):%s (com)'%(you_core,com_core))
    time.sleep(0.5)

print('OK.Now game over,the winner is')
if you_core>com_core:
    print('you!!')
elif com_core>you_core:
    print('computer!!')
else:
    print('Again!')