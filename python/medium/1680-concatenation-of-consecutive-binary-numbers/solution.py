class Solution:
    def concatenatedBinary(self, n: int) -> int:
        binary = ""
        mod = 10**9 + 7

        for i in range(1, n+1):
            binary += bin(i)[2:]
        return int(binary, 2) % mod