"""พูดจาภาษากระต่าย"""
def main():
    """pep8"""
    text = input().upper()

    if all(char in "IT" for char in text):
        print("unknown", len(text))
        return

    max_a = 0
    count_a = 0

    for i, char in enumerate(text):
        if char == "R":
            if i + 1 >= len(text) or text[i + 1] != "A":
                print("no", i)
                return

        elif char == "B":
            if i + 1 >= len(text) or text[i + 1] not in "IT":
                print("no", i)
                return

        elif char == "A":
            if i == 0 or text[i - 1] not in "RA":
                print("no", i)
                return

        if char == "A":
            count_a += 1
            max_a = max(max_a, count_a)
        else:
            count_a = 0

    print("yes", max_a)


main()
