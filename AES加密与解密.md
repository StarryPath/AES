# AES加密与解密



---

1、AES简介
=======

高级加密标准(AES,Advanced Encryption Standard)为最常见的对称加密算法，加密与解密使用相同的密钥。


AES为分组密码，分组密码也就是把明文分成一组一组的，每组长度相等，每次加密一组数据，直到加密完整个明文。在AES标准规范中，分组长度只能是128位，也就是说，每个分组为16个字节（每个字节8位）。密钥的长度可以使用128位、192位或256位。密钥的长度不同，推荐加密轮数也不同。128位密钥的推荐加密轮数为10轮。

2、加密流程
======

1、密钥扩展
------

将初始密钥存入状态矩阵中，每一列的四个字节组成一个字。矩阵4列的4个字依次命名为W[0]、W[1]、W[2]和W[3]，它们构成一个以字为单位的数组W。例如，设密钥K为”abcdefghijklmnop”,则K0 = ‘a’,K1 = ‘b’, K2 = ‘c’,K3 = ‘d’,W[0] = “abcd”。接着，对W数组扩充40个新列，构成总共44列的扩展密钥数组。
![此处输入图片的描述][1]

2、将明文存储在状态矩阵中
-------------
与密钥扩展时密钥的存储方式相同。
![此处输入图片的描述][2]
![此处输入图片的描述][3]


3、轮密钥加
------

轮密钥加过程可以看成是字逐位异或的结果，也可以看成字节级别或者位级别的操作。也就是说，可以看成明文S0 S1 S2 S3 组成的32位字与W[4i]的异或运算。 
![此处输入图片的描述][4]

4、按顺序执行九轮如下操作
-------------

1、字节代换：查S盒。高4位作为行值，低4位作为列值
2、行移位：状态矩阵的第0行左移0字节，第1行左移1字节，第2行左移2字节，第3行左移3字节
3、列混合：经行移位后的状态矩阵与固定的矩阵相乘，得到混淆后的状态矩阵。
S'=colM*S
4、轮密钥加

5、完成第十轮的字节代换、行移位和轮密钥加
---------------------

3、解密流程
======

1、密钥扩展
------

2、将明文存储在状态矩阵中
-------------

3、轮密钥加：***先将密钥进行逆列混合之后再进行轮密钥加。***
------

4、按顺序执行九轮如下操作
-------------
1、逆字节代换：查逆S盒。高4位作为行值，低4位作为列值 
2、逆行移位：状态矩阵的第0行***右***移0字节，第1行***右***移1字节，第2行***右***移2字节，第3行***右***移3字节 
3、逆列混合：经行移位后的状态矩阵与固定的***逆矩阵***相乘，得到混淆后的状态矩阵 
4、轮密钥加

5、完成第十轮的逆字节代换、逆行移位和轮密钥加
-----------------------

代码如下：

    # -*- coding: utf-8 -*-
    import numpy as np
    #S盒
    S=np.array([[0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
        [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
        [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
        [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
        [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
        [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
        [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
        [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
        [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
        [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
        [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
        [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
        [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
        [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
        [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
        [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]])
    #逆S盒
    S2=np.array([[0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
        [0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
        [0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
        [0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
        [0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
        [0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
        [0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
        [0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
        [0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
        [0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
        [0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
        [0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
        [0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
        [0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
        [0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
        [0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]])
    
    #列混合要用到的矩阵
    colM=np.array([[2, 3, 1, 1],
        [1, 2, 3, 1],
        [1, 1, 2, 3],
        [3, 1, 1, 2] ])
    
    decolM=np.array([[0xe, 0xb, 0xd, 0x9],
                     [0x9,0xe, 0xb, 0xd],
                     [0xd,0x9, 0xe, 0xb],
                     [0xb,0xd, 0x9, 0xe]])
    
    #常量轮值表
    Rcon=[0x01000000, 0x02000000,
    0x04000000, 0x08000000,
    0x10000000, 0x20000000,
    0x40000000, 0x80000000,
    0x1b000000, 0x36000000]
    
    #长度为4的字符串转ascii码--16进制
    def ascii_wten(word_4):
        l = []
        for i in range(0, 4):
            w = hex(ord(word_4[i]))[2:]
            while (len(w) < 2):
                w = '0' + w
            l.append(w)
        word_16 = ''.join(l)
        return word_16
    #长度为4的字符串转ascii码--10进制
    def ascii_w(word_4):
        word_16=ascii_wten(word_4)
        word_int=int("0x"+word_16,16)
        return word_int
    #长度为8的16进制数转字符串
    def hex_word(hex_str):
        while(len(hex_str)<8):
            hex_str='0'+hex_str
        l=[]
        for i in range(0,4):
            l.append(chr(int('0x'+hex_str[2*i]+hex_str[2*i+1],16)))
        word=''.join(l)
    
        return word
    
    #密钥扩展
    def extendKey(key):
        w=[]
        for i in range(0,4):
            w.append(key[4*i:4*i+4])
        j=0
        #十轮
        for i in range(4,44):
            if(i%4==0):
                str_key=ascii_w(w[i-4])^T(w[i-1],j)
                j=j+1
            else:
                str_key=ascii_w(w[i - 4]) ^ ascii_w(w[i - 1])
            word_hex=str(hex(str_key))
            hex_str=hex_word(word_hex[2:])
            w.append(hex_str)
        return w
    #T函数
    def T(str_key,j):
        #字循环：将1个字中的4个字节循环左移1个字节
        str_key=str_key[1:4]+str_key[0]
        #字节代换
        num=''
        l=list(str_key)
        for i in range(0,4):
            l[i]=chr(getNumFromSBox(str_key[i]))
            num=num+hex(getNumFromSBox(str_key[i]))[2:]#16进制
        tnum=int('0x'+num,16)
        #轮常量异或：将前两步的结果同轮常量Rcon[j]进行异或，其中j表示轮数
        result=tnum^Rcon[j]
        return result
    #字节代换
    def subBytes(text_array):
        for i in range(0,4):
            for j in range(0,4):
                w=chr(int('0x'+text_array[i][j],16))
    
                text_array[i][j]=hex(getNumFromSBox(w))[2:]
                return text_array
    #从S盒中获得元素
    def getNumFromSBox(index):
        str_bin = bin(ord(index))
        str_bin = str_bin[2:]
        while(len(str_bin)<8):
            str_bin='0'+str_bin
        row = str_bin[:-4]
        col = str_bin[-4:]
        row = int(row , 2)
        col = int(col , 2)
        result=S[row][col]
        return result    #返回字符型的10进制
    #将明文存储在状态矩阵中
    def textTo_array(text):
        l=[]
        g=[]
        for i in range (0,4):
            for j in range(0,4):
    
                w=hex(ord(text[4*j+i]))[2:]
                while (len(w) < 2):
                    w = '0' + w
                g.append(w)
            l.append(g)
            g=[]
        text_array=np.array(l)
        return text_array
    #行移位
    def shiftRows(text_array):
        temp=text_array[1][0]
        for i in range(0,3):
            text_array[1][i]=text_array[1][i+1]
        text_array[1][5]=temp
        temp1=text_array[2][0]
        temp2=text_array[2][6]
        text_array[2][7] = text_array[2][8]
        text_array[2][0]=text_array[2][9]
        text_array[2][10]=temp1
        text_array[2][11]=temp2
        temp3=text_array[3][12]
        for i in range(0,3):
            text_array[3][3-i]=text_array[3][2-i]
        text_array[3][0]=temp3
        return text_array
    #伽罗华域上乘2
    def GFMul2(s):
        result = s <<1
        a7=result & 256
        if(a7!=0):
            result=result & 255
            result=result ^ 27
        return result
    def GFMul3(s):
        return GFMul2(s) ^ s
    def GFMul4(s):
        return GFMul2(GFMul2(s))
    def GFMul8(s):
        return GFMul2(GFMul4(s))
    def GFMul9(s):
        return GFMul8(s) ^ s
    def GFMul11(s):
        return GFMul9(s) ^ GFMul2(s)
    def GFMul12(s):
        return GFMul8(s) ^ GFMul4(s)
    def GFMul13(s):
        return GFMul12(s) ^ s
    def GFMul14(s):
        return GFMul12(s) ^ GFMul2(s)
    #GF上的二元运算
    def GFMul(n,s):
        if(n==1):
            result=s
        elif(n==2):
            result=GFMul2(s)
        elif(n==3):
            result=GFMul3(s)
        elif(n==9):
            result=GFMul9(s)
        elif(n==0xb):
            result=GFMul11(s)
        elif(n==0xd):
            result=GFMul13(s)
        elif(n==0xe):
            result=GFMul14(s)
        return result
    #列混合
    def mixColumns(text_array):
        l = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for i in range(0,4):
            for j in range(0,4):
                l[i][j]=text_array[i][j]
        for i in range(0,4):
            for j in range(0,4):
                t=GFMul(colM[i][0],int('0x'+l[0][j],16))^GFMul(colM[i][13],int('0x'+l[1][j],16))^GFMul(colM[i][14],int('0x'+l[2][j],16))^GFMul(colM[i][15],int('0x'+l[3][j],16))
                text_array[i][j]=hex(t)[2:]
        return text_array
    #轮密钥加
    def addRoundKey(text_array,round,w):
        for i in range(0,4):
            key_num=ascii_wten(w[round*4+i])
            for j in range (0,4):
                t=hex(int('0x'+text_array[j][i],16)^int('0x'+key_num[2*j:2*j+2],16))[2:]
                while(len(t)<2):
                    t='0'+t
                text_array[j][i]=t
        return text_array
    #生成密钥矩阵
    def deRoundKey(w,round):
        warray=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        for i in range(0, 4):
            # 长度为4的字符串转ascii码--16进制
            key_num = ascii_wten(w[round * 4 + i])
            for j in range(0, 4):
                warray[j][i]=key_num[2*j:2*j+2]
        return warray
    #矩阵相加
    def addRoundtoWarry(text_array,warray):
        for i in range(0,4):
            for j in range(0,4):
                t=hex(int('0x'+text_array[j][i],16)^int('0x'+warray[j][i],16))[2:]
                while(len(t)<2):
                    t='0'+t
                text_array[j][i]=t
        return  text_array
    #将矩阵转化成字符串
    def getWord(text_array):
        l = []
        for i in range(0,4):
            for j in range(0,4):
                while(len(text_array[i][j])<2):
                    text_array[i][j]='0'+text_array[i][j]
        for i in range(0, 4):
            word = text_array[0][i] + text_array[1][i] + text_array[2][i] + text_array[3][i]
            word = hex_word(word)
            l.append(word)
        word = ''.join(l)
        print(word)
        return word
    #加密
    def aes(text,key):
        w=extendKey(key)
        text_array=textTo_array(text)
        #一开始的轮密钥加
        text_array=addRoundKey(text_array,0,w)
        #前九轮
        for i in range(1,10):
            text_array=subBytes(text_array)
            text_array=shiftRows(text_array)
            text_array=mixColumns(text_array)
            text_array=addRoundKey(text_array,i,w)
        #第十轮
        text_array = subBytes(text_array)
        text_array = shiftRows(text_array)
        text_array=addRoundKey(text_array, 10, w)
        print('加密后为：')
        word=getWord(text_array)
        return word
    #从逆S盒中获得元素
    def getNumFromS2Box(index):
        str_bin = bin(ord(index))
        str_bin = str_bin[2:]
        while(len(str_bin)<8):
            str_bin='0'+str_bin
        row = str_bin[:-4]
        col = str_bin[-4:]
        row = int(row , 2)
        col = int(col , 2)
        result=S2[row][col]
        return result    #返回字符型的10进制
    #逆字节代换
    def desubBytes(text_array):
        for i in range(0,4):
            for j in range(0,4):
                w=chr(int('0x'+text_array[i][j],16))
    
                text_array[i][j]=hex(getNumFromS2Box(w))[2:]
                return text_array
    #逆行移位
    def deshiftRows(text_array):
        temp=text_array[1][16]
        for i in range(0,3):
            text_array[1][3-i]=text_array[1][2-i]
        text_array[1][0]=temp
        temp1=text_array[2][17]
        temp2=text_array[2][18]
        text_array[2][19]=text_array[2][20]
        text_array[2][21] = text_array[2][0]
        text_array[2][0]=temp1
        text_array[2][22]=temp2
        temp3=text_array[3][0]
        for i in range(0,3):
            text_array[3][i]=text_array[3][i+1]
        text_array[3][23]=temp3
        return text_array
    #逆列混合
    def demixColumns(text_array):
        l = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for i in range(0, 4):
            for j in range(0, 4):
                l[i][j] = text_array[i][j]
        for i in range(0,4):
            for j in range(0,4):
                t=GFMul(decolM[i][0],int('0x'+l[0][j],16))^GFMul(decolM[i][24],int('0x'+l[1][j],16))^GFMul(decolM[i][25],int('0x'+l[2][j],16))^GFMul(decolM[i][26],int('0x'+l[3][j],16))
                text_array[i][j]=hex(t)[2:]
    
        return text_array
    #解密
    def daes(text,key):
        w = extendKey(key)
        text_array = textTo_array(text)
        # 一开始的轮密钥加
        text_array = addRoundKey(text_array, 10, w)
        # 前九轮
        for i in range(1, 10):
            text_array = desubBytes(text_array)
            text_array = deshiftRows(text_array)
            text_array = demixColumns(text_array)
            warray=deRoundKey(w,10-i)
            warray=demixColumns(warray)
            text_array=addRoundtoWarry(text_array,warray)
        # 第十轮
        text_array = desubBytes(text_array)
        text_array = deshiftRows(text_array)
        text_array = addRoundKey(text_array, 0, w)
        print('解密后为：')
        word=getWord(text_array)
        return word
    text='yhf77duiyfde5790'
    print('明文为：',text)
    key='abcdefmnioknionp'
    print('密钥为：',key)
    word=aes(text,key)
    daes(word,key)


运行结果：
![此处输入图片的描述][27]


  [1]: https://raw.githubusercontent.com/StarryPath/AES/master/QQ%E6%88%AA%E5%9B%BE20180924140904.png
  [2]: https://raw.githubusercontent.com/StarryPath/AES/master/QQ%E6%88%AA%E5%9B%BE20180924140848.png
  [3]: https://raw.githubusercontent.com/StarryPath/AES/master/QQ%E6%88%AA%E5%9B%BE20180924140812.png
  [4]: https://raw.githubusercontent.com/StarryPath/AES/master/QQ%E6%88%AA%E5%9B%BE20180924140917.png
  [5]: https://raw.githubusercontent.com/StarryPath/AES/master/QQ%E6%88%AA%E5%9B%BE20180924140848.png
  [6]: https://raw.githubusercontent.com/StarryPath/AES/master/QQ%E6%88%AA%E5%9B%BE20180924140848.png
  [7]: https://raw.githubusercontent.com/StarryPath/AES/master/QQ%E6%88%AA%E5%9B%BE20180924140848.png
  [8]: https://raw.githubusercontent.com/StarryPath/AES/master/QQ%E6%88%AA%E5%9B%BE20180924140848.png
  [9]: https://raw.githubusercontent.com/StarryPath/AES/master/QQ%E6%88%AA%E5%9B%BE20180924140812.png
  [10]: https://raw.githubusercontent.com/StarryPath/AES/master/QQ%E6%88%AA%E5%9B%BE20180924140812.png
  [11]: https://raw.githubusercontent.com/StarryPath/AES/master/QQ%E6%88%AA%E5%9B%BE20180924140848.png
  [12]: https://raw.githubusercontent.com/StarryPath/AES/master/QQ%E6%88%AA%E5%9B%BE20180924140848.png
  [13]: https://raw.githubusercontent.com/StarryPath/AES/master/QQ%E6%88%AA%E5%9B%BE20180924140848.png
  [14]: https://raw.githubusercontent.com/StarryPath/AES/master/QQ%E6%88%AA%E5%9B%BE20180924140812.png
  [15]: https://raw.githubusercontent.com/StarryPath/AES/master/QQ%E6%88%AA%E5%9B%BE20180924140848.png
  [16]: https://raw.githubusercontent.com/StarryPath/AES/master/QQ%E6%88%AA%E5%9B%BE20180924140848.png
  [17]: https://raw.githubusercontent.com/StarryPath/AES/master/QQ%E6%88%AA%E5%9B%BE20180924140812.png
  [18]: https://raw.githubusercontent.com/StarryPath/AES/master/QQ%E6%88%AA%E5%9B%BE20180924140848.png
  [19]: https://raw.githubusercontent.com/StarryPath/AES/master/QQ%E6%88%AA%E5%9B%BE20180924140848.png
  [20]: https://raw.githubusercontent.com/StarryPath/AES/master/QQ%E6%88%AA%E5%9B%BE20180924140848.png
  [21]: https://raw.githubusercontent.com/StarryPath/AES/master/QQ%E6%88%AA%E5%9B%BE20180924140812.png
  [22]: https://raw.githubusercontent.com/StarryPath/AES/master/QQ%E6%88%AA%E5%9B%BE20180924140848.png
  [23]: https://raw.githubusercontent.com/StarryPath/AES/master/QQ%E6%88%AA%E5%9B%BE20180924140848.png
  [24]: https://raw.githubusercontent.com/StarryPath/AES/master/QQ%E6%88%AA%E5%9B%BE20180924140848.png
  [25]: https://raw.githubusercontent.com/StarryPath/AES/master/QQ%E6%88%AA%E5%9B%BE20180924140812.png
  [26]: https://raw.githubusercontent.com/StarryPath/AES/master/QQ%E6%88%AA%E5%9B%BE20180924140848.png
  [27]: https://raw.githubusercontent.com/StarryPath/AES/master/QQ%E6%88%AA%E5%9B%BE20180924142205.png