class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numDict = { }
        for i, x in enumerate(numbers):
            if target-x in numDict.keys():
                return [numDict[target-x],i+1]
            else:
                if x not in numDict.keys():
                    numDict[x] = i+1
                    
                
        