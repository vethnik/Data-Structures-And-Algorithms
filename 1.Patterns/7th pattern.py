class Solution:
    def printTriangle(self, n):
        # Code here
        for i in range(1,2*n):
            
            if i<=n:
                stars=i
            else:
                stars=2*n-i
            for j in range(0,stars):
                print("*",end='')
            print()
n=int(input())
obj=Solution()
obj.printTriangle(n)