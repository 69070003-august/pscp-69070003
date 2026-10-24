"""MissingNumber"""
def main():
    """Find missing numbers."""
    n = int(input())
    numbers = set()

    while True:
        num = int(input())
        if num == 0:
            break
        numbers.add(num)

    for i in range(1, n + 1):
        if i not in numbers:
            print(i)
main()
