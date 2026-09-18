"""Elon Musk (X-shape)"""
def main():
    """pep8"""
    x, k = input().split()
    x = int(x)

    mid = x // 2

    for row in range(x):
        line = ""
        for col in range(x):
            if col == row or col == x - 1 - row:
                if k == "#":
                    line += "#"
                else:
                    distance = abs(mid - row)
                    char = chr(ord(k) + distance)
                    line += char
            else:
                line += "-"
        print(line)
main()
