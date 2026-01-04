---
problem_id: SRT_SEARCH_ROTATED_DUPLICATES_PARITY__9062
display_id: SRT-007
slug: search-rotated-duplicates-parity
title: "Search Rotated With Duplicates Parity Count"
difficulty: Medium
difficulty_score: 52
topics:
  - Sorting
  - Binary Search
  - Rotated Arrays
tags:
  - binary-search
  - rotated-array
  - duplicates
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# SRT-007: Search Rotated With Duplicates Parity Count

## Problem Statement

Given a rotated sorted array that may contain duplicates, count how many occurrences of a value `x` appear at even indices.

Indices are 0-based.

![Problem Illustration](../images/SRT-007/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers
- Third line: integer `x`

## Output Format

- Single integer: count of occurrences of `x` at even indices

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a[i], x <= 10^9`

## Example

**Input:**

```
6
4 5 5 1 2 3
5
```

**Output:**

```
1
```

**Explanation:**

Value 5 appears at indices 1 and 2; only index 2 is even.

![Example Visualization](../images/SRT-007/example-1.png)

## Notes

- Find the rotation pivot to map to a sorted order
- Use binary search to locate the range of `x`
- Count how many indices in the occurrence range are even
- Time complexity: O(log n)

## Related Topics

Binary Search, Rotated Array, Counting

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int countEvenIndices(int n, int[] a, int x) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] a = new int[n];
            for (int i = 0; i < n; i++) a[i] = sc.nextInt();
            int x = sc.nextInt();

            Solution sol = new Solution();
            System.out.println(sol.countEvenIndices(n, a, x));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def count_even_indices(self, n: int, a: list, x: int) -> int:
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    a = [int(val) for val in input_data[1:1+n]]
    x = int(input_data[1+n])

    sol = Solution()
    print(sol.count_even_indices(n, a, x))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int countEvenIndices(int n, vector<int>& a, int x) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (cin >> n) {
        vector<int> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];
        int x;
        cin >> x;

        Solution sol;
        cout << sol.countEvenIndices(n, a, x) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countEvenIndices(n, a, x) {
    // Implement here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

let input = [];
rl.on("line", (line) => {
  if (line.trim()) input.push(...line.trim().split(/\s+/));
}).on("close", () => {
  if (input.length < 2) return;
  const n = parseInt(input[0]);
  const a = input.slice(1, 1 + n).map(Number);
  const x = parseInt(input[1 + n]);

  const sol = new Solution();
  console.log(sol.countEvenIndices(n, a, x));
});
```
