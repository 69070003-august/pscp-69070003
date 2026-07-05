"""Safe Password"""
def main():
    """oj"""
    char = input()
    number = input()
    if char == "H" and number == "4567":
        print("safe unlocked")
    elif char =="H":
        print("safe locked - change digit")
    elif number == "4567":
        print("safe locked - change char")
    else:
        print("safe locked")
main()
