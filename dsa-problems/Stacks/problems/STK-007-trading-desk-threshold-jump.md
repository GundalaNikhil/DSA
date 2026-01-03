---
problem_id: STK_TRADING_DESK_THRESHOLD_JUMP__2549
display_id: STK-007
slug: trading-desk-threshold-jump
title: "Trading Desk Threshold Jump"
difficulty: Medium
difficulty_score: 48
topics:
  - Stack
  - Monotonic Stack
  - Arrays
tags:
  - stack
  - monotonic
  - next-greater
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-007: Trading Desk Threshold Jump

## Problem Statement

Given prices `p[i]` and a threshold `t`, for each index find how many steps forward until you see a price at least `t` higher than `p[i]`. If no such future price exists, output `0`.

![Problem Illustration](../images/STK-007/problem-illustration.png)

## Input Format

- First line: integers `n` and `t`
- Second line: `n` space-separated integers

## Output Format

- Single line: `n` integers of wait steps (0 if none)

## Constraints

- `1 <= n <= 200000`
- `0 <= p[i], t <= 10^9`

## Example

**Input:**

```
5 2
3 1 4 6 5
```

**Output:**

```
2 1 1 0 0
```

**Explanation:**

For 3, the first price at least 2 higher is 4 at distance 2. For 6, no future price is >= 8.

![Example Visualization](../images/STK-007/example-1.png)

## Notes

- Use a monotonic stack of indices
- Compare `p[j] - p[i] >= t`
- Pop indices that are satisfied by the current price
- Time complexity: O(n)

## Related Topics

Next Greater Element, Monotonic Stack, Arrays

---

## Solution Template
### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int[] thresholdJump(int[] prices, int t) {
        //Implement here
        return new int[0];
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // Read N
        String line = "";
        while ((line = br.readLine()) != null && line.trim().isEmpty()) {}
        if (line == null) return;
        int n = Integer.parseInt(line.trim());
        
        // Read Array
        List<Integer> list = new ArrayList<>();
        StringTokenizer st = new StringTokenizer("");
        
        while (list.size() < n) {
            while (!st.hasMoreTokens()) {
                String l = br.readLine();
                if (l == null) break;
                st = new StringTokenizer(l);
            }
            if (!st.hasMoreTokens()) break;
            list.add(Integer.parseInt(st.nextToken()));
        }
        
        int[] prices = new int[list.size()];
        for(int i=0; i<list.size(); i++) prices[i] = list.get(i);
        
        // Read T
        while (!st.hasMoreTokens()) {
            String l = br.readLine();
            if (l == null) break;
            st = new StringTokenizer(l);
        }
        int t = 0;
        if (st.hasMoreTokens()) {
            t = Integer.parseInt(st.nextToken());
        }
        
        Solution sol = new Solution();
        int[] res = sol.thresholdJump(prices, t);
        for (int val : res) {
            System.out.println(val);
        }
    }
}
```

### Python

```python
def threshold_jump(prices: list[int], t: int) -> list[int]:
    # //Implement here
    return 0

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if not lines:
        return

    n = int(lines[0])
    prices = list(map(int, lines[1].split()))
    t = int(lines[2])
    result = threshold_jump(prices, t)
    for r in result:
        print(r)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <climits>

using namespace std;

class Solution {
public:
    vector<int> thresholdJump(vector<int>& prices, int t) {
        //Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> prices(n);
    for (int i = 0; i < n; i++) {
        cin >> prices[i];
    }
    
    int t;
    cin >> t;
    
    Solution sol;
    vector<int> res = sol.thresholdJump(prices, t);
    
    for (int val : res) {
        cout << val << "\n";
    }
    
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  thresholdJump(prices, t) {
    //Implement here
    return 0;
  }
}

const readline = require("readline");
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
  const prices = [];
  for (let i = 0; i < n; i++) {
    prices.push(parseInt(data[idx++], 10));
  }
  const t = parseInt(data[idx++], 10);
  
  const solution = new Solution();
  const res = solution.thresholdJump(prices, t);
  console.log(res.join("\n"));
});
```

