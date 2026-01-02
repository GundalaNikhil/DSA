---
problem_id: BIT_MAX_SUBARRAY_XOR_START__8405
display_id: BIT-005
slug: max-subarray-xor-with-start
title: "Max Subarray XOR With Start"
difficulty: Medium
difficulty_score: 50
topics:
  - Bitwise Operations
  - XOR
  - Trie
  - Prefix Sum
tags:
  - bitwise
  - xor
  - trie
  - prefix-xor
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-005: Max Subarray XOR With Start

## Problem Statement

Given an array of integers and a fixed starting index `s`, find the subarray `a[s...k]` (where `k >= s`) that has the maximum XOR sum.

![Problem Illustration](../images/BIT-005/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]
- Third line: integer s (0-based)

## Output Format

Print the maximum XOR of a subarray starting at s.

## Constraints

- `1 <= n <= 200000`
- `0 <= a[i] <= 1000000000`

## Example

**Input:**

```
4
3 8 2 6
1
```

**Output:**

```
12
```

**Explanation:**

The subarray [8, 2, 6] has XOR 12, which is the maximum among subarrays starting at 1.

![Example Visualization](../images/BIT-005/example-1.png)

## Notes

- Index s is 0-based.
- The subarray must start at s but can end at any index >= s.

## Related Topics

Bitwise Operations, XOR, Trie

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long maxSubarrayXorWithStart(int[] a, int s) {
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        int s = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.maxSubarrayXorWithStart(a, s));
        sc.close();
    }
}
```

### Python

```python
import sys

def max_subarray_xor_with_start(a: list[int], s: int) -> int:
    return 0
def main():
    input_data = sys.stdin.read()
    data = input_data.split()
    if not data: return
    
    ptr = 0
    n = int(data[ptr]); ptr += 1
    a = []
    for _ in range(n):
        a.append(int(data[ptr])); ptr += 1
    
    s = int(data[ptr]); ptr += 1
    
    result = max_subarray_xor_with_start(a, s)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    long long maxSubarrayXorWithStart(vector<int>& a, int s) {
        long long currentXor = 0;
        long long maxXor = 0;
        bool first = true;
        
        for (int i = s; i < a.size(); i++) {
            currentXor ^= a[i];
            if (first) {
                maxXor = currentXor;
                first = false;
            } else {
                maxXor = max(maxXor, currentXor);
            }
        }
        return maxXor;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    int s;
    cin >> s;
    
    Solution solution;
    cout << solution.maxSubarrayXorWithStart(a, s) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxSubarrayXorWithStart(a, s) {
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
    const a = [];
    for (let i = 0; i < n; i++) a.push(Number(tokens[ptr++]));
    const s = Number(tokens[ptr++]);
    
    const solution = new Solution();
    console.log(String(solution.maxSubarrayXorWithStart(a, s)));
});
```

