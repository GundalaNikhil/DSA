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
    public int maxChunks(String s, int L) {
        // Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            if (sc.hasNextInt()) {
                int L = sc.nextInt();
                Solution sol = new Solution();
                System.out.println(sol.maxChunks(s, L));
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
    if len(input_data) < 2:
        return
    s = input_data[0]
    L = int(input_data[1])
    solution = Solution()
    print(solution.max_chunks(s, L))

class Solution:
    def max_chunks(self, s: str, L: int) -> int:
        # Implement here
        return 0

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    int maxChunks(string s, int L) {
        // Implement here
        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    int L;
    if (cin >> s >> L) {
        Solution sol;
        cout << sol.maxChunks(s, L) << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxChunks(s, L) {
    // Implement here
    return 0;
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
  if (input.length >= 2) {
    const s = input[0];
    const L = parseInt(input[1]);
    const sol = new Solution();
    console.log(sol.maxChunks(s, L));
  }
});
```
