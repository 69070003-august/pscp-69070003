"""pep8"""
def main():
    """pep8"""
    A = 0
    a = 0
    num = 0
    text = input()
    for i in text:
        b = ord(i)
        if 65 <= b <= 90:
            A += 1
        elif 97 <= b <= 122:
            a += 1
        elif 48 <= b <= 57:
            num += 1
    print(f"{A} {a} {num}")
main()
