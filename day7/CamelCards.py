from collections import Counter
from itertools import chain

def hand_type(input_list):
    counts = Counter(input_list)
    return tuple(sorted(list(counts.values())))

def hand_type_2(input_list):
    counts = Counter(input_list)

    if 0 in counts and len(counts) != 1:
        val = counts[0]
        del counts[0]
        replacement = sorted(counts.items(), key=lambda item: (item[1], item[0]), reverse=True)[0][0]
        counts[replacement] += val


    return tuple(sorted(list(counts.values())))

hand_classes = {(1, 1, 1, 1, 1): 'HIGH', (1, 1, 1, 2): 'ONEP', (1, 2, 2): 'TWOP', (1, 1, 3): 'THREE', (2, 3): 'FULL', (1, 4): 'FOUR', (5,): 'FIVE'}
classified = dict()
for key in hand_classes.values():
    classified[key] = []


def part_1(data):

    # prepare and format input
    POWER = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}

    rank = 0
    n = len(data)
    for i in range(n):
        hand, bid = data[i].split()
        hand = list(hand)
        for j in range(5):
            hand[j] = POWER[hand[j]]
        data[i] = [hand, int(bid), rank]


    # divides the hands into the types
    for row in data:
        hand = row[0]
        type = hand_type(hand)
        classified[hand_classes[type]].append(row)



    k = 1
    # gives each hand a rank in each catagory
    for key in list(classified.keys()):
        all_hands = classified[key]

        n = len(all_hands)
        all_hands = sorted(all_hands, key=lambda x:x[0])
        for i in range(n):
            all_hands[i][2] = i+k
        k += n




    # un pack dict and calculate winnings
    merged_list = list(chain(*classified.values()))
    winnings = 0
    for hand in merged_list:
        winnings += hand[2]*hand[1]
    return winnings

def part_2(data):
    POWER = {"A": 13, "K": 12, "Q": 11, "J": 0, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}
    rank = 0

    n = len(data)
    for i in range(n):
        hand, bid = data[i].split()
        hand = list(hand)
        for j in range(5):
            hand[j] = POWER[hand[j]]
        data[i] = [hand, int(bid), rank]


    # divides the hands into the types
    for row in data:
        hand = row[0]
        type = hand_type_2(hand)
        classified[hand_classes[type]].append(row)



    k = 1
    # gives each hand a rank in each catagory
    for key in list(classified.keys()):
        all_hands = classified[key]

        n = len(all_hands)
        all_hands = sorted(all_hands, key=lambda x:x[0])
        for i in range(n):
            all_hands[i][2] = i+k
        k += n



    # un pack dict and calculate winnings
    merged_list = sorted(list(chain(*classified.values())), key=lambda x:x[-1])

    for i in merged_list:
        print()

    winnings = 0
    for hand in merged_list:
        winnings += hand[2]*hand[1]
    return winnings




with open("input.txt","r") as input:
    data = input.read()
    data = data.split("\n")

    print(f"result part 1: {part_1(data)}")
    print(f"result part 2 : {part_2(data)}")


