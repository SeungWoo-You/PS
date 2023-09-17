from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    checked: defaultdict[str, set[str]] = defaultdict(set)
    count: dict[str, int] = {i: 0 for i in id_list}
    for R in report:
        src, dst = R.split()
        if dst not in checked[src]:
            checked[src].add(dst)
            count[dst] += 1
    banned: set[str] = set()
    for user, num in count.items():
        if num >= k:
            banned.add(user)
    for idx in id_list:
        answer.append(len(checked[idx] & banned))
    return answer