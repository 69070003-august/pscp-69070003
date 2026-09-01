"""พิมพ์สัญลักษณ์"""
def main():
    """pep8"""
    num = int(input())
    for i in range(1,num + 1):
        if not i % 5:
            print("X",end="")
        else:
            print("*",end="")
main()
