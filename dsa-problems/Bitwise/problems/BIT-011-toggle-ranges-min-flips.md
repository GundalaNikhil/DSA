---
problem_id: BIT_TOGGLE_RANGES_MIN_FLIPS__8411
display_id: BIT-011
slug: toggle-ranges-min-flips
title: "Toggle Ranges Minimum Flips"
difficulty: Medium
difficulty_score: 45
topics:
  - Bitwise Operations
  - Array
  - Greedy
  - Flipping
tags:
  - bitwise
  - array-transformation
  - greedy
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-011: Toggle Ranges Minimum Flips

## Problem Statement

You may flip all bits in any chosen subarray (0 -> 1, 1 -> 0). Find the minimum number of flips required to convert binary array A into binary array B.

![Problem Illustration](../images/BIT-011/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated bits of A
- Third line: n space-separated bits of B

## Output Format

Print the minimum number of flips.

## Constraints

- `1 <= n <= 200000`

## Example

**Input:**
```
4
0 1 1 0
1 0 1 1
```

**Output:**
```
2
```

**Explanation:**

Mismatch segments are indices 0..1 and 3, so two flips are sufficient.

![Example Visualization](../images/BIT-011/example-1.png)

## Notes

- A flip inverts every bit in the chosen subarray.
- Count contiguous mismatch runs to minimize flips.

## Related Topics

Bitwise Operations, Greedy

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int toggleRangesMinFlips(int[] A, int[] B) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] A = new int[n];
        for (int i = 0; i < n; i++) A[i] = sc.nextInt();
        int[] B = new int[n];
        for (int i = 0; i < n; i++) B[i] = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.toggleRangesMinFlips(A, B));
        sc.close();
    }
}
```

### Python

```python
import sys

def toggle_ranges_min_flips(A: list[int], B: list[int]) -> int:
    # Implementation here
    return 0

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    ptr = 0
    n = int(data[ptr]); ptr += 1
    A = []
    for _ in range(n):
        A.append(int(data[ptr])); ptr += 1
    B = []
    for _ in range(n):
        B.append(int(data[ptr])); ptr += 1
        
    result = toggle_ranges_min_flips(A, B)
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
    int toggleRangesMinFlips(vector<int>& A, vector<int>& B) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> A(n);
    for (int i = 0; i < n; i++) cin >> A[i];
    vector<int> B(n);
    for (int i = 0; i < n; i++) cin >> B[i];

    Solution solution;
    cout << solution.toggleRangesMinFlips(A, B) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  toggleRangesMinFlips(A, B) {
    // Implementation here
    return null;
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
    const A = [];
    for (let i = 0; i < n; i++) A.push(Number(tokens[ptr++]));
    const B = [];
    for (let i = 0; i < n; i++) B.push(Number(tokens[ptr++]));
    
    const solution = new Solution();
    console.log(solution.toggleRangesMinFlips(A, B));
});
```
