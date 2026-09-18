"""Right Arrow"""
def main():
    """pep8"""
    k = int(input())
    n = int(input())
    mid = n // 2
    for row in range(mid + 1):
        print(" " * row + "*" * k)
    for row in range(mid - 1, -1, -1):
        print(" " * row + "*" * k)
main()
