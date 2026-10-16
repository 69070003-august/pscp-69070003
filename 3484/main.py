
"""[LEARNING LOGS] หุ่นยนต์เคาะเสียงกระเบื้อง"""
def main():
    """pep8"""
    first = input().split()
    n = int(first[0])
    p = float(first[1])

    col_cnt = [0] * n   # จำนวนกระเบื้องที่เสียงไม่สมบูรณ์ในแต่ละคอลัมน์
    col_sum = [0] * n   # จำนวนจุดที่เสียงไม่สมบูรณ์ในแต่ละคอลัมน์
    total_tiles = 0
    total_points = 0

    for _ in range(n):
        row = list(map(int, input().split()))
        r_cnt = 0
        r_sum = 0
        for j in range(n):
            x = row[j]
            if x > 0:
                r_cnt += 1
                col_cnt[j] += 1
            r_sum += x
            col_sum[j] += x
        total_tiles += r_cnt
        total_points += r_sum
        print(" ".join(map(str, row)), r_cnt, r_sum)

    print(" ".join(map(str, col_cnt)))
    print(" ".join(map(str, col_sum)))
    print(total_tiles, total_points, "%.2f" % (total_points * p))

main()
