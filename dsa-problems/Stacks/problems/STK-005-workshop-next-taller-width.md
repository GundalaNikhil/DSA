---
problem_id: STK_WORKSHOP_NEXT_TALLER_WIDTH__8156
display_id: STK-005
slug: workshop-next-taller-width
title: "Workshop Next Taller with Width"
difficulty: Medium
difficulty_score: 45
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
# STK-005: Workshop Next Taller with Width

## Problem Statement

For each height `h[i]`, find the next taller height to its right within distance at most `w`. If no taller height exists within `w`, output `-1` for that position.

![Problem Illustration](../images/STK-005/problem-illustration.png)

## Input Format

- First line: integers `n` and `w`
- Second line: `n` space-separated integers

## Output Format

- Single line: `n` integers, the next taller heights or `-1`

## Constraints

- `1 <= n <= 200000`
- `0 <= h[i] <= 10^9`
- `1 <= w <= n`

## Example

**Input:**

```
5 2
1 7 3 4 2
```

**Output:**

```
7 -1 4 -1 -1
```

**Explanation:**

For index 0, the next taller within distance 2 is 7. For index 2, 4 is taller and within width.

![Example Visualization](../images/STK-005/example-1.png)

## Notes

- Use a monotonic decreasing stack of indices
- Remove indices that are more than `w` away
- Pop while current height is taller to resolve answers
- Time complexity: O(n)

## Related Topics

Monotonic Stack, Next Greater Element, Sliding Window

---

## Solution Template
### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int[] nextTallerWithin(int[] h, int w) {
        //Implement here
        return new int[0];
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // Read N (Line 1) or first token
        String line = "";
        while ((line = br.readLine()) != null && line.trim().isEmpty()) {}
        if (line == null) return;
        
        // We might need to handle token-based parsing robustly
        // Problem format: N, then Array, then W.
        // Array tokens might be on second line. W on third line.
        // Or all spread out.
        // Let's use a tokenizer approach.
        
        StringTokenizer st = new StringTokenizer(line);
        if (!st.hasMoreTokens()) st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int[] h = new int[n];
        
        int loaded = 0;
        while (loaded < n) {
            if (!st.hasMoreTokens()) {
                String l = br.readLine();
                if (l == null) break;
                st = new StringTokenizer(l);
            }
            if (st.hasMoreTokens()) {
                h[loaded++] = Integer.parseInt(st.nextToken());
            }
        }
        
        // Read W
        while (!st.hasMoreTokens()) {
            String l = br.readLine();
            if (l == null) break;
            st = new StringTokenizer(l);
        }
        int w = 0;
        if (st.hasMoreTokens()) {
            w = Integer.parseInt(st.nextToken());
        }
        
        Solution sol = new Solution();
        int[] res = sol.nextTallerWithin(h, w);
        for (int val : res) {
            System.out.println(val);
        }
    }
}
```

### Python

```python
def next_taller_within(h: list[int], w: int) -> list[int]:
    # //Implement here
    return 0

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if not lines:
        return

    n = int(lines[0])
    h = list(map(int, lines[1].split()))
    w = int(lines[2])
    result = next_taller_within(h, w)
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
    vector<int> nextTallerWithin(vector<int>& h, int w) {
        //Implement here
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
    
    int w;
    cin >> w;
    
    Solution sol;
    vector<int> res = sol.nextTallerWithin(h, w);
    
    for (int val : res) {
        cout << val << "\n";
    }
    
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  nextTallerWithin(h, w) {
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
  const h = [];
  for (let i = 0; i < n; i++) {
    h.push(parseInt(data[idx++], 10));
  }
  const w = parseInt(data[idx++], 10);
  
  const solution = new Solution();
  const res = solution.nextTallerWithin(h, w);
  console.log(res.join("\n"));
});
```

