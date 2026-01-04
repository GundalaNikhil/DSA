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

Print two space-separated integers `L R` representing the chosen interval of minimum length.

- `L` is the left endpoint (inclusive)
- `R` is the right endpoint (inclusive)

If no valid interval exists, print `NONE`.

**Note about length**: The "length" of an interval [L, R] is defined as `R - L` (the difference). For example:

- Interval [1, 5] has length 4 (not 5 elements)
- Interval [1, 3] has length 2
- You want to minimize this difference while satisfying the coverage requirement

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

We have 3 lists:

- List 0: [1, 2, 10]
- List 1: [2, 3, 11]
- List 2: [1, 3, 12]

The interval [1, 3] contains:

- From List 0: 1, 2 (2 elements) ✓
- From List 1: 2, 3 (2 elements) ✓
- From List 2: 1, 3 (2 elements) ✓

The interval length is 3 - 1 = 2. This is optimal (minimum possible).

Other possible intervals that work:

- [2, 3]: length 1, contains {2}, {2,3}, {3} - List 0 only has 1! ✗
- [1, 10]: length 9, works but much longer
- [2, 11]: length 9, works but much longer

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
    public void findBalancedInterval(int k, List<List<Integer>> lists) {
        // Implement here
        // If NONE, print "NONE"
        // Else print "L R"
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int k = sc.nextInt();
            List<List<Integer>> lists = new ArrayList<>();
            for (int i = 0; i < k; i++) {
                int m = sc.nextInt();
                List<Integer> list = new ArrayList<>();
                for (int j = 0; j < m; j++) list.add(sc.nextInt());
                lists.add(list);
            }
            Solution sol = new Solution();
            sol.findBalancedInterval(k, lists);
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def find_balanced_interval(self, k: int, lists: list):
        # Implement here
        # If NONE, print "NONE"
        # Else print "L R"
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    k = int(input_data[0])
    lists = []
    ptr = 1
    for _ in range(k):
        m = int(input_data[ptr])
        curr_list = [int(x) for x in input_data[ptr+1 : ptr+1+m]]
        lists.append(curr_list)
        ptr += 1 + m

    sol = Solution()
    sol.find_balanced_interval(k, lists)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    void findBalancedInterval(int k, const vector<vector<int>>& lists) {
        // Implement here
        // If NONE, cout << "NONE" << endl;
        // Else cout << L << " " << R << endl;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int k;
    if (cin >> k) {
        vector<vector<int>> lists(k);
        for (int i = 0; i < k; i++) {
            int m;
            cin >> m;
            lists[i].resize(m);
            for (int j = 0; j < m; j++) cin >> lists[i][j];
        }

        Solution sol;
        sol.findBalancedInterval(k, lists);
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findBalancedInterval(k, lists) {
    // Implement here
    // If NONE, console.log("NONE");
    // Else console.log(`${L} ${R}`);
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
  if (input.length < 1) return;
  const k = parseInt(input[0]);
  const lists = [];
  let ptr = 1;
  for (let i = 0; i < k; i++) {
    const m = parseInt(input[ptr]);
    const currentList = input.slice(ptr + 1, ptr + 1 + m).map(Number);
    lists.push(currentList);
    ptr += 1 + m;
  }

  const sol = new Solution();
  sol.findBalancedInterval(k, lists);
});
```
