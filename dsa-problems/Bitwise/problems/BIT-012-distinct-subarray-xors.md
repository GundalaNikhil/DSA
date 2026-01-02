---
problem_id: BIT_DISTINCT_SUBARRAY_XORS__8412
display_id: BIT-012
slug: distinct-subarray-xors
title: "Distinct Subarray XORs"
difficulty: Medium
difficulty_score: 55
topics:
  - Bitwise Operations
  - XOR
  - Subarray
  - Trie
tags:
  - bitwise
  - xor
  - subarray
  - trie
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-012: Distinct Subarray XORs

## Problem Statement

Count the number of **distinct** values obtained by XORing elements of all possible subarrays of `a`.

![Problem Illustration](../images/BIT-012/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]

## Output Format

Print the number of distinct subarray XOR values.

## Constraints

- `1 <= n <= 10000`
- `0 <= a[i] <= 1000000000`

## Example

**Input:**

```
3
1 2 3
```

**Output:**

```
4
```

**Explanation:**

The distinct XORs across all subarrays are {0, 1, 2, 3}.

![Example Visualization](../images/BIT-012/example-1.png)

## Notes

- The total number of subarrays is n \* (n + 1) / 2.
- Use a set to track distinct XOR results.

## Related Topics

Bitwise Operations, Prefix XOR

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long distinctSubarrayXors(int[] a) {
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

        Solution solution = new Solution();
        System.out.println(solution.distinctSubarrayXors(a));
        sc.close();
    }
}
```

### Python

```python
import sys

def distinct_subarray_xors(a: list[int]) -> int:
    return 0
def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    ptr = 0
    n = int(data[ptr]); ptr += 1
    a = []
    for _ in range(n):
        a.append(int(data[ptr])); ptr += 1
        
    result = distinct_subarray_xors(a)
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
    long long distinctSubarrayXors(vector<int>& a) {
        int n = a.size();
        long long size = (long long)n * (n + 1) / 2;
        vector<int> results;
        results.reserve(size);
        
        for (int i = 0; i < n; i++) {
            int currentXor = 0;
            for (int j = i; j < n; j++) {
                currentXor ^= a[j];
                results.push_back(currentXor);
            }
        }
        
        sort(results.begin(), results.end());
        
        // Count unique
        if (results.empty()) return 0;
        long long count = 1;
        for (size_t i = 1; i < results.size(); i++) {
            if (results[i] != results[i-1]) {
                count++;
            }
        }
        return count;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    Solution solution;
    cout << solution.distinctSubarrayXors(a) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  distinctSubarrayXors(a) {
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
    
    const solution = new Solution();
    console.log(String(solution.distinctSubarrayXors(a)));
});
```

