"""113"""
def main():
    """pep8"""
    s = input().strip()
    stack = []

    for ch in s:
        stack.append(ch)
        if stack[-3:] == ["1", "1", "3"]:
            del stack[-3:]

    print("".join(stack))
main()
