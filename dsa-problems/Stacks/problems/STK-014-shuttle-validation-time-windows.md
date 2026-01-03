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
import java.io.*;

class Solution {
    public boolean validate(List<Integer> push, List<Integer> pushT, 
                            List<Integer> pop, List<Integer> popT,
                            Map<Integer, Integer> windows, Set<Integer> priority) {
        //Implement here
        return false;
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        
        // Helper to read tokens robustly
        // State machine parsing based on counts
        
        String line = br.readLine();
        while (line != null && line.trim().isEmpty()) line = br.readLine();
        if (line == null) return;
        
        int numPush = Integer.parseInt(line.trim());
        List<Integer> push = new ArrayList<>();
        List<Integer> pushT = new ArrayList<>();
        
        for (int i = 0; i < numPush; i++) {
            String[] parts = br.readLine().trim().split("\\s+");
            push.add(Integer.parseInt(parts[0]));
            pushT.add(Integer.parseInt(parts[1]));
        }
        
        int numPop = Integer.parseInt(br.readLine().trim());
        List<Integer> pop = new ArrayList<>();
        List<Integer> popT = new ArrayList<>();
        
        for (int i = 0; i < numPop; i++) {
            String[] parts = br.readLine().trim().split("\\s+");
            pop.add(Integer.parseInt(parts[0]));
            popT.add(Integer.parseInt(parts[1]));
        }
        
        int numWindows = Integer.parseInt(br.readLine().trim());
        Map<Integer, Integer> windows = new HashMap<>();
        
        for (int i = 0; i < numWindows; i++) {
            String[] parts = br.readLine().trim().split("\\s+");
            windows.put(Integer.parseInt(parts[0]), Integer.parseInt(parts[1]));
        }
        
        int numPriority = Integer.parseInt(br.readLine().trim());
        Set<Integer> priority = new HashSet<>();
        
        for (int i = 0; i < numPriority; i++) {
            String l = br.readLine();
            if (l != null && !l.trim().isEmpty()) {
                priority.add(Integer.parseInt(l.trim()));
            }
        }
        
        Solution sol = new Solution();
        boolean res = sol.validate(push, pushT, pop, popT, windows, priority);
        System.out.println(res ? "YES" : "NO");
    }
}
```

### Python

```python
def validate(push, push_t, pop, pop_t, windows, priority) -> bool:
    # //Implement here
    return 0

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if not lines:
        return

    num_push = int(lines[0])
    push = []
    push_t = []
    for i in range(1, num_push + 1):
        parts = lines[i].split()
        push.append(int(parts[0]))
        push_t.append(int(parts[1]))

    num_pop = int(lines[num_push + 1])
    pop = []
    pop_t = []
    for i in range(num_push + 2, num_push + 2 + num_pop):
        parts = lines[i].split()
        pop.append(int(parts[0]))
        pop_t.append(int(parts[1]))

    num_windows = int(lines[num_push + 2 + num_pop])
    windows = {}
    for i in range(num_push + 3 + num_pop, num_push + 3 + num_pop + num_windows):
        parts = lines[i].split()
        windows[int(parts[0])] = int(parts[1])

    num_priority = int(lines[num_push + 3 + num_pop + num_windows])
    priority = set()
    for i in range(num_push + 4 + num_pop + num_windows, num_push + 4 + num_pop + num_windows + num_priority):
        priority.add(int(lines[i]))

    result = validate(push, push_t, pop, pop_t, windows, priority)
    print("YES" if result else "NO")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <climits>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool validate(vector<int>& push, vector<int>& pushT,
                 vector<int>& pop, vector<int>& popT,
                 map<int, int>& windows, set<int>& priority) {
        //Implement here
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int numPush;
    if (!(cin >> numPush)) return 0;
    
    vector<int> push(numPush);
    vector<int> pushT(numPush);
    for (int i = 0; i < numPush; i++) {
        cin >> push[i] >> pushT[i];
    }
    
    int numPop;
    cin >> numPop;
    vector<int> pop(numPop);
    vector<int> popT(numPop);
    for (int i = 0; i < numPop; i++) {
        cin >> pop[i] >> popT[i];
    }
    
    int numWindows;
    cin >> numWindows;
    map<int, int> windows;
    for (int i = 0; i < numWindows; i++) {
        int k, v;
        cin >> k >> v;
        windows[k] = v;
    }
    
    int numPriority;
    cin >> numPriority;
    set<int> priority;
    for (int i = 0; i < numPriority; i++) {
        int val;
        cin >> val;
        priority.insert(val);
    }
    
    Solution sol;
    cout << (sol.validate(push, pushT, pop, popT, windows, priority) ? "YES" : "NO") << endl;
    
    return 0;
}
```

### JavaScript

```javascript
class Solution {
  validate(push, pushT, pop, popT, windows, priority) {
    //Implement here
    return 0;
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => {
  lines.push(line);
});

rl.on("close", () => {
  if (lines.length === 0) return;
  
  let lineIdx = 0;
  const numPush = parseInt(lines[lineIdx++].trim(), 10);
  
  const push = [];
  const pushT = [];
  
  for (let i = 0; i < numPush; i++) {
    const parts = lines[lineIdx++].trim().split(/\s+/);
    push.push(parseInt(parts[0], 10));
    pushT.push(parseInt(parts[1], 10));
  }
  
  const numPop = parseInt(lines[lineIdx++].trim(), 10);
  const pop = [];
  const popT = [];
  
  for (let i = 0; i < numPop; i++) {
    const parts = lines[lineIdx++].trim().split(/\s+/);
    pop.push(parseInt(parts[0], 10));
    popT.push(parseInt(parts[1], 10));
  }
  
  const numWindows = parseInt(lines[lineIdx++].trim(), 10);
  const windows = new Map();
  
  for (let i = 0; i < numWindows; i++) {
    const parts = lines[lineIdx++].trim().split(/\s+/);
    windows.set(parseInt(parts[0], 10), parseInt(parts[1], 10));
  }
  
  const numPriority = parseInt(lines[lineIdx++].trim(), 10);
  const priority = new Set();
  
  for (let i = 0; i < numPriority; i++) {
    if (lineIdx < lines.length) {
       const l = lines[lineIdx++].trim();
       if (l) priority.add(parseInt(l, 10));
    }
  }
  
  const solution = new Solution();
  const res = solution.validate(push, pushT, pop, popT, windows, priority);
  console.log(res ? "YES" : "NO");
});
```

