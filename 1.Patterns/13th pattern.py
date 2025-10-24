def nNumberTriangle(n: int) -> None:
    # Write your solution here.
    num=1
    for i in range(1,n):
        for j in range(0,i):
            print(num,end=" ")
            num+=1
        print()