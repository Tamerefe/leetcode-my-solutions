class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = [[] for _ in range(rowIndex + 1)]
        for i in range(rowIndex + 1):
            arr[i].append(1)
            for j in range(1, i):
                arr[i].append(arr[i-1][j-1] + arr[i-1][j])
            arr[i].append(1)
        if rowIndex == 0:
            return [1]
        else:    
            return arr[-1]