class Solution:
    def sumOfMultiples(self, n: int) -> int:
        mylist = list(range(1, n+1))
        mynum = 0
        for i in range(1, n):
            if(mylist[i] % 3 == 0):
                mynum += mylist[i]
            elif(mylist[i] % 5 == 0):
                mynum += mylist[i]
            elif(mylist[i] % 7 == 0):
                mynum += mylist[i]
        return mynum
        