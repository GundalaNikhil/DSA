---
title: Stable Sort By Two Keys
slug: stable-sort-two-keys
difficulty: Easy
difficulty_score: 30
tags:
- Sorting
- Stability
- Records
problem_id: SRT_STABLE_SORT_TWO_KEYS__5920
display_id: SRT-003
topics:
- Sorting
- Stability
- Records
---
# Stable Sort By Two Keys - Editorial

## Problem Summary

You are given a list of `n` records, where each record consists of two keys: `key1` and `key2`. You need to sort these records primarily by `key1` in ascending order, and secondarily by `key2` in ascending order. Crucially, the sort must be **stable**: if two records have identical `key1` and `key2`, their relative order from the input must be preserved.

## Real-World Scenario

Imagine you are organizing a **Leaderboard for a Game Tournament**.
-   Players are ranked primarily by **Score** (higher is better).
-   If scores are tied, they are ranked by **Time Taken** (lower is better).
-   If both Score and Time are identical, you want to list the players in the order they registered (original input order).
-   This requires a multi-key sort where stability ensures fairness for identical performances.

## Problem Exploration

### 1. Multi-Key Sorting
-   We need to compare two records `A` and `B`.
-   First, compare `A.key1` and `B.key1`.
    -   If `A.key1 < B.key1`, `A` comes first.
    -   If `A.key1 > B.key1`, `B` comes first.
-   If `A.key1 == B.key1`, compare `A.key2` and `B.key2`.
    -   We want `key2` ascending.
    -   If `A.key2 < B.key2`, `A` comes first.
    -   If `A.key2 > B.key2`, `B` comes first.
-   If both keys are equal, we consider them "equal" for the sorting algorithm.

### 2. Stability
-   A sorting algorithm is **stable** if equal elements appear in the sorted output in the same order as they appeared in the input.
-   Most built-in sort functions in modern languages (Java `Arrays.sort` for Objects, Python `sort`, C++ `stable_sort`, JS `sort`) are stable or have stable variants.
-   However, C++ `std::sort` is **not** guaranteed to be stable. You must use `std::stable_sort`.
-   Java's `Arrays.sort` for primitives is not stable (Dual-Pivot Quicksort), but for Objects (TimSort) it is stable. Since we are sorting records (arrays or objects), it will be stable.

### 3. Custom Comparator
-   We need to define a comparator function that implements the logic from step 1.
-   Comparator `cmp(A, B)`:
    -   `if A[0] != B[0] return A[0] - B[0]`
    -   `else return A[1] - B[1]` (ascending order for key2)

## Approaches

### Approach 1: Built-in Stable Sort with Comparator
-   Use the language's built-in stable sort.
-   Define a custom comparator.
-   Complexity: `O(N log N)` time, `O(N)` or `O(log N)` space depending on implementation.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int[][] stableSort(int[][] records) {
        // Java's Arrays.sort for objects (int[]) is stable (TimSort)
        Arrays.sort(records, (a, b) -> {
            if (a[0] != b[0]) {
                return Integer.compare(a[0], b[0]);
            } else {
                return Integer.compare(a[1], b[1]); // Ascending for key2
            }
        });
        return records;
    }
}
```

### Python

```python
def stable_sort(records: list[list[int]]) -> list[list[int]]:
    # Python's sort is stable (Timsort)
    # Sort by key1 ascending, then key2 ascending
    records.sort(key=lambda x: (x[0], x[1]))
    return records

def main():
    n = int(input())
    records = []
    for _ in range(n):
        k1, k2 = map(int, input().split())
        records.append([k1, k2])

    result = stable_sort(records)
    for k1, k2 in result:
        print(k1, k2)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> stableSort(vector<vector<int>> records) {
        // C++ std::sort is NOT stable. Use std::stable_sort.
        stable_sort(records.begin(), records.end(), [](const vector<int>& a, const vector<int>& b) {
            if (a[0] != b[0]) {
                return a[0] < b[0];
            }
            return a[1] < b[1]; // Ascending for key2
        });
        return records;
    }
};
```

### JavaScript

```javascript
class Solution {
  stableSort(records) {
    // JavaScript's sort is stable (since ES2019)
    records.sort((a, b) => {
      if (a[0] !== b[0]) {
        return a[0] - b[0];
      }
      return a[1] - b[1]; // Ascending for key2
    });
    return records;
  }
}
```

## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
`3`
`1 2`
`1 1`
`0 9`

1.  **Comparisons**:
    -   `(1, 2)` vs `(1, 1)`: Key1 equal. Key2 `2 > 1`. So `(1, 1)` comes before `(1, 2)`.
    -   `(1, 1)` vs `(0, 9)`: Key1 `1 > 0`. So `(0, 9)` comes before `(1, 1)`.
2.  **Sorting**:
    -   `(0, 9)` is smallest (Key1=0).
    -   `(1, 1)` is next (Key1=1, Key2=1).
    -   `(1, 2)` is last (Key1=1, Key2=2).
3.  **Result**:
    -   `0 9`
    -   `1 1`
    -   `1 2`

## Proof of Correctness

-   **Primary Key**: The comparator checks `key1` first. This ensures groups are ordered by `key1`.
-   **Secondary Key**: Within equal `key1`, it checks `key2` ascending. This ensures correct sub-ordering.
-   **Stability**: By using a stable sort algorithm, any records with equal `key1` AND equal `key2` will remain in their original relative order.

## Interview Extensions

1.  **What if the language doesn't have a stable sort?**
    -   You can augment the records to include their original index: `(key1, key2, original_index)`.
    -   Then sort by `(key1, key2, original_index)`. This makes every element unique and enforces stability manually.
2.  **Radix Sort?**
    -   You can use Radix Sort for linear time sorting `O(N)`.
    -   Sort by `key2` ascending first (stable).
    -   Then sort by `key1` ascending (stable).
    -   This works because the second sort preserves the relative order established by the first sort for equal primary keys.

### Common Mistakes

-   **Using Unstable Sort**: In C++, using `std::sort` instead of `std::stable_sort` will fail stability tests.
-   **Comparator Logic**: Ensuring the correct order for both keys (ascending for both key1 and key2).
-   **Integer Overflow**: In Java/C++, `a[0] - b[0]` can overflow if values are close to `Integer.MIN_VALUE` and `Integer.MAX_VALUE`. Use `Integer.compare` or explicit `<` checks.
