"""Filter"""
import json
def main():
    """Filter students by final score."""
    students = json.loads(input())
    minimum = float(input())

    result = sorted(
        (student_id, score)
        for student_id, score in students.items()
        if score >= minimum
    )

    if result:
        for student_id, score in result:
            print(f"{student_id}\t{score:.2f}")
    else:
        print("Nope")


main()
