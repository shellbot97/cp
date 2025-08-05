def bruteForceLongestConsecutive(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    length = 0
    max_length = 0
    nums_unique = list(set(nums))
    nums_unique.sort()
    for i in range(len(nums_unique)-1):
        if nums_unique[i + 1] == nums_unique[i] + 1:
            length += 1
            max_length = max(length, max_length)
        else:
            length = 0
    return max_length + 1 if max_length > 0 else 1


def optimisedLongestConsecutiveSequence(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    
    maxLength = 0
    uniqueNums = set(nums)

    for num in uniqueNums:
        if (num - 1) not in uniqueNums:
            currentNum = num
            currentLength = 1
            while currentNum + 1 in uniqueNums:
                currentLength += 1
                currentNum += 1
            maxLength = max(currentLength, maxLength)
    return maxLength

print(bruteForceLongestConsecutive([100,4,200,1,3,2]))