"""buu"""
def main():
    """pep8"""
    text = input()
    lower_text = text.lower()
    max_u = 0
    for i in range(len(text)):
        if lower_text[i] == "b":
            count = 0
            j = i + 1
            while j < len(text) and lower_text[j] == "u":
                count += 1
                j += 1
            if count >= 2:
                if count > max_u:
                    max_u = count
    if max_u > 0:
        print("Yes", max_u)
    elif "b" in lower_text:
        position = lower_text.index("b")
        print(text[:position + 1] + "U" * (len(text) - position - 1))
    else:
        result = ""
        while len(result) < len(text):
            result += "BUU"
        print(result[:len(text)])
main()
