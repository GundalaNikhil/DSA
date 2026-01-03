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
time_limit: 1000
memory_limit: 256
---

# GMT-009: Take-or-Split Heap

## Problem Statement

You are given `n` heaps of stones.
Two players take turns making a move.
In each turn, a player must choose one heap with `x` stones (`x > 1`) and perform one of the following actions:
1.  **Remove** `k` stones from the heap, where `1 <= k < x`. The heap size becomes `x - k`.
2.  **Split** the heap into two non-empty heaps of sizes `a` and `b` such that `a + b = x`. The original heap is replaced by these two new heaps.

The player who cannot make a valid move loses.
(This happens when all heaps have size 1).

Determine if the first player has a winning strategy.

![Problem Illustration](../images/GMT-009/problem-illustration.png)

## Input Format

- The first line contains an integer `n`, the number of heaps.
- The second line contains `n` space-separated integers, the sizes of the heaps.

## Output Format

- Return "First" if the first player wins, and "Second" if the second player wins.

## Constraints

- `1 <= n <= 10^5`
- `1 <= heap_size <= 10^9`

## Example

**Input:**
```
2
2 2
```

**Output:**
```
Second
```

**Explanation:**
- Heaps: `[2, 2]`.
- Moves from a heap of size 2:
  - Remove 1 -> Size 1.
  - Split 1+1 -> Sizes 1, 1.
- If P1 picks the first heap (size 2):
  - Option A: Remove 1. Heaps become `[1, 2]`.
  - Option B: Split 1+1. Heaps become `[1, 1, 2]`.
- From `[1, 2]`, P2 can pick the heap of size 2 and remove 1 -> `[1, 1]`.
  - Now heaps are `[1, 1]`. No valid moves (size 1 cannot be reduced or split). P1 loses.
- From `[1, 1, 2]`, P2 can pick size 2 and split -> `[1, 1, 1, 1]`.
  - No moves. P1 loses.
- Since P1 loses in all branches, P2 wins.

![Example Visualization](../images/GMT-009/example-1.png)

## Notes

- A heap of size 1 is a terminal state (Grundy value 0).
- The game is equivalent to Nim with modified pile sizes.

## Related Topics

Game Theory, Sprague-Grundy Theorem

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public String takeOrSplit(int n, int[] heaps) {
        //Implement here
        return "";
    }
}

class Main {
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
    # //Implement here
    return 0

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
        //Implement here
        return "";
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
    //Implement here
    return 0;
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

