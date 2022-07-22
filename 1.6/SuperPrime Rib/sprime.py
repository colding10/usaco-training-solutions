'''
ID: colindi1
LANG: PYTHON3
TASK: sprime
'''

with open('sprime.in', 'r') as file:
    rib_length = int(file.readline())

def isPrime(n):
    """Returns True if n is prime."""
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

possible_digits = []
current_rib = []

current_number = []
for _ in range(rib_length):
    for index, digit in enumerate(range(1, 11, 2)):
        possible_digits[index].append(digit)

with open('sprime.out', 'w') as file:
    file.write()
    file.write('\n')