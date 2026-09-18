"""[LEARNING LOGS] ของขวัญและขโมย"""
def main():
    """pep8"""
    n,k,t = map(int,input().split())
    person = 1
    count = 1
    if person == t:
        print(count)
        return
    while True:
        person = (person + k - 1) % n + 1
        if person == 1:
            break
        count += 1
        if person == t:
            break
    print(count)

main()
