"""Classify"""
def main():
    """Group students by year and faculty."""
    students = []

    while True:
        student_id = input().strip()
        if student_id == "END":
            break
        students.append(student_id)

    groups = {}

    for student_id in students:
        year = student_id[:2]
        faculty = student_id[2]

        if year not in groups:
            groups[year] = {}

        groups[year][faculty] = groups[year].get(faculty, 0) + 1

    for year in sorted(groups, reverse=True):
        print(year, *[
            f"{faculty} {groups[year][faculty]}"
            for faculty in sorted(groups[year])
        ])


main()

