# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        temp=head
        count=0
        while (count<k):
            if (temp==None):
                return head
            temp=temp.next
            count+=1
        prevNode=self.reverseKGroup(temp,k)

        temp=head
        count=0
        while(count<k):
            nxt=temp.next
            temp.next=prevNode
            prevNode=temp
            temp=nxt
            count+=1
        return prevNode