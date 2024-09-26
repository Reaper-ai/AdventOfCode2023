import json

with open('clean-input.json', 'r') as file:
    cards = json.load(file)

SUM = 0

for card in cards:
    win_num, card_num = cards[card]

    points = 0
    for num in win_num:
        if num in card_num:
             points =  1 if points == 0 else points<<1

    SUM += points

print(SUM)