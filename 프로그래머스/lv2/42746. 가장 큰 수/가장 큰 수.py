def solution(numbers):
    nums = sorted(map(str, numbers), key=lambda x: x*3, reverse=True)
    return str(int(''.join(nums)))