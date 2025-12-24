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

![Problem Illustration](../images/GMT-005/problem-illustration.png)

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

class Solution {
    public String intervalRemovalGame(int n, int[][] intervals) {
        // Your implementation here
        return "Second";
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[][] intervals = new int[n][2];
            for (int i = 0; i < n; i++) {
                intervals[i][0] = sc.nextInt();
                intervals[i][1] = sc.nextInt();
            }

            Solution solution = new Solution();
            System.out.println(solution.intervalRemovalGame(n, intervals));
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List

def interval_removal_game(n: int, intervals: List[List[int]]) -> str:
    # Your implementation here
    return "Second"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        intervals = []
        for _ in range(n):
            l = int(next(iterator))
            r = int(next(iterator))
            intervals.append([l, r])
            
        print(interval_removal_game(n, intervals))
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
    string intervalRemovalGame(int n, vector<vector<int>>& intervals) {
        // Your implementation here
        return "Second";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (cin >> n) {
        vector<vector<int>> intervals(n, vector<int>(2));
        for (int i = 0; i < n; i++) {
            cin >> intervals[i][0] >> intervals[i][1];
        }
        
        Solution solution;
        cout << solution.intervalRemovalGame(n, intervals) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  intervalRemovalGame(n, intervals) {
    // Your implementation here
    return "Second";
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
  
  const intervals = [];
  for (let i = 0; i < n; i++) {
      const l = parseInt(flatData[idx++]);
      const r = parseInt(flatData[idx++]);
      intervals.push([l, r]);
  }

  const solution = new Solution();
  console.log(solution.intervalRemovalGame(n, intervals));
});
```
