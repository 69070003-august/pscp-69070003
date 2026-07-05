"""elo"""
def main():
    """elo"""
    ra = int(input())
    rb = int(input())
    text = input()
    real_ea = (1 / (1 + (10 ** ((rb - ra)/400))))
    real_eb = (1 / (1 + (10 ** ((ra - rb)/400))))
    if text == "A":
        print(f"{real_ea:.2f}")
    elif text == "B":
        print(f"{real_eb:.2f}")
main()
