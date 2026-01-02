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
    public Object[] shortestCoveringWindow(List<String> arr, Set<String> T) {
        // Implementation here
        return new Object[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int arr_n = sc.nextInt();
        List<String> arr = new ArrayList<>();
        for(int i=0; i<arr_n; i++) arr.add(sc.next());
        int T_n = sc.nextInt();
        Set<String> T = new HashSet<>();
        for(int i=0; i<T_n; i++) T.add(sc.next());
        Solution sol = new Solution();
        Object[] res = sol.shortestCoveringWindow(arr, T);
        System.out.println(res[0]);
        @SuppressWarnings("unchecked")
        List<String> list = (List<String>)res[1];
        for(String s : list) System.out.println(s);
        if(list.isEmpty()) System.out.println("NONE");
        sc.close();
    }
}
```

### Python

```python
import sys

def shortest_covering_window(arr: list[str], T: set[str]) -> tuple[int, list[str]]:
    # Implementation here
    return ()

def main():
    import sys


    # Read input
    input_data = sys.stdin.read().strip()
    if not input_data:
        print(0)
        return

    parts = input_data.split()
    if not parts:
        return

    iterator = iter(parts)
    try:
        # Read Array
        N = int(next(iterator))
        arr = []
        for _ in range(N):
            arr.append(next(iterator))

        # Read Set T
        K = int(next(iterator))
        T = set()
        for _ in range(K):
            T.add(next(iterator))

        length, window = shortest_covering_window(arr, T)

        print(length)
        for item in window:
            print(item)

    except StopIteration:
        pass
    except ValueError:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
#include <utility>

using namespace std;

class Solution {
public:
    pair<int, vector<string>> shortestCoveringWindow(vector<string>& arr, unordered_set<string>& T) {
        // Implementation here
        return {0, {}};
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int arr_n;
    if (!(cin >> arr_n)) return 0;
    vector<string> arr(arr_n);
    for(int i=0; i<arr_n; i++) cin >> arr[i];

    int T_n;
    cin >> T_n;
    unordered_set<string> T;
    for(int i=0; i<T_n; i++) { string s; cin >> s; T.insert(s); }

    Solution sol;
    pair<int, vector<string>> res = sol.shortestCoveringWindow(arr, T);
    cout << res.first << endl;
    for(const string& s : res.second) cout << s << endl;
    if(res.second.empty()) cout << "NONE" << endl;
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  shortestCoveringWindow(arr, T) {
    // Implementation here
    return null;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let tokens = [];
rl.on("line", (line) => {
  tokens.push(...line.trim().split(/\s+/));
});
rl.on("close", () => {
  if (tokens.length === 0) return;
  let ptr = 0;
  const arr_n = parseInt(tokens[ptr++]);
  const arr = [];
  for (let i = 0; i < arr_n; i++) arr.push(tokens[ptr++]);
  const T_n = parseInt(tokens[ptr++]);
  const T = new Set();
  for (let i = 0; i < T_n; i++) T.add(tokens[ptr++]);
  const res = new Solution().shortestCoveringWindow(arr, T);
  console.log(res[0]);
  if (res[1].length > 0) {
    for (const s of res[1]) console.log(s);
  } else {
    console.log("NONE");
  }
});
```
