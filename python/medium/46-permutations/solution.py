from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        perm_list = list(permutations(nums))
        return perm_list