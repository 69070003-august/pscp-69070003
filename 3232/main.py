"""[LEARNING LOGS] กบน้อยกระโดด"""
def main():
    """pep8"""
    jump, goal = map(int, input().split())
    count = 0
    distance = 0

    while jump > 0:
        distance += jump
        count += 1
        if distance >= goal:
            print(count)
            return
        jump -= 2
    print(-1)


main()
