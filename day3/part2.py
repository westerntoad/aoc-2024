import re

raw = open('input.txt').read()

total = 0
enabled = True
pattern = r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))"
for match in re.finditer(pattern, raw):
    m = match.group(0)
    if enabled:
        if m == "don't()":
            enabled = False
        elif m != "do()":
            print(m)
            nums = re.findall(r'\d{1,3}', m)
            total += int(nums[0]) * int(nums[1])
    elif m == "do()":
        enabled = True

print(total)
