"""Ticket"""
def main():
    """pep"""
    a,b = input().split()
    a = int(a)
    if a < 5:
        price = 0
    elif a <= 18:
        price = 100
    elif a >= 19:
        price = 150
    if b == "Wed":
        price = price // 2
    print(price)
main()
