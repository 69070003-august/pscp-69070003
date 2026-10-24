"""[LEARNING LOGS] Impostor"""
def main():
    """Among Us"""
    import json

    members = {}

    # รับข้อมูลสมาชิกจนเจอ Start
    while True:
        data = input()

        if data == "Start":
            break

        members.update(json.loads(data))

    # รับชื่อคนที่ถูกโหวตออก
    dead = {}

    while True:
        name = input()

        if name == "End":
            break

        if name in members:
            dead[name] = members.pop(name)

    # นับจำนวน Impostor ที่ยังอยู่
    count = 0
    for role in members.values():
        if role == "Impostor":
            count += 1

    print(count, "Impostor Remains")
    print("***Alive***")

    # แสดงผู้ที่ยังอยู่ เรียงตามชื่อ
    for name in sorted(members):
        print(name, ":", members[name])

    print("***Dead***")

    # แสดงผู้ที่ถูกโหวตออก เรียงตามชื่อ
    for name in sorted(dead):
        print(name, ":", dead[name])


if __name__ == "__main__":
    main()
