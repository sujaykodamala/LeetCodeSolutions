class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Given : An array of numbers
        # Find : return an array of sub arrays of three elements that sum up to 0
        # Constraints: 0 <= len(arr) <= 3000 , -10*5 <= nums[i] <= 10*5
        
        resultSet = []
        if len(nums) == 0:
            return []
        nums.sort()
        #Iterate the iterate from first value and find the result set in rest of the array 0  to n-3
        i = 0
        while i < len(nums)-2:
            j = i + 1
            k = len(nums)-1
            if i > 0:
                if nums[i] == nums[i-1]:
                    i += 1
                    continue
            while j < k:
                if nums[j]+nums[k] == -nums[i]:
                    lastInsertion = [] if len(resultSet) == 0 else resultSet[len(resultSet)-1]
                    if  lastInsertion != [nums[i],nums[j],nums[k]]:
                        resultSet.append([nums[i],nums[j],nums[k]])                   
                    j += 1
                    k -= 1
                elif nums[j]+nums[k] < -nums[i]:
                    j += 1
                elif nums[j] + nums[k] > -nums[i]:
                    k -= 1
            i += 1
            
        return resultSet
        
            
        # In each iteration, reference two pointers
        # Compare leftIndex value to rightIndex 
        # if the sum is less than target - increase leftIndex (arr value that has less weight)
        # If the sum is more than target - decrease right Index (arr value that has more weight)