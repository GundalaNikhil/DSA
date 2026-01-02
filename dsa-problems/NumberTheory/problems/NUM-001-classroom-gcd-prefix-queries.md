---
problem_id: NUM_CLASSROOM_GCD_PREFIX_QUERIES__4821
display_id: NUM-001
slug: classroom-gcd-prefix-queries
title: "Classroom GCD Prefix Queries"
difficulty: Easy
difficulty_score: 25
topics:
  - Number Theory
  - GCD
  - Prefix Computation
tags:
  - number-theory
  - gcd
  - prefix
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-001: Classroom GCD Prefix Queries

## Problem Statement

You are given an array `a`. For each query `r`, return the greatest common divisor of the prefix `a[0..r]` (inclusive). Preprocess once to answer all queries efficiently.

![Problem Illustration](../images/NUM-001/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` integers `a[i]`
- Next `q` lines: integer `r` (0-based index)

## Output Format

- For each query, print `gcd(a[0..r])` on its own line

## Constraints

- `1 <= n <= 200000`
- `1 <= q <= 200000`
- `-10^9 <= a[i] <= 10^9`
- `0 <= r < n`

## Example

**Input:**

```
3 3
12 18 6
0
1
2
```

**Output:**

```
12
6
6
```

**Explanation:**

Prefix GCDs:

- r=0 -> gcd(12) = 12
- r=1 -> gcd(12,18) = 6
- r=2 -> gcd(12,18,6) = 6

![Example Visualization](../images/NUM-001/example-1.png)

## Notes

- Use absolute values when computing gcd
- Precompute prefix gcd in O(n)
- Each query is O(1)
- Space complexity: O(n)

## Related Topics

GCD, Prefix Arrays, Number Theory

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public int[] prefixGcds(int[] a) {
        return null;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        int q = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] pref = solution.prefixGcds(a);
        
        for (int i = 0; i < q; i++) {
            int r = sc.nextInt();
            System.out.println(pref[r]);
        }
        sc.close();
    }
}
```

### Python

```python
import sys
from math import gcd
from typing import List

def prefix_gcds(a: List[int]) -> List[int]:
    return []
def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    try:
        n = int(next(iterator))
        q = int(next(iterator))
        a = [int(next(iterator)) for _ in range(n)]
        
        pref = prefix_gcds(a)
        
        results = []
        for _ in range(q):
            r = int(next(iterator))
            results.append(str(pref[r]))
            
        print('\n'.join(results))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <cmath>
#include <algorithm>

using namespace std;

class Solution {
    int gcd(int a, int b) {
        return 0;
    }

public:
    vector<int> prefixGcds(const vector<int>& a) {
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    Solution solution;
    vector<int> pref = solution.prefixGcds(a);
    
    for (int i = 0; i < q; i++) {
        int r;
        cin >> r;
        cout << pref[r] << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function gcd(a, b) {
    return 0;
  }

function prefixGcds(a) {
    return 0;
  }

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (let i = 0; i < parts.length; i++) {
    if (parts[i].length > 0) data.push(parts[i]);
  }
});
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const q = parseInt(data[idx++], 10);
  const a = [];
  for (let i = 0; i < n; i++) a.push(parseInt(data[idx++], 10));
  
  const pref = prefixGcds(a);
  const out = [];
  for (let i = 0; i < q; i++) {
    const r = parseInt(data[idx++], 10);
    out.push(pref[r].toString());
  }
  console.log(out.join("\n"));
});
```

