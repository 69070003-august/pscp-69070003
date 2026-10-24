"""[LEARNING LOGS] isPrime_large"""
def main():
    """Check prime number."""
    n = int(input())

    if n < 2:
        print("NO")
        return

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("NO")
            return

    print("YES")


if __name__ == "__main__":
    main()

