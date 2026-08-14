"""เหมือนกันหมด"""
def main():
    """pep8"""
    a = float(input())
    b = float(input())
    c = float(input())

    if a == b and b == c:
        print("all the same")
    elif a == b or a == c or b == c:
        print("neither")
    else:
        print("all different")
main()
