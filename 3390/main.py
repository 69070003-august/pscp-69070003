
"""[LEARNING LOGS] 2D Array Anomaly"""
def main():
    """pep8"""
    arr = [list(map(int, input().split())) for _ in range(5)]

    row = -1
    col = -1

    for i in range(5):
        if sum(arr[i]) % 2 != 0:
            row = i

    for j in range(5):
        total = 0
        for i in range(5):
            total += arr[i][j]

        if total % 2 != 0:
            col = j

    print(row, col)


main()
