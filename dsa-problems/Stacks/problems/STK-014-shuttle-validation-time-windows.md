---
problem_id: STK_SHUTTLE_VALIDATION_TIME_WINDOWS__2743
display_id: STK-014
slug: shuttle-validation-time-windows
title: "Shuttle Validation with Time Windows"
difficulty: Medium
difficulty_score: 61
topics:
  - Stack
  - Simulation
  - Constraints
tags:
  - stack
  - simulation
  - validation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STK-014: Shuttle Validation with Time Windows

## Problem Statement

You are given a push sequence and a pop sequence for a stack, along with timestamps for each push and pop. Some elements have time window constraints `W[x]` that require the element to be popped within `W[x]` time units after it was pushed. Some elements are marked as `priority` and must be popped before any larger non-priority element.
Determine whether all three conditions hold:

1. The pop sequence is valid for the given push sequence
2. Every constrained element is popped within its time window
3. Each priority element is popped before any larger non-priority element
   Output `true` if all conditions hold, otherwise `false`.
   ![Problem Illustration](../images/STK-014/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` integers (push sequence)
- Third line: `n` integers (push times)
- Fourth line: `n` integers (pop sequence)
- Fifth line: `n` integers (pop times)
- Sixth line: integer `w` (number of window constraints)
- Next `w` lines: `value window`
- Next line: integer `p` (number of priority values)
- Next line: `p` integers (priority values)

## Output Format

- Single line: `true` or `false`

## Constraints

- `1 <= n <= 100000`
- `0 <= times <= 10^9`
- All values are integers and unique in the push sequence

## Example

**Input:**

```
3
4 5 6
0 2 4
6 5 4
5 6 10
1
5 2
1
4
```

**Output:**

```
false
```

**Explanation:**
Value 5 must be popped within 2 time units of push at time 2, but it is popped at time 6, so the window constraint fails.
![Example Visualization](../images/STK-014/example-1.png)

## Notes

- Simulate stack pushes and pops in order
- Check time window when an element is popped
- Track the smallest pending priority value
- Time complexity: O(n)

## Related Topics

## Stack Simulation, Constraints Checking, Validation

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public boolean validate(int n, int[] pushSeq, long[] pushTimes, int[] popSeq, long[] popTimes,
                           Map<Integer, Long> windows, Set<Integer> priorities) {
        // Implement here
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] pushSeq = new int[n];
            for (int i = 0; i < n; i++) pushSeq[i] = sc.nextInt();
            long[] pushTimes = new long[n];
            for (int i = 0; i < n; i++) pushTimes[i] = sc.nextLong();
            int[] popSeq = new int[n];
            for (int i = 0; i < n; i++) popSeq[i] = sc.nextInt();
            long[] popTimes = new long[n];
            for (int i = 0; i < n; i++) popTimes[i] = sc.nextLong();

            int w = sc.nextInt();
            Map<Integer, Long> windows = new HashMap<>();
            for (int i = 0; i < w; i++) {
                int val = sc.nextInt();
                long win = sc.nextLong();
                windows.put(val, win);
            }

            int p = sc.nextInt();
            Set<Integer> priorities = new HashSet<>();
            for (int i = 0; i < p; i++) priorities.add(sc.nextInt());

            Solution sol = new Solution();
            System.out.println(sol.validate(n, pushSeq, pushTimes, popSeq, popTimes, windows, priorities));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def validate(self, n: int, push_seq: list, push_times: list, pop_seq: list, pop_times: list,
                 windows: dict, priorities: set) -> bool:
        # Implement here
        return False

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    n = int(input_data[idx]); idx += 1
    push_seq = [int(x) for x in input_data[idx:idx+n]]; idx += n
    push_times = [int(x) for x in input_data[idx:idx+n]]; idx += n
    pop_seq = [int(x) for x in input_data[idx:idx+n]]; idx += n
    pop_times = [int(x) for x in input_data[idx:idx+n]]; idx += n

    w = int(input_data[idx]); idx += 1
    windows = {}
    for _ in range(w):
        val = int(input_data[idx]); idx += 1
        win = int(input_data[idx]); idx += 1
        windows[val] = win

    p = int(input_data[idx]); idx += 1
    priorities = set()
    for _ in range(p):
        priorities.add(int(input_data[idx])); idx += 1

    sol = Solution()
    print(str(sol.validate(n, push_seq, push_times, pop_seq, pop_times, windows, priorities)).lower())

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <stack>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool validate(int n, const vector<int>& pushSeq, const vector<long long>& pushTimes,
                  const vector<int>& popSeq, const vector<long long>& popTimes,
                  unordered_map<int, long long>& windows, unordered_set<int>& priorities) {
        // Implement here
        return false;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (cin >> n) {
        vector<int> pushSeq(n);
        for (int i = 0; i < n; i++) cin >> pushSeq[i];
        vector<long long> pushTimes(n);
        for (int i = 0; i < n; i++) cin >> pushTimes[i];
        vector<int> popSeq(n);
        for (int i = 0; i < n; i++) cin >> popSeq[i];
        vector<long long> popTimes(n);
        for (int i = 0; i < n; i++) cin >> popTimes[i];

        int w;
        cin >> w;
        unordered_map<int, long long> windows;
        for (int i = 0; i < w; i++) {
            int val;
            long long win;
            cin >> val >> win;
            windows[val] = win;
        }

        int p;
        cin >> p;
        unordered_set<int> priorities;
        for (int i = 0; i < p; i++) {
            int val;
            cin >> val;
            priorities.insert(val);
        }

        Solution sol;
        cout << (sol.validate(n, pushSeq, pushTimes, popSeq, popTimes, windows, priorities) ? "true" : "false") << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  validate(n, pushSeq, pushTimes, popSeq, popTimes, windows, priorities) {
    // Implement here
    return false;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

let input = [];
rl.on("line", (line) => {
  if (line.trim()) input.push(...line.trim().split(/\s+/));
}).on("close", () => {
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const pushSeq = input.slice(idx, idx + n).map(Number);
  idx += n;
  const pushTimes = input.slice(idx, idx + n).map(BigInt);
  idx += n;
  const popSeq = input.slice(idx, idx + n).map(Number);
  idx += n;
  const popTimes = input.slice(idx, idx + n).map(BigInt);
  idx += n;

  const w = parseInt(input[idx++]);
  const windows = new Map();
  for (let i = 0; i < w; i++) {
    const val = parseInt(input[idx++]);
    const win = BigInt(input[idx++]);
    windows.set(val, win);
  }

  const p = parseInt(input[idx++]);
  const priorities = new Set(input.slice(idx, idx + p).map(Number));

  const sol = new Solution();
  console.log(
    sol.validate(n, pushSeq, pushTimes, popSeq, popTimes, windows, priorities)
  );
});
```
