"""Electric_Using"""
def main():
    """pep8"""
    n = int(input())
    money = 0

    if n <= 10:
        money = n * 5
    elif n <= 50:
        money = 10 * 5
        money += (n - 10) * 7
    elif n <= 100:
        money = 10 * 5
        money += 40 * 7
        money += (n - 50) * 10
    elif n <= 200:
        money = 10 * 5
        money += 40 * 7
        money += 50 * 10
        money += (n - 100) * 12
    else:
        money = 10 * 5
        money += 40 * 7
        money += 50 * 10
        money += 100 * 12
        money += (n - 200) * 15
    ft = n * 0.50
    vat = money * 0.07
    total = money + ft + vat
    print(f"{total:.1f}")
main()
