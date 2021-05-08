# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calculateSum(self,root:TreeNode, pathSum: int,targetSum:int) :
        if root == None:
            return False
        if root.left == None and root.right == None:
            pathSum += root.val
            if pathSum == targetSum:
                return True
            else:
                return False
        return self.calculateSum(root.left, pathSum+root.val, targetSum) or self.calculateSum(root.right,  pathSum+root.val, targetSum) 
        
        
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root == None:
            return False
        return self.calculateSum(root,0,targetSum)