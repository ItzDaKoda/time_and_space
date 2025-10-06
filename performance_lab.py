# Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    return max(frequency, key=frequency.get)

"""
Time and Space Analysis for problem 1:
- Best-case: O(n) — you must count each element once.
- Worst-case: O(n) — still linear regardless of distribution.
- Average-case: O(n)
- Space complexity: O(k), where k is the number of unique elements.
- Why this approach? Using a dictionary allows fast counting in one pass.
- Could it be optimized? Not really; counting frequencies requires scanning all data.
"""


# Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

"""
Time and Space Analysis for problem 2:
- Best-case: O(n) — each element checked once.
- Worst-case: O(n) — still linear even with all unique elements.
- Average-case: O(n)
- Space complexity: O(n) for the set and output list.
- Why this approach? A set provides O(1) lookup to track seen elements efficiently.
- Could it be optimized? Not significantly; maintaining order requires extra space.
"""


# Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs

"""
Time and Space Analysis for problem 3:
- Best-case: O(n) — single scan through list.
- Worst-case: O(n) — same since only one pass and set lookups are O(1).
- Average-case: O(n)
- Space complexity: O(n) for the set and list of pairs.
- Why this approach? Hash set allows quick lookup for complements.
- Could it be optimized? You could sort + use two pointers (O(n log n)), but this is faster for unsorted input.
"""


# Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 1
    size = 0
    arr = []

    for i in range(n):
        if size == capacity:
            print(f"Resizing from capacity {capacity} to {capacity * 2}")
            capacity *= 2
        arr.append(i)
        size += 1
        print(f"Added item {i}, size = {size}, capacity = {capacity}")

"""
Time and Space Analysis for problem 4:
- When do resizes happen? Whenever size == capacity.
- Worst-case for a single append: O(n), during resize (copying elements).
- Amortized time per append: O(1) — doubling spreads out the cost.
- Space complexity: O(n)
- Why does doubling reduce the cost overall? Because total copies are logarithmic in n, not linear per append.
"""


# Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    result = []
    total = 0
    for num in nums:
        total += num
        result.append(total)
    return result

"""
Time and Space Analysis for problem 5:
- Best-case: O(n) — must sum through all elements.
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n) for the result list.
- Why this approach? Single-pass cumulative addition is the most efficient.
- Could it be optimized? Not meaningfully — each element contributes to the total.
"""

def find_pairs(nums, target):
    """
    Refactored version using sorting and two-pointer technique.
    Compared to the original hash set solution, this reduces space usage
    from O(n) → O(1), but slightly increases time complexity due to sorting (O(n log n)).
    """
    nums.sort()  # Sort the list in place
    left, right = 0, len(nums) - 1
    pairs = []

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            pairs.append((nums[left], nums[right]))
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return pairs


"""
Comparison with Original Version:

Original Version (Hash Set):

Time Complexity: O(n)
Space Complexity: O(n)
Why? Stores all seen elements in a set for O(1) lookups.

Refactored Version (Two-Pointer):

Time Complexity: O(n log n) — due to sorting step
Space Complexity: O(1) — only uses variables, no set or dictionary
Why? Sorts the list once and scans with two pointers to find pairs.

Optimization Explanation:
This refactored version trades a bit of time (because of sorting)
for better space efficiency. If memory is limited or n is very large,
the two-pointer approach is preferable.
"""
