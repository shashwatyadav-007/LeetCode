# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or k==0:
            return head
            
        temp=head
        count=0
        while(temp):
            count+=1
            if (temp.next==None):
                last=temp
            temp=temp.next
        k=k%count
        if k==0:
            return head
        newLast=head
        for i in range(count-k-1):
            newLast=newLast.next

        newhead = newLast.next
        last.next=head
        newLast.next=None

        return newhead