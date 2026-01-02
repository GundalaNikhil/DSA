---
problem_id: STK_AUDITORIUM_HISTOGRAM_ONE_BOOSTER__9153
display_id: STK-013
slug: auditorium-histogram-one-booster
title: "Auditorium Histogram With One Booster"
difficulty: Medium
difficulty_score: 60
topics:
  - Stack
  - Histogram
  - Optimization
tags:
  - stack
  - histogram
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-013: Auditorium Histogram With One Booster

## Problem Statement

You are given histogram heights. You may increase exactly one bar by at most `b` units (you may choose to add less than `b`). Compute the maximum possible rectangle area after the boost.

![Problem Illustration](../images/STK-013/problem-illustration.png)

## Input Format

- First line: integers `n` and `b`
- Second line: `n` space-separated integers (heights)

## Output Format

- Single integer: maximum possible rectangle area

## Constraints

- `1 <= n <= 200000`
- `0 <= h[i], b <= 10^9`

## Example

**Input:**

```
3 3
2 4 2
```

**Output:**

```
7
```

**Explanation:**

Boost the middle bar to 7; the best rectangle has area 7.

![Example Visualization](../images/STK-013/example-1.png)

## Notes

- The classic largest-rectangle-in-histogram uses a monotonic stack
- You must account for a single boosted bar
- Consider how far each bar can extend as the minimum height
- Time complexity should be near O(n)

## Related Topics

Histogram, Monotonic Stack, Optimization

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long maxAreaWithBoost(int[] h, int b) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String line = "";
        while ((line = br.readLine()) != null && line.trim().isEmpty()) {}
        if (line == null) return;
        int n = Integer.parseInt(line.trim());
        
        List<Integer> list = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        while (list.size() < n) {
            while (!st.hasMoreTokens()) {
                String l = br.readLine();
                if (l == null) break;
                st = new StringTokenizer(l);
            }
            if (!st.hasMoreTokens()) break;
            list.add(Integer.parseInt(st.nextToken()));
        }
        
        int[] h = new int[list.size()];
        for(int i=0; i<list.size(); i++) h[i] = list.get(i);
        
        // Read B
        while (!st.hasMoreTokens()) {
            String l = br.readLine();
            if (l == null) break;
            st = new StringTokenizer(l);
        }
        int b = 0;
        if (st.hasMoreTokens()) {
            b = Integer.parseInt(st.nextToken());
        }
        
        Solution sol = new Solution();
        System.out.println(sol.maxAreaWithBoost(h, b));
    }
}
```

### Python

```python
import sys

def max_area_with_boost(h: list[int], b: int) -> int:
    # Implementation here
    return 0

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if not lines:
        return

    n = int(lines[0])
    h = list(map(int, lines[1].split()))
    b = int(lines[2])
    result = max_area_with_boost(h, b)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    long maxAreaWithBoost(vector<int>& h_in, int b) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> h(n);
    for (int i = 0; i < n; i++) {
        cin >> h[i];
    }
    
    int b;
    cin >> b;
    
    Solution sol;
    cout << sol.maxAreaWithBoost(h, b) << endl;
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  build(node, start, end) {
    // Implementation here
    return null;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/).filter(x => x !== "");
  for (const p of parts) data.push(p);
});

rl.on("close", () => {
  if (data.length === 0) return;
  
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const h = [];
  for (let i = 0; i < n; i++) {
    h.push(parseInt(data[idx++], 10));
  }
  const b = parseInt(data[idx++], 10);
  
  const solution = new Solution();
  console.log(solution.maxAreaWithBoost(h, b));
});
```
