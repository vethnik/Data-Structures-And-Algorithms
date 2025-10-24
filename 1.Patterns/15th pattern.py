def nLetterTriangle(n: int):
    
    for i in range(0,n):
        for j in range(0,n-i):
            print(chr(65+j),end=" ")
        print()
