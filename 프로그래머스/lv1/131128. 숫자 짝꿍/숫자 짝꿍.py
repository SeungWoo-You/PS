from collections import Counter

def solution(X, Y):
    X = str(X)
    Y = str(Y)
    count_x = Counter(list(X))
    count_y = Counter(list(Y))
    answer = ''
    for i in range(9, 0, -1):
        i = str(i)
        answer += min(count_x[i], count_y[i]) * i
    if answer == '':
        answer = '0' if count_x['0'] and count_y['0'] else '-1'
    else:
        answer += min(count_x['0'], count_y['0']) * '0'
    return answer 