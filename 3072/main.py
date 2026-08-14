"""[LEARNING LOGS] A-E-I-O-U"""
def main():
    """pep8"""
    word = input().upper()
    a = word.count("A")
    e = word.count("E")
    i = word.count("I")
    o = word.count("O")
    u = word.count("U")

    if a > 0:
        print(f"a : {a}")
    if e > 0:
        print(f"e : {e}")
    if i > 0:
        print(f"i : {i}")
    if o > 0:
        print(f"o : {o}")
    if u > 0:
        print(f"u : {u}")
main()
