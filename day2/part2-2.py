
lines = open("input.txt").readlines()

def isSafe(nums):
    diff = abs(nums[0] - nums[1])
    if diff > 3 or diff < 1:
        return False

    increasing = nums[0] < nums[1]

    for i in range(2, len(nums)):
        diff = nums[ i ] - nums[i-1]

        if diff == 0 or abs(diff) > 3 or (diff < 0 and increasing) or (diff > 0 and not increasing):
            return False

    return True

def isSafeRemoved(nums):
    if isSafe(nums):
        return True

    for i in range(len(nums)):
        cp = nums.copy()
        cp.pop(i)

        if isSafe(cp):
            return True

    return False


numSafe = 0
for line in lines:
    nums = list(map(int, line.split()))
    if isSafeRemoved(nums):
        numSafe += 1

print(numSafe)


