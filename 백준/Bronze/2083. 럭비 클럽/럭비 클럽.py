def main():
    name, age, weight = input().split(" ")
    while name != '#':
        if int(age) > 17 or int(weight) >= 80:
            club = 'Senior'
        else:
            club = 'Junior'
        print(f"{name} {club}")
        name, age, weight = input().split(" ")


if __name__ == '__main__':
    main()
