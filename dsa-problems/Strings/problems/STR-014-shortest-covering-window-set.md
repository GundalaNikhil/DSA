---
problem_id: STR_SHORTEST_COVERING_WINDOW_SET__1014
display_id: STR-014
slug: shortest-covering-window-set
title: "Shortest Covering Window for Set"
difficulty: Medium
difficulty_score: 41
topics:
  - String Array
  - Sliding Window
  - Hashing
tags:
  - substring-search
  - coverage
  - two-pointers
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-014: Shortest Covering Window for Set

## Problem Statement

Given an array of strings `arr` and a set of required strings `T`, find the shortest contiguous subarray whose elements cover all strings in `T`. Return the length and one such window.

## Input Format

- First line: Integer `n` (size of arr)
- Next n lines: One string per line (elements of arr)
- Next line: Integer `m` (size of set T)
- Next m lines: One string per line (elements of T)

## Output Format

- First line: Integer representing window length
- Following lines: Strings in the shortest window

## Constraints

- `1 ≤ |arr| ≤ 10^5`
- `|T| ≤ 10^3`

## Example 1

**Input:**

```
6
db
aa
cc
db
aa
cc
2
aa
cc
```

**Output:**

```
2
aa
cc
```

**Explanation:**

- Window [1:3] = ["aa","cc"] covers all required strings
- Length 2 is minimal

## Notes

- Sliding window with frequency tracking
- Expand until all covered, then contract
- O(n) time complexity

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public String[] shortestCoveringWindow(int n, String[] arr, int m, String[] T) {
        // Implement here
        return new String[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            String[] arr = new String[n];
            for (int i = 0; i < n; i++) {
                if (sc.hasNext()) arr[i] = sc.next();
            }
            if (sc.hasNextInt()) {
                int m = sc.nextInt();
                String[] T = new String[m];
                for (int i = 0; i < m; i++) {
                    if (sc.hasNext()) T[i] = sc.next();
                }
                Solution sol = new Solution();
                String[] res = sol.shortestCoveringWindow(n, arr, m, T);
                System.out.println(res.length);
                for (String s : res) {
                    System.out.println(s);
                }
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    arr = input_data[1:1+n]
    m = int(input_data[1+n])
    T = input_data[2+n:2+n+m]

    solution = Solution()
    res = solution.shortest_covering_window(n, arr, m, T)
    print(len(res))
    for s in res:
        print(s)

class Solution:
    def shortest_covering_window(self, n: int, arr: list, m: int, t: list) -> list:
        # Implement here
        return []

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    vector<string> shortestCoveringWindow(int n, const vector<string>& arr, int m, const vector<string>& T) {
        // Implement here
        return {};
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (cin >> n) {
        vector<string> arr(n);
        for (int i = 0; i < n; i++) cin >> arr[i];
        int m;
        if (cin >> m) {
            vector<string> T(m);
            for (int i = 0; i < m; i++) cin >> T[i];
            Solution sol;
            vector<string> res = sol.shortestCoveringWindow(n, arr, m, T);
            cout << res.size() << endl;
            for (const string& s : res) cout << s << endl;
        }
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  shortestCoveringWindow(n, arr, m, T) {
    // Implement here
    return [];
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", (line) => {
  input.push(...line.trim().split(/\s+/));
}).on("close", () => {
  if (input.length > 0) {
    const n = parseInt(input[0]);
    const arr = input.slice(1, 1 + n);
    const m = parseInt(input[1 + n]);
    const T = input.slice(2 + n, 2 + n + m);

    const sol = new Solution();
    const res = sol.shortestCoveringWindow(n, arr, m, T);
    console.log(res.length);
    res.forEach((s) => console.log(s));
  }
});
```
