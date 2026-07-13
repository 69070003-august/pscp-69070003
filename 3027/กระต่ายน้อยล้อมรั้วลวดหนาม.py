"""กระต่ายน้อยล้อมรั้วลวดหนาม"""
def main():
    """pep8"""
    w,l,s = input().split()
    price = int(input())
    total = ((int(w)*2) + (int(l)*2)) * int(s)
    print(total)
    print(total * price)
main()
