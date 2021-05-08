class Solution:
    def addValToCollection(self, nodeValCollection: List[List[int]] , nodeCollection:List[TreeNode]):
        tempList = []
        tempNodeList = []
        for root in nodeCollection:
            if root != None:
                tempList.append(root.val)
                if root.left != None:
                    tempNodeList.append(root.left)
                if root.right != None:
                    tempNodeList.append(root.right)
        if len(tempList) > 0:
             nodeValCollection.append(tempList)
        return tempNodeList,nodeValCollection

        
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        #Input is a root node which is a binary tree
        # in each iteration print the level node values
        # modify the node collection 
        nodeValCollection : List[List[int]] = []
        nodeCollection = [root]
        while  len(nodeCollection) > 0:
            nodeCollection,nodeValCollection = self.addValToCollection(nodeValCollection, nodeCollection)
        return nodeValCollection