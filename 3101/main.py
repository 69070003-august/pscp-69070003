"""สถานะน้ำ"""
def main():
    """pep8"""
    num = int(input())
    cha = input().upper()
    if cha == "F":
        num = (num - 32) / 1.8
    if num <= 0:
        print("solid")
    elif num >= 100:
        print("gas")
    else:
        print("liquid")
main()
