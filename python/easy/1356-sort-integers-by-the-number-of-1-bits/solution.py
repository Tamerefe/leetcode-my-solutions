class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        new_arr = []

        for i in range(len(arr)):
            x = arr[i] 

            tf = False
            for j in range(len(new_arr)):
                if (x.bit_count(), x) < (new_arr[j].bit_count(), new_arr[j]):
                    new_arr.insert(j, x)
                    tf = True
                    break

            if not tf:
                new_arr.append(x)

        return new_arr