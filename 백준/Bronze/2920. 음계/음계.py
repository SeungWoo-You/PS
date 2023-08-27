def main():
    musics = list(map(int, input().split()))
    if musics == list(range(1, 9)):
        print("ascending")
    elif musics == list(reversed(range(1, 9))):
        print("descending")
    else:
        print("mixed")


if __name__ == '__main__':
    main()
