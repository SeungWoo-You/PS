import sys


def main():
    while True:
        try:
            n = int(input())
            x = '1'
            while True:
                if int(x) % n == 0:
                    break
                x += '1'
            print(len(x))
        except:
            return


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
