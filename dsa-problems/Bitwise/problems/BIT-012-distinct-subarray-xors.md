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

Compute the number of distinct XOR values that appear among all possible subarrays.

## Input Format

- First line: Integer `n`
- Second line: `n` space-separated integers

## Output Format

Single integer representing count of distinct XOR values

## Constraints

- `1 <= n <= 10^4`
- `0 <= a[i] <= 10^9`

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

All subarrays and their XORs:

| Subarray | Calculation | XOR Value |
|----------|-------------|-----------|
| [1] | 1 | 1 |
| [2] | 2 | 2 |
| [3] | 3 | 3 |
| [1,2] | 1⊕2 | 3 |
| [2,3] | 2⊕3 | 1 |
| [1,2,3] | 1⊕2⊕3 | 0 |

**Distinct XOR values:** {0, 1, 2, 3}

**Count:** 4 distinct values

**Note:** There are 6 total subarrays, but only 4 have distinct XOR values (some values appear multiple times).

## Notes

- Use prefix XOR with Trie
- Track unique XOR values incrementally

## Related Topics

XOR Prefix, Trie, Subarray XOR, Set Operations

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int distinctSubarrayXORs(int[] a) {
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        Solution solution = new Solution();
        System.out.println(solution.distinctSubarrayXORs(a));
        sc.close();
    }
}
```

### Python

```python
def distinct_subarray_xors(a: list[int]) -> int:
    return 0

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(distinct_subarray_xors(a))

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
    int distinctSubarrayXORs(vector<int>& a) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    Solution solution;
    cout << solution.distinctSubarrayXORs(a) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  distinctSubarrayXORs(a) {
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
  const n = parseInt(data[0]);
  const a = data[1].split(" ").map(Number);
  const solution = new Solution();
  console.log(solution.distinctSubarrayXORs(a));
});
```
