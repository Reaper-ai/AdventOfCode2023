from functools import cache

file = open("input", "r")
data = file.read().split("\n")
@cache # for part two
def part1(cfg, rcfg):
    if cfg == "":
        return 1 if rcfg == () else 0

    if rcfg == ():
        return 0 if "#" in cfg else 1


    comb = 0
    if cfg[0] in ".?":
        comb += part1(cfg[1:], rcfg)

    if cfg[0] in "#?":
        # if num > string (invalid) | there should be no broken springs in num block | no good spring next to block or no spring left
        if rcfg[0] <= len(cfg) and "." not in cfg[:rcfg[0]] and (rcfg[0] == len(cfg) or cfg[rcfg[0]] != "#"):
            comb += part1(cfg[rcfg[0]+1:], rcfg[1:])

    return comb

def part2(config,rConfig):
    config = "?".join([config]*5)
    rConfig = rConfig*5

    result = part1(config,rConfig)

    return result



result1 = 0
result2 = 0
for line in data:
    config, rConfig  = line.split()
    rConfig = tuple(map(int,rConfig.split(",")))
    result1 += part1(config,rConfig)
    result2 += part2(config,rConfig)

print(f"result part1 : {result1}")
print(f"result part2 : {result2}")

