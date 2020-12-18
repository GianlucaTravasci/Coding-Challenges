from collections import defaultdict

with open('input.txt', 'r') as file:
    data = file.read().split('\n\n')

rules = data[0]
my_ticket_row = data[1]
nearby_tickets = data[2]

# part1


valid_seat = set()
headers = defaultdict(set)
invalid_seat_counter = 0
nearby_tickets_valid = []

for range_data in rules.splitlines():
    field, range_data = range_data.split(':')
    ranges = range_data.split()
    ranges_one = ranges[-3].split('-')
    ranges_two = ranges[-1].split('-')
    for i in range(int(ranges_one[0]), int(ranges_one[1]) + 1):
        valid_seat.add(i)
        headers[field].add(i)
    for i in range(int(ranges_two[0]), int(ranges_two[1]) + 1):
        valid_seat.add(i)
        headers[field].add(i)

for nearby_ticket in nearby_tickets.splitlines():
    if nearby_ticket[0] == 'n':
        continue
    flag = True
    nearby_ticket = list(map(int, nearby_ticket.split(',')))
    for value in nearby_ticket:
        if value not in valid_seat:
            invalid_seat_counter += value
            flag = False
    if flag:
        nearby_tickets_valid.append(nearby_ticket)

print("solution 1:", invalid_seat_counter)

# part 2


my_ticket = list(map(int, my_ticket_row.splitlines()[1].split(',')))
found =[None] * len(my_ticket)
while None in found:
    for header_key, header_val in headers.items():
        if header_key in found:
            continue
        candidates = set()
        for index, key in enumerate(found):
            does_work = True
            if key is not None:
                continue
            for nearby_ticket_valid in nearby_tickets_valid:
                if nearby_ticket_valid[index] not in header_val:
                    does_work = False
            if does_work:
                candidates.add(index)
        if len(candidates) == 1:
            found[candidates.pop()] = header_key
            break


my_anotated_ticket = {
    name: my_ticket[index] for index, name in enumerate(found) if name.startswith('departure')
}

product = 1
for val in my_anotated_ticket.values():
    product *= val
print("solution 2:", product)
