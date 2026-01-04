---
problem_id: GMT_INTERVAL_REMOVAL__5921
display_id: GMT-005
slug: interval-removal-game
title: "Interval Removal Game"
difficulty: Medium
difficulty_score: 40
topics:
  - Game Theory
  - Bitwise Operations
tags:
  - nim-game
  - sprague-grundy
  - xor-sum
premium: true
subscription_tier: basic
time_limit: 1000
memory_limit: 256
---

# GMT-005: Interval Removal Game

## Problem Statement

You are given a set of disjoint intervals on a line.
Two players take turns making a move.
In each turn, a player must choose one interval `[L, R]` and remove a sub-interval of **positive length** from it.
Removing a sub-interval might split the original interval into two smaller intervals, or reduce it to one smaller interval, or remove it completely.
The player who cannot make a valid move loses.

Determine if the first player has a winning strategy.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767513719/dsa/gametheory/gqxa2d0ootusmfps4ifm.jpg)

## Input Format

- The first line contains an integer `n`, the number of intervals.
- The next `n` lines each contain two integers `L` and `R`, representing the interval `[L, R]`.

## Output Format

- Return "First" if the first player wins, and "Second" if the second player wins.

## Constraints

- `1 <= n <= 10^5`
- `0 <= L < R <= 10^9`
- Intervals are guaranteed to be disjoint.

## Example

**Input:**

```
2
0 2
5 6
```

**Output:**

```
First
```

**Explanation:**

- Interval 1: `[0, 2]`, length 2.
- Interval 2: `[5, 6]`, length 1.
- This is equivalent to a Nim game with piles of size 2 and 1.
- XOR sum = `2 ^ 1 = 3`.
- Since 3 > 0, First player wins.

![Example Visualization](../images/GMT-005/example-1.png)

## Notes

- The length of an interval `[L, R]` is `R - L`.
- The game is impartial and equivalent to Nim.

## Related Topics

Game Theory, Nim Game, XOR

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public String determineWinner(int n, long[][] intervals) {
        // Implement here
        return "";
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        int n = Integer.parseInt(line.trim());

        long[][] intervals = new long[n][2];
        for (int i = 0; i < n; i++) {
            String[] parts = br.readLine().trim().split("\\s+");
            intervals[i][0] = Long.parseLong(parts[0]);
            intervals[i][1] = Long.parseLong(parts[1]);
        }

        Solution sol = new Solution();
        System.out.println(sol.determineWinner(n, intervals));
    }
}
```

### Python

```python
import sys

class Solution:
    def determine_winner(self, n, intervals):
        # Implement here
        return ""

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    intervals = []
    idx = 1
    for _ in range(n):
        intervals.append([int(input_data[idx]), int(input_data[idx+1])])
        idx += 2

    sol = Solution()
    print(sol.determine_winner(n, intervals))

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
    string determineWinner(int n, vector<pair<long long, long long>>& intervals) {
        // Implement here
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<pair<long long, long long>> intervals(n);
    for (int i = 0; i < n; i++) {
        cin >> intervals[i].first >> intervals[i].second;
    }

    Solution sol;
    cout << sol.determineWinner(n, intervals) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  determineWinner(n, intervals) {
    // Implement here
    return "";
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const intervals = [];
  for (let i = 0; i < n; i++) {
    intervals.push([BigInt(input[idx++]), BigInt(input[idx++])]);
  }

  const sol = new Solution();
  console.log(sol.determineWinner(n, intervals));
}

solve();
```
