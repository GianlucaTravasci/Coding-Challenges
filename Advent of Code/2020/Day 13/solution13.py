from functools import reduce
from operator import mul

with open("input.txt") as file:
    earliest = int(file.readline())
    buses = file.readline().strip().split(',')
    ids = [int(bus) for bus in buses if bus != 'x']


def earliest_to_wait():
    timestamp = earliest
    while True:
        departs = list(filter(lambda bus: timestamp % bus == 0, ids))
        if departs:
            return departs[0] * (timestamp - earliest)
        timestamp += 1


def offset_matches():
    timestamp = 0
    offset = list(map(lambda bus: buses.index(str(bus)), ids))
    while True:
        departs = list(filter(lambda bus: (timestamp + offset[ids.index(bus)]) % bus == 0, ids))
        if departs == ids:
            return timestamp + offset[0]
        timestamp += reduce(mul, departs)


print("Earliest x wait:", earliest_to_wait())
print("Offsets match:", offset_matches())
