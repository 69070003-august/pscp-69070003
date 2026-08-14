"""กระต่ายอ้วน"""
def main():
    """pep8"""
    n = int(input())
    a = 0
    count =0
    name =""
    for _ in range(n):
        x, y = input().split(" ")
        y = int(y)
        if y > 15:
            count += 1
        if y > a:
            a = y
            name = x
    print(count)
    print(name)
main()
