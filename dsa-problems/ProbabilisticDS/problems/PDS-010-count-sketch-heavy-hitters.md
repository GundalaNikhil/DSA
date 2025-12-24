---
problem_id: PDS_COUNT_SKETCH_HEAVY_HITTERS__3405
display_id: PDS-010
slug: count-sketch-heavy-hitters
title: "Heavy Hitters with Count Sketch"
difficulty: Medium
difficulty_score: 55
topics:
  - Probabilistic Data Structures
  - Count Sketch
  - Streaming
tags:
  - probabilistic-ds
  - count-sketch
  - heavy-hitters
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-010: Heavy Hitters with Count Sketch

## Problem Statement

Given the Count Sketch signed estimates for a single item across `d` rows, compute its frequency estimate as the median of the signed counts.

Each row provides:

- `count`: the bucket count
- `sign`: either `+1` or `-1`

The signed value is `count * sign`.

![Problem Illustration](../images/PDS-010/problem-illustration.png)

## Input Format

- First line: integer `d` (odd)
- Next `d` lines: `count` and `sign`

## Output Format

- Single integer: the median of signed counts

## Constraints

- `1 <= d <= 101`, `d` is odd
- `count` fits in 32-bit signed integer
- `sign` is either -1 or 1

## Example

**Input:**

```
3
10 1
9 -1
11 1
```

**Output:**

```
10
```

**Explanation:**

Signed counts are [10, -9, 11]. Median is 10.

![Example Visualization](../images/PDS-010/example-1.png)

## Notes

- For odd `d`, the median is the middle after sorting
- Time complexity: O(d log d)
- Space complexity: O(d)

## Related Topics

Count Sketch, Heavy Hitters, Streaming

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int countSketchEstimate(int[] count, int[] sign) {
        // Your implementation here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int d = sc.nextInt();
        int[] count = new int[d];
        int[] sign = new int[d];
        for (int i = 0; i < d; i++) {
            count[i] = sc.nextInt();
            sign[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.countSketchEstimate(count, sign));
        sc.close();
    }
}
```

### Python

```python
def count_sketch_estimate(count, sign):
    # Your implementation here
    return 0

def main():
    d = int(input())
    count = []
    sign = []
    for _ in range(d):
        c, s = map(int, input().split())
        count.append(c)
        sign.append(s)
    print(count_sketch_estimate(count, sign))

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
    int countSketchEstimate(const vector<int>& count, const vector<int>& sign) {
        // Your implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int d;
    cin >> d;
    vector<int> count(d), sign(d);
    for (int i = 0; i < d; i++) {
        cin >> count[i] >> sign[i];
    }

    Solution solution;
    cout << solution.countSketchEstimate(count, sign) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function countSketchEstimate(count, sign) {
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
  const d = parseInt(data[idx++], 10);
  const count = [];
  const sign = [];
  for (let i = 0; i < d; i++) {
    count.push(parseInt(data[idx++], 10));
    sign.push(parseInt(data[idx++], 10));
  }
  console.log(countSketchEstimate(count, sign));
});
```
