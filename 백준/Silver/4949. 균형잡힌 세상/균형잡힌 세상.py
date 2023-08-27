def main():
    line = ''
    while True:
        keep = True
        line = input()
        if line == '.':
            break
        stack: list[str] = []
        for char in line:
            if char == '(' or char == '[':
                stack.append(char)
            elif char == ')':
                if not stack:
                    print("no")
                    keep = False
                    break
                pair = stack.pop()
                if pair != '(':
                    print("no")
                    keep = False
                    break
            elif char == ']':
                if not stack:
                    print("no")
                    keep = False
                    break
                pair = stack.pop()
                if pair != '[':
                    print("no")
                    keep = False
                    break
        if keep == True:
            print("yes") if not stack else print("no")


if __name__ == '__main__':
    main()
