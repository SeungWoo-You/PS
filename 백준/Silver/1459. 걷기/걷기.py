def main():
    X, Y, W, S = map(int, input().split())
    dist = min(X, Y)
    res = 0
    if 2 * W >= S:
        res += dist * S
        X -= dist
        Y -= dist
        dist = X if X != 0 else Y
        if W >= S:
            if dist % 2 == 0:
                res += dist * S
            else:
                res += (dist - 1) * S + W
        else:
            res += dist * W
    else:
        res = (X + Y) * W
    print(res)


if __name__ == '__main__':
    main()
