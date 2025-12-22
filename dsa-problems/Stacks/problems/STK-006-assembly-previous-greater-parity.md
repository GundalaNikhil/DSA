---
problem_id: STK_ASSEMBLY_PREVIOUS_GREATER_PARITY__6802
display_id: STK-006
slug: assembly-previous-greater-parity
title: "Assembly Previous Greater with Parity"
difficulty: Medium
difficulty_score: 46
topics:
  - Stack
  - Monotonic Stack
  - Parity
tags:
  - stack
  - monotonic
  - parity
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-006: Assembly Previous Greater with Parity

## Problem Statement

For each element `a[i]`, find the nearest element to its left that is strictly greater and has opposite parity (one even, one odd). If no such element exists, output `-1` for that position.

![Problem Illustration](../images/STK-006/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers

## Output Format

- Single line: `n` integers, the previous greater with opposite parity or `-1`

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a[i] <= 10^9`

## Example

**Input:**

```
5
2 9 5 7 3
```

**Output:**

```
-1 2 9 9 9
```

**Explanation:**

For 9 (odd), previous greater with opposite parity is 2. For 5 (odd), previous greater even is 9.

![Example Visualization](../images/STK-006/example-1.png)

## Notes

- Maintain separate monotonic stacks for even and odd values
- Pop smaller values while searching for a greater element
- Each element is pushed and popped at most once
- Time complexity: O(n)

## Related Topics

Monotonic Stack, Parity, Previous Greater Element

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public int[] prevGreaterOppositeParity(int[] arr) {
        // Your implementation here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        Solution solution = new Solution();
        int[] result = solution.prevGreaterOppositeParity(arr);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            if (i > 0) sb.append(' ');
            sb.append(result[i]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
```

### Python

```python
def prev_greater_opposite_parity(arr: list[int]) -> list[int]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    arr = [int(x) for x in data[1:1+n]]

    result = prev_greater_opposite_parity(arr)
    sys.stdout.write(" ".join(str(x) for x in result))

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
    vector<int> prevGreaterOppositeParity(const vector<int>& arr) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];

    Solution solution;
    vector<int> result = solution.prevGreaterOppositeParity(arr);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i) cout << ' ';
        cout << result[i];
    }
    cout << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  prevGreaterOppositeParity(arr) {
    // Your implementation here
    return [];
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(parseInt(data[idx++], 10));

  const solution = new Solution();
  const result = solution.prevGreaterOppositeParity(arr);
  console.log(result.join(" "));
});
```
