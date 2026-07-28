"""ค่าตั๋ว"""
def main():
    """pep8"""
    a = int(input())
    b = input().lower()
    if a < 18 or b == "s":
        print("20")
    else:
        print("50")
main()
