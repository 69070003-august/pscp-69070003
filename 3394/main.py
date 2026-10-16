"""[LEARNING LOGS] ส่งต่อ"""
def main():
    """pep8"""
    n, s = map(int, input().split())
    students = []

    for _ in range(n):
        students.append(int(input()))

    visited = set()
    current = s

    while current != 0 and current not in visited:
        visited.add(current)
        current = students[current - 1]

    print(len(visited))
main()
