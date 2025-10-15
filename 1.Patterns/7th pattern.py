class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(0,N):
            for k in range(0,N-i-1):
                print(" ",end="")
            for j in range(0,2*i+1):
                print("*",end="")
            # for k in range(1,N-i+1):
            #     print(" ",end="")
            print()
N=int(input())
obj=Solution()
obj.printTriangle(N)