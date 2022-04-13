# 141. x的平方根
# https://www.lintcode.com/problem/141/
# https://www.lintcode.com/problem/sqrtx/description
# Given a sorted array, 'remove' the duplicates in place such that each element appear only once and return the 'new' length.
# Do not allocate extra space for another array, you must do this in place with constant memory. We will determine correctness by the length k of the returned array, intercepting the first k elements of the array.
# 实现 int sqrt(int x) 函数，计算并返回 x 的平方根。

class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        print(nums)
        if(nums==[]):return 0
        cInd=0
        for i in range(1,len(nums)):
            if(nums[cInd]!=nums[i]):
                if(i-cInd!=1):
                    nums[cInd+1]=nums[i]
                cInd += 1
        del nums[cInd+1:]
        return cInd + 1

def main():
    S=Solution()
    nums=[1,1,2];print('----before ----nums=',nums);rLen=S.removeDuplicates(nums);print('----after ----nums:',rLen,'; nums=',nums)
    nums=[1,1,2,3,4,4,4,4,5,6];print('----before ----nums=',nums);rLen=S.removeDuplicates(nums);print('----after ----nums:',rLen,'; nums=',nums)
    nums=[1,1,2,3,6,6,6,8,12,12];print('----before ----nums=',nums);rLen=S.removeDuplicates(nums);print('----after ----nums:',rLen,'; nums=',nums)

if __name__ == "__main__":
    main()

