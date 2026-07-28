"""กระดาษห่อของขวัญ"""
def main():
    """pep8"""
    r, h, g = input().split()
    r = float(r)
    h = float(h)
    g = float(g)
    circumference = 2 * 3.14 * r
    width = h + (2 * r)
    length = circumference + g
    print(f"{width:.2f} {length:.2f}")
main()
