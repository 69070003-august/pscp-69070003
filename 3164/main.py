"""ผลรวมของค่าที่มากกว่า"""
def main():
    """pep8"""
    numlist = []
    num = int(input())
    for _ in range(num):
        a = int(input())
        b = int(input())
        if a >= b:
            numlist.append(a)
        else:
            numlist.append(b)
    for i in range(num):
        if i == num -1:
            print(f"{numlist[-1]} = {sum(numlist)}")
        else:
            print(f"{numlist[i]} + ",end="")
main()
