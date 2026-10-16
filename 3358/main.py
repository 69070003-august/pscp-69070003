"""Pig"""
def main():
    """pep8"""
    n = int(input())
    num = list(map(int,input().split()))
    my_list = []
    if n == 1:
        if num[0] >= num[1]:
            print(num[0])
            return
        if num[0] < num[1]:
            print(num[1])
            return
    for i in range(0,(n*2),2):
        if num[i] >= num[i+1]:
            my_list.append(num[i])
        else:
            my_list.append(num[i+1])
    print(f"{" + ".join(map(str,my_list))} = {sum(my_list)}")
main()
