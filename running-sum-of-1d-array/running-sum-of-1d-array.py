class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        idx = 1
        while idx < len(nums):
            nums[idx] += nums[idx-1]
            idx += 1
        return nums
        