---
problem_id: STK_CANTEEN_TOKEN_CLIMB_SPAN__6180
display_id: STK-008
slug: canteen-token-climb-span
title: "Canteen Token Climb Span"
difficulty: Medium
difficulty_score: 50
topics:
  - Stack
  - Monotonic Stack
  - Spans
tags:
  - stack
  - spans
  - monotonic
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-008: Canteen Token Climb Span

## Problem Statement

For each day, compute how many consecutive prior days had demand strictly lower than today's demand. If any prior day equals today's demand, the span resets to 0 at that day.

Return the span counts (not including today).

![Problem Illustration](../images/STK-008/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers (demands)

## Output Format

- Single line: `n` integers of spans

## Constraints

- `1 <= n <= 100000`
- `0 <= demand[i] <= 10^9`

## Example

**Input:**

```
5
3 1 2 2 5
```

**Output:**

```
0 0 1 0 4
```

**Explanation:**

Day 4 (value 5) has four prior days with smaller demand; day 3 equals 2 so its span is 0.

![Example Visualization](../images/STK-008/example-1.png)

## Notes

- Use a strictly increasing stack of (value, index)
- Pop while values are strictly lower
- If the top equals current, span is 0
- Time complexity: O(n)

## Related Topics

Stock Span, Monotonic Stack, Arrays

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int[] spans(int[] demand) {
        return null;
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = "";
        while ((line = br.readLine()) != null && line.trim().isEmpty()) {}
        if (line == null) return;
        
        // Read N
        int n = Integer.parseInt(line.trim());
        
        // Read Array
        // Could be on same line or next line or multiline
        List<Integer> list = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine()); // Try next line
        
        // If next line is empty or null, keep reading?
        // Let's robustly token read
        // Actually, Python reads lines[1].split(). Just one line.
        // Let's mimic robust reading just in case.
        
        while (list.size() < n) {
            while (st != null && !st.hasMoreTokens()) {
                String l = br.readLine();
                if (l == null) { st = null; break; }
                st = new StringTokenizer(l);
            }
            if (st == null) break;
            list.add(Integer.parseInt(st.nextToken()));
        }
        
        int[] demand = new int[list.size()];
        for(int i=0; i<list.size(); i++) demand[i] = list.get(i);
        
        Solution sol = new Solution();
        int[] res = sol.spans(demand);
        for (int val : res) {
            System.out.println(val);
        }
    }
}
```

### Python

```python
def spans(demand: list[int]) -> list[int]:
    return []
def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if not lines:
        return

    n = int(lines[0])
    demand = list(map(int, lines[1].split()))
    result = spans(demand)
    for r in result:
        print(r)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> spans(vector<int>& demand) {
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> demand(n);
    for (int i = 0; i < n; i++) {
        cin >> demand[i];
    }
    
    Solution sol;
    vector<int> res = sol.spans(demand);
    
    for (int val : res) {
        cout << val << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  spans(demand) {
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
  const demand = [];
  for (let i = 0; i < n; i++) {
    demand.push(parseInt(data[idx++], 10));
  }
  
  const solution = new Solution();
  const res = solution.spans(demand);
  console.log(res.join("\n"));
});
```

