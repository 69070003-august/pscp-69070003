"""[Recommend] สามเหลี่ยม"""
def main():
    """pep8"""
    n = int(input())
    for i in range(1,n+1):
        if i in (1,n):
            print("0" * i)
        else:
            for j in range(1,i+1):
                if j == 1:
                    print("0",end="")
                elif j == i:
                    print("0")
                else:
                    print("1",end="")
main()
