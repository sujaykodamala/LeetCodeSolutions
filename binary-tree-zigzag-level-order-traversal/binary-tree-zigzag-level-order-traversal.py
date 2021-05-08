# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printDesiredOrder(self, rootList: List[TreeNode] ,valList:List[List[int]], isZigZag: bool): 
        values = []
        temproots = []
        for root in rootList:
            values.append(root.val)
            if root.left != None and root.right != None:
                temproots.append(root.left)
                temproots.append(root.right)
            elif root.right != None and root.left == None:
                temproots.append(root.right)
            elif root.left != None and root.right == None:
                temproots.append(root.left)
        if len(values) > 0:
            if isZigZag:
                values.reverse()
            valList.append(values)
        rootList = temproots
        return rootList, valList
    
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        rootCollection = [root]
        valList = []
        isZigZag = False
        while len(rootCollection) > 0:
            rootCollection, valList = self.printDesiredOrder(rootCollection,valList ,isZigZag)
            isZigZag = not isZigZag
        return valList