# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def calBranchSums(self, root, depth, minDepth):
        if root is None:
            minDepth = minDepth if depth > minDepth else depth
            return minDepth
        depth += 1
        if root.left != None and root.right != None:
            minDepth = self.calBranchSums(root.left,depth,minDepth)
            minDepth = self.calBranchSums(root.right,depth,minDepth)
        elif root.right == None:
            minDepth = self.calBranchSums(root.left,depth,minDepth)
        else:
            minDepth = self.calBranchSums(root.right, depth, minDepth)
        return minDepth
        
    def minDepth(self, root: TreeNode) -> int:
        #input: a tree
        #output: min depth of the tree
        #Approach 1: calculate each depth and return the min depth from the arrays of depths
        #Algorithm1: if root.left != None and root.right != none, calculate depth on both right and left sub tree, 
        #continued-- sort the array and return min value in the array
        #algorithm2: calculate each depth and compare get the minimum in each calculation
        #to begin with first value to be compared is infinity. 
        if root is None:
            return 0
        depth = 0
        minDepth = float('inf')
        minDepth = self.calBranchSums(root, depth, minDepth)
        
        return minDepth