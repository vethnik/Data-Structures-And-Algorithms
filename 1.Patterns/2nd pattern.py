def print1(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*" ,end='')
        print()
t=int(input())
for h in range(0,t):
    n=int(input())
    print1(n)