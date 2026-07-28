"""ฟิลเตอร์ AR TikTok"""
def main():
    """pep8"""
    r,x,y = input().split()
    r = int(r)
    x = int(x)
    y = int(y)
    if x**2 + y**2 < r**2:
        print("IN")
    elif x**2 + y**2 == r**2:
        print("ON")
    elif x**2 +y **2 > r**2:
        print("OUT")
main()
