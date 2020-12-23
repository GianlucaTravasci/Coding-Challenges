import re
from collections import defaultdict

with open('input.txt') as file:
    data = file.read().splitlines()

# Part 1

cnt = defaultdict(int)
map = {}

for l in data:

    ing = re.findall(r'(.+)\(', l)[0].split()
    alle = re.findall(r'\(contains (.+)\)', l)[0].replace(',', '').split()

    for i in ing:
        cnt[i] += 1

    for i in alle:
        if i in map:
            map[i] &= set(ing)
        else:
            map[i] = set(ing)

sus = set()
for i in map.values():
    sus |= i

answer = 0
for i in cnt:
    if i not in sus:
        answer += cnt[i]

print(answer)

cnt = defaultdict(int)
map = {}

for l in data:

    ing = re.findall(r'(.+)\(', l)[0].split()
    alle = re.findall(r'\(contains (.+)\)', l)[0].replace(',', '').split()

    for i in ing:
        cnt[i] += 1

    for i in alle:
        if i in map:
            map[i] &= set(ing)
        else:
            map[i] = set(ing)

sus = set()
for i in map.values():
    sus |= i

visited = defaultdict(bool)

for _ in range(len(map)):
    for idx in map:
        if len(map[idx]) == 1 and not visited[idx]:
            visited[idx] = True
            target_idx = idx
            target_field = [e for e in map[idx]][0]
            break

    for idx in map:
        if idx == target_idx:
            continue
        if target_field in map[idx]:
            map[idx].remove(target_field)

answer = ''
for i in sorted(list(map.keys())):
    answer += (map[i].pop() + ',')

print(answer[:-1])
