"""LastStand"""
def main():
    """pep8"""
    a = input()
    my_list = a.strip("[]").split(",")
    for i in my_list:
        i = i.strip()
        print(i[-1])
main()
