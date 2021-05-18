# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtreeValid(self, root, branchMin, branchMax):
        if root is None:
            return True
        #rooot value should be greater than left value, root value should be less than right values
        if root.val >= branchMax or root.val <= branchMin:
            return False
        if root.right is not None and root.left is not None:
            if root.val <= root.left.val or root.val >= root.right.val:
                return False
        elif root.right is not None:
            if root.val >= root.right.val:
                return False
        elif root.left is not None:
            if root.val <= root.left.val:
                return False
        return self.isSubtreeValid(root.left, branchMin, root.val) and self.isSubtreeValid(root.right, root.val, branchMax)
    
    def isValidBST(self, root: TreeNode) -> bool:
        #the node value is less than node values on the right
        #the node values should be greater than the left
        if root is None:
            return True
        return self.isSubtreeValid(root.left, float('-inf'), root.val) and self.isSubtreeValid(root.right, root.val, float('inf'))