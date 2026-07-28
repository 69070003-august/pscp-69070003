"""กระดาษห่อของขวัญ"""
def main():
    """pep8"""
    r,h,g = input().split()
    r = float(r)
    h = float(h)
    g = float(g)
    circumference = 2 * 3.14 * r
    long = (circumference * 2) + g
    print(long)
main()
