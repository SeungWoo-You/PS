import sys


def main():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_score, B_score = 0, 0
    draw_winner = 'D'
    for i, (a, b) in enumerate(zip(A, B), start=1):
        if a > b:
            A_score += 3
            draw_winner = 'A'
        elif b > a:
            B_score += 3
            draw_winner = 'B'
        else:
            A_score += 1
            B_score += 1
    print(A_score, B_score)
    if A_score == B_score:
        print(draw_winner)
    else:
        print('A' if A_score > B_score else 'B')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
