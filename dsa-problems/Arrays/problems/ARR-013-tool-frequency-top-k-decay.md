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

class Solution {
    public List<Integer> topKWithDecay(int[][] events, int now, int D, int k) {
        //Implement here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[][] events = new int[n][2];
        for (int i = 0; i < n; i++) {
            events[i][0] = sc.nextInt();
            events[i][1] = sc.nextInt();
        }
        int now = sc.nextInt();
        int D = sc.nextInt();
        int k = sc.nextInt();

        Solution solution = new Solution();
        List<Integer> result = solution.topKWithDecay(events, now, D, k);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.size(); i++) {
            sb.append(result.get(i)).append(i == result.size() - 1 ? "" : " ");
        }
        System.out.println(sb);
        sc.close();
    }
}
```

### Python

```python
import sys
import math

def top_k_with_decay(events: list[tuple[int, int]], now: int, D: int, k: int) -> list[int]:
    # //Implement here
    return 0

def main():
    n = int(input())
    events = []
    for _ in range(n):
        value, timestamp = map(int, input().split())
        events.append((value, timestamp))
    now, D, k = map(int, input().split())

    result = top_k_with_decay(events, now, D, k)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> topKWithDecay(vector<pair<int,int>>& events, int now, int D, int k) {
        //Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<pair<int,int>> events(n);
    for (int i = 0; i < n; i++) cin >> events[i].first >> events[i].second;
    
    int now, D, k;
    cin >> now >> D >> k;

    Solution solution;
    vector<int> result = solution.topKWithDecay(events, now, D, k);
    for (size_t i = 0; i < result.size(); i++) {
        cout << result[i] << (i == result.size() - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  topKWithDecay(events, now, D, k) {
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
    const tokens = data.join(" ").split(/\s+/);
    if (tokens.length === 0 || tokens[0] === "") return;
    
    let ptr = 0;
    const n = Number(tokens[ptr++]);
    const events = [];
    for (let i = 0; i < n; i++) {
      const v = Number(tokens[ptr++]);
      const t = Number(tokens[ptr++]);
      events.push([v, t]);
    }
    
    const now = Number(tokens[ptr++]);
    const D = Number(tokens[ptr++]);
    const k = Number(tokens[ptr++]);
    
    const solution = new Solution();
    const result = solution.topKWithDecay(events, now, D, k);
    console.log(result.join(" "));
});
```

