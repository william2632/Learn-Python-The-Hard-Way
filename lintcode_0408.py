# 408 · Add Binary      408. 二进制求和
# https://www.lintcode.com/problem/408/
# Given two binary strings, return their sum (In binary notation).

class Solution:
    """
    @param a: a number
    @param b: a number
    @return: the result
    """
    def add_binary(self, a: str, b: str) -> str:
        # write your code here
        print(a,b)
        aR=a[::-1]
        bR=b[::-1]
        cUpgread=0
        c0,c1='0','1'
        c=''
        ac,bc='',''
        for i in range(max(len(a),len(b))+1):
            if(i>=len(a)):ac=c0
            else: ac=aR[i]
            if(i>=len(b)):bc=c0
            else: bc=bR[i]
            #print(i,ac,bc)
            if(ac==c0 and bc==c0):
                if(cUpgread==0):
                    c=f'{c}{c0}'
                else:
                    c=f'{c}{c1}';cUpgread=0
            elif(ac==c1 and bc==c1):
                if(cUpgread==0):
                    c=f'{c}{c0}';cUpgread=1
                else:
                    c=f'{c}{c1}';cUpgread=1
            else:
                if(cUpgread==0):
                    c=f'{c}{c1}';cUpgread=0
                else:
                    c=f'{c}{c0}';cUpgread=1
        for j in range(i,0,-1):
            if(c[j]!=c0):break
        if(j>1):c=c[:(j+1)]
        else:c=c[:j]
        return c[::-1]

    def add_binary2(self, a: str, b: str) -> str:
        # write your code here
        print(a,b)
        indexa=len(a)-1
        indexb=len(b)-1
        carry=0
        Ssum=''
        while indexa>=0 or indexb >=0:
            if(indexa<0):aV=0
            else:aV=(a[indexa])
            if(indexb<0):bV=0
            else:bV=(b[indexb])
            S=(int(aV)+int(bV)+carry)%2
            carry=(int(aV)+int(bV)+carry)//2
            Ssum = str(S) + Ssum
            #print(aV,bV)
            #print(Ssum, carry)
            indexa -= 1
            indexb -= 1
        if(carry==1): Ssum = '1' + Ssum
        iSum=str(int(Ssum))
        return iSum

def main():
    S=Solution()
    print(S.add_binary('0','0'))
    print(S.add_binary('00000','00000'))
    print(S.add_binary('11','1'))
    print(S.add_binary('1010','10'))
    print(S.add_binary('1010','1011'))

    print(S.add_binary2('0','0'))
    print(S.add_binary2('00000','0000'))
    print(S.add_binary2('11','1'))
    print(S.add_binary2('1010','10'))
    print(S.add_binary2('1010','1011'))
if __name__ == "__main__":
    main()

