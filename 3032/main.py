"""คะแนนสอบ"""
def main():
    """top"""
    super_a = []
    a = int(input())
    for _ in range(0,a):
        b = int(input())
        super_a.append(b)
    c = max(super_a)
    d = super_a.count(c)
    print(c)
    print(d)
main()
