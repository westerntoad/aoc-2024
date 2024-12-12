
lines = open("input2.txt").readlines()

a = []
b = dict()

for line in lines:
    locs = line.split()
    a.append(int(locs[0]))
    second = int(locs[1])
    if second in b:
        b[second] += 1
    else:
        b[second] = 1

output = 0

for num in a:
    if num in b:
        output += num * b[num]

print(output)

