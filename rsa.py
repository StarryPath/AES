#扩展欧几里得算法
def ext_gcd(a, b):
    if b == 0:
        x = 1
        y = 0
        r = a
        return r, x, y
    else:
        r, x1, y1 = ext_gcd(b, a % b)
        x = y1
        y = x1 - a // b * y1
        return r, x, y


#生成公钥私钥，p,q为大素数
def get_key(p,q):
    n=p*q
    fn=(p-1)*(q-1)

    e=3889
    r,x,y=ext_gcd(e,fn)

    print(x)

    d=x
    #返回公钥对和私钥对
    return (n, e), (n, d)
#蒙哥马利大整数模幂算法
def mod(m,e,n):
    #e变成二进制并倒序
    e_bin=bin(e)[2:][::-1]
    l=len(e_bin)
    mul=1
    for i in range(0,l):
        if i==0:
            a=m%n
        else:
            a=a*a%n

        if e_bin[i]=='1':
            mul=mul*a
    mul=mul%n

    return mul

def rsa(m,pkey):
    n=pkey[0]
    e=pkey[1]
    c=mod(m,e,n)
    return c
def drsa(c,skey):
    n=skey[0]
    d=skey[1]
    m=mod(c,d,n)
    return m
def main():
    p=106697219132480173106064317148705638676529121742557567770857687729397446898790451577487723991083173010242416863238099716044775658681981821407922722052778958942891831033512463262741053961681512908218003840408526915629689432111480588966800949428079015682624591636010678691927285321708935076221951173426894836169
    q=144819424465842307806353672547344125290716753535239658417883828941232509622838692761917211806963011168822281666033695157426515864265527046213326145174398018859056439431422867957079149967592078894410082695714160599647180947207504108618794637872261572262805565517756922288320779308895819726074229154002310375209
    #生成公钥私钥
    pkey,skey=get_key(p,q)
    m=' Hello RSA ! 2018.9.26 '
    print('明文为：',m)
#将明文转成ascii码
    l=len(m)
    t=[]
    for i in range(0,l):
        s=hex(ord(m[i]))[2:]
        if len(s)<2:
            s='0'+s
        t.append(s)
    num=int('0x'+''.join(t),16)
#对ascii码加密
    c=rsa(num,pkey)
    print('加密后为：',c)
#解密
    d=drsa(c,skey)
#将ascii码转成字符串
    num=hex(d)[2:]
    l=len(num)
    tt=[]
    for i in range(0,l,2):

        s=num[i]+num[i+1]
        s=chr(int('0x'+s,16))
        tt.append(s)
    d=''.join(tt)
    print('解密后为：',d)

if __name__ == '__main__':
    main()