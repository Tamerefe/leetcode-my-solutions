class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        lst = []
        kids = 0  
            
        for n in candies:
            for x in candies:
                if n + extraCandies >= max(candies):
                    lst.append(True)
                else:
                    lst.append(False)
                break
        return lst