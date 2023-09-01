import re

def solution(new_id):
    answer = new_id.lower()
    answer = re.sub(r'[^a-z0-9\-_.]', '', answer)
    answer = re.sub(r'\.+', '.', answer)
    answer = answer.strip('.')
    if answer == '':
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
    answer = answer.strip('.')
    if len(answer) <= 2:
        answer += answer[-1] * (3 - len(answer))
    return answer