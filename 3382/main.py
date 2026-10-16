"""Day08-0_02-Backward"""
def main():
    """pep8"""
    my_list = []
    while True:
        a = input()
        if a == "NULL":
            break
        my_list.append(a)
    for i in my_list[::-1]:
        print(i)
main()
