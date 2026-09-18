"""ผลรวมของค่าที่มากกว่า"""
def main():
    """pep8"""
    numlist = []
    num = int(input())
    for _ in range(num):
        a = int(input())
        b = int(input())
        if a >= b:
            numlist.append(a)
        else:
            numlist.append(b)
    if num == 1:
        print(numlist[0])
    else:
        print(" + ".join(map(str, numlist)), "=", sum(numlist))

main()
