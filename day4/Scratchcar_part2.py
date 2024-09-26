import json

with open('clean-input.json', 'r') as file:
    cds = json.load(file)


# convert string keys to int counter parts
keys = list(cds.keys())
values = list(cds.values())
keys = [ int(i) for i in keys]
cards = dict(zip(keys,values))
# initialize count dict
card_count = dict(zip(cards.keys(),[1]*len(cards)))
# clean up memory
del cds, values, keys


for card in cards:
    win_num, card_num = cards[card]

    points = 0
    # count number of winnings
    for num in win_num:
        if num in card_num:
             points += 1




    mul = card_count[card]
    for i in range(1,points+1):
        # to prevent shit like key value 101, 103 from happening
        if card+i in card_count:
            card_count[card+i] +=mul




print(sum(card_count.values()))oad(file)