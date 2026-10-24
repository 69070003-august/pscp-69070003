"""CaesarV2"""
import sys
import re

def decrypt_caesar():
    # อ่านข้อความทั้งหมดจาก Standard Input
    encrypted_text = sys.stdin.read().strip()
    if not encrypted_text:
        return

    # รายการคำศัพท์ที่พบบ่อยตามที่โจทย์กำหนด
    common_words = {
        "what", "when", "why", "which", "this", "there", "where", 
        "the", "is", "am", "are", "you", "we", "they", "he", "she", "it"
    }

    best_score = -1
    best_decryption = encrypted_text

    # ลองทุกค่าการเลื่อนที่เป็นไปได้ตั้งแต่ 1 ถึง 25
    for shift in range(1, 26):
        decrypted_chars = []
        for char in encrypted_text:
            if 'a' <= char <= 'z':
                # ถอดรหัสตัวอักษรพิมพ์เล็ก (เลื่อนย้อนกลับ)
                new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                decrypted_chars.append(new_char)
            elif 'A' <= char <= 'Z':
                # ถอดรหัสตัวอักษรพิมพ์ใหญ่
                new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                decrypted_chars.append(new_char)
            else:
                # อักขระอื่นๆ เช่น ช่องว่าง หรือเครื่องหมายวรรคตอน ปล่อยไว้ตามเดิม
                decrypted_chars.append(char)
        
        candidate = "".join(decrypted_chars)
        
        # ตัดคำในข้อความและแปลงเป็นตัวพิมพ์เล็กเพื่อตรวจสอบกับชุดคำศัพท์
        words = re.findall(r'\b[a-zA-Z]+\b', candidate.lower())
        score = sum(1 for w in words if w in common_words)
        
        # เลือกข้อความที่มีคะแนน (จำนวนคำที่ตรงกัน) สูงที่สุด
        if score > best_score:
            best_score = score
            best_decryption = candidate

    print(best_decryption)

if __name__ == '__main__':
    decrypt_caesar()