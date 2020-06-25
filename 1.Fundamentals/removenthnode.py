# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curA = head
        curB = head
        count = 0
        
        while n > count:
            curB = curB.next
            count += 1
        
        if not curB:
            return head.next
        
        while curB:
            prev = curA
            curA = curA.next
            curB = curB.next
        prev.next = curA.next
        return head