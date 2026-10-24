"""HorizontalHistogram"""
def main():
    """Count character frequencies and display a histogram."""
    text = input()
    freq = {}

    for char in text:
        freq[char] = freq.get(char, 0) + 1

    chars = sorted(freq, key=lambda c: (c.isupper(), c.lower()))

    for char in chars:
        count = freq[char]
        bars = "-" * (count % 5)
        bars = "|" .join(["-" * 5] * (count // 5))

        if count % 5:
            if count // 5:
                bars += "|"
            bars += "-" * (count % 5)

        print(f"{char} : {bars}")


main()
