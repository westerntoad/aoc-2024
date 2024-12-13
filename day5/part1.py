import sys

raw = open(sys.argv[1]).read()
split = raw.split('\n\n')
rules = dict()
total = 0

for rawRule in split[0].split('\n'):
    rule = rawRule.split('|')

    if not rule[0] in rules:
        rules[rule[0]] = set()

    rules[rule[0]].add(rule[1])

def updateVal(update):
    nums = update.split(',')
    n = len(nums)
    for i in range(n):
        for j in range(i - 1, -1, -1):
            if nums[i] in rules and nums[j] in rules[nums[i]]:
                return 0

    return int(nums[n // 2])


for update in split[1].split('\n')[:-1]:
    total += updateVal(update)

print(total)
