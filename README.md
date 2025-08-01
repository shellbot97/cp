# cp

## workspace:

```
{
	"folders": [
		{
			"path": "."
		}
	],
	"settings": {
		"gitHubCopilot.enableAutoCompletion": false
	}
}
```

---

## Efficiency optimization

| **Algorithm Type**              | **Time Complexity**         | **Meaning**                                  | **Efficient Target**                             | **Optimization Strategy**                                 |
|--------------------------------|-----------------------------|----------------------------------------------|--------------------------------------------------|------------------------------------------------------------|
| Search (unsorted)              | O(n)                        | Linear scan of all elements                  | ✅ O(1) or O(log n)                               | Use hash sets/maps (O(1)), or sort & binary search (O(log n)) |
| Search (sorted)                | O(log n)                    | Halves search space each step               | Already optimal                                 | N/A (Binary Search)                                        |
|                                | O(n²)                       | Nested comparisons (Bubble, etc.)            | ✅ O(n log n)                                    | Use Merge Sort / Quick Sort                               |
|                                | O(n log n)                  | Divide and conquer                          | Best general case                               | N/A (Merge/Quick)                                          |
| Sorting                        | O(n)                        | Only if elements are small integers          | Special cases                                   | Use Counting/Radix Sort                                   |
| Duplicate detection            | O(n²)                       | Compare each pair                           | ✅ O(n)                                          | Use a set() to track seen values                          |
| Max/min in list                | O(n)                        | Scan once                                   | Already optimal                                 | N/A                                                       |
| String matching                | O(n·m)                      | Naive scan                                  | ✅ O(n + m)                                      | Use KMP or Rabin-Karp                                     |
| Subset/Combination gen.       | O(2ⁿ)                       | Generate all subsets/combinations           | Can’t avoid, but can prune                      | Use backtracking + early stopping or memoization         |
| Fibonacci (naive recursion)   | O(2ⁿ)                       | Exponential growth                          | ✅ O(n)                                          | Use memoization or bottom-up DP                          |
| Matrix multiplication         | O(n³)                       | Triple nested loop                          | ✅ O(n^2.373) (Strassen, Coppersmith–Winograd)  | Use optimized algorithms or libraries                    |
| Graph traversal                | O(n²) (matrix)              | Check all connections                        | ✅ O(n + m)                                      | Use adjacency list + BFS/DFS                             |
| Shortest path (Dijkstra)      | O(n²)                       | Scan all nodes naively                      | ✅ O((n + m) log n)                              | Use min-heap priority queue                              |
| Topological sort              | O(n + m)                    | Linear time w/DFS                           | Already optimal                                 | N/A                                                       |

---

## Edge Cases

| **Category**                | **Edge Case Scenarios**    | **Example(s)**                                      |
| --------------------------- | -------------------------- | --------------------------------------------------- |
| **Input Size Extremes**     | Empty input                | `[]`, `""`                                          |
|                             | Single element             | `[42]`, `"a"`                                       |
|                             | Max constraints            | `n = 10^5` or `10^6`                                |
| **Value Extremes**          | Minimum values             | `0`, `-1`, `-10^9`                                  |
|                             | Maximum values             | `10^9`, `10^18`                                     |
|                             | Alternating extremes       | `[1, 10^9, 1, 10^9]`                                |
| **Special Patterns**        | Sorted ascending           | `[1, 2, 3, 4]`                                      |
|                             | Sorted descending          | `[4, 3, 2, 1]`                                      |
|                             | All duplicates             | `[7, 7, 7, 7]`                                      |
|                             | No duplicates              | `[1, 2, 3, 4]`                                      |
|                             | Palindrome sequence        | `[1, 2, 3, 2, 1]`                                   |
|                             | Already optimal            | Best-case input for algo                            |
|                             | Worst-case                 | Triggers slowest execution                          |
| **Logical Edge Cases**      | No valid answer possible   | Return `-1`, `"NO"`, `null`                         |
|                             | Multiple valid answers     | Any acceptable output                               |
|                             | Tie values                 | Same frequency/value                                |
|                             | Circular behavior          | Wrap-around indexing                                |
| **Data Structure Specific** | Strings                    | `""`, `"aaaa"`, spaces, mixed case                  |
|                             | Graphs                     | No edges, fully connected, disconnected, self-loops |
|                             | Linked Lists               | Single node, two nodes, circular                    |
|                             | Trees                      | Only root, skewed, balanced                         |
| **Algorithmic Traps**       | Off-by-one                 | Loops with wrong bounds                             |
|                             | Inclusive/exclusive ranges | `[low, high)` vs `[low, high]`                      |
|                             | Index underflow/overflow   | `i-1` when `i=0`                                    |
|                             | Integer division           | `5/2 → 2`                                           |
|                             | Modulo negative numbers    | Language-specific result                            |
|                             | Recursion depth limit      | Large recursion stack                               |
| **Constraint Triggers**     | Time complexity            | Test `n = 10^5+`                                    |
|                             | Space complexity           | Memory-heavy data                                   |
|                             | Mutable input changes      | Accidentally altering input                         |
|                             | Floating-point precision   | `0.1 + 0.2 != 0.3`                                  |

---

## Data Type 

| **Data Type**               | **Size (bytes)**  | **Size (bits)** | **Typical Value Range**                                     |
| --------------------------- | ----------------- | --------------- | ----------------------------------------------------------- |
| **char**                    | 1 byte            | 8 bits          | `-128` to `127` (signed) or `0` to `255` (unsigned)         |
| **bool**                    | 1 byte            | 8 bits          | `true` / `false`                                            |
| **short**                   | 2 bytes           | 16 bits         | `-32,768` to `32,767`                                       |
| **unsigned short**          | 2 bytes           | 16 bits         | `0` to `65,535`                                             |
| **int**                     | 4 bytes           | 32 bits         | `-2,147,483,648` to `2,147,483,647`                         |
| **unsigned int**            | 4 bytes           | 32 bits         | `0` to `4,294,967,295`                                      |
| **long** (C/Java)           | 4 bytes           | 32 bits         | Same as `int` in C (Java always 64-bit)                     |
| **long long**               | 8 bytes           | 64 bits         | `-9,223,372,036,854,775,808` to `9,223,372,036,854,775,807` |
| **unsigned long long**      | 8 bytes           | 64 bits         | `0` to `18,446,744,073,709,551,615`                         |
| **float**                   | 4 bytes           | 32 bits         | \~6–7 decimal digits precision                              |
| **double**                  | 8 bytes           | 64 bits         | \~15–16 decimal digits precision                            |
| **long double**             | 16 bytes (varies) | 128 bits        | \~18–19 decimal digits precision                            |
| **pointer** (32-bit system) | 4 bytes           | 32 bits         | Memory address                                              |
| **pointer** (64-bit system) | 8 bytes           | 64 bits         | Memory address                                              |


---

## Prompt

I am trying to solve leetcode problem “238. Product of Array Except Self”. I have written the following program which works for the mentioned test case:

```'
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

```

testcase:

```
nums = [1,2,3,4]
products = [24,12,8,6]
```

For this solution, I have calculated the time complexity as o(n^2). Your task is to go through the written solution carefully and 

1. check if the calculated time complexity is correct or not
2. find out if I have missed handling any edge case
3. suggest a more optimized/clean solution if you can come up with one

Please let me know in advance if you are not familiar with leetcode problem I will give you the problem statement
