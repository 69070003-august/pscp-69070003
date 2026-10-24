"""[LEARNING LOGS] B - Fully pair?"""
def main():
    """Find unpaired letters"""
    text = input()
    count = {}

    for char in text:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    result = ""

    for char in text:
        if count[char] % 2 == 1:
            result += char
            count[char] -= 1

    if result:
        print(result)
    else:
        print("fully paired")


if __name__ == "__main__":
    main()
