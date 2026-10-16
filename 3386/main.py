"""[LEARNING LOGS] Duplicate I"""
def main():
    """pep8"""
    a = set()
    b = set()
    m = int(input())
    n = int(input())

    for _ in range(m):
        a.add(int(input()))

    for _ in range(n):
        b.add(int(input()))

    answer = sorted(a & b, reverse=True)

    if answer:
        for i in answer:
            print(i)
    else:
        print("Nope")
main()
