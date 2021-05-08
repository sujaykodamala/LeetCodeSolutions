class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # input: array of integers, target
        # output: indices of numbers that sum up to the target
        
        myDict = {}
        
        for idx, value in enumerate(nums):
            if target-value in myDict.keys():
                return [idx, myDict[target-value]]
            else:
                myDict[value] = idx
        return []
        
