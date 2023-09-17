def solution(seoul):
    for i, X in enumerate(seoul):
        if X == 'Kim':
            return f"김서방은 {i}에 있다"