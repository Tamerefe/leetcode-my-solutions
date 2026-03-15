class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            t = -int(str(-x)[::-1])
        else:
            t = int(str(x)[::-1])
        
        if t > 2147483647 or t < -2147483648:
            return 0
        else:
            return t