def bruteContainsDuplicate(nums: list[int]):
    frequency = []
    for num in nums: # loop 1 O(n)
        if num in frequency: # loop 2 O(n) => this is a linear scan due to which complexity ⬆️
            return True
        frequency.append(num)    
    return False

def optimizedContainsDuplicate(nums: list[int]):
    seen = set()
    for num in nums: 
        if num in seen:
            return True
        seen.add(num)
    return False

nums = [1,2,3,1]
if optimizedContainsDuplicate(nums):
    print("duplicate")
else:
    print("no duplicates")