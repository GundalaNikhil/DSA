---
problem_id: STK_ROOFTOP_SUNSET_COUNT__2974
display_id: STK-004
slug: rooftop-sunset-count
title: "Rooftop Sunset Count"
difficulty: Easy
difficulty_score: 32
topics:
  - Stack
  - Monotonic Stack
  - Arrays
tags:
  - stack
  - monotonic
  - arrays
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-004: Rooftop Sunset Count

## Problem Statement

Given building heights from west to east, a building can see the sunset if there is no taller building to its left. Count how many buildings can see the sunset.

![Problem Illustration](../images/STK-004/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers (heights)

## Output Format

- Single integer: number of buildings with sunset view

## Constraints

- `1 <= n <= 200000`
- `0 <= h[i] <= 10^9`

## Example

**Input:**

```
5
2 5 2 6 1
```

**Output:**

```
3
```

**Explanation:**

Buildings with sunset view are heights 2, 5, and 6.

![Example Visualization](../images/STK-004/example-1.png)

## Notes

- Use a monotonic decreasing stack
- Pop while current height is greater than or equal to stack top
- Count remaining stack size at the end
- Time complexity: O(n)

## Related Topics

Monotonic Stack, Visibility, Arrays

---

## Solution Template
### Java

```java
import java.util.*;
import java.io.*;
import java.math.BigInteger;

class Solution {
    public int countVisible(BigInteger[] h) {
        //Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line1 = br.readLine();
        if (line1 == null) return;
        
        String line2 = br.readLine();
        if (line2 == null) return;
        
        String[] parts = line2.trim().split("\\s+");
        List<BigInteger> hList = new ArrayList<>();
        
        for (String p : parts) {
            if (!p.isEmpty()) {
                hList.add(new BigInteger(p));
            }
        }
        
        BigInteger[] h = hList.toArray(new BigInteger[0]);
        Solution sol = new Solution();
        System.out.println(sol.countVisible(h));
    }
}
```

### Python

```python
def count_visible(h: list[int]) -> int:
    # //Implement here
    return 0

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if not lines:
        return

    n = int(lines[0])
    h = list(map(int, lines[1].split()))
    result = count_visible(h)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <stack>
#include <string>
#include <sstream>

using namespace std;

class Solution {
public:
    int countVisible(vector<string>& h) {
        //Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string line;
    // Read N (line 1)
    if (!getline(cin, line)) return 0;
    
    // Read Array (line 2)
    if (!getline(cin, line)) return 0;
    
    stringstream ss(line);
    string val;
    vector<string> h;
    while (ss >> val) {
        h.push_back(val);
    }
    
    Solution sol;
    cout << sol.countVisible(h) << endl;
    
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  countVisible(h) {
    //Implement here
    return 0;
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => {
  lines.push(line);
});

rl.on("close", () => {
  if (lines.length < 2) return;
  
  // Line 0 is N, ignore
  // Line 1 is the array
  const parts = lines[1].trim().split(/\s+/).filter(x => x !== "");
  const h = parts.map(x => BigInt(x));
  
  const solution = new Solution();
  console.log(solution.countVisible(h));
});
```

