"""จำนวนสระ"""
def main():
    """pep8"""
    mylist = ["A","E","I","O","U"]
    n = int(input())
    count = 0
    for _ in range(n):
        cha = input()
        if cha in mylist:
            count += 1
    print(count)
main()
