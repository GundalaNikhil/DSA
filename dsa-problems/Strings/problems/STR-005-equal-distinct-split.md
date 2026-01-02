---
problem_id: STR_EQUAL_DISTINCT_SPLIT__1005
display_id: STR-005
slug: equal-distinct-split
title: "Equal Distinct Split"
difficulty: Medium
difficulty_score: 38
topics:
  - String Manipulation
  - Prefix-Suffix
  - Hashing
tags:
  - distinct-characters
  - split-point
  - frequency-analysis
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-005: Equal Distinct Split

## Problem Statement

Given a string `s` of lowercase English letters, count the number of split points where the left substring and right substring have the same number of distinct characters.

A split point after index `i` creates:

- Left: s[0..i]
- Right: s[i+1..n-1]

## Input Format

- A single string `s` (1 ≤ |s| ≤ 2 × 10^5)

## Output Format

- A single integer representing the count of valid split points

## Constraints

- `1 ≤ |s| ≤ 2 × 10^5`
- `s` contains only lowercase English letters

## Example 1

**Input:**

```
ababa
```

**Output:**

```
2
```

**Explanation:**

- Split after index 1: left="ab" (2 distinct), right="aba" (2 distinct) ✓
- Split after index 2: left="aba" (2 distinct), right="ba" (2 distinct) ✓
- Total: 2 valid splits

## Example 2

**Input:**

```
abc
```

**Output:**

```
0
```

**Explanation:**

- Split after index 0: left="a" (1), right="bc" (2) ✗
- Split after index 1: left="ab" (2), right="c" (1) ✗
- No valid splits

## Notes

- Precompute suffix distinct counts in O(n)
- Scan left-to-right maintaining prefix distinct count
- O(n) time and O(n) space solution

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int countEqualDistinctSplits(String s) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.useDelimiter("\\A").hasNext() ? sc.next() : "";
        s = s.trim();
        Solution sol = new Solution();
        System.out.println(sol.countEqualDistinctSplits(s));
        sc.close();
    }
}
```

### Python

```python
def count_equal_distinct_splits(s: str) -> int:
    return 0
def main():
    import sys

    # Read input string
    input_data = sys.stdin.read().strip()
    if not input_data:
        print(0)
        return
        
    # Call solution
    result = count_equal_distinct_splits(input_data)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
using namespace std;

#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
class Solution {
public:
    int countEqualDistinctSplits(string s) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s((istreambuf_iterator<char>(cin)), istreambuf_iterator<char>());
    while(!s.empty() && isspace(s.back())) s.pop_back();
    while(!s.empty() && isspace(s.front())) s.erase(0, 1);
    Solution sol;
    cout << sol.countEqualDistinctSplits(s) << endl;
    return 0;
}
```

### JavaScript

```javascript
function countEqualDistinctSplits(s) {
    return 0;
  }

const fs = require('fs');
const s = fs.readFileSync(0, 'utf-8').trim();
console.log(countEqualDistinctSplits(s));
```

