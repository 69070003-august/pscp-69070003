"""ค่าน้อยที่สุด (4 ค่า)"""
def main():
    """pep8"""
    mylist =[]
    a = int(input())
    for _ in range(a):
        mylist.append(int(input()))
    mylist.sort()
    print(mylist[0])
main()
