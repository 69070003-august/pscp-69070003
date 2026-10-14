"""มากี่คน"""
def main():
    """pep8"""
    man = 0
    woman = 0
    while True:
        n = int(input())
        if n < 0:
            break
        if not n % 2:
            woman += 1
        else:
            man += 1
    print(f"{man} {woman} {man + woman}")
main()
