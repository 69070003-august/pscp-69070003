"""pep8"""
def main():
    """Temperature"""
    temperature = float(input())
    char_1 = input()
    char_2 = input()

    if char_1 == "C":
        if char_2 == "C":
            print(f"{temperature :.2f}")
        elif char_2 == "F":
            print(f"{temperature * 9 / 5 + 32 :.2f}")
        elif char_2 == "K":
            print(f"{temperature + 273.15 :.2f}")
        elif char_2 == "R":
            print(f"{(temperature + 273.15) * 9 / 5 :.2f}")

    elif char_1 == "F":
        if char_2 == "F":
            print(f"{temperature :.2f}")
        elif char_2 == "C":
            print(f"{(temperature - 32) * 5 / 9 :.2f}")
        elif char_2 == "K":
            print(f"{(temperature - 32) * 5 / 9 + 273.15 :.2f}")
        elif char_2 == "R":
            print(f"{temperature + 459.67 :.2f}")

    elif char_1 == "K":
        if char_2 == "K":
            print(f"{temperature :.2f}")
        elif char_2 == "C":
            print(f"{temperature - 273.15 :.2f}")
        elif char_2 == "F":
            print(f"{(temperature - 273.15) * 9 / 5 + 32 :.2f}")
        elif char_2 == "R":
            print(f"{temperature * 9 / 5 :.2f}")

    elif char_1 == "R":
        if char_2 == "R":
            print(f"{temperature :.2f}")
        elif char_2 == "C":
            print(f"{temperature * 5 / 9 - 273.15 :.2f}")
        elif char_2 == "F":
            print(f"{temperature - 459.67 :.2f}")
        elif char_2 == "K":
            print(f"{temperature * 5 / 9 :.2f}")

main()
