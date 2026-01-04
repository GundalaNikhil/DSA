---
problem_id: ARR_TOPK_DECAY_SCORE__1198
display_id: ARR-013
slug: tool-frequency-top-k-decay
title: "Tool Frequency Top K with Recency Decay"
difficulty: Medium
difficulty_score: 58
topics:
  - Arrays
  - Heap
  - Hashing
tags:
  - arrays
  - heap
  - hashing
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-013: Tool Frequency Top K with Recency Decay

## Problem Statement

Each value appears with a timestamp. The score of a value v at time now is the sum of exp(-(now - t) / D) over all timestamps t where v appears.
Return the k values with the highest decayed scores. Break ties by smaller value.

![Problem Illustration](../images/ARR-013/problem-illustration.png)

## Input Format

- First line: integer n
- Next n lines: value and timestamp
- Last line: integers now, D, and k

## Output Format

Print k values in descending score order, space-separated.

## Constraints

- `1 <= n <= 200000`
- `Timestamps are non-decreasing`
- `1 <= k <= n`
- `1 <= D <= 1000000`

## Example

**Input:**

```
3
5 0
5 1
3 2
5 2 1
```

**Output:**

```
3
```

**Explanation:**

Score(5) = exp(-(5-0)/2) + exp(-(5-1)/2) = exp(-2.5) + exp(-2).
Score(3) = exp(-(5-2)/2) = exp(-1.5), which is larger, so 3 is returned.

![Example Visualization](../images/ARR-013/example-1.png)

## Notes

- Use double precision for scores.
- Ties are broken by smaller value.

## Related Topics

Heap, Hashing, Arrays

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public List<Integer> topKDecay(int n, int[][] logs, int now, int D, int k) {
        // Implement here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        int[][] logs = new int[n][2];
        for (int i = 0; i < n; i++) {
            String[] parts = br.readLine().trim().split("\\s+");
            logs[i][0] = Integer.parseInt(parts[0]);
            logs[i][1] = Integer.parseInt(parts[1]);
        }

        String lastLine = br.readLine();
        if (lastLine == null) return;
        String[] parts = lastLine.trim().split("\\s+");
        int now = Integer.parseInt(parts[0]);
        int D = Integer.parseInt(parts[1]);
        int k = Integer.parseInt(parts[2]);

        Solution sol = new Solution();
        List<Integer> result = sol.topKDecay(n, logs, now, D, k);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.size(); i++) {
            sb.append(result.get(i)).append(i == result.size() - 1 ? "" : " ");
        }
        System.out.println(sb);
    }
}
```

### Python

```python
import sys
import math
import heapq

class Solution:
    def top_k_decay(self, n, logs, now, D, k):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        logs = []
        for _ in range(n):
            val = int(next(iterator))
            ts = int(next(iterator))
            logs.append((val, ts))

        now = int(next(iterator))
        D = int(next(iterator))
        k = int(next(iterator))
    except StopIteration:
        pass

    sol = Solution()
    result = sol.top_k_decay(n, logs, now, D, k)

    print(*(result))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <unordered_map>
#include <algorithm>
#include <iomanip>

using namespace std;

class Solution {
public:
    vector<int> topKDecay(int n, vector<pair<int, int>>& logs, int now, int D, int k) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<pair<int, int>> logs(n);
    for (int i = 0; i < n; i++) {
        cin >> logs[i].first >> logs[i].second;
    }

    int now, D, k;
    cin >> now >> D >> k;

    Solution sol;
    vector<int> result = sol.topKDecay(n, logs, now, D, k);

    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << (i == result.size() - 1 ? "" : " ");
    }
    cout << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  topKDecay(n, logs, now, D, k) {
    // Implement here
    return [];
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
  const logs = [];
  for (let i = 0; i < n; i++) {
    const v = readInt();
    const t = readInt();
    logs.push([v, t]);
  }
  const now = readInt();
  const D = readInt();
  const k = readInt();

  const sol = new Solution();
  const result = sol.topKDecay(n, logs, now, D, k);

  console.log(result.join(" "));
}

solve();
```
