
"""[LEARNING LOGS] Pad Thai"""
def main():
    """pep8"""
    ingredients = {
        "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp",
        "Bean Sprouts", "Noodle", "Chives", "Lime",
        "Egg", "Oil", "Peanuts"
    }
    flavors = {"Sweet", "Sour", "Salty"}

    used_ingredients = set()
    used_flavors = set()
    invalid_ingredient = False

    while True:
        item = input()
        if item == "Cook":
            break
        if item not in ingredients:
            invalid_ingredient = True
        used_ingredients.add(item)

    while True:
        flavor = input()
        if flavor == "End":
            break
        used_flavors.add(flavor)

    if invalid_ingredient:
        print("This is not Pad Thai!!!")
    elif used_ingredients != ingredients:
        print("This is bad!")
    elif used_flavors != flavors:
        print("Not Bad...")
    else:
        print("Delicious!")


main()
