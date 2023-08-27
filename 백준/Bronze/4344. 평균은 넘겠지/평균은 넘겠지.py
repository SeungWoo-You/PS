import statistics as stc


def main():
    C = int(input())
    for _ in range(C):
        students = list(map(int, input().split()))[1:]
        mean = stc.mean(students)
        count = 0
        for score in students:
            if score > mean:
                count += 1
        print(f'{count / len(students):.3%}')


if __name__ == '__main__':
    main()
