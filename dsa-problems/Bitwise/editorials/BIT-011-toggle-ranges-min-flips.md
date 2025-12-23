---
problem_id: BIT_TOGGLE_RANGES_MIN_FLIPS__8411
display_id: BIT-011
slug: toggle-ranges-min-flips
title: "Toggle Ranges Minimum Flips"
difficulty: Medium
difficulty_score: 45
topics:
  - Bitwise Operations
  - Array
  - Greedy
  - Flipping
tags:
  - bitwise
  - array-transformation
  - greedy
  - medium
premium: true
subscription_tier: basic
---

# BIT-011: Toggle Ranges Minimum Flips

## 📋 Problem Summary

Given two binary arrays `A` and `B`, you can perform an operation: choose any subarray and flip all bits in it (0 becomes 1, 1 becomes 0). Find the minimum number of operations to transform `A` to `B`.

## 🌍 Real-World Scenario

**Scenario Title:** Magnetic Tape Correction

You are restoring data on a magnetic tape.
- **State**: The tape has magnetic domains oriented Up (1) or Down (0). Current state `A`.
- **Target**: You need to match the master recording `B`.
- **Tool**: You have a magnetic head that can "sweep" a continuous segment of the tape, inverting the polarity of every domain it passes over.
- **Cost**: Activating the head is expensive (energy/wear).
- **Goal**: Minimize the number of sweeps to fix all errors.

**Why This Problem Matters:**

- **Difference Array**: Relates range updates to point updates.
- **Greedy Optimality**: Proving that processing errors from left to right is optimal.
- **State Compression**: Reducing the problem to processing the "Difference XOR" array.

![Real-World Application](../images/BIT-011/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Zones of Mismatch
```
A: 0 1 1 0 1 0
B: 1 0 1 1 1 1

Diff (A^B):
   1 1 0 1 0 1
   ^ ^   ^   ^
   Run1  Run2 Run3

Mismatches form contiguous "islands".
We flip Range1 (idx 0-1) -> Fixes Run1.
We flip Range2 (idx 3-3) -> Fixes Run2.
We flip Range3 (idx 5-5) -> Fixes Run3.
Total 3 Ops.
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input**: Two arrays of 0s and 1s.
- **Values**: Only 0/1. `N` up to 200,000.
- **Subarray**: Continuous range.

Common interpretation mistake:

- ❌ Trying BFS to find shortest path (State space is $2^N$).
- ✅ Identifying that the problem is equivalent to counting contiguous segments of mismatches.

### Core Concept: Difference Array Logic

Let `D[i] = A[i] ^ B[i]`. This array marks the errors (1=Error, 0=Correct).
An operation `Flip(L, R)` toggles `D[L...R]`.
We want to turn all 1s in `D` to 0s.
Is it ever optimal to overlapping flips?
Consider `D = 1 0 1`.
- Option 1: Flip `[0]`, Flip `[2]`. Cost 2. Result `0 0 0`.
- Option 2: Flip `[0..2]`. Result `0 1 0`. Now must Flip `[1]`. Total Cost 2. Result `0 0 0`.
Overlapping/merging disjoint errors never reduces the operation count. It just shifts the error.
Thus, the optimal strategy corresponds to treating each contiguous block of errors as one operation.

## Naive Approach (Simulation/BFS)

### Intuition

Try all ranges.

### Algorithm

1. BFS on state of array.

### Time Complexity

- **O(2^N)**. Too slow.

### Space Complexity

- **O(2^N)**.

## Optimal Approach (Greedy Count)

### Key Insight

The number of operations is exactly the number of contiguous segments of 1s in the XOR difference array `D`.

### Algorithm

1. `cnt = 0`.
2. Loop `i` from 0 to `n-1`:
   - `mismatch = A[i] ^ B[i]`.
   - If `mismatch == 1`:
     - If we are at start (`i==0`) OR previous was match (`A[i-1]^B[i-1] == 0`):
       - Start of new run -> `cnt++`.
3. Return `cnt`.

### Time Complexity

- **O(N)**. Single pass.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/BIT-011/algorithm-visualization.png)
![Algorithm Steps](../images/BIT-011/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int toggleRangesMinFlips(int[] A, int[] B) {
        int n = A.length;
        int count = 0;
        int prevDiff = 0;
        
        for (int i = 0; i < n; i++) {
            int currDiff = A[i] ^ B[i];
            
            // If current is mismatch (1) and previous was match (0),
            // we have entered a new island of mismatches.
            // We greedily "start" a flip here. The flip "continues"
            // until the mismatch run ends, handled implicitly.
            if (currDiff == 1 && prevDiff == 0) {
                count++;
            }
            prevDiff = currDiff;
        }
        
        return count;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] A = new int[n];
        for (int i = 0; i < n; i++) A[i] = sc.nextInt();
        int[] B = new int[n];
        for (int i = 0; i < n; i++) B[i] = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.toggleRangesMinFlips(A, B));
        sc.close();
    }
}
```

### Python

```python
import sys

def toggle_ranges_min_flips(A: list[int], B: list[int]) -> int:
    count = 0
    prev_diff = 0
    
    for a_val, b_val in zip(A, B):
        curr_diff = a_val ^ b_val
        if curr_diff == 1 and prev_diff == 0:
            count += 1
        prev_diff = curr_diff
        
    return count

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    ptr = 0
    n = int(data[ptr]); ptr += 1
    A = []
    for _ in range(n):
        A.append(int(data[ptr])); ptr += 1
    B = []
    for _ in range(n):
        B.append(int(data[ptr])); ptr += 1
        
    result = toggle_ranges_min_flips(A, B)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int toggleRangesMinFlips(vector<int>& A, vector<int>& B) {
        int n = A.size();
        int count = 0;
        int prevDiff = 0;
        
        for (int i = 0; i < n; i++) {
            int currDiff = A[i] ^ B[i];
            if (currDiff == 1 && prevDiff == 0) {
                count++;
            }
            prevDiff = currDiff;
        }
        return count;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> A(n);
    for (int i = 0; i < n; i++) cin >> A[i];
    vector<int> B(n);
    for (int i = 0; i < n; i++) cin >> B[i];

    Solution solution;
    cout << solution.toggleRangesMinFlips(A, B) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  toggleRangesMinFlips(A, B) {
    let count = 0;
    let prevDiff = 0;
    
    for (let i = 0; i < A.length; i++) {
      const currDiff = A[i] ^ B[i];
      if (currDiff === 1 && prevDiff === 0) {
        count++;
      }
      prevDiff = currDiff;
    }
    return count;
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
    const A = [];
    for (let i = 0; i < n; i++) A.push(Number(tokens[ptr++]));
    const B = [];
    for (let i = 0; i < n; i++) B.push(Number(tokens[ptr++]));
    
    const solution = new Solution();
    console.log(solution.toggleRangesMinFlips(A, B));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `A=[0,1,1,0]`, `B=[1,0,1,1]`.
**D (XOR)**: `[1, 1, 0, 1]`.
- i=0: `D=1`. Prev=0. Start Run. Count=1. Prev=1.
- i=1: `D=1`. Prev=1. Continue. Prev=1.
- i=2: `D=0`. Prev=1. End Run. Prev=0.
- i=3: `D=1`. Prev=0. Start Run. Count=2. Prev=1.
**Total**: 2.

## ✅ Proof of Correctness

### Invariant

We count the number of disjoint segments of 1s in `A ^ B`. Each operation `Flip(L, R)` can remove exactly one contiguous segment of 1s. Thus, the minimum operations equal the number of such segments. Merging two segments with a flip over 0s creates a gap of 1s (inverted 0s) that requires remediation, never improving the count.

## 💡 Interview Extensions (High-Value Add-ons)

- **Flip K times**: Maximize matching bits with K flips (Requires merging logic / DP).
- **2D Grid**: Flip rectangle subarrays (Much harder).

## Common Mistakes to Avoid

1. **Changing A in-place**:
   - ❌ Modifying A as you iterate might be confusing if not careful.
   - ✅ Ideally just track state in variables.
2. **Boundary Cases**:
   - ❌ `D` ending with 1.
   - ✅ Logic `prevDiff` handles start of runs correctly.

## Related Concepts

- **Run-Length Encoding**: We are counting runs of 1s.
- **Problem Reduction**: Reducing complex string transforms to simple array properties.
