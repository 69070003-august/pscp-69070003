"""[LEARNING LOGS] SurprisingVote"""
def main():
    """pep8"""
    a = float(input())
    b = float(input())
    c = a - (2*b)
    if  b  <= 2:
        print("Not surprising")
    elif b - c > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
