---
problem_id: BIT_TWO_UNIQUE_TRIPLES__8402
display_id: BIT-002
slug: two-unique-with-triples-mask
title: "Two Unique With Triple Others Under Mask"
difficulty: Medium
difficulty_score: 45
topics:
  - Bitwise Operations
  - XOR
  - Array
  - Bit Counting
  - Mathematics
tags:
  - bitwise
  - xor
  - bit-manipulation
  - array
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-002: Two Unique With Triple Others Under Mask

## Problem Statement

Every number appears exactly three times except two distinct numbers that appear once each. You are also given a mask M; the two uniques are guaranteed to differ in at least one bit that is set in M. Find the two unique values.

![Problem Illustration](../images/BIT-002/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]
- Third line: integer M

## Output Format

Print the two unique values in ascending order.

## Constraints

- `2 <= n <= 200000`
- `0 <= M <= 1000000000`

## Example

**Input:**
```
8
5 5 5 9 9 9 3 6
1
```

**Output:**
```
3 6
```

**Explanation:**

The only values appearing once are 3 and 6, so they are returned in ascending
order.

![Example Visualization](../images/BIT-002/example-1.png)

## Notes

- The output must be in ascending order for deterministic checking.
- The mask M guarantees a separating bit for partitioning.

## Related Topics

Bitwise Operations, Counting Bits

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] twoUniqueWithTriplesMask(int[] a, int M) {
        // Your implementation here
        return new int[0];
    }
}

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        int M = sc.nextInt();

        Solution solution = new Solution();
        int[] result = solution.twoUniqueWithTriplesMask(a, M);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            if (i > 0) sb.append(" ");
            sb.append(result[i]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
```


### Python

```python
def two_unique_with_triples_mask(a: list[int], M: int) -> list[int]:
    # Your implementation here
    return []

def main():
    n = int(input())
    a = list(map(int, input().split()))
    M = int(input())

    result = two_unique_with_triples_mask(a, M)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
```


### C++

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>
#include <tuple>
using namespace std;


class Solution {
public:
    vector<int> twoUniqueWithTriplesMask(vector<int>& a, int M) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    int M;
    cin >> M;

    Solution solution;
    vector<int> result = solution.twoUniqueWithTriplesMask(a, M);
    for (size_t i = 0; i < result.size(); i++) {
        if (i) cout << " ";
        cout << result[i];
    }
    cout << "\n";
    return 0;
}
```


### JavaScript

```javascript
const fs = require("fs");
const data = fs.readFileSync(0, "utf8").trim().split(/\s+/);
if (data.length === 1 && data[0] === "") {
  process.exit(0);
}

class Solution {
  twoUniqueWithTriplesMask(a, M) {
    // Your implementation here
    return [];
  }
}

let idx = 0;
const n = Number(data[idx++]);
const a = [];
for (let i = 0; i < n; i++) {
  a.push(Number(data[idx++]));
}
const M = Number(data[idx++]);

const solution = new Solution();
const result = solution.twoUniqueWithTriplesMask(a, M);
console.log(result.join(" "));
```

