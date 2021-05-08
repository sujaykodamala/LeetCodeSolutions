# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def BFS(self, myqueue: Queue)-> List[int]:
        
        initialQueueLength = myqueue.qsize()
        i = 0
        subValList = []
        while i < initialQueueLength:
            node : TreeNode = myqueue.get()
            i += 1    
            if node is None:
                continue
            subValList.append(node.val) 
            if node.left is not None:
                myqueue.put(node.left)
            if node.right is not None:
                myqueue.put(node.right)
        return subValList
        
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        myqueue = Queue()
        if root is None:
            return []
        myqueue.put(root)
        valList = []
        while myqueue.qsize() > 0:
            valList.append(self.BFS(myqueue))
        return valList