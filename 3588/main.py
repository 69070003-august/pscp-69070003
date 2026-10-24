"""GCD_N"""
import math
def main():
    """Find GCD of N integers."""
    n = int(input())
    result = int(input())

    for _ in range(n - 1):
        num = int(input())
        result = math.gcd(result, num)

    print(result)


main()
