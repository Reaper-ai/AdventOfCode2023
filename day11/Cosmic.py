
file = open("input","r")
image = file.read()
image = image.split("\n")
for i in range(len(image)):
    image[i] = list(image[i])

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

# part1
def expand(image):
    corrected_image = []
    for i in image:
        if '#' not in i:
            corrected_image.append(i)
        corrected_image.append(i)

    return corrected_image

corrected_image = expand(image)
corrected_image = transpose(expand(transpose(corrected_image)))

def locations(img):
    g = []
    for i in range(len(img)):
        for j in range(len(img[0])):
            if img[i][j] == "#":
                g.append((i,j))

    return g

galaxies = locations(corrected_image)
result = 0
m = len(galaxies)
# shortest path = manhattan distance
for i in range(m):
    for j in range(i+1,m):
        x1, y1 = galaxies[i]
        x2, y2 = galaxies[j]
        result += (abs(x1 - x2) + abs(y1 - y2))

print(f"result part 1 : {result}")

# part 2
# scale path by 999_999 wherever there is a empty row/col b/w two galaxies
def calc_empty(img):
    lst = []
    for i in range(len(img)):
        if "#" not in img[i]:
            lst.append(i)
    return lst

empty_rows = calc_empty(image)
empty_cols = calc_empty(transpose(image))

E = 999_999

galaxies = locations(image)
result = 0
for i in range(m):
    for j in range(i+1,m):
        x1, y1 = galaxies[i]
        x2, y2 = galaxies[j]

        for r in empty_rows:
            if r in range(x1+1,x2):
                result += E
        for c in empty_cols:
            if c in range(min(y1,y2),max(y1,y2)+1):
                result += E

        result += (abs(x1 - x2 ) + abs(y1 - y2))

print(f"result part 2 : {result}")
