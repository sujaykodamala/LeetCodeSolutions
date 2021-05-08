class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = 0
        z = x
        factor = 10
        while x > 0:
            remainder = x%factor
            y = y *factor + remainder
            x = x//10
        if z == y:
            return True
        else:
            return False