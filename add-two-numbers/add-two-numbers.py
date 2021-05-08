# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Problem:
#Given: A list of non empty linked lists 
#Linked Lists : Contain two non negative integers, 
#digits are stored in a reverse order
#each node has a single digit
#add two numbers and return the sum as a linked list
#Constraints: two numbers do not contain any leading zero

#two non empty linked list represents two non negative integers 
#in reverse order
#these integers (which are given in reverse order) are to be added and returned
#linked list are not cyclic or not double linked list
# two number do not contain any leading zero

#Given : two non-empty linked lists representing two non negative values
#Find : Return the sum of integers (a reverse order  as a linked list
#none of these value having a leading zero unless it is zero itself
#does not spepcifiy anything about the number of nodes (same or not)

class Solution:
    
    def getNumbersList(self, l: ListNode):
        #iterate through linkedlist until the last node is None
        sumlist = []
        while(l is not None) :
             #meanwhile gather the elements
            sumlist.append(l.val)
            l = l.next
        #reverse them
        #sumlist.reverse()
        return sumlist
        #return them
        
    def addTwoLists(self, list1, list2,leftOver ):
        maxlength = len(list1) if len(list1) > len(list2) else len(list2)
        sumlist = []
        i = 0
        while i < maxlength:
            val = (0 if i >= len(list1) else list1[i]) +                                                              (0 if i >= len(list2) else list2[i]) +leftOver
            leftOver = 0 if val < 10 else 1
            val  = val if val < 10 else (val-10)
            sumlist.append(val)
            i += 1
        if leftOver > 0 :
            sumlist.append(leftOver)
        return sumlist    
               
    def prepareLinkedList(self, l):
        
        listNode = None
        if len(l) is 0:
            listNode = None
        else:
            if(len(l) > 0):
                listNode = ListNode(l[0],None)
                listNode.next = None if len(l) == 1 else self.prepareLinkedList(l[1:len(l)])
        return listNode
                
            
            
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #Iterate through the nodes and prepare a number
        numbers1= self.getNumbersList(l1)
        numbers2 = self.getNumbersList(l2)
        #declare a method that return the sum of both values in the lists
        sumlist = self.addTwoLists(numbers1,numbers2,0)
        finalListNode = self.prepareLinkedList(sumlist)
        return finalListNode
    
    
    
    
            
        