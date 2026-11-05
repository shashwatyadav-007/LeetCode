# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        curr=head
        arr=[]
        while(curr):
            arr.append(curr.val)
            curr=curr.next
        arr2=arr[::-1]
        return arr==arr2