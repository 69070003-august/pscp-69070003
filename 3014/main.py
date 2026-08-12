"""pep8"""
def main():
    """milk"""
    a = float(input())
    b = int(input())
    c = int(input())
    d = float(input())
    first = int(d // a)
    if not b:
        print(first)
    else:
        count = first
        empty = first
        while empty >= b:
            new = (empty // b) * c
            count += new
            empty = (empty % b) + new
        print(count)
main()
