def main():
    A = list(input())
    B = input().split(" ")
    for i, a in enumerate(A):
        if a in B:
            A[i] = a.lower()
    print(''.join(A))


if __name__ == '__main__':
    main()
