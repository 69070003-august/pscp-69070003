"""seven"""
def main():
    """oj"""
    number = int(input())
    seven = number % 4
    if seven == 1:
        print("7")
    elif seven == 2:
        print("9")
    elif seven == 3:
        print("3")
    else:
        print("1")
main()
