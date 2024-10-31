
def part1():
    # puzzle input part 1
    TIME = [48, 93, 84, 66]
    DISTANCE = [261, 1192, 1019, 1063]


    n = len(TIME)
    ways_to_win = [0] * n
    for i in range(n):
        T = TIME[i]
        record = DISTANCE[i]

        for j in range(1,int(T/2)+1):
            if j*(T-j) > record:
                ways_to_win[i] += 2

        if T%2 == 0:
            ways_to_win[i] -=1

    result = 1
    for ways in ways_to_win:
        result *= ways

    return result

print(f"result : {part1()}" )

def part2():
    # puzzle input part 2
    TIME = 48_938_466
    DISTANCE = 261_119_210_191_063

    """
    => x(a-x) > c
    =>  ax - x2 - c > 0
    => x2 - ax + c < 0
    => result = difference of roots
    => diff. of roots = root D / a
    """
    result = (TIME**2 - 4*DISTANCE)**0.5

    return int(result)

print(f"result : {part2()}" )