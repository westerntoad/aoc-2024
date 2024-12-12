import re

raw = open('input.txt').read()

total = 0
for match in re.findall(r'mul\(\d{1,3},\d{1,3}\)', raw):
    nums = re.findall(r'\d{1,3}', match)
    total += int(nums[0]) * int(nums[1])

print(total)
