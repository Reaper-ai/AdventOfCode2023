f = open("input.txt","r")
data = f.read().split("\n")
for i in range(len(data)):
    data[i] = list(map(int,data[i].split()))


# the puzzle is about the "method of differences"
# a mathematical algorithm used to calculate nth term of
# non-traditional series
def nth_term(sequence, n):
    # Generate difference sequences
    diff_sequences = [sequence]
    while len(diff_sequences[-1]) > 1:
        next_diff = [j - i for i, j in zip(diff_sequences[-1], diff_sequences[-1][1:])]
        diff_sequences.append(next_diff)

    # Calculate the nth term using the method of differences
    nth_term = 0
    for i, diff in enumerate(diff_sequences):
        if i >= n:
            break
        nth_term += diff[0] * combination(n - 1, i)

    return nth_term

def combination(n, r):
    from math import factorial
    return factorial(n) // (factorial(r) * factorial(n - r))

# for part one
a_n = []
for series in data:
    n =  nth_term(series,len(series)+1)
    a_n.append(n)
print(f"result part 1 : {sum(a_n)}")

# for part 2
a_n = []
for series in data:
    series.reverse()
    n = nth_term(series, len(series) + 1)
    a_n.append(n)
print(f"result part 2 : {sum(a_n)}")