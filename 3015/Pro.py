"""Buffet"""
def main():
    """Pro"""
    count = int(input())
    pay = int(input())
    price = float(input())
    real_count = float(input())
    free = (real_count // count) * (count - pay)
    print(f"{price * (real_count - free):.0f}")
main()
