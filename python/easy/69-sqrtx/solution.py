class Solution:
    def mySqrt(self, x: int) -> int:
        n = 2
        prev = -1
        while True: 
            n = (n + x/n)/2

            if int(n) == prev:
                return int(n)
            prev = int(n)
        