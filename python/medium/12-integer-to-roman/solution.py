class Solution:
    def intToRoman(self, num: int) -> str:
        romanNum = [
            ("I", "V", "X"),
            ("X", "L", "C"),
            ("C", "D", "M"),
            ("M", "", "")
        ]

        digits = list(map(int, str(num)))[::-1]
        result = ""

        for i, digit in enumerate(digits):
            one, five, ten = romanNum[i]
            
            if digit <= 3:
                result = one * digit + result
            elif digit == 4:
                result = one + five + result
            elif digit <= 8:
                result = five + one * (digit - 5) + result
            elif digit == 9:
                result = one + ten + result
        return result