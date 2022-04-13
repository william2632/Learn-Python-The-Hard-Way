# 64 · Merge Sorted Array (easy version)    合并排序数组
# https://www.lintcode.com/problem/64/
# Given two sorted integer arrays A and B, merge B into A as one sorted array.
# Modify array A in-place to merge array B into the back of array A.

class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray1(self, A, m, B, n):
        # write your code here
        #print('A=',A,';B=',B,';m=',m,';n=',n)
        C=[]
        i,j=0,0
        while(i<m or j<n):
            #print('----in ----i=',i,';j=',j,';A=',A,';B=',B,';C=',C)
            if i>= m:
                C.append(B[j])
                j +=1
            elif j>= n:
                C.append(A[i])
                i +=1
            elif A[i]<=B[j]:
                C.append(A[i])
                i +=1
            else:
                C.append(B[j])
                j +=1
            #print('----out----i=',i,';j=',j,';A=',A,';B=',B,';C=',C)
        for i in range(len(A)): A[i]=C[i]
        return A

    def mergeSortedArray2(self, A, m, B, n):
        # write your code here
        #print('A=',A,';B=',B,';m=',m,';n=',n)
        i,j,k=m-1,n-1,m+n-1
        while(k>=0):
            #print('----in ----i=',i,';j=',j,';A=',A,';B=',B,';')
            if(i<0):
                A[k]=B[j]
                j -=1
            elif(j<0):
                A[k]=A[i]
                i -=1
            elif A[i]<=B[j]:
                A[k]=B[j]
                j -=1
            elif A[i]>B[j]:
                A[k]=A[i]
                i -=1
            k -=1
            #print('----out----i=',i,';j=',j,';A=',A,';B=',B,';')
        return

def main():
    S=Solution()
    A=[1,2,3,0,0];B=[4,5];m,n=3,2;print('----before ----A=',A,';B=',B,';')
    S.mergeSortedArray1(A,m,B,n);print(A)
    A=[1,2,3,0,0];B=[4,5];m,n=3,2;print('----before ----A=',A,';B=',B,';')
    S.mergeSortedArray2(A,m,B,n);print(A)


    A=[4,5,9,0,0];B=[3,6];m,n=3,2;print('----before ----A=',A,';B=',B,';')
    S.mergeSortedArray1(A,m,B,n);print(A)
    A=[4,5,9,0,0];B=[3,6];m,n=3,2;print('----before ----A=',A,';B=',B,';')
    S.mergeSortedArray2(A,m,B,n);print(A)


if __name__ == "__main__":
    main()

