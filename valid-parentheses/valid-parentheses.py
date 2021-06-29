class Solution:
    def isValid(self, s: str) -> bool:
        openType = {}
        openType[')'] = '('
        openType['}'] = '{'
        openType[']'] = '['
        
        stack = []
        for char in s:
            if char in openType:
                if len(stack) == 0:
                    return False
                if stack[-1] != openType[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return (len(stack)==0)