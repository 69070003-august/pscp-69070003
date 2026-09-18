"""โรงแรมกลางกรุง ไม่มีชั้น 13"""
def main():
    """pep8"""
    n = input()
    a = int(n[0])
    b = int(n[1])
    c = int(n[2])
    d = int(n[3])
    e = int(n[4])

    if a > 5:
        floor = 9
    elif b > 5:
        floor = 10
    elif c > 5:
        floor = 11
    elif d > 5:
        floor = 12
    elif e > 5:
        floor = 14
    else:
        floor = 13

    if n == n[::-1]:
        if a + e > 5:
            room_1 = 1
        elif b * d > 5:
            room_1 = 2
        else:
            room_1 = 0
    else:
        if e > 0 and a // e > 5:
            room_1 = 1
        elif b - e > 5:
            room_1 = 2
        else:
            room_1 = 0

    total = a + b + c + d + e
    product = a * b * c * d * e
    if total > 25:
        room_2 = 1
    elif product > 55:
        room_2 = 2
    else:
        room_2 = 0

    print(f"{floor}{room_1}{room_2}")
main()
