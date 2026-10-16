"""บุพเพสันนิวาส"""
def main():
    """pep8"""
    a = input().strip()
    b = input().strip()

    size = max(len(a), len(b))
    a = "".join(a[i % len(a)] for i in range(size))
    b = "".join(b[i % len(b)] for i in range(size))

    charm = ""
    for x, y in zip(a, b):
        if x.lower() in "love" or y.lower() in "love":
            charm += "w"
        else:
            charm += "$"

    if charm.count("w") % 2 == 1:
        longest = 0
        run = 0
        for ch in charm:
            if ch == "w":
                run += 1
                longest = max(longest, run)
            else:
                run = 0
        charm += str(longest)
    elif "ww" not in charm:
        charm += "#"

    print(charm)
main()
