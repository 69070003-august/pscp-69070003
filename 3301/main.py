"""Box Packing"""
def main():
    """pep8"""
    w, l, m, n = map(int, input().split())
    ans = float("inf")
    for a in range(m, n + 1):
        waste = (w % a) * (l % a)
        if waste < ans:
            ans = waste
    print(ans)
main()
