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
        myDict['0'] = ['0']
        myDict['1'] = ['1']
        asciiIdx = 97
        idx = 2
        while asciiIdx < 120 and idx <= 9:
            myDict[str(idx)] = [chr(asciiIdx),chr(asciiIdx+1),chr(asciiIdx+2)]
            if str(idx) == '7':
                myDict['7'].append('s')
                asciiIdx += 1
            idx += 1
            asciiIdx += 3
            
        myDict['9'].append('z') 
        result = []
        if len(digits) == 1:
            return myDict[digits[0]]
        else:
            result = myDict[digits[0]]
            result = self.createMnemonics(deque(digits[1:]), result, myDict)
        return result