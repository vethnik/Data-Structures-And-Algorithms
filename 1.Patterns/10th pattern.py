def nStarTriangle(n: int) -> None:
    # Write your code here.
    for i in range(1,2*n):
        
        stars=i
        if(i>n):
            stars=2*n-i

        for j in range(0,stars):
            print("*",end='')
        print()