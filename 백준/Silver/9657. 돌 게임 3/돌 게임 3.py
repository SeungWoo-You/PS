def main():
    N = int(input())
    res = ['SK', 'CY', 'SK', 'SK']
    for i in range(4, N):
        wins = [res[i - 1], res[i - 3], res[i - 4]]
        if 'CY' in wins:
            res.append('SK')
        else:
            res.append('CY')
    print(res[N - 1])


if __name__ == '__main__':
    main()
