import sys

raw = open(sys.argv[1]).read()
#print(raw)
data = raw.split('\n')[:-1]
size = len(data)
total = 0
deltas = [
    ( 0,  1),
    ( 1,  1),
    ( 1,  0),
    ( 1, -1),
    ( 0, -1),
    (-1, -1),
    (-1,  0),
    (-1,  1)
]

def deltaToCardinal(delta):
    out = ''

    if delta[1] == -1:
        out  += 'N'
    elif delta[1] == 1:
        out += 'S'

    if delta[0] == 1:
        out += 'E'
    elif delta[0] == -1:
        out += 'W'

    return out


def numXMAS(x, y):
    numFound = 0
    for delta in deltas:
        for i in range(1, 4):
            dx = x + (delta[0] * i)
            dy = y + (delta[1] * i)

            if dx < 0 or dy < 0 or dx > size - 1 or dy > size - 1:
                break

            letter = 'urdu'
            if i == 1:
                letter = 'M'
            elif i == 2:
                letter = 'A'
            elif i == 3:
                letter = 'S'

            val = data[dy][dx]
            if val != letter:
                break

            if i == 3:
                #print('FOUND', x, y, deltaToCardinal(delta))
                numFound += 1

    return numFound


for line in enumerate(data):
    for ch in enumerate(line[1]):
        if ch[1] == 'X':
            x = ch[0]
            y = line[0]
            total += numXMAS(x, y)

print('TOTAL:', total)

