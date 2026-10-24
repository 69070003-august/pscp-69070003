"""Kabata"""
def main():
    """Check whether strings follow Kabata language rules."""
    n = int(input())

    for _ in range(n):
        text = input().strip()
        i = 0
        valid = True
        previous = ""

        while i < len(text):
            if text[i:i + 2] == "ka":
                if previous == "ba":
                    valid = False
                    break
                previous = "ka"
                i += 2

            elif text[i:i + 2] == "ba":
                previous = "ba"
                i += 2

            elif text[i:i + 2] == "ta":
                previous = "ta"
                i += 2

            else:
                valid = False
                break

        print("yes" if valid else "no")


main()
