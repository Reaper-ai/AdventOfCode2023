
SUM = 0

# access input line by line
with open("input.txt", "r") as file:
    for line in file:

        # initialize right pointer
        r = len(line)-2

        # initialize digits
        f_digit, l_digit = None, None

        # initialize left pointer
        # while loop was on drugs , got stuck in infinite loop
        for l in range(len(line)-1):

            if f_digit is None and line[l].isdigit():
                    f_digit = int(line[l])

            if l_digit is None and line[r].isdigit():
                    l_digit = int(line[r])

            # stop loop when both digits found
            if (f_digit is int and l_digit is int):
                break
            r -= 1

        SUM += f_digit*10 + l_digit

print(SUM)

