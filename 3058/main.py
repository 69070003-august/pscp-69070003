"""[LEARNING LOGS] BrickBridge"""
def main():
    """pep8"""
    a = int(input())
    b = int(input())
    goal = int(input())
    if b * 5 >= goal:
        goal %= 5
        if a >= goal:
            print(goal)
        elif a < goal:
            print(-1)
    else:
        goal -= b * 5
        if a >= goal:
            print(goal)
        elif a < goal:
            print(-1)
main()
