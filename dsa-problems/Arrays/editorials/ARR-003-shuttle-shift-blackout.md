---
problem_id: ARR_SHUTTLE_SHIFT_BLACKOUT__2845
display_id: ARR-003
slug: shuttle-shift-blackout
title: "Shuttle Shift With Blackout"
difficulty: Easy-Medium
difficulty_score: 32
topics:
  - Arrays
  - Rotation
  - Simulation
tags:
  - arrays
  - rotation
  - simulation
  - easy-medium
premium: true
subscription_tier: basic
---

# ARR-003: Shuttle Shift With Blackout

## 📋 Problem Summary

Perform a **left rotation** of the array by elements, but strictly skip over any indices marked as "blackout". The values at blackout indices do not move, and moving values skip over them as if they didn't exist in the rotation path.

## 🌍 Real-World Scenario

**Scenario Title:** The Factory Coveyor Belt Repair

Imagine a circular conveyor belt assembling products.
Normally, the belt shifts left by `k` steps to move products to the next station.
However, `b` stations are currently **under maintenance** (blackout).
- Products at maintenance stations must NOT move (safety procedure).
- Products at working stations must shift `k` logical steps to the next *working* station, skipping any maintenance stations in between.

Your software controls the belt logic. You need to simulate where every product ends up after the shift!

**Why This Problem Matters:**

- **Simulation Logic**: Translating physical constraints (skip broken nodes) into array logic.
- **Index Mapping**: Fundamental in implementing hash maps (probing) or memory allocators.
- **Order Preservation**: Maintaining relative order while ignoring subsets of data is common in filtering algorithms.

![Real-World Application](../images/ARR-003/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: The Skipping Rotation
```
Index:      0     1     2     3     4
Block:     [ ]   [X]   [ ]   [X]   [ ]
Value:      1     2     3     4     5
            ^     ^     ^     ^     ^
          Move  Fixed  Move  Fixed Move

Extract Moving: [1, 3, 5]
Rotate Left 2:  [5, 1, 3]

Place Back:
Index 0 receives 5
Index 2 receives 1
Index 4 receives 3

Result:     5     2     1     4     3
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Left Rotation**: Elements move towards index 0. `arr[i]` moves to a logically lower index.
- **Circular**: The rotation wraps around.
- **Blackout Set**: Indices in this set are immutable holes.
- **k can be large**: `k` can be greater than `n`. Use modulo arithmetic.

Common interpretation mistake:

- ❌ Shifting elements and overwriting blackout indices.
- ❌ Treating blackout indices as empty spots that can be filled (they are occupied and fixed).
- ✅ Treating the non-blackout elements as a separate, contiguous subsequence, rotating that, and putting it back.

### Core Concept: Extraction and Re-insertion

Since the blackout indices are just obstacles, the "moving" elements form a subsequence.
1. Extract all moving elements into a list.
2. Rotate this list.
3. Put terms back into the empty spots in order.

## Naive Approach

### Intuition

Create a new array. For each element, find its new position by stepping `k` times, skipping blackouts.

### Algorithm

1. Mark valid indices.
2. For each valid index `i`:
   - Find the `k`-th valid index to the left (wrapping around).
   - Place `arr[i]` there.
This is complex to implement O(N) due to "finding k-th valid".

## Optimal Approach (Extraction)

### Key Insight

The relative order of moving elements is preserved, just cyclically shifted. We can isolate them, rotate them efficiently, and assume their original positions.

### Algorithm

1. Identify all `valid_indices`: loop `0` to `n-1`, if `i` not in blackout, add to list.
2. Extract `values`: for each `idx` in `valid_indices`, get `arr[idx]`.
3. Rotate `values` left by `k % len(values)`.
   - `new_values[i] = values[(i + k) % count]`
4. Write back: for each `i` from `0` to `count-1`:
   - `arr[valid_indices[i]] = new_values[i]`

### Time Complexity

- **O(N)**: Scan array to extract (N), rotate (counts <= N), write back (counts <= N). All linear.

### Space Complexity

- **O(N)**: We store `valid_indices` and `values`, both bounded by N.

### Why This Is Optimal

We must look at all elements. The extraction/insertion is direct and easy to implement correctly compared to in-place simulation which is error-prone.

![Algorithm Visualization](../images/ARR-003/algorithm-visualization.png)
![Algorithm Steps](../images/ARR-003/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int[] shuttleShiftBlackout(int[] arr, int k, Set<Integer> blackout) {
        List<Integer> validIndices = new ArrayList<>();
        List<Integer> values = new ArrayList<>();
        
        // 1. Extract
        for (int i = 0; i < arr.length; i++) {
            if (!blackout.contains(i)) {
                validIndices.add(i);
                values.add(arr[i]);
            }
        }
        
        if (values.isEmpty()) return arr;
        
        // 2. Rotate
        int count = values.size();
        k = k % count;
        List<Integer> rotatedValues = new ArrayList<>(count);
        // Left rotate: element at i comes from (i + k) % count
        for (int i = 0; i < count; i++) {
            rotatedValues.add(values.get((i + k) % count));
        }
        
        // 3. Write Back
        for (int i = 0; i < count; i++) {
            arr[validIndices.get(i)] = rotatedValues.get(i);
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
        
        int k = sc.nextInt();
        int b = sc.nextInt();
        Set<Integer> blackout = new HashSet<>();
        for (int i = 0; i < b; i++) blackout.add(sc.nextInt());

        Solution solution = new Solution();
        int[] result = solution.shuttleShiftBlackout(arr, k, blackout);
        
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

def shuttle_shift_blackout(arr: list[int], k: int, blackout: set[int]) -> list[int]:
    """
    Left rotate non-blackout elements by k.
    """
    valid_indices = [i for i in range(len(arr)) if i not in blackout]
    
    if not valid_indices:
        return arr
        
    values = [arr[i] for i in valid_indices]
    count = len(values)
    k %= count
    
    # Left rotate list
    # values[k:] + values[:k] gives elements shifted left
    rotated_values = values[k:] + values[:k]
    
    # Write back
    for i, val in zip(valid_indices, rotated_values):
        arr[i] = val
        
    return arr

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    ptr = 0
    n = int(data[ptr]); ptr += 1
    arr = []
    for _ in range(n):
        arr.append(int(data[ptr])); ptr += 1
        
    k = int(data[ptr]); ptr += 1
    b = int(data[ptr]); ptr += 1
    
    blackout = set()
    for _ in range(b):
        blackout.add(int(data[ptr])); ptr += 1
        
    result = shuttle_shift_blackout(arr, k, blackout)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> shuttleShiftBlackout(vector<int>& arr, int k, unordered_set<int>& blackout) {
        vector<int> validIndices;
        vector<int> values;
        
        // Extract
        for (int i = 0; i < arr.size(); i++) {
            if (blackout.find(i) == blackout.end()) {
                validIndices.push_back(i);
                values.push_back(arr[i]);
            }
        }
        
        if (values.empty()) return arr;
        
        // Rotate
        int count = values.size();
        k %= count;
        // std::rotate performs left rotation
        rotate(values.begin(), values.begin() + k, values.end());
        
        // Write Back
        for (int i = 0; i < count; i++) {
            arr[validIndices[i]] = values[i];
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
    
    int k, b;
    cin >> k >> b;
    
    unordered_set<int> blackout;
    for (int i = 0; i < b; i++) {
        int idx;
        cin >> idx;
        blackout.insert(idx);
    }

    Solution solution;
    vector<int> result = solution.shuttleShiftBlackout(arr, k, blackout);
    
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
  shuttleShiftBlackout(arr, k, blackout) {
    const validIndices = [];
    const values = [];
    
    for (let i = 0; i < arr.length; i++) {
      if (!blackout.has(i)) {
        validIndices.push(i);
        values.push(arr[i]);
      }
    }
    
    const count = values.length;
    if (count === 0) return arr;
    
    k = k % count;
    
    // Left rotate
    const rotatedValues = new Array(count);
    for (let i = 0; i < count; i++) {
      rotatedValues[i] = values[(i + k) % count];
    }
    
    for (let i = 0; i < count; i++) {
      arr[validIndices[i]] = rotatedValues[i];
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
    
    const k = Number(tokens[ptr++]);
    const b = Number(tokens[ptr++]);
    const blackout = new Set();
    for (let i = 0; i < b; i++) blackout.add(Number(tokens[ptr++]));
    
    const solution = new Solution();
    const result = solution.shuttleShiftBlackout(arr, k, blackout);
    console.log(result.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `arr=[1, 2, 3, 4, 5]`, `k=2`, `blackout={1, 3}`

1. **Extract**:
   - `idx=0` (valid) -> val `1`
   - `idx=1` (BLACK)
   - `idx=2` (valid) -> val `3`
   - `idx=3` (BLACK)
   - `idx=4` (valid) -> val `5`
   - `validIndices`: `[0, 2, 4]`
   - `values`: `[1, 3, 5]`

2. **Rotate** `k=2` Left:
   - `values` size is 3. `k` is 2.
   - Pos 0 gets old pos `(0+2)%3 = 2` -> `values[2]=5`
   - Pos 1 gets old pos `(1+2)%3 = 0` -> `values[0]=1`
   - Pos 2 gets old pos `(2+2)%3 = 1` -> `values[1]=3`
   - `rotatedValues`: `[5, 1, 3]`

3. **Put Back**:
   - `validIndices[0] (0)` gets `rotatedValues[0] (5)`
   - `validIndices[1] (2)` gets `rotatedValues[1] (1)`
   - `validIndices[2] (4)` gets `rotatedValues[2] (3)`
   - Blackout indices `1` and `3` keep old values `2` and `4`.

**Result**: `[5, 2, 1, 4, 3]`

*(Note: There may be edge cases or input format discrepancies in examples; always follow the logical definition of "Left Rotation".)*

![Example Visualization](../images/ARR-003/example-1.png)

## ✅ Proof of Correctness

### Invariant

The set of values at blackout indices is constant. The set of values at valid indices is a permutation (cyclic shift) of the original values.

### Why the approach is correct

By extracting valid values to a contiguous buffer, we reduce the problem to the standard "rotate array" problem, which is well-solved. Rewriting them back to valid steps guarantees the blackout constraint is respected.

## 💡 Interview Extensions (High-Value Add-ons)

- **In-Place?**: Can you do this O(1) space? (A: Yes, if you treat the valid indices as a virtual array and use the 3-reversal algorithm, but "indexing" the virtual array is O(N) or O(1) with preprocessing. Preprocessing valid indices takes O(N) space though. True O(1) space is hard without modifying array structure initially.)
- **Large K**: Handle `k > 10^9`. (A: `k %= count`).
- **All Blackout**: Handle `b = n`. (A: Array valid list empty, no change).

## Common Mistakes to Avoid

1. **Mod by N**:
   - ❌ Doing `k % n` for rotation.
   - ✅ Must do `k % count` where `count` is number of *non-blackout* elements.

2. **Index Alignment**:
   - ❌ Putting rotated `values[0]` back into `arr[0]`.
   - ✅ Must put `values[0]` into `validIndices[0]`.

3. **1-based vs 0-based**:
   - ❌ Confusing user input indices. Problem uses 0-based.

## Related Concepts

- **Filters/Streams**: Processing a stream with invalid packets dropped.
- **Circular Buffer**: Standard ring buffer logic.
