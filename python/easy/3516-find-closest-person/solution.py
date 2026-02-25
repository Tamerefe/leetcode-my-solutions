class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        p13 = abs(z - x)
        p23 = abs(z - y)
        if p23 > p13:
            return 1
        elif p13 > p23:
            return 2
        elif p13 == p23:
            return 0