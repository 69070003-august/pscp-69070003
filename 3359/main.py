"""กองชาม"""
def main():
    """pep8"""
    n = int(input())
    count = {}

    for _ in range(n):
        size = input().strip()
        count[size] = count.get(size, 0) + 1

    print(max(count.values()))
main()
