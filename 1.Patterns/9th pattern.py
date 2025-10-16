def erect_pyramid(N):
    # Outer loop for rows
    for i in range(N):
        for j in range(N - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        for j in range(N - i - 1):
            print(" ", end="")
        print()


def inverted_pyramid(N):
    # Outer loop for rows
    for i in range(N):
        for j in range(i):
            print(" ", end="")
        for j in range(2 * N - (2 * i + 1)):
            print("*", end="")
        for j in range(i):
            print(" ", end="")
        print()


def main():
    N = int(input())
    erect_pyramid(N)
    inverted_pyramid(N)
if __name__ == "__main__":
    main()
