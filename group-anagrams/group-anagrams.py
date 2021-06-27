class Solution:
    def getAnagramDict(self, strs):
        anagramDict = {}
        idx = 0
        while idx < len(strs):
            word = ''.join(sorted(strs[idx]))
            if word in anagramDict:
                anagramDict[word].append(idx)
            else:
                anagramDict[word] = [idx]
            idx += 1
        return anagramDict
    
    def prepareResult(self, strs, anagramDict):
        result = []
        idx = 0
        for i in anagramDict.keys():
            localResult = []
            for j in anagramDict[i]:
                localResult.append(strs[j])
            result.append(localResult)
        return result
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return self.prepareResult(strs, self.getAnagramDict(strs))