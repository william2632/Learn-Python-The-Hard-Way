# 56 · Two Sum  两数之和
# https://www.lintcode.com/problem/56/description
# Given an array of integers, find two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are zero-based.

from typing import (
    List,
)

class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def two_sum1(self, numbers: List[int], target: int) -> List[int]:
        # write your code here
        listLen=len(numbers)
        for i in range(listLen-1):
            #if numbers[i]<=target:          # 不对，可能有负数
            for j in range(i+1,listLen-1):
                if numbers[i]+numbers[j]==target:
                    return [i,j]
        return[0,0]

    def two_sum2(self, numbers: List[int], target: int) -> List[int]:
        # write your code here
        um=dict()
        listLen=len(numbers)
        for i in range(listLen-1):
            if numbers[i] in um:
                result=[]
                result.append(um[numbers[i]])
                result.append(i)
                return result
            um[target-numbers[i]]=i
        return[0,0]

    def two_sum3(self, numbers: List[int], target: int) -> List[int]:
        # write your code here
        backUp = numbers[:]         # this is link, not deep copy
        numbers = sorted(numbers)   # but sorted created a deep copy
        i,j = 0, len(numbers)-1
        while i<j:
            if numbers[i]+numbers[j]==target: break
            elif numbers[i]+numbers[j]<target: i+=1
            else: j -= 1
        a,b=0,0
        for k in range(len(numbers)):
            if backUp[k]==numbers[i] and a==0:
                i=k
                a=1
            elif backUp[k]==numbers[j] and b==0:
                j=k
                b=1
            elif a==1 and b==1: break
        return sorted([i,j])

def main():
    S=Solution()
    source = [2,7,11,15]; target = 9
    print('------source={0:s},target={1:d}'.format((',').join([str(i) for i in source]),target))
    print('str1:',S.two_sum1(source,target))
    print('str2:',S.two_sum2(source,target))
    print('str3:',S.two_sum3(source,target))

    S=Solution()
    source = [15,2,7,11]; target = 9
    print('------source={0:s},target={1:d}'.format((',').join([str(i) for i in source]),target))
    print('str1:',S.two_sum1(source,target))
    print('str2:',S.two_sum2(source,target))
    print('str3:',S.two_sum3(source,target))
        

if __name__ == "__main__":
    main()

