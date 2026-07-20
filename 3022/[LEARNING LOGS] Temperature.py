"""pep8"""
def main():
    """[LEARNING LOGS] Temperature"""
    temperature = float(input())
    char_1 = input()
    char_2 = input()
    if char_1 == "C":
        if char_2 == "C":
            print(temperature)
        elif char_2 == "F":
            print(temperature)
main()