"""
CP1404/CP5632 Practical
Color names in a dictionary
"""

COLOR_TO_HEX_DICT = {
    "ANTIQUEWHITE": "#faebd7",
    "AQUAMARINE1": "#7fffd4",
    "BROWN": "#a52a2a",
    "CORAL": "#ff7f50",
    "DARKGREEN": "#006400",
    "DEEPPINK1": "#ff1493",
    "GOLD1": "#ffd700"
}

color = input("Enter color name: ")
while color != "":
    if color.upper() in COLOR_TO_HEX_DICT:
        print(color.upper(), "has the hex code:", COLOR_TO_HEX_DICT[color.upper()])
    else:
        print("Invalid Color Name")
    color = input("Enter color name: ")
