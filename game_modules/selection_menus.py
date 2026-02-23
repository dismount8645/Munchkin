# ============================
# SELECTION MENUS
# ============================
def choose_gender():
    """Presents a menu for the user to select the character's gender and returns the selection."""
    options = ["Male", "Female", "Other"]
    print("Choose gender:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    return options[int(input("Enter number: ")) - 1]


def choose_class():
    """Presents a menu for the user to select the character's class and returns the selection."""
    classes = ["Explorer", "Officer", "Mechanic", "Tycoon"]
    print("Choose class:")
    for i, c in enumerate(classes, start=1):
        print(f"{i}. {c}")
    return classes[int(input("Enter number: ")) - 1]
