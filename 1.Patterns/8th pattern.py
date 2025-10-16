class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(0,N):
            for j in range(0,i):
                print(" ",end="")
            for k in range(0,2*N-(2*i+1)):
                print("*",end='')
            print()