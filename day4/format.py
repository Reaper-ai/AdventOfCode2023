import json
# returns hash , 3 red 4 green => {red:3, green:4}
def hash_set_maker(outcome):
    hs = dict()
    ls = outcome.split(",")
    for cube in ls:
        num, color = cube.split()
        hs[color] = num

    return hs



with open("input.txt","r") as file:

    # structure
    all_cards = dict()

    # {1:[[<winning>], [<card nums>]]}
    for line in file:
        # split the card head from the outcomes
        colon_seprator = line.split(":")

        # make "Card 1" to "1"
        card = colon_seprator[0][5:].strip()

        # split the numbers
        sep = colon_seprator[1].split("|")
        winning_nums = sep[0].split()
        card_nums = sep[1].split()

        # convert string numbers to int
        convert = lambda nums: [ int(i) for i in nums]
        num_set = [convert(winning_nums), convert(card_nums)]

        all_cards[card] = num_set

with open('clean-input.json', 'w') as file:
    json.dump(all_cards, file)