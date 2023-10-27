import sys


def main():
    check = False
    for i in range(1, 6):
        name = input().strip()
        if 'FBI' in name:
            print(i)
            check = True
    if check == False:
        print('HE GOT AWAY!')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
