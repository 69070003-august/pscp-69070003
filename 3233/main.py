"""[LEARNING LOGS] สลากกินแบ่ง"""
def main():
    """pep8"""
    a, A = input().split()
    b, B = input().split()

    if a == b and A == B:
        print(1000000)
    elif A == B:
        print(100000)
    elif a == b and A[-3:] == B[-3:]:
        print(2000)
    elif A[-3:] == B[-3:]:
        print(200)
    elif a == b and A[-2:] == B[-2:]:
        print(1000)
    elif A[-2:] == B[-2:]:
        print(100)
    elif a == b:
        print(20)
    else:
        print(0)
main()
