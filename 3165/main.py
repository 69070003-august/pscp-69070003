"""เดินเล่นในงานเทศกาล"""
def main():
    """pep8"""
    x = 0
    y = 0
    char = input()
    for i in char:
        if i == "N":
            y += 1
        elif i == "S":
            y -= 1
        elif i == "E":
            x += 1
        elif i == "W":
            x -= 1
    print(f"{x} {y} {abs(x)+abs(y)}")
main()
