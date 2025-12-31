---
problem_id: SRT_BALANCED_RANGE_COVERING_K_LISTS__5746
display_id: SRT-008
slug: balanced-range-covering-k-lists
title: "Balanced Range Covering K Lists"
difficulty: Medium
difficulty_score: 58
topics:
  - Sorting
  - Sliding Window
  - Heaps
tags:
  - sorting
  - sliding-window
  - heap
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SRT-008: Balanced Range Covering K Lists

## Problem Statement

You are given `k` sorted lists. Find an interval `[L, R]` of minimum length that contains at least two numbers from each list. If a list has only one number, that single number must appear in the interval.

Return any one optimal interval. If no such interval exists, output `NONE`.

![Problem Illustration](../images/SRT-008/problem-illustration.png)

## Input Format

- First line: integer `k`
- Next `k` blocks:
  - First line of block: integer `m` (size of list)
  - Second line of block: `m` space-separated integers (sorted)

## Output Format

- Two integers `L R` for the chosen interval, or `NONE`

**Important:** Test cases appear to evaluate a specific metric derived from the optimal interval (such as the range length, a specific list index, or element count). Analyze test patterns carefully to determine the exact output requirement.

## Constraints

- `1 <= k <= 100000`
- Total elements across all lists <= 200000
- List values fit in 32-bit signed integer

## Example

**Input:**

```
3
3
1 2 10
3
2 3 11
3
1 3 12
```

**Output:**

```
1 3
```

**Explanation:**

Interval `[1,3]` contains two numbers from each list: {1,2}, {2,3}, {1,3}.

![Example Visualization](../images/SRT-008/example-1.png)

## Notes

- Merge all lists with their list IDs
- Use a sliding window to maintain counts per list
- Ensure each list contributes at least two elements
- Time complexity: O(N log N)

## Related Topics

Sliding Window, Heaps, Range Cover

---

## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public int[] smallestRange(List<int[]> lists) {
        // Your implementation here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();
        List<int[]> lists = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            int m = sc.nextInt();
            int[] arr = new int[m];
            for (int j = 0; j < m; j++) arr[j] = sc.nextInt();
            lists.add(arr);
        }

        Solution solution = new Solution();
        int[] result = solution.smallestRange(lists);
        if (result.length == 0) {
            System.out.println("NONE");
        } else {
            System.out.println(result[0] + " " + result[1]);
        }
        sc.close();
    }
}
```

### Python

```python
def smallest_range(lists: list[list[int]]) -> list[int]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    lists = []
    for _ in range(k):
        m = int(next(it))
        lists.append([int(next(it)) for _ in range(m)])

    result = smallest_range(lists)
    if not result:
        print("NONE")
    else:
        print(result[0], result[1])

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
    vector<int> smallestRange(const vector<vector<int>>& lists) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) return 0;
    vector<vector<int>> lists;
    lists.reserve(k);
    for (int i = 0; i < k; i++) {
        int m;
        cin >> m;
        vector<int> arr(m);
        for (int j = 0; j < m; j++) cin >> arr[j];
        lists.push_back(arr);
    }

    Solution solution;
    vector<int> result = solution.smallestRange(lists);
    if (result.empty()) {
        cout << "NONE\n";
    } else {
        cout << result[0] << " " << result[1] << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  smallestRange(lists) {
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
  const k = parseInt(data[idx++], 10);
  const lists = [];
  for (let i = 0; i < k; i++) {
    const m = parseInt(data[idx++], 10);
    const arr = [];
    for (let j = 0; j < m; j++) arr.push(parseInt(data[idx++], 10));
    lists.push(arr);
  }

  const solution = new Solution();
  const result = solution.smallestRange(lists);
  if (result.length === 0) {
    console.log("NONE");
  } else {
    console.log(result[0] + " " + result[1]);
  }
});
```
