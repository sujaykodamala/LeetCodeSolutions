from collections import deque
class Solution:
    def createMnemonics(self, digitsQueue, result, myDict):
        if len(digitsQueue) == 0:
            return result
        ele = digitsQueue.popleft()
        temp = []
        for i in result:
            for j in myDict[ele]:
                temp.append(i+j)
        result = self.createMnemonics(digitsQueue, temp, myDict)
        return result
    
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        myDict = {}
        asciiIdx = 97
        idx = 2
        while asciiIdx < 120 and idx <= 7:
            myDict[str(idx)] = [chr(asciiIdx), chr(asciiIdx+1), chr(asciiIdx+2)]
            idx += 1
            asciiIdx += 3
        myDict['7'].append('s')
        myDict['8'] = ['t','u','v']
        myDict['9'] = ['w','x','y','z']
        myDict['0'] = ['0']
        myDict['1'] = ['1']
        result = []
        if len(digits) == 1:
            return myDict[digits[0]]
        else:
            result = myDict[digits[0]]
            result = self.createMnemonics(deque(digits[1:]), result, myDict)
        return result