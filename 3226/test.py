"""[Recommend] Inflation"""
def main():
    """pep8"""
    money = float(input())
    year = int(input())

    for _ in range(year):
        money *= 1.0381
        money = int(money * 100) / 100

    print(f"{money:.2f}")


main()
