"""สมดุลย์ชีวิต"""
def main():
    """pep8"""
    over = 0
    under = 0
    a = int(input())
    for _ in range(a):
        h = int(input())
        if h > 18:
            over += 1
        else:
            under += 1
    answer = a + max(0, over - under - 1)
    print(answer)
main()
