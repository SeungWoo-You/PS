def main():
    n = int(input())
    ls = input()
    count = 0
    j = 0
    while j < n:
        try:
            if ls[j] == 'p':
                if ls[j + 1] == 'P':
                    if ls[j + 2] == 'A':
                        if ls[j + 3] == 'p':
                            j += 4
                            count += 1
                        else:
                            j += 3
                    else:
                        j += 2
                else:
                    j += 1
            else:
                j += 1
        except:
            break
    print(count)


if __name__ == '__main__':
    main()
