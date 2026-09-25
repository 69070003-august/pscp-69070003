"""ตั๋วหนังสุดป่วน"""
def main():
    """pep8"""
    seats = int(input())

    while seats > 0:
        try:
            age, ticket = map(int, input().split())
        except EOFError:
            break

        if age < 15:
            print(-1)
            continue

        if ticket > seats:
            print(-2)
            continue

        if 15 <= age <= 22:
            price = 120 * ticket

            if ticket >= 2:
                print(price, 10)
            else:
                print(price, 0)

        elif age >= 60:
            price = 75 * ticket
            print(price, 0)

        else:
            price = 150 * ticket
            print(price, 0)
        seats -= ticket
main()
