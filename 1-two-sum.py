def bruteTwoSum(nums: list[int], target: int) -> list[int]:
    remainders = {}
    for index, num in enumerate(nums):
        remainders[target - num] = index
    for index, num in enumerate(nums): 
        if (num in remainders) and (index != remainders[num]):
            return [index, remainders[num]]
    return []

nums = [3,2,4]
target = 6
print(bruteTwoSum(nums, target))