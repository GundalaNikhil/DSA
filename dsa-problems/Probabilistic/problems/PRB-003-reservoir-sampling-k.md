---
problem_id: PRB_RESERVOIR_SAMPLING_K__5716
display_id: PRB-003
slug: reservoir-sampling-k
title: "Reservoir Sampling K Items"
difficulty: Medium
difficulty_score: 52
topics:
  - Probability
  - Randomized Algorithms
  - Streaming
tags:
  - probability
  - sampling
  - streaming
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-003: Reservoir Sampling K Items

## Problem Statement

You are given a stream of integers `1..n` and need to select `k` items uniformly at random using reservoir sampling. Use the following deterministic RNG for reproducibility:

```
state = seed
state = (state * 6364136223846793005 + 1) mod 2^64
rand() = state
```

For each item `i` (1-indexed):

- If `i <= k`, place `i` in the reservoir
- Else draw `j = rand() % i`. If `j < k`, replace reservoir[j]

Output the final reservoir in order.

![Problem Illustration](../images/PRB-003/problem-illustration.png)

## Input Format

- Single line: integers `n`, `k`, and `seed`

## Output Format

- Single line: `k` integers from the reservoir, space-separated
- If `k = 0`, print an empty line

## Constraints

- `0 <= k <= n <= 10^6`
- `0 <= seed < 2^64`

## Example

**Input:**

```
5 2 1
```

**Output:**

```
1 5
```

**Explanation:**

Using the specified RNG, the final reservoir contains items 1 and 5.

![Example Visualization](../images/PRB-003/example-1.png)

## Notes

- This is deterministic due to the fixed RNG
- Each item is processed once
- Time complexity: O(n)
- Space complexity: O(k)

## Related Topics

Reservoir Sampling, Randomized Streaming

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int[] reservoirSample(int n, int k, long seed) {
        // Your implementation here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        long seed = sc.nextLong();

        Solution solution = new Solution();
        int[] res = solution.reservoirSample(n, k, seed);
        for (int i = 0; i < res.length; i++) {
            System.out.print(res[i]);
            if (i + 1 < res.length) System.out.print(" ");
        }
        System.out.println();
        sc.close();
    }
}
```

### Python

```python
def reservoir_sample(n: int, k: int, seed: int):
    # Your implementation here
    return []

def main():
    n, k, seed = map(int, input().split())
    res = reservoir_sample(n, k, seed)
    print(" ".join(str(x) for x in res))

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
    vector<int> reservoirSample(int n, int k, unsigned long long seed) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    unsigned long long seed;
    cin >> n >> k >> seed;

    Solution solution;
    vector<int> res = solution.reservoirSample(n, k, seed);
    for (int i = 0; i < (int)res.size(); i++) {
        if (i) cout << " ";
        cout << res[i];
    }
    cout << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function reservoirSample(n, k, seed) {
  // Your implementation here
  return [];
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const n = parseInt(data[0], 10);
  const k = parseInt(data[1], 10);
  const seed = BigInt(data[2]);
  const res = reservoirSample(n, k, seed);
  console.log(res.join(" "));
});
```
