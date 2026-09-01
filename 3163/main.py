"""สินค้าส่งออก"""
def main():
    """pep8"""
    mylist = []
    num = int(input())
    even = 0
    odd = 0
    for _ in range(num):
        a = int(input())
        mylist.append(a)
        if not a % 2:
            even += 1
        else:
            odd += 1
    print(f"SUM {sum(mylist)}")
    print(f"EVEN {even}")
    print(f"ODD {odd}")
main()
