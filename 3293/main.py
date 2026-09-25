"""[LEARNING LOGS] BigFrame"""
def main():
    """pep8"""
    my_list = []
    for _ in range(5):
        my_list.append(input().strip())
    fraime = max(len(text) for text in my_list)
    print("*" * (fraime + 4))
    for text in my_list:
        print(f"* {text + " " * (fraime - len(text))} *")
    print("*" * (fraime + 4))
main()
