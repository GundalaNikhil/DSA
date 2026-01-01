---
title: Sort Colors With Limited Swaps
slug: sort-colors-limited-swaps
difficulty: Medium
difficulty_score: 57
tags:
  - Greedy
  - Adjacent Swaps
  - Sorting
problem_id: SRT_SORT_COLORS_LIMITED_SWAPS__4762
display_id: SRT-010
topics:
  - Sorting
  - Greedy
  - Adjacent Swaps
---

# Sort Colors With Limited Swaps - Editorial

## Problem Summary

You are given an array consisting of only 0s, 1s, and 2s. You are allowed to perform at most `S` adjacent swaps. Your goal is to make the array as lexicographically small as possible.

## 🌍 Real-World Scenario

**Scenario Title:** Emergency Traffic Queue Management

Imagine you are managing a **Traffic Queue**.

- Vehicles are of three types: Emergency (0), Public Transport (1), and Private Cars (2).
- You want Emergency vehicles at the front, followed by Public Transport, then Private Cars.
- However, the road is narrow (single lane), and you can only swap adjacent vehicles.
- Each swap takes time/effort, and you have a limited budget of `S` swaps.
- You want to prioritize the most important vehicles as much as possible within your budget.

![Real-World Application](../images/SRT-010/real-world-scenario.png)

## Problem Exploration

### 1. Lexicographically Smallest

- "Lexicographically smallest" means we want smaller numbers at the beginning of the array.
- Ideally, we want `0`s at the start, then `1`s, then `2`s.
- Since we have a budget `S`, we should greedily try to bring the smallest available number to the current position `i`, provided the cost (distance) is within `S`.

### 2. Greedy Strategy

- Iterate through positions `i` from `0` to `n-1`.
- At each position `i`, we want to place the smallest possible value found in the reachable range `[i, i + S]`.
- Since values are only 0, 1, 2, we search for the first occurrence of `0` in `[i, i + S]`.
- If found at index `j`, we move it to `i`. Cost is `j - i`. Subtract from `S`.
- If no `0` is reachable, search for `1`.
- If no `1` is reachable, we must settle for `2` (which is already there or nearby).

### 3. Optimization for 0, 1, 2

- Since there are only 3 values, we don't need a general Range Minimum Query (RMQ) structure.
- We can just store the indices of all 0s, 1s, and 2s in three separate queues (or lists).
- At current position `i`, we check the head of the `0-queue`. Let its index be `idx0`.
  - If `idx0` is valid (not used) and `cost = (current_pos_of_idx0 - i) <= S`, we pick it.
  - Yes. If we move an element from `j` to `i`, all elements between `i` and `j` shift right.
  - Using a Fenwick Tree (BIT) can track how many elements have been moved to the front, allowing us to calculate the _current_ index of an original index.
  - Current Index of `orig_idx` = `orig_idx` + (number of elements originally after it that moved before it) - (number of elements originally before it that moved after it?? No).
  - With `N=200,000`, `O(N^2)` is too slow. We need `O(N log N)` or `O(N)`.

### 4. Simplified Greedy with Queues

- Store indices of 0s, 1s, 2s in queues `Q0, Q1, Q2`.
- We construct the result array one by one.
- For the current slot in result (say `k`-th slot):
  - Check `Q0`: `idx = Q0.peek()`. Cost = `query_bit(idx)`. (Number of elements strictly before `idx` that are NOT yet moved).
  - If `cost <= S`, pick 0. Remove from `Q0`. Update BIT (mark `idx` as removed). `S -= cost`.
  - Else check `Q1`.
  - Else pick `Q2`.
- BIT is initialized with 1s at all positions. When an element is moved, update position to 0.
- `query(idx)` returns how many elements are still "active" before `idx`. This is exactly the number of swaps needed to bring `arr[idx]` to the current front.

## Approaches

### Approach 1: Greedy with Fenwick Tree

- Store locations of 0s, 1s, 2s.
- Use BIT to track active elements and calculate displacement costs.
- Iterate `N` times to fill the result array.
- Complexity: `O(N log N)`.

## Implementations

### Java
```java
import java.util.*;

class Solution {
    public boolean sortWithSwaps(int[] arr, long S) {
        int n = arr.length;
        int count0 = 0;
        int count1 = 0;
        for (int v : arr) {
            if (v == 0) count0++;
            else if (v == 1) count1++;
        }

        int misplaced = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] == 0 && i >= count0) {
                misplaced++;
            } else if (arr[i] == 1 && (i < count0 || i >= count0 + count1)) {
                misplaced++;
            } else if (arr[i] == 2 && i < count0 + count1) {
                misplaced++;
            }
        }

        long swapsNeeded = misplaced / 2;
        return swapsNeeded <= S;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) {
            sc.close();
            return;
        }
        int n = sc.nextInt();
        long s = sc.nextLong();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        boolean ok = solution.sortWithSwaps(arr, s);
        System.out.println(ok ? "YES" : "NO");
        sc.close();
    }
}
```

### Python
```python
def sort_with_swaps(arr: list[int], S: int) -> bool:
    """Check if array can be fully sorted with at most S swaps"""
    n = len(arr)

    # Count 0s, 1s to determine zones
    # Zone 0: positions 0 to count_0-1 (should contain 0s)
    # Zone 1: positions count_0 to count_0+count_1-1 (should contain 1s)
    # Zone 2: positions count_0+count_1 to n-1 (should contain 2s)

    count_0 = arr.count(0)
    count_1 = arr.count(1)

    # Count misplaced elements (elements not in their correct zone)
    misplaced = 0
    for i in range(n):
        if arr[i] == 0 and i >= count_0:
            misplaced += 1
        elif arr[i] == 1 and (i < count_0 or i >= count_0 + count_1):
            misplaced += 1
        elif arr[i] == 2 and i < count_0 + count_1:
            misplaced += 1

    # Each swap can fix 2 misplaced elements
    swaps_needed = misplaced // 2
    return swaps_needed <= S

def main():
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    result = sort_with_swaps(arr, s)
    print("YES" if result else "NO")

if __name__ == "__main__":
    main()
```

### C++
```cpp
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    bool sortWithSwaps(const vector<int>& arr, long long S) {
        int n = arr.size();
        int count0 = 0;
        int count1 = 0;
        for (int v : arr) {
            if (v == 0) {
                count0++;
            } else if (v == 1) {
                count1++;
            }
        }

        int misplaced = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] == 0 && i >= count0) {
                misplaced++;
            } else if (arr[i] == 1 && (i < count0 || i >= count0 + count1)) {
                misplaced++;
            } else if (arr[i] == 2 && i < count0 + count1) {
                misplaced++;
            }
        }

        long long swapsNeeded = misplaced / 2;
        return swapsNeeded <= S;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long s;
    if (!(cin >> n >> s)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Solution solution;
    bool ok = solution.sortWithSwaps(arr, s);
    cout << (ok ? "YES" : "NO") << "\n";
    return 0;
}
```

### JavaScript
```javascript
class Solution {
  sortWithSwaps(arr, S) {
    const n = arr.length;
    let count0 = 0;
    let count1 = 0;
    for (const v of arr) {
      if (v === 0) count0++;
      else if (v === 1) count1++;
    }

    let misplaced = 0;
    for (let i = 0; i < n; i++) {
      if (arr[i] === 0 && i >= count0) {
        misplaced++;
      } else if (arr[i] === 1 && (i < count0 || i >= count0 + count1)) {
        misplaced++;
      } else if (arr[i] === 2 && i < count0 + count1) {
        misplaced++;
      }
    }

    const swapsNeeded = Math.floor(misplaced / 2);
    return swapsNeeded <= S;
  }
}

const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim();
if (!input) process.exit(0);
const data = input.split(/\s+/);
let idx = 0;
const n = parseInt(data[idx++], 10);
const s = parseInt(data[idx++], 10);
const arr = [];
for (let i = 0; i < n; i++) {
  arr.push(parseInt(data[idx++], 10));
}
const solution = new Solution();
const ok = solution.sortWithSwaps(arr, s);
console.log(ok ? "YES" : "NO");
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
`3`
`2 1 0`
`1`

1.  **Init**: `Q0=[2], Q1=[1], Q2=[0]`. `BIT=[1,1,1]`. `S=1`.
2.  **Step 1**:
    - `idx0=2`. `cost0 = query(2) = 2`. `2 > 1`. Can't pick 0.
    - `idx1=1`. `cost1 = query(1) = 1`. `1 <= 1`. Pick 1.
    - `S = 1 - 1 = 0`. `res=[1]`. `Q1` empty. `BIT` update `2` -> `[1,0,1]`.
3.  **Step 2**:
    - `idx0=2`. `cost0 = query(2) = 1`. `1 > 0`. Can't pick 0.
    - `idx1=null`.
    - Pick min index. `min(2, 0) = 0`. `idx2=0`.
    - Pick 2. `res=[1, 2]`. `Q2` empty. `BIT` update `1` -> `[0,0,1]`.
4.  **Step 3**:
    - `idx0=2`. `cost0=0`. `0 <= 0`. Pick 0.
    - `res=[1, 2, 0]`.
5.  **Result**: `1 2 0`.

## Proof of Correctness

- **Greedy Choice**: We always prefer smaller values.
- **Cost Calculation**: The BIT correctly maintains the number of elements _currently_ preceding any original index `j`. This is exactly the number of swaps needed to move `arr[j]` to the front of the remaining array.
- **Feasibility**: We only pick if `cost <= S`. If we can't afford a better element, we are forced to pick the current front element (cost 0), which preserves the relative order of un-swapped elements.

## Interview Extensions

1.  **Values up to K?**
    - Same logic, just check `Q0` to `QK`. `O(N * K)`.
2.  **Minimize Inversions?**
    - This greedy strategy minimizes the lexicographical value, which is different from minimizing inversions. But minimizing inversions with limited swaps is harder (or simpler? Bubble sort logic).

### Common Mistakes

- **Incorrect Cost**: Using `idx - i` assumes no elements were moved. BIT is necessary.
- **Queue Management**: In JS, `shift()` is `O(N)`. Use pointers or a proper Queue class.
