import sys
def moon_weight():
        print('请输入你的体重')
        First=int(sys.stdin.readline())
        print('请输入每年增加的体重')
        And=int(sys.stdin.readline())
        print('请输入总共有多少年')
        Year=int(sys.stdin.readline())
        for x in range(1,Year+1):
	        Moon=(First+And)*0.165
	        First=First+And
	        print('第%s年 = %s'%(x,Moon))
moon_weight()
