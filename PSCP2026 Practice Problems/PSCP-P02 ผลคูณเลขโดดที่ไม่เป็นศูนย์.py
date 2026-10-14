"""pep8"""
def main():
    """pep8"""
    num_input = input()
    answer = 1
    found = False
    for digit in num_input:
        if digit != "0":
            answer *= int(digit)
            found = True
    if found:
        print(answer)
    else:
        print(0)
main()
