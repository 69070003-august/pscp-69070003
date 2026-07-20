"""ฉันจะเป็น Saitama ให้ได้เลย"""
def main():
    """pep8"""
    do1 = int(input())
    do2 = int(input())
    do3 = int(input())
    do4 = int(input())

    saitama1 = int(input())
    saitama2 = int(input())
    saitama4 = int(input())
    saitama3 = int(input())

    ppap1 = do1 / saitama1
    ppap2 = do2 / saitama2
    ppap3 = do3 / saitama3
    ppap4 = do4 / saitama4

    longest = max(ppap1,ppap2,ppap3,ppap4)
    if longest == ppap1:
        if not do1 % saitama1:
            print(int(do1 // saitama1))
        else:
            print(int(do1 // saitama1)+1)
    elif longest == ppap2:
        if not do2 % saitama2:
            print(do2 // saitama2)
        else:
            print(int(do2 // saitama2)+1)
    elif longest == ppap3:
        if not do3 % saitama3:
            print(int(do3 // saitama3))
        else:
            print(int(do3 // saitama3)+1)
    elif longest == ppap4:
        if not do4 % saitama4:
            print(int(do4 // saitama4))
        else:
            print(int(do4 // saitama4)+1)
main()
