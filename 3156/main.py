"""Conan"""
def main():
    """pep8"""
    text = input()
    num = int(input())
    answer = ""
    for i in text:
        after = ord(i) - 97
        after += num
        after %= 26
        answer += chr(after + 97)
    print(answer)
main()
