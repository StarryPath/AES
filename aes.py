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
    #print("word:",word_16)
    return word_int
#长度为8的16进制数转字符串
def hex_word(hex_str):
    #print(len(hex_str))
    while(len(hex_str)<8):
        hex_str='0'+hex_str
    l=[]
   # print('hex_str:',len(hex_str))
    for i in range(0,4):
        l.append(chr(int('0x'+hex_str[2*i]+hex_str[2*i+1],16)))
    word=''.join(l)

    return word

#密钥扩展
def extendKey(key):
    w=[]
    for i in range(0,4):
        w.append(key[4*i:4*i+4])
    #print(w)
    j=0
    #十轮
    for i in range(4,44):
        if(i%4==0):
            str_key=ascii_w(w[i-4])^T(w[i-1],j)
            #print(type(str_key))
            j=j+1
        else:
            str_key=ascii_w(w[i - 4]) ^ ascii_w(w[i - 1])
        word_hex=str(hex(str_key))
        #print("word_hex:"+str(i),word_hex)
        hex_str=hex_word(word_hex[2:])
        #print("hex_str:",hex_str)
        w.append(hex_str)
    #print(w)
    return w


#T函数
def T(str_key,j):
    #print(len(str_key))
    #字循环：将1个字中的4个字节循环左移1个字节
    str_key=str_key[1:4]+str_key[0]
   # print(str_key)
    #字节代换
    num=''
    l=list(str_key)
    for i in range(0,4):
        l[i]=chr(getNumFromSBox(str_key[i]))
        num=num+hex(getNumFromSBox(str_key[i]))[2:]#16进制

       # print(l)
   # print(Rstr)
    tnum=int('0x'+num,16)
    #轮常量异或：将前两步的结果同轮常量Rcon[j]进行异或，其中j表示轮数
    result=tnum^Rcon[j]
    #print(result)
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
    #print("index:",index)
    #print("indexord:",ord(index))
    str_bin = bin(ord(index))
    str_bin = str_bin[2:]
    while(len(str_bin)<8):
        str_bin='0'+str_bin

    row = str_bin[:-4]
    col = str_bin[-4:]
    row = int(row , 2)
    col = int(col , 2)
    result=S[row][col]
    #print(result)
   # print(row,col)
   # print(S[row][col])
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
    #print(text_array)
    return text_array

#行移位
def shiftRows(text_array):
    temp=text_array[1][0]
    for i in range(0,3):
        text_array[1][i]=text_array[1][i+1]
    text_array[1][3]=temp
    temp1=text_array[2][0]
    temp2=text_array[2][1]
    text_array[2][1] = text_array[2][3]
    text_array[2][0]=text_array[2][2]
    text_array[2][2]=temp1
    text_array[2][3]=temp2
    temp3=text_array[3][3]
    for i in range(0,3):
        text_array[3][3-i]=text_array[3][2-i]
    text_array[3][0]=temp3
    #print(text_array)
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
            t=GFMul(colM[i][0],int('0x'+l[0][j],16))^GFMul(colM[i][1],int('0x'+l[1][j],16))^GFMul(colM[i][2],int('0x'+l[2][j],16))^GFMul(colM[i][3],int('0x'+l[3][j],16))
            text_array[i][j]=hex(t)[2:]
            #print(text_array)
           # print(l)
           # print('-----------------------------------------')
    return text_array
#arr=np.array([['c9','e5','fd','2b'],['7a','f2','78','6e'],['63','9c','26','67'],['b0','a7','82','e5']])
#arr=mixColumns(arr)
#print(arr)
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
def deRoundKey(w,round):
    warray=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(0, 4):
        # 长度为4的字符串转ascii码--16进制
        key_num = ascii_wten(w[round * 4 + i])
        for j in range(0, 4):
            warray[j][i]=key_num[2*j:2*j+2]
    return warray
def addRoundtoWarry(text_array,warray):
    for i in range(0,4):
        for j in range(0,4):
            t=hex(int('0x'+text_array[j][i],16)^int('0x'+warray[j][i],16))[2:]
            while(len(t)<2):
                t='0'+t
            text_array[j][i]=t
    return  text_array


#getNumFromSBox("b")

#T("abcd",1)







#a='3CA10B2157F01916902E1380ACC107BD'
#a='456471B0129468A682BA7B262E7B7C9B'
#c=''.join([chr(int(b, 16)) for b in [a[i:i+2] for i in range(0, len(a), 2)]])
#print(c)
#print(308211336^273761383)
#str_bin=bin(ord('a'))
#str_bin=str_bin[2:]
#aa=str_bin[:-4]
#bb=str_bin[-4:]
#print(str_bin)
#print(aa)
#print(bb)
#aa=int(aa,2)
#print(aa)
#print(87^69)
def getWord(text_array):
    l = []
    for i in range(0, 4):
        word = text_array[i][0] + text_array[i][1] + text_array[i][2] + text_array[i][3]
        word = hex_word(word)
        l.append(word)
    word = ''.join(l)
    print(word)
    return word
def aes(text,key):
    w=extendKey(key)
    #print(w)
    text_array=textTo_array(text)
    #一开始的轮密钥加
    text_array=addRoundKey(text_array,0,w)
    #前九轮
    for i in range(1,10):
        text_array=subBytes(text_array)
        text_array=shiftRows(text_array)
        text_array=mixColumns(text_array)
        text_array=addRoundKey(text_array,i,w)
        #getWord(text_array)

    #第十轮
    text_array = subBytes(text_array)
    text_array = shiftRows(text_array)
    text_array=addRoundKey(text_array, 10, w)

    word=getWord(text_array)
    return word


#从逆S盒中获得元素
def getNumFromS2Box(index):
    #print("index:",index)
    #print("indexord:",ord(index))
    str_bin = bin(ord(index))
    str_bin = str_bin[2:]
    while(len(str_bin)<8):
        str_bin='0'+str_bin

    row = str_bin[:-4]
    col = str_bin[-4:]
    row = int(row , 2)
    col = int(col , 2)
    result=S2[row][col]
    #print(result)
   # print(row,col)
   # print(S[row][col])
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
    temp=text_array[1][3]
    for i in range(0,3):
        text_array[1][3-i]=text_array[1][2-i]
    text_array[1][0]=temp
    temp1=text_array[2][2]
    temp2=text_array[2][3]

    text_array[2][3]=text_array[2][1]
    text_array[2][2] = text_array[2][0]
    text_array[2][0]=temp1
    text_array[2][1]=temp2
    temp3=text_array[3][0]
    for i in range(0,3):
        text_array[3][i]=text_array[3][i+1]
    text_array[3][3]=temp3
    #print(text_array)
    return text_array

#逆列混合
def demixColumns(text_array):
    l = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(0, 4):
        for j in range(0, 4):
            l[i][j] = text_array[i][j]
    for i in range(0,4):
        for j in range(0,4):
            t=GFMul(decolM[i][0],int('0x'+l[0][j],16))^GFMul(decolM[i][1],int('0x'+l[1][j],16))^GFMul(decolM[i][2],int('0x'+l[2][j],16))^GFMul(decolM[i][3],int('0x'+l[3][j],16))
            text_array[i][j]=hex(t)[2:]

    return text_array

#arry=np.array([['d4', 'e7', 'cd', '66'],
 #['28' ,'2' ,'e5' ,'bb'],
# ['be' ,'c6' ,'54' ,'bf'],
 #['22' ,'f', '5d', 'a5']])
#arry=demixColumns(arry)
#print(arry)




def daes(text,key):
    w = extendKey(key)
    #print(w)
    text_array = textTo_array(text)
    #print(text_array)
    # 一开始的轮密钥加
    text_array = addRoundKey(text_array, 10, w)
    #print(text_array)
    # 前九轮
    for i in range(1, 10):
        text_array = desubBytes(text_array)
        text_array = deshiftRows(text_array)
        text_array = demixColumns(text_array)
        #w_str=w[44-4*i]+w[45-4*i]+w[46-4*i]+w[47-4*i]
        #warray=textTo_array(w_str)
        warray=deRoundKey(w,10-i)
        warray=demixColumns(warray)
        text_array=addRoundtoWarry(text_array,warray)
        #getWord(text_array)



    # 第十轮
    text_array = desubBytes(text_array)
    text_array = deshiftRows(text_array)
    text_array = addRoundKey(text_array, 0, w)
    #print(text_array)

    word=getWord(text_array)
    return word
text='abcdefghijklmnop'
key='abcdefghijklmnop'
word=aes(text,key)
print(key)
daes(word,key)
