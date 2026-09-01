"""[LEARNING LOGS] สหกรณ์โรงเรียน"""
from decimal import Decimal, ROUND_HALF_UP
def main():
    """pep8"""
    member = input()
    n = int(input())
    total = Decimal("0")
    for _ in range(n):
        price = Decimal(input())
        total += price
    if member == "Y":
        discount = total * Decimal("0.05")
    elif member == "N" and total >= Decimal("500"):
        discount = total * Decimal("0.03")
    else:
        discount = Decimal("0")
    net = total - discount
    net = net.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    print(net)
main()
