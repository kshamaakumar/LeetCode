# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output = []
        totallen = max(len(l1),len(l2))

        for i in range(totallen-1,-1,-1):
            output[i] = l1[i] + l2[i]
        
        return output

        