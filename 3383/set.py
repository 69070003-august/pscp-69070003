"""Difference"""
def main():
    """pep8"""
    n = int(input())
    m = int(input())

    set_a = set()
    set_b = set()

    for _ in range(n):
        set_a.add(int(input()))

    for _ in range(m):
        set_b.add(int(input()))

    answer = sorted(set_a - set_b)
    print(*answer)
main()
