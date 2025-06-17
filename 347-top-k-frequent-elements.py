from collections import defaultdict

def kMostFrequent(k: int, nums: list[int]) -> list[int]:
    counts = defaultdict(list)
    for num in nums:
        counts[num] = counts.get(num, 0) + 1 
    sortedCounts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    top_k = [key for key, value in sortedCounts[:k]]
    return top_k

print(kMostFrequent(2, [6,6, 5,1,1,1,2,2,2,3]))