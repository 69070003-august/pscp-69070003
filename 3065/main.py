"""ตัวเลขโรมันแบบง่าย"""
def main():
    """pep8"""
    roman = [(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]
    a = int(input())
    if a < 0:
        print("Error : Please input positive number")
    elif a == 0 or a > 9:
        print("Error : Out of range")
    else:
        roman_num = ""
        for b,c in roman:
            while a >= b:
                roman_num += c 
                a -= b
    print(roman_num)
main()
