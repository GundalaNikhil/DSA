---
problem_id: STK_BIKE_REPAIR_PLATES__5937
display_id: STK-015
slug: bike-repair-plates
title: "Bike Repair Plates"
difficulty: Medium
difficulty_score: 47
topics:
  - Stack
  - Monotonic Stack
  - Simulation
tags:
  - stack
  - monotonic
  - simulation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-015: Bike Repair Plates

## Problem Statement

You have a stack of metal plates with diameters, listed from top to bottom. Plates are removed one by one from the top. If a plate is smaller than a plate beneath it at the moment that plate is revealed, the lower plate is marked unsafe.

Count how many plates become unsafe during the entire removal process.

![Problem Illustration](../images/STK-015/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers (diameters, top to bottom)

## Output Format

- Single integer: number of unsafe plates

## Constraints

- `1 <= n <= 200000`
- `1 <= d[i] <= 10^9`

## Example

**Input:**

```
3
5 2 4
```

**Output:**

```
1
```

**Explanation:**

When the top plate 5 is removed, 2 is revealed (safe). When 2 is removed, 4 is revealed and marked unsafe because 2 < 4.

![Example Visualization](../images/STK-015/example-1.png)

## Notes

- Scan from top to bottom
- Track the last removed plate diameter
- A plate is unsafe if it is larger than the plate removed just above it
- Time complexity: O(n)

## Related Topics

Stack Simulation, Monotonic Patterns, Arrays

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int countUnsafe(int[] d) {
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
        
        // Read Array (robust)
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
        
        int[] d = new int[list.size()];
        for(int i=0; i<list.size(); i++) d[i] = list.get(i);
        
        Solution sol = new Solution();
        System.out.println(sol.countUnsafe(d));
    }
}
```

### Python

```python
def count_unsafe(d: list[int]) -> int:
    return 0
def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    n = int(lines[0])
    d = list(map(int, lines[1].split()))
    result = count_unsafe(d)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int countUnsafe(vector<int>& d) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> d(n);
    for (int i = 0; i < n; i++) {
        cin >> d[i];
    }
    
    Solution sol;
    cout << sol.countUnsafe(d) << endl;
    
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  countUnsafe(d) {
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
  const d = [];
  for (let i = 0; i < n; i++) {
    d.push(parseInt(data[idx++], 10));
  }
  
  const solution = new Solution();
  console.log(solution.countUnsafe(d));
});
```

