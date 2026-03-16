class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        output = 0
        for sub in accounts:
            if sum(sub) > output:
                output = sum(sub)
        return output