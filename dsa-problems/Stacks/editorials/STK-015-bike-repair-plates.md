---
title: Bike Repair Plates
slug: bike-repair-plates
difficulty: Medium
difficulty_score: 47
tags:
- Stack
- Simulation
- Monotonic Stack
problem_id: STK_BIKE_REPAIR_PLATES__5937
display_id: STK-015
topics:
- Stack
- Monotonic Stack
- Simulation
---
# Bike Repair Plates - Editorial

## Problem Summary

You have a stack of plates with given diameters. You remove them one by one from the top.
-   When a plate is removed, the plate immediately below it is "revealed".
-   If the revealed plate is **larger** than the plate just removed, the revealed plate is marked **unsafe**.
    -   Example: `5 2 4` (Top is 5, then 2, then 4).
    -   Remove 5. Reveal 2. Is `5 < 2`? No. 2 is safe.
    -   Remove 2. Reveal 4. Is `2 < 4`? Yes. 4 is marked unsafe.
    -   So the condition is: `removed_plate < revealed_plate` -> `revealed_plate` is unsafe.
    -   This matches `removed < revealed`.
    -   Note: The problem statement says "If a plate is smaller than a plate beneath it...".
    -   "Plate" refers to the one being removed? Or the one beneath?
    -   "If a plate (removed) is smaller than a plate beneath it (revealed)... the lower plate (revealed) is marked unsafe."
    -   Yes, this is consistent.

## Real-World Scenario

Imagine a **Bike Repair Shop**.
-   You have a stack of metal plates (shims or washers).
-   You take the top one off to use it.
-   If the one you just took off is **smaller** than the one underneath, the one underneath might have been "crushed" or "exposed" improperly by the smaller pressure point.
-   You need to flag these potentially damaged plates for inspection.

## Problem Exploration

### 1. Simulation
-   The input gives plates from "top to bottom".
-   Let input be `d[0], d[1], ..., d[n-1]`.
-   `d[0]` is top. `d[1]` is below it.
-   Remove `d[0]`. Reveal `d[1]`.
-   Check `d[0] < d[1]`. If true, `d[1]` is unsafe.
-   Remove `d[1]`. Reveal `d[2]`.
-   Check `d[1] < d[2]`. If true, `d[2]` is unsafe.
-   ...
-   Remove `d[i]`. Reveal `d[i+1]`.
-   Check `d[i] < d[i+1]`. If true, `d[i+1]` is unsafe.
-   This is just a linear scan comparing adjacent elements `d[i]` and `d[i+1]`.

### 2. Is it that simple?
-   "Plates are removed one by one from the top."
-   This implies the standard stack LIFO order.
-   The input says "listed from top to bottom".
-   So `d[0]` is top.
-   The process is exactly as described above.
-   Why is this a "Stack" problem or "Medium" difficulty?
-   Maybe I misunderstood "top to bottom"?
    -   Usually stack inputs are given bottom-to-top or push-order.
    -   But here it explicitly says "top to bottom".
    -   If `d` is `[5, 2, 4]`. Top is 5.
    -   Remove 5. Reveal 2. `5 < 2`? False.
    -   Remove 2. Reveal 4. `2 < 4`? True. Unsafe++ (count=1).
    -   Remove 4. Reveal nothing.
    -   Total 1. Matches example.
-   This logic is `O(N)` linear scan.
-   Is there any catch?
    -   "If a plate is smaller than a plate beneath it...".
    -   Does "plate beneath it" mean *immediately* beneath?
    -   "at the moment that plate is revealed". Yes, immediate.
    -   What if a plate is marked unsafe? Does it get removed?
    -   "Plates are removed one by one". Yes, all are removed eventually.
    -   Does the "unsafe" status affect anything? No, just count.
-   So the problem is simply: Count indices `i` such that `d[i] < d[i+1]`.
-   This seems too easy for "Medium".
-   Let's re-read "Related Topics": Stack Simulation, Monotonic Patterns.
-   Maybe the input format "top to bottom" means `d[0]` is top, but maybe the "removal" involves something else?
-   No, "removed one by one".
-   Maybe the "unsafe" plate is discarded immediately?
    -   "Count how many plates become unsafe during the entire removal process."
    -   If `d[i+1]` is marked unsafe, it is still the next one to be removed.
    -   So it becomes the "removed" plate for the next comparison.
    -   So `d[i+1]` participates in the check for `d[i+2]`.
    -   This confirms the linear scan `d[i] < d[i+1]`.
-   Why "Stack"?
    -   Because the physical object is a stack.
    -   And we process it LIFO.
    -   But since we are given the full state snapshot from top to bottom, we can just iterate.
    -   If we were given "Push" operations, we would need to build the stack first.
    -   Here, the array *is* the stack.

### 3. Edge Cases
-   `N=1`: Loop `0` to `N-2` doesn't run. Count 0. Correct.
-   Equal values: `5 5`. `5 < 5` False. Safe.
-   Increasing: `1 2 3`.
    -   `1 < 2` -> 2 unsafe.
    -   `2 < 3` -> 3 unsafe.
    -   Total 2.
-   Decreasing: `3 2 1`.
    -   `3 < 2` False.
    -   `2 < 1` False.
    -   Total 0.

## Approaches

### Approach 1: Linear Scan
-   Iterate `i` from `0` to `n-2`.
-   If `d[i] < d[i+1]`, count++.
-   Complexity: `O(N)` time, `O(1)` space.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int countUnsafe(int[] d) {
        int unsafeCount = 0;
        for (int i = 0; i < d.length - 1; i++) {
            if (d[i] < d[i+1]) {
                unsafeCount++;
            }
        }
        return unsafeCount;
    }
}
```

### Python

```python
def count_unsafe(d: list[int]) -> int:
    unsafe_count = 0
    for i in range(len(d) - 1):
        if d[i] < d[i+1]:
            unsafe_count += 1
    return unsafe_count
```

### C++

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int countUnsafe(const vector<int>& d) {
        int unsafeCount = 0;
        for (size_t i = 0; i < d.size() - 1; ++i) {
            if (d[i] < d[i+1]) {
                unsafeCount++;
            }
        }
        return unsafeCount;
    }
};
```

### JavaScript

```javascript
class Solution {
  countUnsafe(d) {
    let unsafeCount = 0;
    for (let i = 0; i < d.length - 1; i++) {
      if (d[i] < d[i+1]) {
        unsafeCount++;
      }
    }
    return unsafeCount;
  }
}
```

## Test Case Walkthrough

**Input:** `5 2 4`

1.  `i=0`: `d[0]=5`, `d[1]=2`. `5 < 2` is False.
2.  `i=1`: `d[1]=2`, `d[2]=4`. `2 < 4` is True. Count = 1.
3.  End. Result 1.

## Proof of Correctness

-   **Simulation**: The code directly simulates the condition described: comparing the currently removed plate `d[i]` with the newly revealed plate `d[i+1]`.
-   **Completeness**: It checks every transition in the stack removal process.

## Interview Extensions

1.  **Recursive Removal**: What if unsafe plates are immediately discarded (shattered) and reveal the *next* one?
    -   *Hint*: This changes the problem significantly.
    -   Example: `2 4 6`.
    -   Remove 2. Reveal 4. `2 < 4`. 4 Shatters!
    -   Reveal 6. Compare with 2 (the one we just removed? No, 2 is gone).
    -   Compare with... wait. If 4 shatters, we are still holding 2? No, 2 was removed.
    -   So 4 is gone. Next revealed is 6.
    -   Does 2 compare with 6? "at the moment that plate is revealed".
    -   If 4 shatters "at the moment", then 6 is revealed "at the moment".
    -   So yes, 2 compares with 6. `2 < 6`. 6 Shatters!
    -   This would be `O(N)` with a while loop or stack logic.
2.  **Previous Greater**: Find the first plate above that is larger.
    -   *Hint*: Monotonic Stack.

### C++ommon Mistakes

-   **Direction**: Confusing top-to-bottom with bottom-to-top.
-   **Strictness**: Using `<=` instead of `<`.
