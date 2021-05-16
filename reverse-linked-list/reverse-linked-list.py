# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, reversedList):
        if head == None:
            return reversedList
        tempNode = ListNode(head.val,reversedList)
        reversedList = tempNode
        reversedList = self.reverse(head.next, reversedList)
        return reversedList
    
    def reverseList(self, head: ListNode) -> ListNode:
        reversedList = None
        reversedList = self.reverse(head, reversedList)
        return reversedList