"""นับเลขคู่และเลขคี่"""
def main():
    """pep8"""
    mylist = []
    count = 0
    for _ in range(3):
        mylist.append(int(input()))
    for i in mylist:
        if not i % 2:
            count += 1
    print(count)
    print(abs(count - 3))


main()
