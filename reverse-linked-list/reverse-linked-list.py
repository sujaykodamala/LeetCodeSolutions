# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, reversedList):
        if head == None:
            return reversedList
        reversedList = ListNode(head.val,reversedList)
        reversedList = self.reverse(head.next, reversedList)
        return reversedList
    
    def reverseList(self, head: ListNode) -> ListNode:
        
        reversedList = self.reverse(head, None)
        return reversedList