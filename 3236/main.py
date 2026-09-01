"""รหัสแฝดเทค"""
def main():
    """pep8"""
    n = int(input())
    a = input()
    b = input()
    count = 0
    for i in range(n):
        if int(a[i]) + int(b[i]) == 9:
            count += 0
        elif int(a[i]) + int(b[i]) != 9:
            count += 1
    if not count:
        print("YES")
    else:
        print(f"NO {count}")
main()
