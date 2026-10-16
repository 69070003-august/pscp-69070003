"""[LEARNING LOGS] Cat and Fox"""
import json
def main():
    """pep8"""
    animals = {}  # หมายเลข -> ชื่อ
    n = int(input())

    for _ in range(n):
        data = json.loads(input())
        for name, number in data.items():
            animals[number] = name

    animals.setdefault("Cat01", "Garfield")
    animals.setdefault("Fox01", "Fubuki")

    cats = {k: v for k, v in animals.items() if k.startswith("Cat")}
    foxes = {k: v for k, v in animals.items() if k.startswith("Fox")}

    print(f"Cat : {len(cats)}")
    print(f"Fox : {len(foxes)}")

    for number in sorted(cats, key=lambda x: int(x[3:])):
        print(f"{cats[number]} : {number}")

    for number in sorted(foxes, key=lambda x: int(x[3:])):
        print(f"{foxes[number]} : {number}")
main()
