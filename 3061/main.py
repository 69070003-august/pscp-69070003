"""ผ่าน/ไม่ผ่าน"""
def main():
    """pep8"""
    a = int(input())
    b = int(input())
    c = a+b
    if c >= 50:
        print(c)
        print("pass")
    else:
        print(c)
        print("fail")
main()
