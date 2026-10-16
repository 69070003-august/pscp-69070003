"""Bus Seat"""
def main():
    """pep8"""
    seats = int(input())
    rows = int(input())
    mine = int(input())

    for line in range(seats - 1, -1, -1):
        cells = []
        for r in range(rows):
            number = r * seats + line + 1
            cells.append("XX" if number == mine else f"{number:02d}")
        print(" ".join(cells))

        if line % 2 == 0 and line != 0:
            print()


main()