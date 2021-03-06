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

def main():
    S=Solution()
    source = "abcdabcdefg"; target = "bcd"
    print('------source=%s,target=%s'.format(source,target))
    print('str1:',S.str_str1(source,target))
    print('str2:',S.str_str2(source,target))

    source = "a"; target = "bcd"
    print('------source=%s,target=%s'.format(source,target))
    print('str1:',S.str_str1(source,target))
    print('str2:',S.str_str2(source,target))

    source = "abc"; target = ""
    print('------source=%s,target=%s'.format(source,target))
    print('str1:',S.str_str1(source,target))
    print('str2:',S.str_str2(source,target))

    source = "abc"; target = "edgef"
    print('------source=%s,target=%s'.format(source,target))
    print('str1:',S.str_str1(source,target))
    print('str2:',S.str_str2(source,target))


if __name__ == "__main__":
    main()