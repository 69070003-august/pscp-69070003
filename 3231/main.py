"""เกมทายลูกเต๋า"""
def main():
    """pep8"""
    mylist = ["1","2","3","4","5","6"]
    taw_A = input()
    taw_B = input()

    if taw_A in mylist and taw_B in mylist:
        if taw_A == taw_B:
            print("Correct!")
        else:
            print("Wrong!")
    else:
        print("Invalid")
main()
