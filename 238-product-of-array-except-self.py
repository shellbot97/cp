
def bruteProductExceptSelf(nums : list[int]) -> list[int]:
    products = []
    for i in range(len(nums)):
        copyNums = nums.copy()
        copyNums.pop(i)
        product = multiply(copyNums)
        products.append(product)
    return products

def multiply(nums: list[int]) -> int:
    product = 1
    for num in nums:
        product = product * num
    return product

print(bruteProductExceptSelf([1,2,3,4]))
