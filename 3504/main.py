"""[MINI EXAM] Hamming"""
def main():
    """pep8"""
    a = input()
    b = input()
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    print(count)
main()
