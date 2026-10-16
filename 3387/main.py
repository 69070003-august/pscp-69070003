"""Tuple's Sad life"""
def main():
    """pep8"""
    t = tuple(input().split())
    x = input().strip()

    pos = t.index(x)
    size = t.count(x)

    for _ in range(size):
        print(" ".join([str(pos)] * size))
main()
