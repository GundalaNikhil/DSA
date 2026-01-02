---
problem_id: STR_LONGEST_CHUNKED_BOUNDED__1011
display_id: STR-011
slug: longest-chunked-bounded
title: "Longest Chunked Decomposition (Bounded)"
difficulty: Medium
difficulty_score: 44
topics:
  - String Manipulation
  - Two Pointers
  - Greedy
tags:
  - palindrome-decomposition
  - chunk-matching
  - symmetric-structure
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-011: Longest Chunked Decomposition (Bounded)

## Problem Statement

Split a string `s` into the maximum number of chunks where the i-th chunk from the start equals the i-th chunk from the end. All chunks must have length ≤ `L`.

## Input Format

- First line: String `s` (1 ≤ |s| ≤ 10^5)
- Second line: Integer `L` (1 ≤ L ≤ |s|)

## Output Format

- A single integer representing the maximum number of chunks

## Constraints

- `1 ≤ |s| ≤ 10^5`
- `1 ≤ L ≤ |s|`
- `s` contains only lowercase English letters

## Example 1

**Input:**

```
abcabc
3
```

**Output:**

```
2
```

**Explanation:**

- Match "abc" from both ends → 2 chunks
- Middle is empty

## Example 2

**Input:**

```
abacaba
3
```

**Output:**

```
5
```

**Explanation:**

- Match "a" from both ends → 2 chunks
- Match "b" from both ends → 2 chunks
- Middle "aca" → 1 chunk
- Total: 5 chunks

## Notes

- Greedy two-pointer matching
- Match smallest valid chunks first
- O(n × L) time complexity

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int longestChunkedDecomposition(String s, int L) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int L = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.longestChunkedDecomposition(s, L));
        sc.close();
    }
}
```

### Python

```python
import sys

def longest_chunked_decomposition(s: str, L: int) -> int:
    # Implementation here
    return 0

def main():
    import sys


    # Read input
    input_data = sys.stdin.read().strip()
    if not input_data:
        print(0)
        return
        
    parts = input_data.split()
    if len(parts) >= 2:
        s = parts[0]
        try:
            L = int(parts[1])
            print(longest_chunked_decomposition(s, L))
        except ValueError:
            pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;

class Solution {
public:
    int longestChunkedDecomposition(string s, int L) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s; cin >> s;
    int L; cin >> L;
    Solution sol;
    cout << sol.longestChunkedDecomposition(s, L) << endl;
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  longestChunkedDecomposition(s, L) {
    // Implementation here
    return null;
  }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const s = tokens[ptr++];
    const L = parseInt(tokens[ptr++]);
    console.log(new Solution().longestChunkedDecomposition(s, L));
});
```
