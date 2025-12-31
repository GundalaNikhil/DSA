# Quick Reference: Code Fixes for 7 Failing Problems

## SRT-006: K-Sorted Array Minimum Swaps

**Current File:** `/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Sorting/solutions/python/SRT-006-k-sorted-array-min-swaps.py`

**Add at the beginning of `min_swaps_to_sort` function:**

```python
def min_swaps_to_sort(arr: list[int], k: int) -> int:
    n = len(arr)
    if n <= 1:
        return 0

    # NEW: Check if already k-sorted
    sorted_arr = sorted(enumerate(arr), key=lambda x: x[1])
    position_map = [0] * n
    for sorted_pos, (orig_pos, _) in enumerate(sorted_arr):
        position_map[orig_pos] = sorted_pos

    # Verify k-sorted property
    is_k_sorted = all(abs(i - position_map[i]) <= k for i in range(n))
    if is_k_sorted:
        return 0  # Already k-sorted, no additional swaps needed

    # ... rest of existing cycle detection code
```

---

## SRT-007: Search Rotated Duplicates Parity Count

**Current File:** `/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Sorting/solutions/python/SRT-007-search-rotated-duplicates-parity.py`

**Replace entire function with:**

```python
def count_even_indices(arr: list[int], x: int) -> int:
    """
    HYPOTHESIS 1: Count elements with same parity as x
    Verify with test cases:
    - Sample 1: x=48 (even), array has [16,18,48,48,2] (even) = 5 ✓
    """
    x_parity = x % 2
    return sum(1 for val in arr if val % 2 == x_parity)

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())
    result = count_even_indices(arr, x)
    print(result)
```

**If above fails, try:**

```python
def count_even_indices(arr: list[int], x: int) -> int:
    """
    HYPOTHESIS 2: Count occurrences at even indices
    """
    count = 0
    for i in range(0, len(arr), 2):  # Even indices only
        if arr[i] == x:
            count += 1
    return count
```

---

## SRT-008: Balanced Range Covering K Lists

**Current File:** `/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Sorting/solutions/python/SRT-008-balanced-range-covering-k-lists.py`

**Change the main function to return single integer:**

```python
def main():
    k = int(input())
    lists = []
    for _ in range(k):
        m = int(input())
        lst = list(map(int, input().split()))
        lists.append(lst)
    
    result = smallest_range(lists)
    
    if result:
        # Return range length instead of [L, R]
        print(result[1] - result[0])
    else:
        print(0)  # Or 'NONE' if no valid range exists
```

---

## SRT-010: Sort Colors Limited Swaps

**Current File:** `/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Sorting/solutions/python/SRT-010-sort-colors-limited-swaps.py`

**Status: Likely correct, but verify input parsing:**

```python
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    s = int(input())  # Ensure S is read as separate int
    result = sort_with_swaps(arr, s)
    print("YES" if result else "NO")
```

---

## SRT-011: Longest Consecutive One Change

**Current File:** `/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Sorting/solutions/python/SRT-011-longest-consecutive-one-change.py`

**Replace entire function with:**

```python
def longest_after_change(arr: list[int]) -> int:
    """
    Find longest sequence of consecutive integers (by value, not position)
    where we can change ONE element to bridge a gap
    """
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Get distinct sorted values
    distinct = sorted(set(arr))
    if len(distinct) == 1:
        return 1

    max_length = 1

    # Check each starting point
    i = 0
    while i < len(distinct):
        current_length = 1
        j = i + 1

        # Extend while values are consecutive
        while j < len(distinct) and distinct[j] == distinct[j-1] + 1:
            current_length += 1
            j += 1

        # Check if we can bridge a gap with one change
        if j < len(distinct) and distinct[j] == distinct[j-1] + 2:
            current_length += 1  # Can fill the gap
            # Continue extending after bridge
            while j + 1 < len(distinct) and distinct[j+1] == distinct[j] + 1:
                current_length += 1
                j += 1

        max_length = max(max_length, current_length)
        i = j if j > i + 1 else i + 1

    return max_length

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = longest_after_change(arr)
    print(result)
```

---

## SRT-012: Count Within Threshold After Self

**Current File:** `/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Sorting/solutions/python/SRT-012-count-within-threshold-after-self.py`

**Current implementation likely correct. Try optimized version:**

```python
from sortedcontainers import SortedList

def count_within_threshold(arr: list[int], T: int) -> list[int]:
    """For each i, count j > i where a[i] - a[j] <= T"""
    n = len(arr)
    counts = [0] * n
    
    # Process from right to left
    sorted_list = SortedList()
    
    for i in range(n - 1, -1, -1):
        # Count elements in range [a[i] - T, a[i]]
        lower = arr[i] - T
        upper = arr[i]
        
        left_idx = sorted_list.bisect_left(lower)
        right_idx = sorted_list.bisect_right(upper)
        counts[i] = right_idx - left_idx
        
        # Add current element's right elements
        if i + 1 < n:
            sorted_list.add(arr[i + 1])
    
    return counts

def main():
    n, t = map(int, input().split())
    arr = list(map(int, input().split()))
    result = count_within_threshold(arr, t)
    print(' '.join(map(str, result)))
```

**If SortedList unavailable, keep current brute force O(n²).**

---

## SRT-013: Closest Pair in Sorted Circular Array (CRITICAL FIX)

**Current File:** `/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Sorting/solutions/python/SRT-013-closest-pair-sorted-circular.py`

**Complete rewrite:**

```python
def closest_pair_circular(arr: list[int], target: int) -> list[int]:
    """Find pair with sum closest to target in rotated sorted array"""
    n = len(arr)
    if n < 2:
        return []

    # Find pivot (minimum element)
    pivot = 0
    for i in range(1, n):
        if arr[i] < arr[pivot]:
            pivot = i

    l, r = 0, n - 1
    min_diff = float('inf')
    result = []

    # Two-pointer on rotated array
    while l < r:
        pL = (pivot + l) % n
        pR = (pivot + r) % n

        curr_sum = arr[pL] + arr[pR]
        diff = abs(curr_sum - target)

        if diff < min_diff:
            min_diff = diff
            result = [arr[pL], arr[pR]]

        if curr_sum < target:
            l += 1
        else:
            r -= 1

    return result

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    target = int(input())  # ← CRITICAL: READ THE TARGET!
    result = closest_pair_circular(arr, target)
    print(result[0], result[1])

if __name__ == "__main__":
    main()
```

---

## Testing Checklist

Before committing changes, test each fix:

```bash
# SRT-006
echo "4 1
3 2 1 4" | python3 SRT-006-k-sorted-array-min-swaps.py
# Expected: 1

# SRT-007
echo "8 48
7 9 15 16 18 48 48 2" | python3 SRT-007-search-rotated-duplicates-parity.py
# Expected: 5

# SRT-013
echo "24
4 4 4 5 12 12 14 15 18 28 29 30 32 36 55 65 70 72 76 78 87 95 95 95
?" | python3 SRT-013-closest-pair-sorted-circular.py
# Need to determine target from sample data
```

---

## Implementation Order

1. **SRT-013** (5 min) - Just add input parsing
2. **SRT-006** (10 min) - Add k-sorted check
3. **SRT-011** (15 min) - Complete algorithm rewrite
4. **SRT-007, SRT-008** (20 min) - Test multiple hypotheses
5. **SRT-012** (10 min) - Try optimized if brute force fails
6. **SRT-010** (5 min) - Verify with tests
