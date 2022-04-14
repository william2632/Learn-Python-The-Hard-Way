# 141. x的平方根
# https://www.lintcode.com/problem/141/
# https://www.lintcode.com/problem/sqrtx/description
# Implement int sqrt(int x). Compute and return the square root of x.
# 实现 int sqrt(int x) 函数，计算并返回 x 的平方根。

class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def sqrt(self, x: int) -> int:
        # write your code here
        if(x==0): return 0
        #if(x==1): return 1
        for i in range(1,x+1):
            if(i*i==x):return i
            if(i*i>x):return i-1

def main():
    S=Solution()
    for i in range(0,20):
        iSqrt=S.sqrt(i);print('----nums:',i,'; sqrt=',iSqrt)
if __name__ == "__main__":
    main()
    print(7//2)
    print(11//2)
    print(11/2)

