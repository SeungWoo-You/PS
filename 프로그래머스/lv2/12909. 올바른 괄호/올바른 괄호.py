def solution(s):
    stack: list[str] = []
    for bracket in s:
        if bracket == '(':
            stack.append(bracket)
        else:
            try:
                if stack.pop() != '(':
                    return False
            except:
                return False
    return True if not stack else False