"""PickThemAgain"""
def main():
    """pep8"""
    a = list(map(int,input().split()))
    zero = False
    for i in a[::-1]:
        if not i % 5 or not i % 3:
            print(i)
            zero =True
    if not zero:
        print("Nope")
main()
