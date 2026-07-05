"""[LEARNING LOGS]"""
def main():
    """Colors"""
    color_1 = input()
    color_2 = input()
    if (color_1 == "Red" and color_2 == "Yellow") or (color_2 == "Red" and color_1 == "Yellow"):
        print("Orange")
    elif (color_1 == "Red" and color_2 == "Blue") or (color_2 == "Red" and color_1 == "Blue"):
        print("Violet")
    elif (color_1 == "Yellow" and color_2 == "Blue") or (color_2 == "Yellow" and color_1 == "Blue"):
        print("Green")
    elif color_1 == "Red" and color_2 == "Red":
        print("Red")
    elif color_1 == "Yellow" and color_2 == "Yellow":
        print("Yellow")
    elif color_1 == "Blue" and color_2 == "Blue":
        print("Blue")
    else:
        print("Error")
main()
