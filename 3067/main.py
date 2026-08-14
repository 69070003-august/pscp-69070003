"""การเพิ่ม/ลด"""
def main():
    """pep8"""
    a = float(input())
    b = float(input())
    c = float(input())

    if a < b < c:
        print("increasing")
    elif c < b < a:
        print("decreasing")
    else:
        print("neither")
main()
