---
problem_id: STC_DISTINCT_SUBSTRINGS_SA__9517
display_id: STC-008
slug: distinct-substrings-sa
title: "Distinct Substrings Count via SA/LCP"
difficulty: Medium
difficulty_score: 46
topics:
  - Strings
  - Suffix Array
  - Counting
tags:
  - strings
  - suffix-array
  - counting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STC-008: Distinct Substrings Count via SA/LCP

## Problem Statement

Given a string `s`, compute the number of distinct substrings. Use the formula:

```
count = n*(n+1)/2 - sum(LCP)
```

where `LCP` is the array of longest common prefixes between adjacent suffixes in suffix array order.

![Problem Illustration](../images/STC-008/problem-illustration.png)

## Input Format

- First line: string `s`

## Output Format

- Single integer: number of distinct substrings

## Constraints

- `1 <= |s| <= 100000`
- `s` contains lowercase English letters

## Example

**Input:**

```
aaa
```

**Output:**

```
3
```

**Explanation:**

Distinct substrings are "a", "aa", "aaa".

![Example Visualization](../images/STC-008/example-1.png)

## Notes

- Build suffix array and LCP array
- Use 64-bit arithmetic for the total count
- Time complexity: O(n log n)
- Space complexity: O(n)

## Related Topics

Suffix Array, LCP, Counting

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long countDistinct(String s) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            Solution solution = new Solution();
            System.out.println(solution.countDistinct(s));
        }
        sc.close();
    }
}
```

### Python

```python
def count_distinct(s: str) -> int:
    return 0
def main():
    import sys
    sys.setrecursionlimit(200000)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    print(count_distinct(s))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long countDistinct(const string& s) {
        int n = s.length();
        if (n == 0) return 0;
        
        // 1. Build SA
        vector<int> sa(n), rank(n), newRank(n);
        for (int i = 0; i < n; i++) {
            sa[i] = i;
            rank[i] = s[i];
        }
        
        for (int k = 1; k < n; k *= 2) {
            auto cmp = [&](int i, int j) {
                if (rank[i] != rank[j]) return rank[i] < rank[j];
                int ri = (i + k < n) ? rank[i + k] : -1;
                int rj = (j + k < n) ? rank[j + k] : -1;
                return ri < rj;
            };
            sort(sa.begin(), sa.end(), cmp);
            
            newRank[sa[0]] = 0;
            for (int i = 1; i < n; i++) {
                if (cmp(sa[i - 1], sa[i])) newRank[sa[i]] = newRank[sa[i - 1]] + 1;
                else newRank[sa[i]] = newRank[sa[i - 1]];
            }
            rank = newRank;
            if (rank[sa[n - 1]] == n - 1) break;
        }
        
        // 2. Build LCP Sum
        long long lcpSum = 0;
        int k = 0;
        for (int i = 0; i < n; i++) {
            if (rank[i] == n - 1) {
                k = 0;
                continue;
            }
            int j = sa[rank[i] + 1];
            while (i + k < n && j + k < n && s[i + k] == s[j + k]) {
                k++;
            }
            lcpSum += k;
            if (k > 0) k--;
        }
        
        long long totalSubstrings = (long long)n * (n + 1) / 2;
        return totalSubstrings - lcpSum;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (cin >> s) {
        Solution solution;
        cout << solution.countDistinct(s) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countDistinct(s) {
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part) data.push(part);
  }
});

rl.on("close", () => {
  if (data.length === 0) return;
  const s = data[0];
  const solution = new Solution();
  console.log(solution.countDistinct(s).toString());
});
```

