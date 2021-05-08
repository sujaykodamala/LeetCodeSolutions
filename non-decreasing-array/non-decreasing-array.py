class Solution:
    def isArraySorted(self,array1, index):
        array1.pop(index)
        subArray = array1.copy()
        subArray.sort()
        return subArray == array1
    
    def checkPossibility(self, nums: List[int]) -> bool:
    
        idx = 1
        while idx < len(nums) :
            if nums[idx] < nums[idx-1]:
                if idx == len(nums)-1:
                    return self.isArraySorted(nums, idx)
                return self.isArraySorted(nums, idx-1 if nums[idx-1] > nums[idx+1] else idx)
            idx +=1 
        
        return True 