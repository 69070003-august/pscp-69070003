"""คำนวณค่าแท็กซี่เบื้องต้น"""
def main():
    """pep8"""
    s = int(input())
    money = 0
    count = 0
    if s >= 1:
        s -= 1
        money += 35
    while count < 9 and s:
        s-=1
        money += 5
        count += 1
    money_2 = s * 8
    print(money + money_2)
main()
