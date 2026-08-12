"""[LEARNING LOGS] Ink"""
import math
def main():
    """pep8"""
    pi = 3.1416
    s, n = map(int, input().split())
    for _ in range(n):
        x, y = map(int, input().split())
        a = pi * (x**2 + y**2)
        time_use = a / s
        print(math.ceil(time_use))
main()
