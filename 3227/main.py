"""[LEARNING LOGS] ไพ่ 44 ใบ"""
def main():
    """pep8"""
    card = input().upper()
    a = card[-1]
    b = card[:-1]
    card_01 = ""
    card_02 = ""

    if b == "A":
        card_01 = "ace"
    elif b == "J":
        card_01 = "jack"
    elif b == "Q":
        card_01 = "queen"
    elif b == "K":
        card_01 = "king"
    else:
        card_01 = b

    if a == "D":
        card_02 = "diamonds"
    elif a == "H":
        card_02 = "hearts"
    elif a == "S":
        card_02 = "spades"
    elif a == "C":
        card_02 = "clubs"

    print(f"{card_01} of {card_02}")
main()
