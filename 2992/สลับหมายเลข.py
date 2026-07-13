"""oj"""
def main():
    """number"""
    number_1 = input()
    op = input()
    number_2 = int(number_1[1] + number_1[0])

    if op == "+":
        print(f"{int(number_1)} + {number_2} = {int(number_1) + number_2}")
    elif op == "*":
        print(f"{int(number_1)} * {number_2} = {int(number_1) * number_2}")
main()
