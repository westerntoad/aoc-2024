import re
import sys

raw = open(sys.argv[1]).read()
print(raw)
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
#for delta in deltas:
    #print(delta[0])
#print(len(data))

print(data)
def numXMAS(x, y):
    numFound = 0
    print('ORIG:', x, y)
    for delta in deltas:
        print('ARR :', delta)
        for i in range(1, 4):
            dx = x + (delta[0] * i)
            dy = y + (delta[1] * i)
            letter = 'urdu'
            if i == 1:
                letter = 'M'
            elif i == 2:
                letter = 'A'
            elif i == 3:
                letter = 'S'

            print('NEW :', min(max(dx, 0), size - 1), min(max(dy, 0), size - 1))
            val = data[min(max(dx, 0), size - 1)][min(max(dy, 0), size - 1)]
            print('LETT:', val)
            if val != letter:
                print('BREAK\n')
                break

            if i == 3:
                print('FOUND\n')
                numFound += 1

    return numFound


for line in enumerate(data):
    for ch in enumerate(line[1]):
        if ch[1] == 'X':
            x = ch[0]
            y = line[0]
            total += numXMAS(x, y)

print('TOTAL:', total)

