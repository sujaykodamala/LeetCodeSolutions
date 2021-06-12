"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def createClone(self, node, processedList,parent):
        if node == None:
            return node
        if node.val in processedList:
            return processedList[node.val]
        clonedNode = Node(node.val, [])
        processedList[node.val] = clonedNode
        for i in node.neighbors:
            clonedNode.neighbors.append(self.createClone(i, processedList, node.val))
        return clonedNode
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        processedList = {}
        parent = 0
        clonedGraph = self.createClone(node, processedList,parent)
        return clonedGraph