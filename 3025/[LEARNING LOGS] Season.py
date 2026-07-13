"""[LEARNING LOGS] Season"""
def main():
    """pep8"""
    month = int(input())
    day = int(input())
    total_day = ((month - 1) * 30) + day
    if total_day <= 81:
        print("winter")
    elif total_day <= 171:
        print("spring")
    elif total_day <= 261:
        print("summer")
    elif total_day <= 351:
        print("fall")
    else:
        print("winter")
main()
