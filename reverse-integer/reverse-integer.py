class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #find reminder
        #find floor
        result = 0
        isNegative = True if x < 0  else False
        if isNegative:
            x *= -1
        while x > 0:
            y = x%10
            result = result*10 + y
            x = x//10
        if isNegative:
            result *= -1
        return result if abs(result) <= 0x7fffffff else 0