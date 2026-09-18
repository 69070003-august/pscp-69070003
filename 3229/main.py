"""ระบบคิดคะแนนเกมออนไลน์"""

def main():
    """pep8"""
    score = int(input())
    bonus = int(input())
    streak = int(input())
    total_score = score + bonus
    if streak > 3:
        total_score *= 1.5
        print(int(total_score))
    else:
        print(int(total_score))

    if total_score >= 1500:
        print(5)
    elif total_score >= 1000:
        print(4)
    elif total_score >= 500:
        print(3)
    elif total_score >= 200:
        print(2)
    elif total_score < 200:
        print(1)

    if total_score >= 1500 and streak >= 7:
        print(99)
    elif 1500 > total_score >= 1000 and bonus > 300:
        print(88)
    else:
        print(0)
main()