
def bruteProductExceptSelf(nums : list[int]) -> list[int]:
    products = []
    for i in range(len(nums)): 
        product = multiply(nums[:i] + nums[i+1:])
        products.append(product)
    return products

def multiply(nums: list[int]) -> int:
    product = 1
    for num in nums:
        product = product * num
    return product

# print(bruteProductExceptSelf([-1,1,0,-3,3]))

def optimizedProductExceptSelf(nums : list[int]) -> list[int]:    
    n = len(nums)
    output = []

    prefix = 1
    for i in range(n):
        output.append(prefix)
        prefix *= nums[i]

    suffix = 1
    for i in range(n-1, -1, -1):
        output[i] *= suffix 
        suffix *= nums[i]

    return output

print(optimizedProductExceptSelf([1,2,3,4]))