---
problem_id: ARR_ZERO_SLIDE_LIMIT__4908
display_id: ARR-006
slug: zero-slide-limit
title: "Zero Slide With Limit"
difficulty: Easy-Medium
difficulty_score: 34
topics:
  - Arrays
  - Two Pointers
  - Simulation
tags:
  - arrays
  - two-pointers
  - simulation
  - easy-medium
premium: true
subscription_tier: basic
---

# ARR-006: Zero Slide With Limit

## 📋 Problem Summary

Move all zeros to the end of the array (or equivalently, move all non-zeros to the front) while maintaining the relative order of non-zero elements. You must stop if you reach the limit of `m` swaps.

## 🌍 Real-World Scenario

**Scenario Title:** The Library Shelf Organizer

You are a librarian organizing a shelf. "Zeros" represent empty gaps between books. "Non-zeros" are the books.
You want to push all books to the left to close the gaps and make space at the end.
However, moving a book takes effort. You only have enough energy for `m` "moves" (swaps).

- You scan from left to right.
- Whenever you see a book that has gaps to its left, you move it to the leftmost available gap.
- If you run out of energy (`m` moves), you stop working immediately, leaving the rest of the shelf as is.

**Why This Problem Matters:**

- **Garbage Collection**: Compacting memory involves moving "live" objects to one end and leaving "free" space at the other. Budgeting operations is akin to real-time GC limits.
- **Data Stream Processing**: Filtering nulls/invalid packets with limited CPU cycles per frame.
- **Partitions**: A variation of the partition step in QuickSort.

![Real-World Application](../images/ARR-006/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Sliding Books

```
Shelf:   [0]   [4]   [0]   [5]   [7]
          ^     ^
        Gap    Book

Action: Move [4] to Gap [0]. Cost 1 swap.
Result:  [4]   [0]   [0]   [5]   [7]

Energy Limit m=1. STOP.
Final:   [4]   [0]   [0]   [5]   [7]
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Swap Definition**: Swapping `arr[i]` (non-zero) with `arr[j]` (zero) counts as **1** swap, regardless of the distance between `i` and `j`. (It is a direct memory swap, not bubbling).
- **Self-Swaps**: If a non-zero element is already in the correct position (no zeros to its left), it stays there. This costs 0 swaps.
- **Order**: Relative order of non-zeros must be preserved.

Common interpretation mistake:

- ❌ "Bubbling" the non-zeros (swapping adjacent elements). This is O(N²) and counts differently.
- ✅ Direct swap to the `write` pointer. This is O(N).

### Core Concept: Two Pointers (Read/Write)

We maintain two pointers:

1. `write_idx`: The position where the next non-zero element SHOULD go.
2. `read_idx`: The current element we are inspecting.

### Why Naive Approach is too slow

A "Bubble push" strategy where we swap zeros repeatedly with right-neighbors is O(N²). For N=200,000, this times out. We need a linear pass.

## Naive Approach

### Intuition

Iterate through array. If `arr[i] == 0` and `arr[i+1] != 0`, swap them. Repeat until no zeros are left of non-zeros or limit reached.

### Algorithm

1. Repeat loop:
   - Scan whole array.
   - Swap adjacent `0, non-zero` pair.
   - Decrement `m`.
2. Stop if sorted or `m=0`.

### Time Complexity

- **O(N²)**: Worst case (all zeros at start, all numbers at end).

### Space Complexity

- **O(1)**.

## Optimal Approach (Writer Pointer)

### Key Insight

We don't need to bubble. We know exactly where the next non-zero goes: the first available '0' (or the current position if no zeros passed yet).
`write_idx` tracks the boundary of the "compacted" prefix.

### Algorithm

1. Initialize `write_idx = 0`.
2. Iterate `read_idx` from 0 to `n-1`.
3. If `arr[read_idx]` is non-zero:
   - Check if we need to move it (`read_idx > write_idx`).
   - If yes:
     - Check if `m > 0`.
     - If `m == 0`, break (cannot perform needed swap).
     - Swap `arr[read_idx]` and `arr[write_idx]`.
     - Decrement `m`.
   - Increment `write_idx` (slot filled).
4. Return modified `arr`.

### Time Complexity

- **O(N)**: Single pass.

### Space Complexity

- **O(1)**: In-place.

### Why This Is Optimal

We traverse the array once. Each element is written at most once.

![Algorithm Visualization](../images/ARR-006/algorithm-visualization.png)
![Algorithm Steps](../images/ARR-006/algorithm-steps.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    public int[] zeroSlideWithLimit(int[] arr, int m) {
        int n = arr.length;
        int writeIdx = 0;

        for (int readIdx = 0; readIdx < n; readIdx++) {
            if (arr[readIdx] != 0) {
                // If needs to move (i.e., there are zeros behind/writeIdx is behind)
                if (readIdx != writeIdx) {
                    if (m <= 0) break; // Limit reached

                    // Swap
                    int temp = arr[writeIdx];
                    arr[writeIdx] = arr[readIdx];
                    arr[readIdx] = temp;

                    m--;
                }
                writeIdx++;
            }
        }
        return arr;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int m = sc.nextInt();

        Solution solution = new Solution();
        int[] result = solution.zeroSlideWithLimit(arr, m);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(result[i]).append(i == n - 1 ? "" : " ");
        }
        System.out.println(sb);
        sc.close();
    }
}
```

### Python
```python
import sys

def zero_slide_with_limit(arr: list[int], m: int) -> list[int]:
    """
    Move zeros to end with swap limit.
    """
    n = len(arr)
    write_idx = 0

    for read_idx in range(n):
        if arr[read_idx] != 0:
            if read_idx != write_idx:
                if m <= 0:
                    break
                # Swap
                arr[write_idx], arr[read_idx] = arr[read_idx], arr[write_idx]
                m -= 1
            write_idx += 1

    return arr

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())

    result = zero_slide_with_limit(arr, m)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
```

### C++
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> zeroSlideWithLimit(vector<int>& arr, int m) {
        int n = arr.size();
        int writeIdx = 0;

        for (int readIdx = 0; readIdx < n; readIdx++) {
            if (arr[readIdx] != 0) {
                if (readIdx != writeIdx) {
                    if (m <= 0) break;

                    swap(arr[writeIdx], arr[readIdx]);
                    m--;
                }
                writeIdx++;
            }
        }
        return arr;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];

    int m;
    cin >> m;

    Solution solution;
    vector<int> result = solution.zeroSlideWithLimit(arr, m);

    for (int i = 0; i < n; i++) {
        cout << result[i] << (i == n - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class Solution {
  zeroSlideWithLimit(arr, m) {
    const n = arr.length;
    let writeIdx = 0;

    for (let readIdx = 0; readIdx < n; readIdx++) {
      if (arr[readIdx] !== 0) {
        if (readIdx !== writeIdx) {
          if (m <= 0) break;

          // Swap
          const temp = arr[writeIdx];
          arr[writeIdx] = arr[readIdx];
          arr[readIdx] = temp;

          m--;
        }
        writeIdx++;
      }
    }
    return arr;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  const tokens = data.join(" ").split(/\s+/);
  if (tokens.length === 0 || tokens[0] === "") return;

  let ptr = 0;
  const n = Number(tokens[ptr++]);
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(Number(tokens[ptr++]));

  const m = Number(tokens[ptr++]);

  const solution = new Solution();
  const result = solution.zeroSlideWithLimit(arr, m);
  console.log(result.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `arr=[0, 4, 0, 5, 7]`, `m=1`

1. **Init**: `write=0`, `read=0`.

   - `arr[0]` is 0. Skip.

2. **Read=1**: `arr[1]` is 4.

   - `read(1) != write(0)`.
   - `m(1) > 0`. Swap `arr[0], arr[1]`.
   - Arr: `[4, 0, 0, 5, 7]`.
   - `m` becomes 0.
   - `write` becomes 1.

3. **Read=2**: `arr[2]` is 0. Skip.

4. **Read=3**: `arr[3]` is 5.
   - `read(3) != write(1)`.
   - `m(0) <= 0`. **BREAK**.

**Output**: `[4, 0, 0, 5, 7]`. Matches Example.

![Example Visualization](../images/ARR-006/example-1.png)

## ✅ Proof of Correctness

### Invariant

`arr[0...writeIdx-1]` contains the compacted non-zero elements encountered so far in relative order. `m` is decremented exactly when a non-zero is moved into a gap (where `gap` is defined by `writeIdx` effectively pointing to a zero or a position that _was_ a zero before a swap).

### Why the approach is correct

The algorithm greedily moves the leftmost available non-zeros to the leftmost available zero-slots. This compaction order is unique and maintains stability. The limit `m` strictly bounds the number of write operations that cross a gap.

## 💡 Interview Extensions (High-Value Add-ons)

- **Snowball Method**: (The one explained here).
- **Minimum Swaps**: What if we want to minimize writes? (A: This greedy approach already minimizes moves for a stable sort with 0).
- **Large M**: If `m >= n`, this becomes the standard Move Zeroes problem.

## Common Mistakes to Avoid

1. **Swapping 0 with 0**:

   - ❌ Swapping when `arr[read] == 0`.
   - ✅ Only act when `arr[read] != 0`.

2. **Counting Self-Swaps**:

   - ❌ Decrementing `m` when `read == write`.
   - ✅ If `read == write`, the element is already in place. No "move" occurred. `m` stays same.

3. **Continuing after M=0**:
   - ❌ Forgetting to break.
   - ✅ Stop immediately.

## Related Concepts

- **Stable Partition**: Separating array into two groups while keeping order.
- **Two Pointers**: Standard Read/Write pattern.
