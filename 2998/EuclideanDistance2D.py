"""2d"""
import math
def main():
    """2d"""
    q1 = float(input())
    q2 = float(input())
    p1 = float(input())
    p2 = float(input())
    euclidean = math.sqrt(((q1 - p1) ** 2) + ((q2 - p2) ** 2))
    print(f"{euclidean}")
main()
