"""oj"""
def main():
    """ko"""
    number = int(input())
    if number == 1:
        print("1")
    else:
        count = 0
        for i in range(1,number+1):
            count += len(str(i))
            count += 1
        print(count)
main()
