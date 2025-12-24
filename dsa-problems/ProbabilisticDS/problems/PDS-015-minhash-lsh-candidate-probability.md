---
problem_id: PDS_PROBLEM_15__4501
display_id: PDS-015
slug: minhash-lsh-candidate-probability
title: "MinHash LSH Candidate Probability"
difficulty: Medium
difficulty_score: 50
topics:
  - Probabilistic Data Structures
  - MinHash
  - LSH
tags:
  - probabilistic-ds
  - lsh
  - minhash
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-015: MinHash LSH Candidate Probability

## Problem Statement

In MinHash LSH with `b` bands and `r` rows per band, the probability that two sets with Jaccard similarity `s` become a candidate pair is:

```
P = 1 - (1 - s^r)^b
```

Compute `P`.

![Problem Illustration](../images/PDS-015/problem-illustration.png)

## Input Format

- Single line: integers `b`, `r`, and real `s`

## Output Format

- Single floating-point number: candidate probability

## Constraints

- `1 <= b, r <= 1000`
- `0 <= s <= 1`

## Example

**Input:**

```
5 2 0.5
```

**Output:**

```
0.762695
```

**Explanation:**

P = 1 - (1 - 0.5^2)^5 = 0.762695.

![Example Visualization](../images/PDS-015/example-1.png)

## Notes

- Use double precision
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

MinHash, LSH, Similarity Search

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double lshCandidateProb(int b, int r, double s) {
        // Your implementation here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int b = sc.nextInt();
        int r = sc.nextInt();
        double s = sc.nextDouble();

        Solution solution = new Solution();
        System.out.println(solution.lshCandidateProb(b, r, s));
        sc.close();
    }
}
```

### Python

```python
def lsh_candidate_prob(b: int, r: int, s: float) -> float:
    # Your implementation here
    return 0.0

def main():
    b, r, s = input().split()
    print(f"{lsh_candidate_prob(int(b), int(r), float(s)):.6f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    double lshCandidateProb(int b, int r, double s) {
        // Your implementation here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int b, r;
    double s;
    cin >> b >> r >> s;
    Solution solution;
    cout << solution.lshCandidateProb(b, r, s) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function lshCandidateProb(b, r, s) {
  // Your implementation here
  return 0.0;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const b = parseInt(data[0], 10);
  const r = parseInt(data[1], 10);
  const s = parseFloat(data[2]);
  console.log(lshCandidateProb(b, r, s).toFixed(6));
});
```
