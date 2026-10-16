
"""[LEARNING LOGS] หั่นขนมปัง"""

def main():
    """Calculate the two largest areas."""
    w, h, m, n = map(int, input().split())

    x = [0] + list(map(int, input().split())) + [w]
    y = [0] + list(map(int, input().split())) + [h]

    widths = []
    heights = []

    for i in range(len(x) - 1):
        widths.append(x[i + 1] - x[i])

    for i in range(len(y) - 1):
        heights.append(y[i + 1] - y[i])

    areas = []

    for width in widths:
        for height in heights:
            areas.append(width * height)

    areas.sort(reverse=True)

    print(areas[0], areas[1])


main()
