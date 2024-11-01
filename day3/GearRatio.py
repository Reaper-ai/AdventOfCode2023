from collections import defaultdict
file = open("input.txt", "r")
data_set = file.readlines()
M = len(data_set)


# prepare input
for i in range(M):
    data_set[i] =  "." + data_set[i].strip() + "."
N = len(data_set[0])

data_set.append(("."*N))
data_set.insert(0,("."*N))


# stored in format [x,(y_start,y_end)]
digits = []
for i in range(1,M+1):
    j = 1
    while j < M+1:
        item = data_set[i][j]
        if item.isdigit():
            s = j
            while item.isdigit():
                j+=1
                item = data_set[i][j]
            digits.append([i,(s,j)])
        else:
            j+=1


def part_1(data_set):
    # identify valid values
    nums = []
    for coords in digits:
        x , Y = coords
        flag = True
        for i in range(x-1,x+2):
            for j in range(Y[0]-1,Y[1]+1):
                item = data_set[i][j]
                if (not item.isdigit()) and item != ".":
                    nums.append(int(data_set[x][Y[0]:Y[1]]))
                    flag = False
                    break
            if not flag:
                break
    return sum(nums)

print(f'result part 1:{part_1(data_set)}')

def part_2(data_set):
    nums = defaultdict(list)
    for coords in digits:
        x , Y = coords
        flag = True
        for i in range(x-1,x+2):
            for j in range(Y[0]-1,Y[1]+1):
                item = data_set[i][j]
                if item == "*":
                    nums[(i,j)].append(int(data_set[x][Y[0]:Y[1]]))


    ratio = 0
    for value in nums.values():
        if len(value) == 2:
            ratio += value[0]*value[1]

    return ratio

print(f"result part 2 : {part_2(data_set)}")


