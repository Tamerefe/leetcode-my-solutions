class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numtotal = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    if i < j:
                        numtotal += 1
        return numtotal