import json

def power_of_games(req_colors):
    prod = 1
    for clr in req_colors:
        prod *= req_colors[clr]
    return prod

SUM = 0
with open('clean-input.json', 'r') as file:
    games = json.load(file)


valid_games = []
# iterate every game
for game in games:
    outcomes = games[game]
    # iterate every outcome of game
    min_req = {"red": 1, "green": 1, "blue": 1}
    for outcome in outcomes:
        # iterate every color
        for color in min_req:
            if color in outcome.keys():
                # store minimum of each ball req
                min_req[color] = max(min_req[color],int(outcome[color]))

    SUM += power_of_games(min_req)


print(SUM)