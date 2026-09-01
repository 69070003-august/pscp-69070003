"""[LEARNING LOGS] Arcade of Time: Store Check"""
def main():
    """pep8"""
    num, check = map(int, input().split())
    diff = [0] * 1442
    for _ in range(num):
        start, stop = map(int, input().split())
        diff[start] += 1
        diff[stop] -= 1
    for i in range(1, 1441):
        diff[i] += diff[i - 1]
    times = list(map(int, input().split()))
    answer = []
    for i in range(check):
        answer.append(str(diff[times[i]]))
    print(" ".join(answer))
main()
