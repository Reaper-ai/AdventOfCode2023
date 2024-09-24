SUM = 0

# adjusted digits to count overlapping numbers
letters = {"one": "o1e", "two": "t2o", "three": "t3e", "four": "4", "five": "5e", "six": "6", "seven": "7n", "eight": "e8t", "nine": "n9e"}

# access input line by line
with open("input.txt", "r") as file:
    for line in file:

        n = len(line)

        # will store all the numbers in [index,number] pair
        digits = []

        # find all the numbers in string format in the input and replace them withg numeric part
        for i in letters:
            flag = True
            while flag:
                index = line.find(i)
                if index != -1:
                    line = line.replace(i,letters[i])

                else:
                    flag = False

        n = len(line)

        # find all the numeric numbers
        for i in range(n - 1):
            if line[i].isdigit():
                digits.append([i, int(line[i])])

        SUM += digits[0][1] * 10 + digits[-1][1]

print(SUM)
