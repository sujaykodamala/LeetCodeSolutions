class Solution:
    def getReversedString(self,s, k, m):
        
        if k < m:
            return s
        s[k],s[m] = s[m],s[k]
        s = self.getReversedString(s,k-1,m+1)
        
        
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s = self.getReversedString(s, len(s)-1,0)
        