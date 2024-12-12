import sys

raw = open(sys.argv[1]).read()
data = raw.split('\n')[:-1]
size = len(data)
total = 0
deltas = [
    ( 1,  1),
    ( 1, -1),
    (-1, -1),
    (-1,  1)
]

def isCrossMAS(x, y):
    if x == 0 or y == 0 or x == size - 1 or y == size - 1:
        return False

    numMAS = 0
    for delta in deltas:
        dxM = x + delta[0]
        dyM = y + delta[1]
        dxS = x - delta[0]
        dyS = y - delta[1]

        if data[dyM][dxM] == 'M' and data[dyS][dxS] == 'S':
            numMAS += 1
    
    return numMAS == 2



for line in enumerate(data):
    for ch in enumerate(line[1]):
        if ch[1] == 'A':
            x = ch[0]
            y = line[0]
            if isCrossMAS(x, y):
                #print('FOUND', x, y)
                total += 1

print('TOTAL:', total)

