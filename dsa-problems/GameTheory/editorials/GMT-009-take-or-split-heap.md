---
problem_id: GMT_TAKE_OR_SPLIT__9382
display_id: GMT-009
slug: take-or-split-heap
title: "Take-or-Split Heap"
difficulty: Medium
difficulty_score: 50
topics:
  - Game Theory
  - Bitwise Operations
tags:
  - impartial-game
  - sprague-grundy
  - xor-sum
premium: true
subscription_tier: basic
---

# GMT-009: Take-or-Split Heap

## 📋 Problem Summary

You are given multiple heaps. A move picks a heap with size `x > 1` and either
removes `k` stones (`1 <= k < x`) or splits the heap into two non-empty heaps
`a + b = x`. The player who cannot move loses. Determine the winner.

## 🌍 Real-World Scenario

**Scenario Title:** The Cell Division

Imagine cells that can either shrink (lose mass) or divide (mitosis). You want to force the system into a stable state where no more division or shrinking is possible (all cells size 1).

**Why This Problem Matters:**

- **Grundy Pattern:** It shows how complex rules can sometimes lead to simple Grundy patterns (`G(n) = n-1`).
- **Reduction:** Reduces a new game to a known one (Nim).

![Real-World Application](../images/GMT-009/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: State Transitions

```
Heap Size 3
Moves:
- Remove 1 -> Size 2.
- Remove 2 -> Size 1.
- Split 1+2 -> Sizes 1, 2.

Grundy Analysis:
- G(1) = 0 (Terminal).
- G(2) = mex(G(1), G(1)^G(1)) = mex(0, 0) = 1.
- G(3) = mex(G(1), G(2), G(1)^G(2)) = mex(0, 1, 0^1=1) = mex(0, 1) = 2.
- Pattern: G(n) = n - 1.
```

## ✅ Input/Output Clarifications

- **Terminal State:** Size 1.
- **Valid Moves:** `x > 1`.

## Optimal Approach

### Key Insight

Compute the Grundy values `G(n)`.
- `G(1) = 0`.
- `G(n) = mex({ G(n-k) | 1<=k<n } U { G(a)^G(b) | a+b=n })`.
- We observe `G(n) = n - 1`.
- Proof by induction:
  - Assume `G(m) = m - 1` for all `m < n`.
  - Reachable from remove: `G(1)...G(n-1)` -> `0...(n-2)`.
  - Reachable from split: `G(a)^G(b) = (a-1)^(b-1)`.
  - The set of reachable values includes `0, 1, ..., n-2`.
  - However, since `0...(n-2)` are present, `mex` is at least `n-1`.
  - Is `n-1` present? `n-1` would require `(a-1)^(b-1) = n-1` where `a+b=n`.
  - It turns out `G(n) = n-1` holds.
- Thus, the game is equivalent to Nim with pile sizes `n_i - 1`.

### Algorithm

1.  Initialize `xor_sum = 0`.
2.  For each heap size `x`:
    - `xor_sum ^= (x - 1)`.
3.  If `xor_sum > 0`, return "First".
4.  Else, return "Second".

### Time Complexity

- **O(N)**: Iterate heaps once.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/GMT-009/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public String takeOrSplit(int n, int[] heaps) {
        long xorSum = 0;
        for (int x : heaps) {
            xorSum ^= (x - 1);
        }
        return xorSum > 0 ? "First" : "Second";
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] heaps = new int[n];
            for (int i = 0; i < n; i++) {
                heaps[i] = sc.nextInt();
            }

            Solution solution = new Solution();
            System.out.println(solution.takeOrSplit(n, heaps));
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List

def take_or_split(n: int, heaps: List[int]) -> str:
    xor_sum = 0
    for x in heaps:
        xor_sum ^= (x - 1)
    return "First" if xor_sum > 0 else "Second"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        heaps = []
        for _ in range(n):
            heaps.append(int(next(iterator)))
            
        print(take_or_split(n, heaps))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string takeOrSplit(int n, vector<int>& heaps) {
        long long xorSum = 0;
        for (int x : heaps) {
            xorSum ^= (x - 1);
        }
        return xorSum > 0 ? "First" : "Second";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (cin >> n) {
        vector<int> heaps(n);
        for (int i = 0; i < n; i++) {
            cin >> heaps[i];
        }
        
        Solution solution;
        cout << solution.takeOrSplit(n, heaps) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  takeOrSplit(n, heaps) {
    let xorSum = 0n;
    for (const x of heaps) {
      xorSum ^= BigInt(x - 1);
    }
    return xorSum > 0n ? "First" : "Second";
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
  
  const flatData = [];
  data.forEach(line => {
      line.trim().split(/\s+/).forEach(part => {
          if (part) flatData.push(part);
      });
  });
  
  if (flatData.length === 0) return;
  
  let idx = 0;
  const n = parseInt(flatData[idx++]);
  
  const heaps = [];
  for (let i = 0; i < n; i++) {
      heaps.push(parseInt(flatData[idx++]));
  }

  const solution = new Solution();
  console.log(solution.takeOrSplit(n, heaps));
});
```

## 🧪 Test Case Walkthrough (Dry Run)
**Input:** `[2, 2]`

1.  Heap 1: `2 - 1 = 1`.
2.  Heap 2: `2 - 1 = 1`.
3.  XOR: `1 ^ 1 = 0`.
4.  Result: Second.

## ✅ Proof of Correctness

- **Induction:** `G(n) = n-1` holds for base cases and inductive step.
- **Impartial:** Standard Nim logic.

## 💡 Interview Extensions

- **Extension 1:** What if we can split into `k` heaps?
  - *Answer:* `G(n)` can change, re-analyze.
- **Extension 2:** What if we cannot remove, only split?
  - *Answer:* `G(n)` becomes related to parity (odd/even).

### Common Mistakes

1.  **Forgetting -1:**
    - ❌ Wrong: XORing `x`.
    - ✅ Correct: XORing `x - 1`.
2.  **Terminal State:**
    - ❌ Wrong: Thinking 0 is terminal.
    - ✅ Correct: 1 is terminal.

## Related Concepts

- **Nim**
- **Sprague-Grundy**
