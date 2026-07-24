"""pep8"""
def main():
    """uuu"""
    a = int(input())
    if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0):
        b ="yes"
    else:
        b ="no"

    c = float(a * 365.25)
    if c % 1 == 0:
        d ="yes"
    else:
        d ="no"

    if b == "yes" or d == "yes":
        print("yes")
    else:
        print("no")
main()
