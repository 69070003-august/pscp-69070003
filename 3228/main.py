"""การนับสระ"""
def main():
    """pep8"""
    mylist = ["a","e","i","o","u"]
    count = 0
    a = input()
    for i in a:
        if i in mylist:
            count += 1
    print(count)
main()
