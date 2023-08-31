def solution(N, src=1, dst=3, sub=2, answer=[]):
    if N == 1:
        answer.append([src,dst])
        return answer
    answer = solution(N - 1, src, sub, dst, answer)
    answer.append([src, dst])
    answer = solution(N - 1, sub, dst, src, answer)
    return answer