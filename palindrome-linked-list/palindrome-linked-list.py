# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        valList = []
        
        while(head is not None):
            valList.append(head.val)
            head = head.next
        if valList == valList[::-1]:
            return True
        else:
            return False
        return True