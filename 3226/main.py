"""[Recommend] Inflation"""
def main():
    """pep8"""
    n = float(input())
    k = int(input())
    money = (n * ((1 + 0.0381)) ** k)
    s = str(money)
    a,b = s.split(".")
    money = float(a + "." + b[0:2])
    print(money)
main()
