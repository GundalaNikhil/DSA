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

Given an array of non-negative integers and a starting index `s`, find the maximum XOR value of any contiguous subarray that **starts at index `s`**.

In other words, find the maximum value of `a[s] XOR a[s+1] XOR ... XOR a[j]` for all valid `j >= s`.

```
ASCII Diagram: Subarray XOR from Start
=======================================
Array: [3, 8, 2, 6], s = 1

Index:  0   1   2   3
Value:  3   8   2   6
            ↑
            s (start)

Valid subarrays starting at s=1:
1. [8]         → XOR = 8
2. [8,2]       → XOR = 8 XOR 2 = 10
3. [8,2,6]     → XOR = 8 XOR 2 XOR 6 = 14 ← Maximum!

Calculation details:
[8]     : 1000
[8,2]   : 1000 XOR 0010 = 1010 = 10
[8,2,6] : 1010 XOR 0110 = 1100 = 14

Result: 14
```

## Input Format

- First line: Two integers `n` and `s` - array size and starting index
- Second line: `n` space-separated integers representing array `a`

## Output Format

A single integer representing the maximum XOR value

## Constraints

- `1 <= n <= 2 * 10^5`
- `0 <= s < n`
- `0 <= a[i] <= 10^9`
- All array elements are non-negative integers

## Example

**Input:**

```
4 1
3 8 2 6
```

**Output:**

```
14
```

**Explanation:**

Starting from index `s = 1`:

```
Subarray Analysis:
==================
[8]:       XOR = 8       = 1000 (binary)
[8,2]:     XOR = 8^2     = 1010 (binary) = 10
[8,2,6]:   XOR = 8^2^6   = 1100 (binary) = 14 ✓ Maximum

Step-by-step for [8,2,6]:
  8  = 1000
  2  = 0010
  6  = 0110

  8 XOR 2:
    1000
  ^ 0010
  -------
    1010 = 10

  10 XOR 6:
    1010
  ^ 0110
  -------
    1100 = 14

Maximum XOR = 14
```

```
ASCII Bit-level Visualization:
===============================
Position: 3 2 1 0
         ───────────
8:        1 0 0 0
2:        0 0 1 0
Result:   1 0 1 0 (10)

10:       1 0 1 0
6:        0 1 1 0
Result:   1 1 0 0 (14)
```

## Notes

- Only subarrays starting at index `s` are considered
- A single element subarray `[a[s]]` is valid
- XOR is associative: `(a XOR b) XOR c = a XOR (b XOR c)`
- Prefix XOR technique can be used for optimization
- Consider using a Trie for efficiently finding maximum XOR

## Related Topics

XOR Properties, Prefix XOR, Trie Data Structure, Maximum XOR

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int maxSubarrayXOR(int[] a, int s) {
        // Your implementation here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int s = sc.nextInt();

        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        int result = solution.maxSubarrayXOR(a, s);

        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
def max_subarray_xor(a: list[int], s: int) -> int:
    # Your implementation here
    return 0

def main():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))

    result = max_subarray_xor(a, s)
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
    int maxSubarrayXOR(vector<int>& a, int s) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, s;
    cin >> n >> s;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    Solution solution;
    cout << solution.maxSubarrayXOR(a, s) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxSubarrayXOR(a, s) {
    // Your implementation here
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
  let ptr = 0;
  const [n, s] = data[ptr++].split(" ").map(Number);
  const a = data[ptr++].split(" ").map(Number);

  const solution = new Solution();
  console.log(solution.maxSubarrayXOR(a, s));
});
```
