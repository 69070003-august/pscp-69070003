"""ผ่านหรือไม่ ค่าเฉลี่ยรายวิชา"""
def main():
    """pep8"""
    myscore = []
    a = int(input())
    for _ in range(a):
        myscore.append(int(input()))
    myscore.sort()
    if myscore[0] >= 50 and sum(myscore)/a >= 60.0:
        print(f"{sum(myscore)/a:.1f}")
        print("PASS")
    else:
        print(f"{sum(myscore)/a:.1f}")
        print("FAIL")
main()
