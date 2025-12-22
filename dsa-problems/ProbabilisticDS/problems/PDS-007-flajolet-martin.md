---
problem_id: PDS_FLAJOLET_MARTIN__2749
display_id: PDS-007
slug: flajolet-martin
title: "Flajolet-Martin Bit Pattern"
difficulty: Medium
difficulty_score: 48
topics:
  - Probabilistic Data Structures
  - Flajolet-Martin
  - Distinct Count
tags:
  - probabilistic-ds
  - flajolet-martin
  - distinct-count
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-007: Flajolet-Martin Bit Pattern

## Problem Statement

Given the maximum number of trailing zeros `R` observed in hashed stream items, estimate the number of distinct elements using:

```
Estimate = 2^R / phi
```

where `phi = 0.77351`.

![Problem Illustration](../images/PDS-007/problem-illustration.png)

## Input Format

- Single line: integer `R`

## Output Format

- Single floating-point number: estimated distinct count

## Constraints

- `0 <= R <= 60`

## Example

**Input:**

```
4
```

**Output:**

```
20.684930
```

**Explanation:**

Estimate = 16 / 0.77351 = 20.68493.

![Example Visualization](../images/PDS-007/example-1.png)

## Notes

- Use double precision
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

Flajolet-Martin, Distinct Counting

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double estimateDistinct(int R) {
        // Your implementation here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int R = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.estimateDistinct(R));
        sc.close();
    }
}
```

### Python

```python
def estimate_distinct(R: int) -> float:
    # Your implementation here
    return 0.0

def main():
    R = int(input())
    print(f"{estimate_distinct(R):.6f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    double estimateDistinct(int R) {
        // Your implementation here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R;
    cin >> R;
    Solution solution;
    cout << solution.estimateDistinct(R) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function estimateDistinct(R) {
  // Your implementation here
  return 0.0;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  const R = parseInt(data[0], 10);
  console.log(estimateDistinct(R).toFixed(6));
});
```
