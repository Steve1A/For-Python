word=input('请输入字母：')
i=''
number=''

def JM(word,word2,num):
    global i
    global number
    if i==word or i==word2:
        if number=='':
            number+=num
        else:
            number+=' '+num

for i in word:
    JM('a', 'A', '1')
    JM('b', 'B', '2')
    JM('c', 'C', '3')
    JM('d', 'D', '4')
    JM('e', 'E', '5')
    JM('f', 'F', '6')
    JM('g', 'G', '7')
    JM('h', 'H', '8')
    JM('i', 'I', '9')
    JM('j', 'J', '10')
    JM('k', 'K', '11')
    JM('l', 'L', '12')
    JM('m', 'M', '13')
    JM('n', 'N', '14')
    JM('o', 'O', '15')
    JM('p', 'P', '16')
    JM('q', 'Q', '17')
    JM('r', 'R', '18')
    JM('s', 'S', '19')
    JM('t', 'T', '20')
    JM('u', 'U', '21')
    JM('v', 'V', '22')
    JM('w', 'W', '23')
    JM('x', 'X', '24')
    JM('y', 'Y', '25')
    JM('z', 'Z', '26')
    try:
        int(i)
        str(i)
        number+=' '+i
    except:
        pass
    if i==',':
        number+=' '+','
print(number)