while True:
    try:
        y=input('输入下限：')
        z=input('输入上限：')
        y=int(y)
        z=int(z)
        break
    except:
        print('这不是数字')
for x in range(y,z):
    coun=0
    if x%2==0:
        continue
    for y in range(2,x):
        if x%y!=0:
            coun+=1
            if coun==x-2:
                print(x)
