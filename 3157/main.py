"""[LEARNING LOGS] เกมสะสมแต้ม"""
def main():
    """pep8"""
    n = int(input())
    score = 0
    for _ in range(n):
        a = input()
        if a == "+":
            score += 10
        elif a =="-":
            score -= 5
    print(score)
main()
