"""op"""
def check(num,op,target):
    """pep8"""
    if op == "==":
        return num == target
    elif op == ">":
        return num > target
    elif op == ">=":
        return num >= target
    elif op == "<":
        return num < target
    elif op == "<=":
        return num <= target
    elif op == "!=":
        return num != target

"""Hint"""
def main():
    """pep8"""
    a_op , a_num = input().split()
    b_op , b_num = input().split()
    c_op , c_num = input().split()

    a_num = int(a_num)
    b_num = int(b_num)
    c_num = int(c_num)

    for i in range(1000):
        hundet = i // 100
        ten = (i // 10) % 10
        unite = i % 10

        if (check(unite,a_op,a_num) and
            check(ten,b_op,b_num) and
            check(hundet,c_op,c_num)):
            print(f"{i:03d}")
main()
