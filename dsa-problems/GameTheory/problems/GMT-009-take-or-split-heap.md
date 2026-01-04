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

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767539107/dsa/gametheory_simple/blnzu8svxmt3yrtxwrv9.jpg)

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
import java.io.*;

class Solution {
    public String determineWinner(int n, long[] heaps) {
        // Implement here
        return "";
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        long[] heaps = new long[n];
        String hLine = br.readLine();
        if (hLine != null) {
            String[] hParts = hLine.trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                heaps[i] = Long.parseLong(hParts[i]);
            }
        }

        Solution sol = new Solution();
        System.out.println(sol.determineWinner(n, heaps));
    }
}
```

### Python

```python
import sys

class Solution:
    def determine_winner(self, n, heaps):
        # Implement here
        return ""

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    heaps = list(map(int, input_data[1:1+n]))

    sol = Solution()
    print(sol.determine_winner(n, heaps))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string determineWinner(int n, vector<long long>& heaps) {
        // Implement here
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> heaps(n);
    for (int i = 0; i < n; i++) {
        cin >> heaps[i];
    }

    Solution sol;
    cout << sol.determineWinner(n, heaps) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  determineWinner(n, heaps) {
    // Implement here
    return "";
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const heaps = [];
  for (let i = 0; i < n; i++) {
    heaps.push(BigInt(input[idx++]));
  }

  const sol = new Solution();
  console.log(sol.determineWinner(n, heaps));
}

solve();
```
