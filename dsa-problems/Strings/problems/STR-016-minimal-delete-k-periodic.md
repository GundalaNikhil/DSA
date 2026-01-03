---
problem_id: STR_MINIMAL_DELETE_K_PERIODIC__1016
display_id: STR-016
slug: minimal-delete-k-periodic
title: "Minimal Delete to Make K-Periodic"
difficulty: Medium
difficulty_score: 39
topics:
  - String Manipulation
  - Greedy
  - Frequency Analysis
tags:
  - periodicity
  - deletion
  - position-class
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-016: Minimal Delete to Make K-Periodic

## Problem Statement

Given a string `s` and an integer `k`, delete the minimum number of characters so that the resulting string is periodic with period exactly `k` (can be written as repetitions of a k-length block).

## Input Format

- First line: String `s` (1 ≤ |s| ≤ 10^5)
- Second line: Integer `k` (1 ≤ k ≤ |s|)

## Output Format

- A single integer representing minimum deletions

## Constraints

- `1 ≤ |s| ≤ 10^5`
- `1 ≤ k ≤ |s|`
- `s` contains only lowercase English letters

## Example 1

**Input:**

```
abac
2
```

**Output:**

```
1
```

**Explanation:**

- Position 0 (mod 2): 'a','a' → keep 'a'
- Position 1 (mod 2): 'b','c' → keep 'b' (or 'c')
- Delete 'c' → 1 deletion
- Pattern: "ab" repeated

## Example 2

**Input:**

```
aabbcc
3
```

**Output:**

```
3
```

**Explanation:**

- For each position mod 3, keep most frequent character
- Total deletions needed: 3

## Notes

- Group positions by i mod k
- Keep most frequent char at each position class
- O(n) greedy algorithm

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int minimalDeleteKPeriodic(String s, int k) {
        //Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int k = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.minimalDeleteKPeriodic(s, k));
        sc.close();
    }
}
```

### Python

```python
def minimal_delete_k_periodic(s: str, k: int) -> int:
    # //Implement here
    return 0

def main():
    import sys


    # Read input
    input_data = sys.stdin.read().strip()
    if not input_data:
        print(0)
        return
        
    parts = input_data.split()
    if len(parts) >= 2:
        s = parts[0]
        try:
            k = int(parts[1])
            print(minimal_delete_k_periodic(s, k))
        except ValueError:
            pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
using namespace std;

#include <algorithm>
#include <string>
#include <vector>
#include <iostream>

class Solution {
public:
    int minimalDeleteKPeriodic(string s, int k) {
        //Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s; cin >> s;
    int k; cin >> k;
    Solution sol;
    cout << sol.minimalDeleteKPeriodic(s, k) << endl;
    return 0;
}
```

### JavaScript

```javascript
function minimalDeleteKPeriodic(s, k) {
  //Implement here
  return 0;
}

const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const s = tokens[ptr++];
    const k = parseInt(tokens[ptr++]);
    console.log(minimalDeleteKPeriodic(s, k));
});
```
