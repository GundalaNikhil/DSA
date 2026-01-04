---
problem_id: ARR_LEAKY_ROOF_REINFORCE__3586
display_id: ARR-011
slug: leaky-roof-reinforcement
title: "Leaky Roof Reinforcement"
difficulty: Medium
difficulty_score: 55
topics:
  - Arrays
  - Prefix Suffix
  - Greedy
tags:
  - arrays
  - prefix-suffix
  - greedy
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-011: Leaky Roof Reinforcement

## Problem Statement

You can add planks to increase heights so the profile becomes non-decreasing up to a single peak and non-increasing after that peak. Find the minimum total height added.

![Problem Illustration](../images/ARR-011/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers height[i]

## Output Format

Print the minimum total added height.

## Constraints

- `1 <= n <= 200000`
- `0 <= height[i] <= 1000000000`

## Example

**Input:**

```
5
4 1 3 1 5
```

**Output:**

```
7
```

**Explanation:**

Choose peak at index 4 with height 5. The reinforced profile is [4, 4, 4, 4, 5],
adding 3 + 1 + 3 = 7 in total.

![Example Visualization](../images/ARR-011/example-1.png)

## Notes

- You may only increase heights, never decrease.
- The peak can be any index.

## Related Topics

Prefix Suffix, Greedy, Arrays

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long minAddedHeight(int n, int[] height) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        int[] height = new int[n];
        String hLine = br.readLine();
        if (hLine != null) {
            String[] parts = hLine.trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                height[i] = Integer.parseInt(parts[i]);
            }
        }

        Solution sol = new Solution();
        System.out.println(sol.minAddedHeight(n, height));
    }
}
```

### Python

```python
import sys

class Solution:
    def min_added_height(self, n, height):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    height = list(map(int, input_data[1:n+1]))

    sol = Solution()
    print(sol.min_added_height(n, height))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long minAddedHeight(int n, vector<int>& height) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> height(n);
    for (int i = 0; i < n; i++) {
        cin >> height[i];
    }

    Solution sol;
    cout << sol.minAddedHeight(n, height) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  minAddedHeight(n, height) {
    // Implement here
    return BigInt(0);
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  function readInt() {
    return parseInt(input[idx++]);
  }

  const n = readInt();
  const height = [];
  for (let i = 0; i < n; i++) height.push(readInt());

  const sol = new Solution();
  console.log(sol.minAddedHeight(n, height).toString());
}

solve();
```
