"""
ID: colindi1
LANG: PYTHON3
TASK: beads
"""

#import os
#try:
#    os.chdir(os.path.dirname(__file__))
#except:
#    pass

with open('beads.in', 'r') as file:
    lines = [i.replace('\n', '') for i in file.readlines()]
    necklace = lines[1]
    length = int(lines[0])

def return_cuts(iterable):
    cuts = []
    for index in range(len(iterable)):
        p1 = iterable[:index]
        p2 = iterable[index:]
        if p1 + p2 == iterable:
            if p1 and p2:
                cuts.append((p1+p2+p1, p2+p1+p2))
    return cuts

counts = []

test_cases = return_cuts(necklace)

for case in test_cases:
    count = 2

    go_left = case[0]
    go_right = case[1]

    go_left = go_left[::-1]
    starting = go_left[0]

    iterations = 0
    for char in go_left[1:]:
        iterations += 1
        if iterations > length:
            break
        if starting == 'w':
            starting = str(char)
            count += 1
            continue
        if char == starting or char == 'w':
            count += 1
            continue
        else:
            break
    
    if necklace != necklace[::-1]:
        starting = go_right[0]
        iterations = 0
        for char in go_right[1:]:
            iterations += 1
            if iterations > length:
                break
            if starting == 'w':
                starting = str(char)
                count += 1
                continue
            if char == starting or char == 'w':
                count += 1
                continue
            else:
                break
    else:
        count -= 2
    counts.append(count)

out = max(counts)
#print(out)
with open('beads.out', 'w') as file:
    file.write(str(out)+'\n')