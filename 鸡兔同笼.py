def roo_and_rab(head,foot):
    roo=2*head
    roo=foot-roo
    rab=roo/2
    roo=head-rab
    roo=int(roo)
    rab=int(rab)
    print('rooster is %s, rabbit is %s'%(roo,rab))
print('请输入头数')
x=int(input())
print('请输入脚数')
y=int(input())
roo_and_rab(x,y)
