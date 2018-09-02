import time#加入time模块
while True:#一个永久执行的循环
    print('输入一个算式')
    time.sleep(0.5)
    while True:
        try:
            x=input()#输入算式
            print(eval('%s'%(x)))#进行估值计算
            break
        except:
            print('这不是算式')
    time.sleep(1)
    print('想要退出吗？输入任意字符即为退出，不想退出按enter')
    y=input()
    if y!='':#问你需不需要退出，判断是或否
        break
