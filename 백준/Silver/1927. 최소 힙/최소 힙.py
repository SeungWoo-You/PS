from queue import PriorityQueue
import sys


def main():
    N = int(input())
    mheap = PriorityQueue()
    for _ in range(N):
        x = int(sys.stdin.readline())
        if x == 0:
            if mheap.qsize() == 0:
                print(0)
            else:
                print(mheap.get())
        else:
            mheap.put(x)


if __name__ == '__main__':
    main()
