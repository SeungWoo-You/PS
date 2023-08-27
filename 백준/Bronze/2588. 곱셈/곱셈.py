def main():
    A = int(input())
    B = input()
    for x in range(len(B) - 1, -1, -1):
        print(A * int(B[x]))
    print(A * int(B))


if __name__ == '__main__':
    main()
