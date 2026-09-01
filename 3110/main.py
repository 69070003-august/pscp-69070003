"[LEARNING LOGS] สงคราม...ส่งด่วน"
def main():
    """pep8"""
    start, end = input().split()
    weight = float(input())
    if start == "BKK" and end == "CNX":
        fee = 10 + (30 * weight)
    elif start == "CNX" and end == "UBP":
        fee = 15 + (40 * weight)
    elif start == "UBP" and end == "BKK":
        fee = 20 + (40 * weight)
    elif start == "BKK" and end == "PKT":
        fee = 25 + (50 * weight)
    elif start == "PKT" and end == "CNX":
        fee = 30 + (60 * weight)
    elif start == "UBP" and end == "PKT":
        fee = 40 + (70 * weight)
    else:
        print("Error")
        return
    print(f"{fee:.2f}")
main()
