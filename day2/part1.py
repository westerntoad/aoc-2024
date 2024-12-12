
lines = open("input.txt").readlines()

numSafe = 0
for line in lines:
    nums = list(map(int, line.split()))
    diff = abs(nums[0] - nums[1])
    if diff > 3 or diff < 1:
        continue

    increasing = nums[0] < nums[1]

    for i in range(2, len(nums)):
        diff = nums[ i ] - nums[i-1]

        if diff == 0 or abs(diff) > 3 or (diff < 0 and increasing) or (diff > 0 and not increasing):
            numSafe -= 1
            break

    numSafe += 1


print(numSafe)


