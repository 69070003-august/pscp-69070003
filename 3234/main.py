"""ไฟคริสตมาส"""
def main():
    """pep8"""
    color, n = input().split()
    n = int(n)
    colors = ["Red", "Green", "Blue"]
    if color == "R":
        start = 0
    elif color == "G":
        start = 1
    else:
        start = 2
    result = []
    for i in range(n):
        result.append(colors[(start + i) % 3])

    print(" ".join(result)) 
main()
