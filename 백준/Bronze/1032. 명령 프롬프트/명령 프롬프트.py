N: int = int(input())
names: list[str] = [input() for i in range(N)]
res: str = ""
for chars in zip(*names):
    char_set: set[str] = set(chars)
    if len(char_set) == 1:
        res += list(char_set)[0]
    else:
        res += "?"
print(res)