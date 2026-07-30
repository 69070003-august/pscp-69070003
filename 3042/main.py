"""[LEARNING LOGS] หาร 10"""
def main():
    """pep8"""
    a = int(input())
    for i in range(a,1,-1):
        if not i % 10:
            print(f"{i}",end=" ")
    print(0)
main()
