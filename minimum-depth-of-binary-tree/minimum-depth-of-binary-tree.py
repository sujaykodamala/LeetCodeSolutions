# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def calBranchSums(self, root, depth, depthCollection):
        if root is None:
            depthCollection.append(depth)
            return depthCollection
        
        depth += 1
        if root.left != None and root.right != None:
            depthCollection = self.calBranchSums(root.left,depth,depthCollection)
            depthCollection = self.calBranchSums(root.right,depth,depthCollection)
        elif root.right == None:
            depthCollection = self.calBranchSums(root.left,depth,depthCollection)
        else:
            depthCollection = self.calBranchSums(root.right, depth, depthCollection)
        return depthCollection
        
    def minDepth(self, root: TreeNode) -> int:
        #input: a tree
        #output: min depth of the tree
        #Approach 1: calculate each depth and return the min depth from the arrays of depths
        #Algorithm1: if root.left != None and root.right != none, calculate depth on both right and left sub tree, 
        #continued-- sort the array and return min value in the array
        if root is None:
            return 0
        depth = 0 
        depthCollection = []
        depthCollection = self.calBranchSums(root, depth, depthCollection)
        depthCollection.sort()
        return 0 if len(depthCollection) ==  0 else depthCollection[0]