'''
ID: colindi1
LANG: PYTHON3
TASK: transform
'''

# define transformation functions and then
# run through each by check if a statement is true

with open ('transform.in', 'r') as file:
    lines = [line.replace('\n', '') for line in file.readlines()]

N = int(lines.pop(0))

original = []
new = []

for _ in range(N):
    original.append(list(lines.pop(0)))

for _ in range(N):
    new.append(list(lines.pop(0)))

def rotate(orig, degrees): #rotated degrees
    rotated = list(orig)
    for _ in range(int(degrees/90)):
        rotated = list(zip(*rotated[::-1]))
    return [list(i) for i in rotated]

def reflection(m, mode): #reflected horizontally or vertically
    tempm = m.copy()
    if mode == 'h':
        for i in range(0,len(tempm),1):
                tempm[i].reverse()
    else:
        tempm.reverse()
    return [list(i) for i in tempm]

seqs = ['rotate(original, 90)==new',
        'rotate(original, 180)==new',
        'rotate(original, 270)==new',
        'reflection(original, "h")==new or reflection(original, "v")==new',
        'rotate(reflection(original, "h"), 90)==new or rotate(reflection(original, "h"), 180)==new or rotate(reflection(original, "h"), 270)==new or (rotate(reflection(original, "v"), 90)==new or rotate(reflection(original, "v"), 180)==new or rotate(reflection(original, "v"), 270)==new)',
        'original == new']

done = False
for seq in seqs:
    res = eval(seq, globals())

    if res:
        done = True
        out = str((seqs.index(seq)+1))
        break

if done == False:
    out = ('7')

with open('transform.out', 'w') as file:
    file.write(out + '\n')