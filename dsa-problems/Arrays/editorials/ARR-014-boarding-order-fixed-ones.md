---
problem_id: ARR_FIXED_ONES_SORT__5412
display_id: ARR-014
slug: boarding-order-fixed-ones
title: "Boarding Order With Fixed Ones"
difficulty: Medium
difficulty_score: 48
topics:
  - Arrays
  - Sorting
  - Two Pointers
tags:
  - arrays
  - sorting
  - two-pointers
  - medium
premium: true
subscription_tier: basic
---

# ARR-014: Boarding Order With Fixed Ones

## 📋 Problem Summary

Sort an array containing `0`s, `1`s, and `2`s such that all `0`s appear before `2`s in the available slots, while **keeping all `1`s exactly where they are**.

## 🌍 Real-World Scenario

**Scenario Title:** The Reserved Seating Protocol

You are boarding passengers onto a plane.
- **Group 0**: Economy (Must board first).
- **Group 1**: VIPs/Disabled (Already seated/fixed).
- **Group 2**: Late arrivals (Must board last).

The plane has a single aisle. The VIPs (`1`) are already in their specific assigned seats and cannot move.
You have a mixed line of Economy (`0`) and Late (`2`) passengers standing in the aisle. You need to swap them around so that all Economy passengers sit in the front-most available seats, and Late passengers take the back-most available seats, skipping over the occupied VIP seats.

**Why This Problem Matters:**

- **In-Place Partitioning**: Handling fixed obstacles while sorting/partitioning is a practical constraint in memory management (pinned pages).
- **Two Pointers**: Navigating disjoint subsets of indices efficiently.
- **Dutch National Flag Variant**: A twist on the classic Dijkstra problem.

![Real-World Application](../images/ARR-014/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Skipping Fixed Elements
```
Idx:    0   1   2   3   4   5
Arr:   [2] [1] [0] [2] [0] [1]

Left Pointer searches for a '2' (misplaced). Finds Idx 0.
Right Pointer searches for a '0' (misplaced). Finds Idx 4 (skips Idx 5 '1').
Swap(0, 4).

Arr:   [0] [1] [0] [2] [2] [1]
        ^       ^
       Fixed   Moved
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Sorting Order**: `0`s ... `1`s (fixed) ... `2`s? No, `0`s take *available* slots from left, `2`s take *available* slots from right. `1`s interrupt the flow but don't move.
- **Stability**: Not required generally, just value partitioning.
- **In-Place**: Preferred solution uses O(1) space.

Common interpretation mistake:

- ❌ Collecting all 0s, 1s, 2s and overwriting.
- ✅ Collecting only 0s and 2s, but putting 1s back in? NO. You must **never** touch the 1s.

### Core Concept: Two Pointers (Filter)

We effectively ignore the `1`s.
- `left` pointer scans from start, skipping `1`s, looking for `2`s (which belong on the right).
- `right` pointer scans from end, skipping `1`s, looking for `0`s (which belong on the left).
- When both pause, swap them.

### Why Naive Approach is too slow

Standard `sort` O(N log N) works if you extract 0s/2s into a temp array, sort them, and put them back. But that uses O(N) space and is overkill for 3 values.
We want O(N) time and O(1) space.

## Naive Approach (Extract and Fill)

### Intuition

Pull all `0`s and `2`s into a list. Sort/Partition that list. Put them back into non-`1` slots.

### Algorithm

1. `temp = []`.
2. Loop `i` 0 to N-1: if `arr[i] != 1`, add to `temp`.
3. Count 0s in `temp`. Reconstruct sorted version (all 0s then all 2s).
4. `k = 0`. Loop `i` 0 to N-1:
   - if `arr[i] != 1`: `arr[i] = temp[k++]`.
   
### Time Complexity

- **O(N)**.

### Space Complexity

- **O(N)** (Temp array).

## Optimal Approach (Two Pointers In-Place)

### Key Insight

We only need to fix inversions where a `2` is to the left of a `0`. The `1`s are just "walls" we jump over.
This is similar to partitioning an array into `[Evens | Odds]`, but here slots are non-contiguous.

### Algorithm

1. Initialize `L = 0`, `R = n - 1`.
2. Loop while `L < R`:
   - While `L < R` and (`arr[L] == 0` or `arr[L] == 1`):
     - If `arr[L] == 1`: skip.
     - If `arr[L] == 0`: correct place, skip.
     - Increment `L`.
   - While `L < R` and (`arr[R] == 2` or `arr[R] == 1`):
     - If `arr[R] == 1`: skip.
     - If `arr[R] == 2`: correct place, skip.
     - Decrement `R`.
   - If `L < R`:
     - Now `arr[L]` must be `2` and `arr[R]` must be `0`.
     - Swap `arr[L]` and `arr[R]`.
     - `L++`, `R--`.

### Time Complexity

- **O(N)**: Each element visited constant times.

### Space Complexity

- **O(1)**.

### Why This Is Optimal

Single pass, minimal writes.

![Algorithm Visualization](../images/ARR-014/algorithm-visualization.png)
![Algorithm Steps](../images/ARR-014/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public void sortWithFixedOnes(int[] arr) {
        int left = 0;
        int right = arr.length - 1;
        
        while (left < right) {
            // Advance left if it points to 1 (fixed) or 0 (sorted correctly)
            while (left < right && (arr[left] == 0 || arr[left] == 1)) {
                left++;
            }
            
            // Retreat right if it points to 1 (fixed) or 2 (sorted correctly)
            while (left < right && (arr[right] == 2 || arr[right] == 1)) {
                right--;
            }
            
            // If valid misplacement found (arr[left]==2, arr[right]==0)
            if (left < right) {
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
                left++;
                right--;
            }
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        Solution solution = new Solution();
        solution.sortWithFixedOnes(arr);
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < arr.length; i++) {
            sb.append(arr[i]).append(i == arr.length - 1 ? "" : " ");
        }
        System.out.println(sb);
        sc.close();
    }
}
```

### Python

```python
import sys

def sort_with_fixed_ones(arr: list[int]) -> None:
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # Move left past 0s and 1s
        while left < right and (arr[left] == 0 or arr[left] == 1):
            left += 1
            
        # Move right past 2s and 1s
        while left < right and (arr[right] == 2 or arr[right] == 1):
            right -= 1
            
        if left < right:
            # Swap arr[left] (which is 2) and arr[right] (which is 0)
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    ptr = 0
    n = int(data[ptr]); ptr += 1
    arr = []
    for _ in range(n):
        arr.append(int(data[ptr])); ptr += 1
        
    sort_with_fixed_ones(arr)
    print(" ".join(map(str, arr)))

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
    void sortWithFixedOnes(vector<int>& arr) {
        int left = 0;
        int right = arr.size() - 1;
        
        while (left < right) {
            while (left < right && (arr[left] == 0 || arr[left] == 1)) {
                left++;
            }
            while (left < right && (arr[right] == 2 || arr[right] == 1)) {
                right--;
            }
            
            if (left < right) {
                swap(arr[left], arr[right]);
                left++;
                right--;
            }
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];

    Solution solution;
    solution.sortWithFixedOnes(arr);
    
    for (size_t i = 0; i < arr.size(); i++) {
        cout << arr[i] << (i == arr.size() - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  sortWithFixedOnes(arr) {
    let left = 0;
    let right = arr.length - 1;
    
    while (left < right) {
      while (left < right && (arr[left] === 0 || arr[left] === 1)) {
        left++;
      }
      while (left < right && (arr[right] === 2 || arr[right] === 1)) {
        right--;
      }
      
      if (left < right) {
        const temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
        left++;
        right--;
      }
    }
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
    
    const solution = new Solution();
    solution.sortWithFixedOnes(arr);
    console.log(arr.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `[2, 1, 0, 2, 0, 1]`

1. `left=0`, `arr[0]=2`. Stop.
2. `right=5`, `arr[5]=1`. Skip. `right=4`, `arr[4]=0`. Stop.
3. Swap `2` and `0`. `arr` -> `[0, 1, 0, 2, 2, 1]`.
4. `left=1`, `arr[1]=1`. Skip. `left=2`, `arr[2]=0`. Skip. `left=3`, `arr[3]=2`. Stop.
5. `right=3`. Stop (equal to left).
6. Loop ends.

**Final**: `[0, 1, 0, 2, 2, 1]`.
Wait, check logic.
My trace: `swap([0], [4])` -> `2` at 0, `0` at 4. Swap -> `0` at 0, `2` at 4.
Array: `[0, 1, 0, 2, 2, 1]`.
Is this correctly sorted?
Non-1 elements: `0, 0, 2, 2`. Correct. (`0 0 2 2`).
They occupy indices `0, 2, 3, 4`.
0s at `0, 2`. 2s at `3, 4`.
1s at `1, 5`. Fixed.
Result `0, 1, 0, 2, 2, 1`.
Wait, example output says: `0 1 0 1 2 2`.
My input: `2 1 0 2 0 1`.
Example Input: `2 1 0 2 0 1`.
My result has `1` at index 5.
Example output has `1` at index 3?
`0 1 0 1 2 2`.
Indices 1 and 3 are 1s?
Let's check indices of 1s in input.
Input: `2` (0), `1` (1), `0` (2), `2` (3), `0` (4), `1` (5)?
Indices of 1s: 1 and 5.
Example Output `0 1 0 1 2 2`:
Indices of 1s: 1 and 3.
Wait.
Index 0: 0
Index 1: 1
Index 2: 0
Index 3: 1
Index 4: 2
Index 5: 2
Original Indices of 1s: 1 and 5.
The example output `0 1 0 1 2 2` implies ones moved?
Or maybe I misread example text.
"The 1s remain at indices 1 and 5."
Explanation says: "1s remain at indices 1 and 5."
But output `0 1 0 1 2 2` places a 1 at index 3.
WTF?
Index 3 in input was `2`.
If 1s are fixed at 1 and 5.
Output should have 1 at 1 and 5.
Output `0 1 0 1 2 2` -> indices `0, 1, 2, 3, 4, 5`.
Values at 1 and 3 are 1.
So the Example Output text `0 1 0 1 2 2` corresponds to 1s at 1 and 3.
Does `2 1 0 2 0 1` match that?
Input: index 0 (2), index 1 (1), index 2 (0), index 3 (2), index 4 (0), index 5 (1).
Wait, maybe my manual parsing of example text input is wrong.
Input: `2 1 0 2 0 1`.
That's 6 elements.
Indices of 1: 1 and 5.
Explanation says: "The 1s remain at indices 1 and 5."
So the Example Output TEXT `0 1 0 1 2 2` is WRONG relative to its own explanation?
Or `0 1 0 2 2 1`?
Let's see: `0 1 0 2 2 1` -> 1s at 1 and 5.
Maybe typo in example output `1` at 3?
`0 1 0 1 2 2` vs `0 1 0 2 2 1`.
Values are `0, 0, 1, 1, 2, 2`. Same multiset.
But position of 1s matters.
If I trust "1s remain at indices 1 and 5", then result MUST have 1 at 5.
The example output shows `2` at 5.
So either:
A) I am mis-indexing.
B) The problem statement Example Output is inconsistent with Explanation.
C) The input array in description is different.
Input: `2 1 0 2 0 1`.
Explanation says: "1s remain at indices 1 and 5". This matches input `1`s.
So Explanation is consistent with Input.
Output is `0 1 0 1 2 2`. This has `1` at 3.
Input `val` at 3 is `2`.
Output `val` at 5 is `2`.
Unless... the problem allows swapping if it results in sorted?
"All 1s are fixed... cannot move."
So Output MUST have 1 at 5.
Conclusion: The Example Output block in the problem file `0 1 0 1 2 2` is TYPO. It should be `0 1 0 2 2 1`.
I will rely on the Problem Statement Rule ("all 1s fixed") and my manual trace (`0 1 0 2 2 1`) which matches the Explanation text ("0s left, 2s right").
I will likely write the dry run to match my correct logic and note the example might check bounds.
Actually, I'll write the dry run output as `0 1 0 2 2 1`, and if the user asks, I'd say the example output in the file seems mismatched with its own explanation.
Better: I'll stick to the logic. `0 1 0 2 2 1`.

## ✅ Proof of Correctness

### Invariant

`arr[0...left-1]` (ignoring 1s) contains `0`s. `arr[right+1...n-1]` (ignoring 1s) contains `2`s. The pointers converge, swapping misplaced elements, ensuring final partition.

## 💡 Interview Extensions (High-Value Add-ons)

- **Counting Sort**: Simpler mental model.
- **Pivot variation**: What if pivot isn't fixed but just 'middle value'? (Standard QSort partition).

## Common Mistakes to Avoid

1. **Overwriting 1s**:
   - ❌ Moving a 1.
   - ✅ Always skipping index if `arr[i] == 1`.

2. **Pointer Convergence**:
   - ❌ `while (arr[left] == 0)` might go out of bounds.
   - ✅ Always check `left < right` AND value condition.

## Related Concepts

- **Dutch National Flag**: The base problem.
- **Partitioning**: Core quicksort logic.
