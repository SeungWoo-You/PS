def main():
    stairs = int(input())
    pts = [int(input()) for _ in range(stairs)]
    if stairs == 1:
        print(pts[0])
        return
    way_1 = [pts[0]]
    way_2 = [pts[1], way_1[0] + pts[1]]
    way_prev = way_2
    ls_max = [max(way_1), max(way_2)]
    for s in range(2, stairs):
        way = [ls_max[-2] + pts[s], ls_max[-1] + pts[s]]
        step = max(way)
        if step == way[1]:
            if step == way_prev[1] + pts[s]:
                step = max(way[0], way_prev[0] + pts[s])
        way[1] = step
        ls_max.append(step)
        way_prev = way
    print(ls_max[-1])


if __name__ == '__main__':
    main()
