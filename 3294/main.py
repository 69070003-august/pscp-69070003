"""Teaching schedule"""
def main():
    """pep8"""
    a = int(input())
    b = int(input())
    c = a * b
    hours = c // 60
    minute = c % 60
    if hours and minute:
        print(f"{hours} hours {minute} minute")
    elif hours and not minute:
        print(f"{hours} hours")
    elif minute and not hours:
        print(f"{minute} minute")
    else:
        print("No teaching")
main()
