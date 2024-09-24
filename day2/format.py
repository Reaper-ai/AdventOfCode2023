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
    all_games = dict()
    # {game1:[{red:5,  blue:7 }, {red:8, green:2}]}
    for line in file:
        # split the game head from the outcomes
        colon_seprator = line.split(":")

        # make "Game 1" to "1"
        game = colon_seprator[0][5:]

        # split the outcomes
        outcomes = colon_seprator[1].split(";")
        result = []
        for outcome in outcomes:
            outcome_set = hash_set_maker(outcome)
            result.append(outcome_set)

        all_games[game] = result

with open('clean-input.json', 'w') as file:
    json.dump(all_games, file)