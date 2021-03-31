# Card Suit Converter
suits = {
    "heart": "♥️",
    "diamond": "♦️",
    "spade": "♠️",
    "club": "♣️"
}
output = ""
words = ["heart", "diamond", "spade", "club"]
for element in words:
    output += suits.get(element, "~") + " "
print(output)