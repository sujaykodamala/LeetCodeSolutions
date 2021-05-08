# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        if root is not None:
            intList = []
            intList.append(root.val)
            for x in self.preorderTraversal(root.left):
                intList.append(x)
            for y in self.preorderTraversal(root.right):
                intList.append(y)
            return intList
        return []    