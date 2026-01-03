---
problem_id: HEP_ROPE_CONNECT_MAXIMIZE_PRIORITY__6742
display_id: HEP-004
slug: rope-connect-maximize-priority
title: "Rope Connection Maximize Strength with Priority Classes"
difficulty: Medium
difficulty_score: 57
topics:
  - Heaps
  - Greedy
  - Priority Classes
tags:
  - heaps
  - greedy
  - priority
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# HEP-004: Rope Connection Maximize Strength with Priority Classes

## Problem Statement

You are given `n` ropes. Each rope has a strength and a priority class:

- Class 1: critical
- Class 2: standard
- Class 3: spare

You may repeatedly connect two ropes into one. The new strength is:

```
strength = s1 + s2 - penalty
```

Penalty rules:

- 0 if both ropes are in the same class
- 1 if classes differ by 1 (1 with 2, or 2 with 3)
- 2 if classes are 1 and 3

The new rope inherits the higher priority class (smaller class number). Continue until one rope remains. Maximize the final rope strength.

![Problem Illustration](../images/HEP-004/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` integers for strengths
- Third line: `n` integers for priority classes (each in {1,2,3})

## Output Format

- Single integer: maximum possible final rope strength

## Constraints

- `1 <= n <= 100000`
- `1 <= strength <= 10^9`
- Priority class is 1, 2, or 3

## Example

**Input:**

```
3
6 5 4
1 2 3
```

**Output:**

```
13
```

**Explanation:**

One optimal sequence:

- Connect strengths 5 (class 2) and 4 (class 3)
  - Penalty = 1, new strength = 5 + 4 - 1 = 8, new class = 2
- Connect strengths 8 (class 2) and 6 (class 1)
  - Penalty = 1, new strength = 8 + 6 - 1 = 13

Final strength = 13.

![Example Visualization](../images/HEP-004/example-1.png)

## Notes

- Keep max-heaps for each class to pick strong candidates
- Prefer same-class merges to avoid penalties when possible
- Time complexity: O(n log n)
- Space complexity: O(n)

## Related Topics

Heaps, Greedy, Priority Scheduling, Merging

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long maxFinalStrength(int[] strengths, int[] priority) {
        //Implement here
        return 0L;
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;

        if ((line = br.readLine()) != null) {
            int n = Integer.parseInt(line.trim());

            int[] strengths = new int[n];
            String[] strengthTokens = br.readLine().trim().split(" ");
            for (int i = 0; i < n; i++) {
                strengths[i] = Integer.parseInt(strengthTokens[i]);
            }

            int[] priority = new int[n];
            String[] priorityTokens = br.readLine().trim().split(" ");
            for (int i = 0; i < n; i++) {
                priority[i] = Integer.parseInt(priorityTokens[i]);
            }

            Solution solution = new Solution();
            System.out.println(solution.maxFinalStrength(strengths, priority));
        }
    }
}
```

### Python

```python
import sys

def max_final_strength(strengths: list, priority: list) -> int:
    # //Implement here
    return 0

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    try:
        n = int(next(it))
        strengths = []
        for _ in range(n):
            strengths.append(int(next(it)))
        priority = []
        for _ in range(n):
            priority.append(int(next(it)))

        print(max_final_strength(strengths, priority))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    long long maxFinalStrength(const vector<int>& strengths, const vector<int>& priority) {
        //Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (cin >> n) {
        vector<int> strengths(n), priority(n);
        for (int i = 0; i < n; i++) cin >> strengths[i];
        for (int i = 0; i < n; i++) cin >> priority[i];

        Solution solution;
        cout << solution.maxFinalStrength(strengths, priority) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxFinalStrength(strengths, priority) {
    //Implement here
    return 0;
  }
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
  const n = parseInt(data[idx++]);
  const strengths = [];
  const priority = [];
  for (let i = 0; i < n; i++) strengths.push(parseInt(data[idx++]));
  for (let i = 0; i < n; i++) priority.push(parseInt(data[idx++]));

  const solution = new Solution();
  console.log(solution.maxFinalStrength(strengths, priority));
});
```
