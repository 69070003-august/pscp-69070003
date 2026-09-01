"""[Recommend] Factorial"""
def main():
    """pep8"""
    n = int(input())
    count = 1
    for i in range(n,0,-1):
        count *= i
    print(count)
main()
