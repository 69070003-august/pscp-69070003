"""GCD_v2"""
def main():
    """Find GCD using Euclidean Algorithm."""
    num1 = int(input())
    num2 = int(input())

    while num2 != 0:
        num1, num2 = num2, num1 % num2

    print(abs(num1))


main()
