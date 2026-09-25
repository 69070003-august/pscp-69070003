"""Ideal Arrows"""
def main():
    """pep8"""
    arrows = input()
    n = int(input())

    for index, arrow in enumerate(arrows):
        if arrow == "R":
            for i in range(n):
                print("  " * i + "*" * (n - i))

            for i in range(n - 2, -1, -1):
                print("  " * i + "*" * (n - i))

        else:
            for i in range(n):
                print(" " * (n - i - 1) + "*" * (n - i))

            for i in range(1, n):
                print(" " * i + "*" * (i + 1))

        if index < len(arrows) - 1:
            print()
main()
