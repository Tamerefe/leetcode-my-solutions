class Solution:
    def romanToInt(self, s: str) -> int:
        romanNum = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        value = 0
        for i in range(len(s)-1):
            if romanNum[s[i]] == romanNum[s[i + 1]]:
                value += romanNum[s[i]]
            elif romanNum[s[i]] > romanNum[s[i + 1]]:
                value += romanNum[s[i]]
            elif romanNum[s[i]] < romanNum[s[i + 1]]:
                value -= romanNum[s[i]]
        value += romanNum[s[-1]]
        return value