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
Stack Simulation, Constraints Checking, Validation
---
## Solution Template
### Java
```java
import java.util.*;
class Solution {
    public boolean validate(int[] push, long[] pushT, int[] pop, long[] popT, Map<Integer, Long> windows, Set<Integer> priority) {
        // Your implementation here
        return false;
    }
}
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] push = new int[n];
        long[] pushT = new long[n];
        int[] pop = new int[n];
        long[] popT = new long[n];
        for (int i = 0; i < n; i++) push[i] = sc.nextInt();
        for (int i = 0; i < n; i++) pushT[i] = sc.nextLong();
        for (int i = 0; i < n; i++) pop[i] = sc.nextInt();
        for (int i = 0; i < n; i++) popT[i] = sc.nextLong();
        int w = sc.nextInt();
        Map<Integer, Long> windows = new HashMap<>();
        for (int i = 0; i < w; i++) {
            int v = sc.nextInt();
            long t = sc.nextLong();
            windows.put(v, t);
        }
        int p = sc.nextInt();
        Set<Integer> priority = new HashSet<>();
        for (int i = 0; i < p; i++) priority.add(sc.nextInt());
        Solution solution = new Solution();
        System.out.println(solution.validate(push, pushT, pop, popT, windows, priority) ? "true" : "false");
        sc.close();
    }
}
```
### Python
```python
def validate(push, push_t, pop, pop_t, windows, priority) -> bool:
    # Your implementation here
    return False
def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    push = [int(next(it)) for _ in range(n)]
    push_t = [int(next(it)) for _ in range(n)]
    pop = [int(next(it)) for _ in range(n)]
    pop_t = [int(next(it)) for _ in range(n)]
    w = int(next(it))
    windows = {}
    for _ in range(w):
        v = int(next(it))
        t = int(next(it))
        windows[v] = t
    p = int(next(it))
    priority = {int(next(it)) for _ in range(p)}
    print("true" if validate(push, push_t, pop, pop_t, windows, priority) else "false")
if __name__ == "__main__":
    main()
```
### C++
```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;
class Solution {
public:
    bool validate(const vector<int>& push, const vector<long long>& pushT, const vector<int>& pop, const vector<long long>& popT,
                  const unordered_map<int,long long>& windows, const unordered_set<int>& priority) {
        // Your implementation here
        return false;
    }
};
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<int> push(n), pop(n);
    vector<long long> pushT(n), popT(n);
    for (int i = 0; i < n; i++) cin >> push[i];
    for (int i = 0; i < n; i++) cin >> pushT[i];
    for (int i = 0; i < n; i++) cin >> pop[i];
    for (int i = 0; i < n; i++) cin >> popT[i];
    int w;
    cin >> w;
    unordered_map<int,long long> windows;
    for (int i = 0; i < w; i++) {
        int v; long long t;
        cin >> v >> t;
        windows[v] = t;
    }
    int p;
    cin >> p;
    unordered_set<int> priority;
    for (int i = 0; i < p; i++) {
        int v; cin >> v;
        priority.insert(v);
    }
    Solution solution;
    cout << (solution.validate(push, pushT, pop, popT, windows, priority) ? "true" : "false") << "\n";
    return 0;
}
```
### JavaScript
```javascript
const readline = require("readline");
class Solution {
  validate(push, pushT, pop, popT, windows, priority) {
    // Your implementation here
    return false;
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
  const n = parseInt(data[idx++], 10);
  const push = [];
  const pushT = [];
  const pop = [];
  const popT = [];
  for (let i = 0; i < n; i++) push.push(parseInt(data[idx++], 10));
  for (let i = 0; i < n; i++) pushT.push(parseInt(data[idx++], 10));
  for (let i = 0; i < n; i++) pop.push(parseInt(data[idx++], 10));
  for (let i = 0; i < n; i++) popT.push(parseInt(data[idx++], 10));
  const w = parseInt(data[idx++], 10);
  const windows = new Map();
  for (let i = 0; i < w; i++) {
    const v = parseInt(data[idx++], 10);
    const t = parseInt(data[idx++], 10);
    windows.set(v, t);
  }
  const p = parseInt(data[idx++], 10);
  const priority = new Set();
  for (let i = 0; i < p; i++) priority.add(parseInt(data[idx++], 10));
  const solution = new Solution();
  console.log(solution.validate(push, pushT, pop, popT, windows, priority) ? "true" : "false");
});
```
