---
problem_id: BIT_MAXIMIZE_OR_K_PICKS__8408
display_id: BIT-008
slug: maximize-or-k-picks
title: "Maximize OR With K Picks"
difficulty: Medium
difficulty_score: 48
topics:
  - Bitwise Operations
  - OR
  - Greedy
  - Array
tags:
  - bitwise
  - or-operation
  - greedy
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-008: Maximize OR With K Picks

## Problem Statement

Choose exactly k elements from the array to maximize the bitwise OR of the chosen set. Return the maximum OR value.

![Problem Illustration](../images/BIT-008/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]
- Third line: integer k

## Output Format

Print the maximum possible OR value.

## Constraints

- `1 <= n <= 200000`
- `1 <= k <= n`

## Example

**Input:**
```
3
1 2 4
2
```

**Output:**
```
6
```

**Explanation:**

Choosing 2 and 4 gives OR = 6, which is the maximum.

![Example Visualization](../images/BIT-008/example-1.png)

## Notes

- You must choose exactly k elements.
- The order of chosen elements does not matter.

## Related Topics

Bitwise Operations, Greedy

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long maximizeOrWithKPicks(int[] a, int k) {
        // Your implementation here
        return 0L;
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
        int k = sc.nextInt();

        Solution solution = new Solution();
        long result = solution.maximizeOrWithKPicks(a, k);
        System.out.println(result);
        sc.close();
    }
}
```


### Python

```python
def maximize_or_with_k_picks(a: list[int], k: int) -> int:
    # Your implementation here
    return 0

def main():
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())

    result = maximize_or_with_k_picks(a, k)
    print(result)

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
    long long maximizeOrWithKPicks(vector<int>& a, int k) {
        // Your implementation here
        return 0;
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
    int k;
    cin >> k;

    Solution solution;
    long long result = solution.maximizeOrWithKPicks(a, k);
    cout << result << "\n";
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
  maximizeOrWithKPicks(a, k) {
    // Your implementation here
    return 0;
  }
}

let idx = 0;
const n = Number(data[idx++]);
const a = [];
for (let i = 0; i < n; i++) {
  a.push(Number(data[idx++]));
}
const k = Number(data[idx++]);

const solution = new Solution();
const result = solution.maximizeOrWithKPicks(a, k);
console.log(String(result));
```

