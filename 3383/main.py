
"""Difference"""
def main():
    """pep8"""
    n_list = []
    m_list = []
    n = int(input())
    m = int(input())

    for _ in range(n):
        a = int(input())
        n_list.append(a)

    for _ in range(m):
        a = int(input())
        m_list.append(a)

    answer = []

    for i in n_list:
        if i not in m_list:
            answer.append(i)

    answer.sort()
    print(" ".join(map(str, answer)))
main()
