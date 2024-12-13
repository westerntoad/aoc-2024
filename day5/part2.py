from functools import cmp_to_key
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

def cmpRule(item1, item2):
    if item1 in rules and item2 in rules[item1]:
        return -1
    elif item2 in rules and item1 in rules[item2]:
        return 1
    else:
        return 0


def isGoodUpdate(update):
    nums = update.split(',')
    n = len(nums)
    for i in range(n):
        for j in range(i - 1, -1, -1):
            if nums[i] in rules and nums[j] in rules[nums[i]]:
                return False

    return True


def updateVal(update):
    if isGoodUpdate(update):
        return 0

    nums = update.split(',')
    n = len(nums)
    numsSanitized = sorted(nums, key=cmp_to_key(cmpRule))

    return int(numsSanitized[n // 2])


for update in split[1].split('\n')[:-1]:
    total += updateVal(update)

print(total)
