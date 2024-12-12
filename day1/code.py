
lines = open("input2.txt").readlines()

a = []
b = []

for line in lines:
    locs = line.split()
    a.append(int(locs[0]))
    b.append(int(locs[1]))

a.sort()
b.sort()

distance = 0

for i in range(len(a)):
    distance += abs(a[i] - b[i])

print(distance)

