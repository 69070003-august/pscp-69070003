"""SqFree"""
def main():
    """pep8"""
    try:
        line = input().strip()
        if not line:
            return
        n = int(line)
    except (EOFError, ValueError):
        return

    # สร้างตะแกรงบอกสถานะ (is_square_free[x] จะเป็น True ถ้า x เป็น square-free)
    # กำหนดค่าเริ่มต้นเป็น True ทั้งหมดตั้งแต่ 0 ถึง n
    is_square_free = [True] * (n + 1)
    
    # 0 ไม่นับรวมในโจทย์
    is_square_free[0] = False

    # หาจำนวนเต็ม i ที่ i^2 <= n
    # การถอดรากที่สองทำได้โดยใช้ n ** 0.5 ตามคำแนะนำ
    limit = int(n ** 0.5)

    # ตัดพหุคูณของ i^2 ออกจากตะแกรง
    for i in range(2, limit + 1):
        square = i * i
        # วนลูปเปลี่ยนสถานะของเลขทุกตัวที่หารด้วย square ลงตัว
        for j in range(square, n + 1, square):
            is_square_free[j] = False

    # นับจำนวนที่เป็น True ตั้งแต่ 1 ถึง n
    ans = sum(is_square_free[1:n + 1])
    print(ans)

if __name__ == '__main__':
    main()