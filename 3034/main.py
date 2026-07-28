"""พอด"""
def main():
    """pep8"""
    mylist = []
    a,b = input().split()
    a = int(a)
    b = int(b)
    for _ in range(0,a):
        mylist.append(input())
        if len(set(mylist)) == b:
            num_in_list = set(mylist)
            for value in num_in_list:
                mylist.remove(value)
    print(len(mylist))
main()
