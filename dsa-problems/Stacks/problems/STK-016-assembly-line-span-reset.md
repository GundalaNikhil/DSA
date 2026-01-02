---
problem_id: STK_ASSEMBLY_LINE_SPAN_RESET__3846
display_id: STK-016
slug: assembly-line-span-reset
title: "Assembly Line Span Reset"
difficulty: Medium
difficulty_score: 45
topics:
  - Stack
  - Spans
  - Arrays
tags:
  - stack
  - spans
  - arrays
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-016: Assembly Line Span Reset

## Problem Statement

Given daily production counts, compute for each day the span of consecutive prior days with counts strictly less than today's count. The span includes today as 1.

Return the span counts.

![Problem Illustration](../images/STK-016/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers

## Output Format

- Single line: `n` integers of spans

## Constraints

- `1 <= n <= 100000`
- `0 <= count[i] <= 10^9`

## Example

**Input:**

```
5
2 1 3 2 5
```

**Output:**

```
1 1 3 1 5
```

**Explanation:**

Day 3 (value 3) covers days 1..3, and day 5 covers all prior days.

![Example Visualization](../images/STK-016/example-1.png)

## Notes

- Use a monotonic decreasing stack of (value, span)
- Pop while top value is strictly less than current
- Add spans as you pop
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
    public int[] spans(int[] counts) {
        // Implementation here
        return new int[0];
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
        
        int[] counts = new int[list.size()];
        for(int i=0; i<list.size(); i++) counts[i] = list.get(i);
        
        Solution sol = new Solution();
        int[] res = sol.spans(counts);
        for (int val : res) {
            System.out.println(val);
        }
    }
}
```

### Python

```python
import sys

def spans(counts: list[int]) -> list[int]:
    # Implementation here
    return []

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if not lines:
        return

    n = int(lines[0])
    counts = list(map(int, lines[1].split()))
    result = spans(counts)
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
    vector<int> spans(vector<int>& counts) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> counts(n);
    for (int i = 0; i < n; i++) {
        cin >> counts[i];
    }
    
    Solution sol;
    vector<int> res = sol.spans(counts);
    
    for (int val : res) {
        cout << val << "\n";
    }
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  spans(counts) {
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
  const counts = [];
  for (let i = 0; i < n; i++) {
    counts.push(parseInt(data[idx++], 10));
  }
  
  const solution = new Solution();
  const res = solution.spans(counts);
  console.log(res.join("\n"));
});
```
