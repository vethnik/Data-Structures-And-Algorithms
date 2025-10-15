def print5(n):
    for i in range(0,n):
        for j in range(0,n-i):
            print(j+1,end="")
        print()
n=int(input())
print5(n)