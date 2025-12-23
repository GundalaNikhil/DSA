---
problem_id: ARR_LEAKY_ROOF_REINFORCE__3586
display_id: ARR-011
slug: leaky-roof-reinforcement
title: "Leaky Roof Reinforcement"
difficulty: Medium
difficulty_score: 55
topics:
  - Arrays
  - Prefix Suffix
  - Greedy
tags:
  - arrays
  - prefix-suffix
  - greedy
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-011: Leaky Roof Reinforcement

## Problem Statement

You can add planks to increase heights so the profile becomes non-decreasing up to a single peak and non-increasing after that peak. Find the minimum total height added.

![Problem Illustration](../images/ARR-011/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers height[i]

## Output Format

Print the minimum total added height.

## Constraints

- `1 <= n <= 200000`
- `0 <= height[i] <= 1000000000`

## Example

**Input:**
```
5
4 1 3 1 5
```

**Output:**
```
7
```

**Explanation:**

Choose peak at index 4 with height 5. The reinforced profile is [4, 4, 4, 4, 5],
adding 3 + 1 + 3 = 7 in total.

![Example Visualization](../images/ARR-011/example-1.png)

## Notes

- You may only increase heights, never decrease.
- The peak can be any index.

## Related Topics

Prefix Suffix, Greedy, Arrays

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long minPlanksForRoof(int[] height) {
        // Your implementation here
        return 0L;
    }
}

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] height = new int[n];
        for (int i = 0; i < n; i++) {
            height[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        long result = solution.minPlanksForRoof(height);
        System.out.println(result);
        sc.close();
    }
}
```


### Python

```python
def min_planks_for_roof(height: list[int]) -> int:
    # Your implementation here
    return 0

def main():
    n = int(input())
    height = list(map(int, input().split()))

    result = min_planks_for_roof(height)
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
    long long minPlanksForRoof(vector<int>& height) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> height(n);
    for (int i = 0; i < n; i++) {
        cin >> height[i];
    }

    Solution solution;
    long long result = solution.minPlanksForRoof(height);
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
  minPlanksForRoof(height) {
    // Your implementation here
    return 0;
  }
}

let idx = 0;
const n = Number(data[idx++]);
const height = [];
for (let i = 0; i < n; i++) {
  height.push(Number(data[idx++]));
}

const solution = new Solution();
const result = solution.minPlanksForRoof(height);
console.log(String(result));
```

