
lines = open("example.txt").readlines()

numSafe = 0
for line in lines:
    nums = list(map(int, line.split()))
    increasingOff = 0
    decreasingOff = 0

    diff = abs(nums[0] - nums[1])
    if diff > 3 or diff < 1:
        increasingOff += 1
        decreasingOff += 1
    
    prev = nums[0]
    nums.pop(0)


    while len(nums) > 0:
        diff = nums[0] - prev
        if diff == 0 or abs(diff) > 3 or diff < 0:
            increasingOff += 1
        else:
            prev = nums[0]
        nums.pop(0)

    nums = list(map(int, line.split()))
    increasingOff2 = 1
    prev = nums[1]
    nums.pop(0)
    nums.pop(0)
    while len(nums) > 0:
        diff = nums[0] - prev
        if diff == 0 or abs(diff) > 3 or diff < 0:
            increasingOff2 += 1
        else:
            prev = nums[0]
        nums.pop(0)
    increasingOff = min(increasingOff, increasingOff2)
    
    nums = list(map(int, line.split()))
    prev = nums[0]
    nums.pop(0)
    while len(nums) > 0:
        diff = nums[0] - prev
        if diff == 0 or abs(diff) > 3 or diff > 0:
            decreasingOff += 1
        else:
            prev = nums[0]
        nums.pop(0)
    
    nums = list(map(int, line.split()))
    decreasingOff2 = 1
    prev = nums[1]
    nums.pop(0)
    nums.pop(0)
    while len(nums) > 0:
        diff = nums[0] - prev
        if diff == 0 or abs(diff) > 3 or diff > 0:
            #print('comparing', prev, 'and', nums[0])
            decreasingOff2 += 1
        else:
            prev = nums[0]
        nums.pop(0)
    #print('decreasingOff1 =',decreasingOff)
    #print('decreasingOff2 =',decreasingOff2)
    decreasingOff = min(decreasingOff, decreasingOff2)

    
    print('increasingOff =',increasingOff)
    print('decreasingOff =',decreasingOff)
    print(line, end='')
    if increasingOff < 2 or decreasingOff < 2:
        numSafe += 1
        print("is safe")
    print("\n")


print(numSafe)


