'''
ID: colindi1
LANG: PYTHON3
TASK: skidesign
'''

#import os
#try:
#    os.chdir(os.path.dirname(__file__))
#except:
#    pass

with open('skidesign.in', 'r') as file:
    lines = [line.replace('\n', '') for line in file.readlines()]

N = int(lines.pop(0))

elevations = []

for _ in range(N):
    elevations.append(int(lines.pop(0)))

elevations.sort()
costs = []

if max(elevations) - min(elevations) <= 17:
    costs.append(0)

for starting_height in range(0, elevations[-1] - 17):
    cost = 0

    ending_height = starting_height + 17

    for hill_elevation in elevations:
        if hill_elevation > ending_height:
            cost += (ending_height - hill_elevation) ** 2
        if hill_elevation < starting_height:
            cost += (starting_height - hill_elevation) ** 2
    
    costs.append(cost)

cheapest = min(costs)

with open('skidesign.out', 'w') as file:
    file.write(str(cheapest) + '\n')