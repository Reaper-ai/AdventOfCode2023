
# set initial location to infinity
min_loc = float("inf")

## make data usable
class Source_to_Sink:
    def __init__(self, mapp):
        self.source = [int(i[1]) for i in mapp]
        self.sink = [int(i[0]) for i in mapp]
        self.range = [int(i[2]) for i in mapp]

    def find_sink(self,source):
        for i,src in enumerate(self.source):
            if source in range(src,src + self.range[i]):
                return source - src + self.sink[i]

        return source
# extract numerical part
def splice(data):
    slice = data.split(":\n")[1]
    slice = slice.split('\n')
    slice = [ i.split() for i in slice]
    slice = Source_to_Sink(slice)
    return slice

with open("input.txt","r") as file:
    data = file.read()
    data = data.split("\n\n")

    seed_profile = data[0].split(":")
    seed_profile = list(map(int,seed_profile[1].split()))


    maps_ = []
    for i in range(1,len(data)):
        maps_.append(splice(data[i]))


    for seed in seed_profile:
        nextmap = seed
        for m in maps_:
            nextmap = m.find_sink(nextmap)

        min_loc = min(nextmap,min_loc)


print(min_loc)