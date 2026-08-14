"""[LEARNING LOGS] จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""
def main():
    """pep8"""
    a = int(input())
    b = int(input())
    d = int(input())
    r = int(input())
    count = 0

    for i in range(a,b+1):
        if i % d == r:
            count += 1
    print(count)
main()
