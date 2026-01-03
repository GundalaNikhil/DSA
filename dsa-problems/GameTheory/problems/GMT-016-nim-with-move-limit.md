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

![Problem Illustration](../images/GMT-016/problem-illustration.png)

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

class Solution {
    public String nimLimit(int n, int[] A, int[] L) {
        //Implement here
        return "";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] A = new int[n];
            for (int i = 0; i < n; i++) {
                A[i] = sc.nextInt();
            }
            int[] L = new int[n];
            for (int i = 0; i < n; i++) {
                L[i] = sc.nextInt();
            }

            Solution solution = new Solution();
            System.out.println(solution.nimLimit(n, A, L));
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List

def nim_limit(n: int, A: List[int], L: List[int]) -> str:
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
        A = []
        for _ in range(n):
            A.append(int(next(iterator)))
        L = []
        for _ in range(n):
            L.append(int(next(iterator)))
            
        print(nim_limit(n, A, L))
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
    string nimLimit(int n, vector<int>& A, vector<int>& L) {
        //Implement here
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (cin >> n) {
        vector<int> A(n);
        for (int i = 0; i < n; i++) {
            cin >> A[i];
        }
        vector<int> L(n);
        for (int i = 0; i < n; i++) {
            cin >> L[i];
        }
        
        Solution solution;
        cout << solution.nimLimit(n, A, L) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  nimLimit(n, A, L) {
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
  
  const A = [];
  for (let i = 0; i < n; i++) {
      A.push(parseInt(flatData[idx++]));
  }
  const L = [];
  for (let i = 0; i < n; i++) {
      L.push(parseInt(flatData[idx++]));
  }

  const solution = new Solution();
  console.log(solution.nimLimit(n, A, L));
});
```

