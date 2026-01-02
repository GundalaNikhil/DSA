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
import java.io.*;

class Solution {
    private int findNearestGreater(List<Integer> stack, int val, int[] arr) {
        // Stack stores indices. 
        // arr[stack[i]] is decreasing as i increases.
        // We want largest index (largest i) such that arr[stack[i]] > val.
        // Since decreasing, valid prefix: [0 ... k]. We want k.
        
        if (stack.isEmpty()) return -1;
        
        int l = 0, r = stack.size() - 1;
        int ansIdx = -1;
        
        while (l <= r) {
            int mid = l + (r - l) / 2;
            int idx = stack.get(mid);
            if (arr[idx] > val) {
                ansIdx = idx;
                l = mid + 1; // Try to find rightmost (larger index/smaller value that is still > val)
            } else {
                r = mid - 1;
            }
        }
        return ansIdx;
    }

    public int[] prevGreaterOppositeParity(int[] arr) {
        return null;
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // Read N (ignores empty lines)
        String line = "";
        while ((line = br.readLine()) != null && line.trim().isEmpty()) {}
        if (line == null) return;
        
        String startLine = line;
        // The numbers could be on same line or next line
        // Use StringTokenizer
        StringTokenizer st = new StringTokenizer(startLine);
        if (!st.hasMoreTokens()) st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int[] arr = new int[n];
        int loaded = 0;
        
        while (loaded < n) {
            if (!st.hasMoreTokens()) {
                String l = br.readLine();
                if (l == null) break;
                st = new StringTokenizer(l);
            }
            if (st.hasMoreTokens()) {
                arr[loaded++] = Integer.parseInt(st.nextToken());
            }
        }
        
        Solution sol = new Solution();
        int[] res = sol.prevGreaterOppositeParity(arr);
        for (int v : res) {
            System.out.println(v);
        }
    }
}
```

### Python

```python
def prev_greater_opposite_parity(arr: list[int]) -> list[int]:
    return []
def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if not lines:
        return

    n = int(lines[0])
    arr = list(map(int, lines[1].split()))
    result = prev_greater_opposite_parity(arr)
    for r in result:
        print(r)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
    int findNearestGreater(const vector<int>& stack, int val, const vector<int>& arr) {
        return 0;
    }

public:
    vector<int> prevGreaterOppositeParity(vector<int>& arr) {
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    Solution sol;
    vector<int> res = sol.prevGreaterOppositeParity(arr);
    
    for (int val : res) {
        cout << val << "\n";
    }
    
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  findNearestGreater(stack, val, arr) {
    return 0;
  }

  prevGreaterOppositeParity(arr) {
    return 0;
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/).filter(x => x !== "");
  for (const p of parts) data.push(p);
});

rl.on("close", () => {
  if (data.length === 0) return;
  
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const arr = [];
  for (let i = 0; i < n; i++) {
    arr.push(parseInt(data[idx++], 10));
  }
  
  const solution = new Solution();
  const res = solution.prevGreaterOppositeParity(arr);
  console.log(res.join("\n"));
});
```

