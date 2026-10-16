"""PickThem"""
import json
def main():
    """pep8"""
    my_list = json.loads(input())
    have = False
    for i in my_list:
        if not i % 2:
            print(i)
            have = True
    if have is False:
        print("Nope")
main()
