---
problem_id: REC_CAMPUS_LIGHTS_PLACEMENT__4928
display_id: REC-007
slug: campus-lights-placement
title: "Campus Lights Placement"
difficulty: Medium
difficulty_score: 47
topics:
  - Recursion
  - Backtracking
  - Combinations
tags:
  - recursion
  - backtracking
  - combinations
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-007: Campus Lights Placement

## Problem Statement

A campus walkway has `n` positions labeled `0` to `n-1`. Place exactly `k` lights so that any two lights are at least `d` positions apart (absolute difference >= `d`).

Generate all valid sets of positions in increasing order.

![Problem Illustration](../images/REC-007/problem-illustration.png)

## Input Format

- First line: integers `n`, `k`, and `d`

## Output Format

- Each valid placement on its own line as space-separated positions
- Output `NONE` if no valid placement exists

## Constraints

- `1 <= n <= 12`
- `0 <= k <= n`
- `0 <= d <= n`

## Example

**Input:**

```
5 2 2
```

**Output:**

```
0 2
0 3
1 3
1 4
2 4
```

**Explanation:**

Each listed pair has distance at least 2.

![Example Visualization](../images/REC-007/example-1.png)

## Notes

- Build positions in increasing order to avoid duplicates
- Prune when remaining positions are insufficient
- Track the last chosen position to enforce distance
- Time complexity is exponential in `n`

## Related Topics

Backtracking, Combinatorics, Recursion

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public List<List<Integer>> placeLights(int n, int k, int d) {
        //Implement here
        return new ArrayList<>();
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int k = sc.nextInt();
        int d = sc.nextInt();
        
        Solution sol = new Solution();
        List<List<Integer>> res = sol.placeLights(n, k, d);
        if(res.isEmpty()) {
            System.out.println("NONE");
        } else {
            for(List<Integer> row : res) {
                for(int i=0; i<row.size(); i++) {
                    System.out.print(row.get(i) + (i==row.size()-1?"":" "));
                }
                System.out.println();
            }
        }
        sc.close();
    }
}
```

### Python

```python
def place_lights(n: int, k: int, d: int) -> list[list[int]]:
    # //Implement here
    return 0

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n, k, d = map(int, data[:3])
    result = place_lights(n, k, d)
    if not result:
        print("NONE")
    else:
        for combo in result:
            print(" ".join(str(x) for x in combo))

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
    vector<vector<int>> placeLights(int n, int k, int d) {
        //Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, k, d;
    if (!(cin >> n >> k >> d)) return 0;
    
    Solution sol;
    vector<vector<int>> res = sol.placeLights(n, k, d);
    
    if (res.empty()) {
        cout << "NONE" << endl;
    } else {
        for(const auto& row : res) { 
            for(size_t i=0; i<row.size(); i++) cout << row[i] << (i==row.size()-1?"":" "); 
            cout << endl; 
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const n = parseInt(tokens[ptr++]);
    const k = parseInt(tokens[ptr++]);
    const d = parseInt(tokens[ptr++]);
    
    const sol = new Solution();
    const res = sol.placeLights(n, k, d);
    
    if (res.length === 0) {
        console.log("NONE");
    } else {
        res.forEach(row => console.log(row.join(' ')));
    }
});

class Solution {
  placeLights(n, k, d) {
    //Implement here
    return 0;
  }
}
```

