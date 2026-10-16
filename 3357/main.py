"""[LEARNING LOGS] Giraffe"""
def main():
    """pep8"""
    my_list = []
    count = 0
    n = int(input())
    for _ in range(n):
        a = int(input())
        my_list.append(a)

    if n == 1:
        print(1)
        return
    for i in range(len(my_list)):
        if i == 0:
            if my_list[i] > my_list[i+1]:
                count += 1
        elif i == len(my_list)-1:
            if my_list[-1] > my_list[-2]:
                count +=1
        else:
            if my_list[i] > my_list[i-1] and my_list[i] > my_list[i+1]:
                count += 1

    print(count)
main()
