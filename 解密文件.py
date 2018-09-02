number=input('请输入数字，注意数字间用空格隔开:')
number=number.split(' ')
words=''
i=''

def JM(num, word):
    global words
    global i
    if i==num:
        words+=word

for i in number:
    JM('1', 'a')
    JM('2', 'b')
    JM('3', 'c')
    JM('4', 'd')
    JM('5', 'e')
    JM('6', 'f')
    JM('7', 'g')
    JM('8', 'h')
    JM('9', 'i')
    JM('10', 'j')
    JM('11', 'k')
    JM('12', 'l')
    JM('13', 'm')
    JM('14', 'n')
    JM('15', 'o')
    JM('16', 'p')
    JM('17', 'q')
    JM('18', 'r')
    JM('19', 's')
    JM('20', 't')
    JM('21', 'u')
    JM('22', 'v')
    JM('23', 'w')
    JM('24', 'x')
    JM('25', 'y')
    JM('26', 'z')
    if i==',':
        words+=','

print(words)
print('（解密后有些数字不正确，请自行修改）')