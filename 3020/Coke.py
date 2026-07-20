"""Coke"""
def main():
    """pep8"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    count = 0
    total_price = 0
    if b == 0:
        c = a
    for _ in range(1,d + 1):
        if count >= b:
            total_price += c
            count = 1
        else:
            total_price += a
            count += 1
    print(total_price)
main()
