# 13 · Implement strStr()   字符串查找
# https://www.lintcode.com/problem/13/description
# For a given source string and a target string, you should output the first index(from 0) of target string in the source string.If the target does not exist in source, just return -1.

class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def str_str1(self, source: str, target: str) -> int:
        # Write your code here
        #print('source:',source)
        #print('target:',target)
        sourceLen=len(source)
        targetLen=len(target)
        if targetLen==0:return 0
        if targetLen>sourceLen:return -1
        return source.index(target)

    def str_str2(self, source, target):
        sourceLen=len(source)
        targetLen=len(target)
        #print(sourceLen,targetLen)
        if targetLen==0:return 0
        if targetLen>sourceLen:return -1
        for i in range(sourceLen - targetLen +1):
            for j in range(targetLen):
                if source[j+i]==target[j]:
                    if j==targetLen-1: return i
                else: break
        return -1

    def str_str3(self, source, target):
        # Write your code here
        sLen=len(source)
        tLen=len(target)
        if sLen<tLen: return -1
        if tLen==0: return 0
        for s in range(sLen-tLen+1):
            iMatch=True
            for t in range(tLen):
                if source[s+t]!=target[t]:
                    iMatch=False
                    break
            if iMatch==True:
                return s
        return -1

def main():
    S=Solution()
    source = "abcdabcdefg"; target = "bcd"
    print('------source={0:s},target={1:s}'.format(source,target))
    print('str1:',S.str_str1(source,target))
    print('str2:',S.str_str2(source,target))
    print('str3:',S.str_str3(source,target))

    source = "a"; target = "bcd"
    print('------source={0:s},target={1:s}'.format(source,target))
    print('str1:',S.str_str1(source,target))
    print('str2:',S.str_str2(source,target))
    print('str3:',S.str_str3(source,target))

    source = "abc"; target = ""
    print('------source={0:s},target={1:s}'.format(source,target))
    print('str1:',S.str_str1(source,target))
    print('str2:',S.str_str2(source,target))
    print('str3:',S.str_str3(source,target))

    source = "abc"; target = "edgef"
    print('------source={0:s},target={1:s}'.format(source,target))
    print('str1:',S.str_str1(source,target))
    print('str2:',S.str_str2(source,target))
    print('str3:',S.str_str3(source,target))


if __name__ == "__main__":
    main()


#KMP
# https://blog.csdn.net/weixin_52622200/article/details/110563434