"""pep8"""
import math
def main():
    """oj"""
    x1 = int(input())
    y1 = int(input())
    r1 = int(input())
    x2 = int(input())
    y2 = int(input())
    r2 = int(input())
    distan = (math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2)))
    if r1 + r2 >= distan:
        print("overlapping")
    elif r1 + r2 < distan:
        print("no overlapping")
main()
