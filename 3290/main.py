"""Left Arrow"""
def main():
    """pep8"""
    k = int(input())
    n = int(input())
    mid = n // 2
    for row in range(n):
        print(" " * abs(mid - row),end="")
        print("*" * k,end="")
        print("")
main()
