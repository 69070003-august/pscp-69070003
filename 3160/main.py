"""Prime numbers"""
def main():
    """Prime numbers"""
    start,end = map(int,input().split())
    total = 0
    total_list = []
    for i in range(start, end + 1):
        count = 0
        for j in range(2, i//2 + 1):
            if not i % j:
                count += 1
                break
        if not count and i != 1 and i:
            total += 1
            total_list.append(str(i))
    if total_list:
        print(" ".join(total_list))
    print(f"Total primes: {total}")
main()
