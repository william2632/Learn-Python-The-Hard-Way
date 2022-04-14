# 174 · Remove Nth Node From End of List    174. 删除链表中倒数第n个节点
# https://www.lintcode.com/problem/174/
# Given a linked list, remove the nth node from the end of list and return its head.

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

"""
Definition of ListNode:
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        # write your code here
        LNlen=0
        Head0=head
        while Head0:
            #print('LNlen=',LNlen,';Val=',Head0.val,';')
            Head0=Head0.next
            LNlen +=1
        #print('LNlen=',LNlen)

        LNlen2=0
        Head1=head
        HeadOut=Head1
        HeadN1=Head1
        while Head1:
            #print('LNlen2=',LNlen2,';Val=',Head1.val,';')
            if(LNlen2==(LNlen-n-1)):HeadN1=Head1
            if(LNlen2==(LNlen-n+1)):
                HeadN1.next=Head1
                break
            Head1=Head1.next
            LNlen2 +=1
        return HeadOut

    def remove_nth_from_end2(self, head: ListNode, n: int) -> ListNode:
        # write your code here
        d=ListNode(0,head)
        Head0=d
        for i in range(0,n):
            head=head.next
        while head:
            head=head.next
            Head0=Head0.next
        Head0.next=Head0.next.next
        return d.next

def main():
    lNode5=ListNode(5)
    lNode4=ListNode(4,lNode5)
    lNode3=ListNode(3,lNode4)
    lNode2=ListNode(2,lNode3)
    lNode1=ListNode(1,lNode2)

    S=Solution()
    NoteAfterRemove=S.remove_nth_from_end(lNode1,2)
    LNlen=0
    while NoteAfterRemove:
        print('LNlen=',LNlen,';Val=',NoteAfterRemove.val,';')
        NoteAfterRemove=NoteAfterRemove.next
        LNlen +=1
    print('LNlen=',LNlen)

    NoteAfterRemove=S.remove_nth_from_end2(lNode1,2)
    LNlen=0
    while NoteAfterRemove:
        print('LNlen=',LNlen,';Val=',NoteAfterRemove.val,';')
        NoteAfterRemove=NoteAfterRemove.next
        LNlen +=1
    print('LNlen=',LNlen)   

if __name__ == "__main__":
    main()

