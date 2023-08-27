import datetime


def main():
    today = datetime.date.today()
    print(f"{today.year}-{today.month:02d}-{today.day}")


if __name__ == '__main__':
    main()
