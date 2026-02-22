class Solution:
    def binaryGap(self, n: int) -> int:
        binary = str(bin(n)[2:])
        indexes = [i for i, ch in enumerate(binary) if ch == "1"]
        distances = [indexes[i] - indexes[i-1] for i in range(1, len(indexes))]
        if distances:
            return max(distances)
        else:
            return 0