import json

# valid game
is_valid = {"red":12, "green":13, "blue":14}
colors = ["red","blue","green"]
valid_games = []
SUM = 0
with open('clean-input.json', 'r') as file:
    games = json.load(file)


valid_games = []
# iterate every game
for game in games:
    bool_game = []
    outcomes = games[game]
    # iterate every outcome of game
    for outcome in outcomes:
        bool_out = []
        # iterate every color and check its validity
        for color in colors:
            if color in outcome:
                # store if outcome is valid
                 bool_out.append(int(outcome[color]) <= is_valid[color])
        # store if game is valid
        bool_game.append(all(bool_out))
    valid_games.append(all(bool_game))


for i in range(len(valid_games)):
    if valid_games[i]:
        SUM += i+1

print(SUM)