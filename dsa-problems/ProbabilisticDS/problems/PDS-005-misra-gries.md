---
problem_id: PDS_MISRA_GRIES__9624
display_id: PDS-005
slug: misra-gries
title: "Frequent Items with Misra-Gries"
difficulty: Medium
difficulty_score: 52
topics:
  - Probabilistic Data Structures
  - Streaming
  - Frequency Estimation
tags:
  - probabilistic-ds
  - misra-gries
  - streaming
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-005: Frequent Items with Misra-Gries

## Problem Statement

Given a stream of `n` integers and a parameter `k`, run the Misra-Gries algorithm with `k-1` counters. Output the set of candidate items after processing the stream.

If no candidates remain, print an empty line.

![Problem Illustration](../images/PDS-005/problem-illustration.png)

## Input Format

- First line: integers `n` and `k`
- Second line: `n` space-separated integers (stream)

## Output Format

- Single line: candidate items in ascending order, space-separated

## Constraints

- `1 <= n <= 10^6`
- `2 <= k <= 1000`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
7 3
1 2 1 3 1 2 4
```

**Output:**

```
1 2
```

**Explanation:**

Misra-Gries keeps at most 2 counters and returns {1,2} as candidates.

![Example Visualization](../images/PDS-005/example-1.png)

## Notes

- The algorithm guarantees all items with frequency > n/k appear in the candidates
- A second pass is needed to verify true frequencies (not required here)
- Time complexity: O(n * k) in the naive implementation, O(n) with hash map

## Related Topics

Heavy Hitters, Streaming Algorithms

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public List<Integer> misraGries(int[] stream, int k) {
        //Implement here
        return new ArrayList<>();
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            int[] stream = new int[n];
            for (int i = 0; i < n; i++) {
                stream[i] = sc.nextInt();
            }
    
            Solution solution = new Solution();
            List<Integer> res = solution.misraGries(stream, k);
            for (int i = 0; i < res.size(); i++) {
                System.out.print(res.get(i));
                if (i + 1 < res.size()) System.out.print(" ");
            }
            System.out.println();
        }
        sc.close();
    }
}
```

### Python

```python
import sys
from collections import Counter

def misra_gries(stream, k):
    # //Implement here
    return 0

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        k = int(next(iterator))
        stream = []
        for _ in range(n):
            stream.append(int(next(iterator)))
            
        res = misra_gries(stream, k)
        print(" ".join(str(x) for x in res))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> misraGries(const vector<int>& stream, int k) {
        //Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (cin >> n >> k) {
        vector<int> stream(n);
        for (int i = 0; i < n; i++) cin >> stream[i];
    
        Solution solution;
        vector<int> res = solution.misraGries(stream, k);
        for (int i = 0; i < (int)res.size(); i++) {
            if (i) cout << " ";
            cout << res[i];
        }
        cout << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function misraGries(stream, k) {
  //Implement here
  return 0;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part !== "") data.push(part);
  }
});
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const k = parseInt(data[idx++], 10);
  const stream = [];
  for (let i = 0; i < n; i++) stream.push(parseInt(data[idx++], 10));
  const res = misraGries(stream, k);
  console.log(res.join(" "));
});
```

