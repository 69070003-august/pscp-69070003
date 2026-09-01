"""วิเคราะห์ยอดขายร้านกาแฟ"""
def main():
    """pep8"""
    my_list = []
    day = int(input())
    for _ in range(day):
        my_list.append(int(input()))
    print(sum(my_list))
    print(max(my_list))
    print(min(my_list))
    print(f"{(sum(my_list) / day):.1f}")
main()
