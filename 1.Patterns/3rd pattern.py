def print1(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j ,end='')
        print()
t=int(input())
for h in range(0,t):
    n=int(input())
    print1(n)