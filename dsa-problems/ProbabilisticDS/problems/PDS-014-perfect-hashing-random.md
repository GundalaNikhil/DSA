---
problem_id: PDS_PERFECT_HASHING_RANDOM__6203
display_id: PDS-014
slug: perfect-hashing-random
title: "Perfect Hashing via Randomization"
difficulty: Medium
difficulty_score: 55
topics:
  - Probabilistic Data Structures
  - Perfect Hashing
  - Randomization
tags:
  - probabilistic-ds
  - perfect-hashing
  - randomized
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-014: Perfect Hashing via Randomization

## Problem Statement

In two-level perfect hashing (FKS), if bucket sizes are `s_1, s_2, ..., s_t`, the total second-level table size is:

```
S = sum s_i^2
```

Compute `S` and report whether `S <= 4n`.

![Problem Illustration](../images/PDS-014/problem-illustration.png)

## Input Format

- First line: integer `n` (number of keys) and integer `t` (number of buckets)
- Second line: `t` integers (bucket sizes)

## Output Format

- Two values: `S` and `YES` if `S <= 4n`, otherwise `NO`

## Constraints

- `1 <= n <= 10^6`
- `1 <= t <= n`
- Sum of bucket sizes = n

## Example

**Input:**

```
6 3
2 1 3
```

**Output:**

```
14 YES
```

**Explanation:**

S = 4 + 1 + 9 = 14, and 4n = 24, so YES.

![Example Visualization](../images/PDS-014/example-1.png)

## Notes

- Use 64-bit integers for S
- Time complexity: O(t)

## Related Topics

Perfect Hashing, FKS, Randomization

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long totalSize(int[] sizes) {
        // Your implementation here
        return 0L;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        int t = sc.nextInt();
        int[] sizes = new int[t];
        for (int i = 0; i < t; i++) sizes[i] = sc.nextInt();

        Solution solution = new Solution();
        long S = solution.totalSize(sizes);
        System.out.println(S + " " + (S <= 4 * n ? "YES" : "NO"));
        sc.close();
    }
}
```

### Python

```python
def total_size(sizes):
    # Your implementation here
    return 0

def main():
    n, t = map(int, input().split())
    sizes = list(map(int, input().split()))
    S = total_size(sizes)
    print(S, "YES" if S <= 4 * n else "NO")

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
    long long totalSize(const vector<int>& sizes) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    int t;
    cin >> n >> t;
    vector<int> sizes(t);
    for (int i = 0; i < t; i++) cin >> sizes[i];

    Solution solution;
    long long S = solution.totalSize(sizes);
    cout << S << " " << (S <= 4 * n ? "YES" : "NO") << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function totalSize(sizes) {
  // Your implementation here
  return 0;
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
  const t = parseInt(data[idx++], 10);
  const sizes = [];
  for (let i = 0; i < t; i++) sizes.push(parseInt(data[idx++], 10));
  const S = totalSize(sizes);
  console.log(S + " " + (S <= 4 * n ? "YES" : "NO"));
});
```
