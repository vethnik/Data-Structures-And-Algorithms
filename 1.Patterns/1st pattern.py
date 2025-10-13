class spat:
    def __init__(self,n):
        '''init function can be written as #def __init__(self,n=5)
        this will take default value as 5 if no value is given'''
        self.n=n
    def pattern(self,n):
        for i in range(0,n):
                for j in range(0,n):
                    print("*",end=" ")
                print()
n=int(input())
r=spat(n)
r.pattern(n)