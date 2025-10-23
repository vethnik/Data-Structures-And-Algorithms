def numberCrown(n: int) -> None:
    # Write your solution here.
    for i in range(1,n+1):
        
        #number
        for j in range(1,i+1):
            print(j,end=" ")
        #space
        space=2*(n-i)
        for j in range(1,space):
            print(" ",end=" ")
        #number
        for j in range(i,0,-1):
            print(j,end=" ")
        
        print()
        