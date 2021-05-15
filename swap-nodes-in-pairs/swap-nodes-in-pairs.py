# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        if head.next == None:
            return head
        firstNode = head.next
        secondNode = head
        secondNode.next = head.next.next if head.next.next != None else None
        firstNode.next = secondNode
        head = firstNode
        head.next = secondNode
        if head.next.next != None:
            head.next.next = self.swapPairs(head.next.next)
        return head