def main():
    N = int(input())
    i = (109 - N) // 10
    grades = ['A', 'A', 'B', 'C', 'D']
    try:
        print(grades[i])
    except:
        print('F')


if __name__ == '__main__':
    main()
