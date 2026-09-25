"""[LEARNING LOGS] RGB Mixed"""
def main():
    """pep8"""
    a1,a2,a3 = map(int,input().split())
    b1,b2,b3 = map(int,input().split())
    c1 = (a1 + b1)//2
    c2 = (a2 + b2)//2
    c3 = (a3 + b3)//2
    print(f"{c1} {c2} {c3}")
main()
