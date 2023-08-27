def main():
    id = list(map(int, input().split(" ")))
    id_square = [x**2 for x in id]
    print(sum(id_square) % 10)


if __name__ == '__main__':
    main()
