class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        left_bin = bin(left)[2:]
        right_bin = bin(right)[2:]
        num = 0
        clc = 0
        for i in range(left, right+1):
            num = bin(i).count("1")
            if num < 2:
                continue
            prime = True
            for d in range(2, int(math.sqrt(num)) + 1):
                if num % d == 0:
                    prime = False
                    break
            if prime:
                clc += 1
        return clc
        