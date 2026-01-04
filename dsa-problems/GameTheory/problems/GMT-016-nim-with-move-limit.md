---
problem_id: GMT_NIM_LIMIT__7392
display_id: GMT-016
slug: nim-with-move-limit
title: "Nim with Move Limit"
difficulty: Easy
difficulty_score: 35
topics:
  - Game Theory
  - Math
tags:
  - impartial-game
  - sprague-grundy
  - xor-sum
premium: true
subscription_tier: basic
time_limit: 1000
memory_limit: 256
---

# GMT-016: Nim with Move Limit

## Problem Statement

You are given `N` heaps of stones. The `i`-th heap has `A[i]` stones.
Each heap also has a specific move limit `L[i]`.
Two players take turns making a move.
In each turn, a player must:

1.  Choose a heap `i` that is not empty.
2.  Remove `k` stones from it, such that `1 <= k <= min(A[i], L[i])`.

The player who cannot make a valid move loses.
(This happens when all heaps are empty).

Determine if the first player has a winning strategy.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767539112/dsa/gametheory_simple/gfjupmih06kpneh56gmg.jpg)

## Input Format

- The first line contains an integer `N`.
- The second line contains `N` space-separated integers `A[i]` (heap sizes).
- The third line contains `N` space-separated integers `L[i]` (move limits).

## Output Format

- Return "First" if the first player wins, and "Second" if the second player wins.

## Constraints

- `1 <= N <= 10^5`
- `1 <= A[i], L[i] <= 10^9`

## Example

**Input:**

```
2
10 15
3 5
```

**Output:**

```
First
```

**Explanation:**

- Heap 1: Size 10, Limit 3.
  - `G(10) = 10 % (3 + 1) = 10 % 4 = 2`.
- Heap 2: Size 15, Limit 5.
  - `G(15) = 15 % (5 + 1) = 15 % 6 = 3`.
- XOR Sum = `2 ^ 3 = 1`.
- Since XOR Sum > 0, First wins.

![Example Visualization](../images/GMT-016/example-1.png)

## Notes

- This is a standard variation of Nim.
- The Grundy value of a heap of size `S` with limit `L` is `S % (L + 1)`.

## Related Topics

Game Theory, Sprague-Grundy Theorem

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public String determineWinner(int n, long[] a, long[] l) {
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

        long[] a = new long[n];
        long[] l = new long[n];

        String aLine = br.readLine();
        if (aLine != null) {
            String[] aParts = aLine.trim().split("\\s+");
            for (int i = 0; i < n; i++) a[i] = Long.parseLong(aParts[i]);
        }

        String lLine = br.readLine();
        if (lLine != null) {
            String[] lParts = lLine.trim().split("\\s+");
            for (int i = 0; i < n; i++) l[i] = Long.parseLong(lParts[i]);
        }

        Solution sol = new Solution();
        System.out.println(sol.determineWinner(n, a, l));
    }
}
```

### Python

```python
import sys

class Solution:
    def determine_winner(self, n, a, l):
        # Implement here
        return ""

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    a = list(map(int, input_data[1:1+n]))
    l = list(map(int, input_data[1+n:1+2*n]))

    sol = Solution()
    print(sol.determine_winner(n, a, l))

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
    string determineWinner(int n, vector<long long>& a, vector<long long>& l) {
        // Implement here
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n), l(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) cin >> l[i];

    Solution sol;
    cout << sol.determineWinner(n, a, l) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  determineWinner(n, a, l) {
    // Implement here
    return "";
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const a = [];
  for (let i = 0; i < n; i++) a.push(BigInt(input[idx++]));
  const l = [];
  for (let i = 0; i < n; i++) l.push(BigInt(input[idx++]));

  const sol = new Solution();
  console.log(sol.determineWinner(n, a, l));
}

solve();
```
