"""3d"""
import math
def main():
    """pep8"""
    num1 = input().split()
    num2 = input().split()
    d = (math.sqrt(((int(num1[0]) - int(num2[0])) ** 2) + ((int(num1[1]) - int(num2[1])) ** 2) + \
                   ((int(num1[2]) - int(num2[2])) ** 2)))
    print(f"{d:.2f}")
main()
