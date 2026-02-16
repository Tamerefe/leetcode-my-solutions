class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[] for _ in range(numRows)]
        arr[0].append(1)
        for i in range(1,numRows):
            arr[i].append(1)
            for j in range(1, i):
                arr[i].append(arr[i-1][j-1] + arr[i-1][j])
            arr[i].append(1)
        return arr