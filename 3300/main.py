"""สมดุลย์ชีวิต"""
def main():
    """pep8"""
    my_list = []
    over = []
    under = []
    count = 0
    a = int(input())
    for _ in range(a):
        my_list.append(int(input()))

    my_list.sort(reverse=True)
    for i in my_list:
        if i > 18:
            over.append()
        else:
            under.append()

    for _ in range(a):
        if len(over):
            over.pop()
            count += 1
            if len(under):
                under.pop()
                count += 1
            else:
                count += 1
        else:
            under +

main()
