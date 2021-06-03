# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        positionCount = 1
        temp = head
        while temp != None:
            positionCount += 1
            temp = temp.next
        positionCount = positionCount - n
        nodeIdx = 1
        temp = head
        while nodeIdx < positionCount and temp != None and positionCount > 1:
            if nodeIdx == positionCount-1:
                temp.next = temp.next.next
            nodeIdx += 1
            temp = temp.next
        if positionCount == 1:
            head = head.next
        return head