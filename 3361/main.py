"""ขายรถยนต์"""
def main():
    """pep8"""
    n = int(input())
    cars = []

    for _ in range(n):
        price, value = input().split()
        cars.append(int(value))

    best = 0
    unsold = 0

    for value in reversed(cars):
        if value > best:
            best = value
        else:
            unsold += 1

    print(unsold)
main()
