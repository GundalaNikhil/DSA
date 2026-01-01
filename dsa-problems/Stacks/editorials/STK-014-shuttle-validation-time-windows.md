---
title: Shuttle Validation with Time Windows
slug: shuttle-validation-time-windows
difficulty: Medium
difficulty_score: 61
tags:
- Stack
- Simulation
- Validation
problem_id: STK_SHUTTLE_VALIDATION_TIME_WINDOWS__2743
display_id: STK-014
topics:
- Stack
- Simulation
- Constraints
---
# Shuttle Validation with Time Windows - Editorial

## Problem Summary

Validate a stack push/pop sequence with two additional constraints:
1.  **Time Windows**: Certain elements must be popped within `W` time units of being pushed.
2.  **Priority Constraint**: Each priority element must be popped before any larger non-priority element. When popping a non-priority element `X`, there must be no priority element `P` currently in the stack such that `X > P`. Priority elements block larger non-priority elements from being popped.


## Constraints

- `1 <= n <= 100000`
- `0 <= times <= 10^9`
- All values are integers and unique in the push sequence
## Real-World Scenario

Imagine a **Space Shuttle Cargo Bay**.
-   **Stack**: Cargo is loaded (pushed) and unloaded (popped) in LIFO order.
-   **Time Windows**: Some perishable items (e.g., food, biological samples) must be unloaded within `W` hours of loading, or they spoil.
-   **Priority**: Some items are "High Priority" (e.g., emergency medical supplies).
-   **Rule**: You cannot unload a large, low-priority crate if there's a smaller, high-priority box still waiting in the stack. The validation checks whether the loading/unloading plan respects these constraints.

## Problem Exploration

### 1. Stack Simulation
-   Standard "Validate Stack Sequences" logic:
    -   Iterate through `pushed` array.
    -   Push `pushed[i]`.
    -   While `stack.top() == popped[j]`:
        -   Pop from stack.
        -   `j++`.
-   If stack is empty at the end, the sequence is valid (structurally).

### 2. Time Window Constraint
-   We are given `pushTimes` and `popTimes`.
-   When we push `x` at `pushT`, we store `(x, pushT)`.
-   When we pop `x` at `popT`, we check if `x` has a window `W`.
-   Condition: `popT - pushT <= W`.
-   If not, return `false`.

### 3. Priority Constraint
-   When popping a non-priority element `X`, there must be no priority element `P` currently in the stack such that `P < X`.
-   We need to efficiently track the **minimum priority element** currently in the stack.
-   Use an auxiliary **Min-Stack** to track the minimum priority value at each stack level.
-   When pushing `val`:
    -   If `val` is Priority: `new_min = min(val, current_min)`.
    -   If `val` is Non-Priority: `new_min = current_min`.
    -   Push `new_min` to the auxiliary stack.
-   When popping a non-priority element `X`:
    -   Check if `X > min_priority_in_stack`.
    -   If true, the constraint is violated.
    -   Pop from the auxiliary stack.

## Approaches

### Approach 1: Simulation with Auxiliary Min-Stack
-   Use a main stack for simulation.
-   Use an auxiliary stack to track the minimum priority element currently in the stack.
-   Check time constraints on pop.
-   Check priority constraints on pop.
-   Complexity: `O(N)` time, `O(N)` space.

## Implementations

### Java
```java
import java.util.*;
import java.io.*;

class Solution {
    public boolean validate(List<Integer> push, List<Integer> pushT, 
                            List<Integer> pop, List<Integer> popT,
                            Map<Integer, Integer> windows, Set<Integer> priority) {
        Stack<Integer> stack = new Stack<>();
        Stack<Integer> timeStack = new Stack<>();
        Stack<Integer> minPriorityStack = new Stack<>();
        
        int j = 0;
        int n = push.size();
        
        for (int i = 0; i < n; i++) {
            int val = push.get(i);
            int t = pushT.get(i);
            
            stack.push(val);
            timeStack.push(t);
            
            int currentMin = minPriorityStack.isEmpty() ? Integer.MAX_VALUE : minPriorityStack.peek();
            if (priority.contains(val)) {
                currentMin = Math.min(currentMin, val);
            }
            minPriorityStack.push(currentMin);
            
            while (!stack.isEmpty() && j < n && stack.peek().equals(pop.get(j))) {
                int poppedVal = stack.pop();
                int pushedTime = timeStack.pop();
                minPriorityStack.pop();
                
                int poppedTime = popT.get(j);
                
                // Check Time Window
                if (windows.containsKey(poppedVal)) {
                    if (poppedTime - pushedTime > windows.get(poppedVal)) {
                        return false;
                    }
                }
                
                // Check Priority
                if (!priority.contains(poppedVal)) {
                    int minP = minPriorityStack.isEmpty() ? Integer.MAX_VALUE : minPriorityStack.peek();
                    if (poppedVal > minP) {
                        return false;
                    }
                }
                
                j++;
            }
        }
        
        return stack.isEmpty();
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
    stack = []
    time_stack = []
    min_priority_stack = []
    
    j = 0
    n = len(push)
    
    for i in range(n):
        val = push[i]
        t = push_t[i]
        
        stack.append(val)
        time_stack.append(t)
        
        current_min = min_priority_stack[-1] if min_priority_stack else float('inf')
        if val in priority:
            current_min = min(current_min, val)
        min_priority_stack.append(current_min)
        
        while stack and j < n and stack[-1] == pop[j]:
            popped_val = stack.pop()
            pushed_time = time_stack.pop()
            min_priority_stack.pop()
            
            popped_time = pop_t[j]
            
            # Check Time Window
            if popped_val in windows:
                if popped_time - pushed_time > windows[popped_val]:
                    return False
            
            # Check Priority
            if popped_val not in priority:
                min_p = min_priority_stack[-1] if min_priority_stack else float('inf')
                if popped_val > min_p:
                    return False
            
            j += 1
            
    return not stack


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
        
        stack<int> st;
        stack<int> timeStack;
        stack<int> minPriorityStack;
        
        int j = 0;
        int n = push.size();
        
        for (int i = 0; i < n; i++) {
            int val = push[i];
            int t = pushT[i];
            
            st.push(val);
            timeStack.push(t);
            
            int currentMin = minPriorityStack.empty() ? INT_MAX : minPriorityStack.top();
            if (priority.count(val)) {
                currentMin = min(currentMin, val);
            }
            minPriorityStack.push(currentMin);
            
            while (!st.empty() && j < n && st.top() == pop[j]) {
                int poppedVal = st.top(); st.pop();
                int pushedTime = timeStack.top(); timeStack.pop();
                minPriorityStack.pop();
                
                int poppedTime = popT[j];
                
                // Check Time Window
                if (windows.count(poppedVal)) {
                    if (poppedTime - pushedTime > windows[poppedVal]) {
                        return false;
                    }
                }
                
                // Check Priority
                if (!priority.count(poppedVal)) {
                    int minP = minPriorityStack.empty() ? INT_MAX : minPriorityStack.top();
                    if (poppedVal > minP) {
                        return false;
                    }
                }
                
                j++;
            }
        }
        
        return st.empty();
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
    const stack = [];
    const timeStack = [];
    const minPriorityStack = [];
    
    let j = 0;
    const n = push.length;
    
    for (let i = 0; i < n; i++) {
      const val = push[i];
      const t = pushT[i];
      
      stack.push(val);
      timeStack.push(t);
      
      let currentMin = minPriorityStack.length === 0 ? Infinity : minPriorityStack[minPriorityStack.length - 1];
      if (priority.has(val)) {
        currentMin = Math.min(currentMin, val);
      }
      minPriorityStack.push(currentMin);
      
      while (stack.length > 0 && j < n && stack[stack.length - 1] === pop[j]) {
        const poppedVal = stack.pop();
        const pushedTime = timeStack.pop();
        minPriorityStack.pop();
        
        const poppedTime = popT[j];
        
        // Check Time Window
        if (windows.has(poppedVal)) {
          if (poppedTime - pushedTime > windows.get(poppedVal)) {
            return false;
          }
        }
        
        // Check Priority
        if (!priority.has(poppedVal)) {
          const minP = minPriorityStack.length === 0 ? Infinity : minPriorityStack[minPriorityStack.length - 1];
          if (poppedVal > minP) {
            return false;
          }
        }
        
        j++;
      }
    }
    
    return stack.length === 0;
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

## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
-   Push: `4 5 6`, Times: `0 2 4`
-   Pop: `6 5 4`, Times: `5 6 10`
-   Window: `5` -> `2`
-   Priority: `4`

1.  Push `4` (t=0). Priority. MinP=`4`. Stack `[4]`.
2.  Push `5` (t=2). Non-P. MinP=`4`. Stack `[4, 5]`.
3.  Push `6` (t=4). Non-P. MinP=`4`. Stack `[4, 5, 6]`.
4.  Pop `6` (t=5).
    -   Window: None.
    -   Priority: `6` is Non-P. Check `MinP` below. Stack below has `[4, 5]`. MinP is `4`.
    -   `6 > 4`. **Violation!**
    -   Return `false`.

The example output returns `false` due to the **Time Window** violation: "Value 5 must be popped within 2 time units... popped at time 6".

Note that this test case also violates the priority constraint (element `6` is non-priority and popped while priority element `4` with smaller value is still in the stack). The implementation may detect either constraint violation first depending on the order of checks. Both are valid reasons for returning `false`.

## Proof of Correctness

-   **Structure**: Standard simulation ensures LIFO validity.
-   **Time**: Direct check `pop - push <= W`.
-   **Priority**: The Min-Stack invariant correctly tracks the minimum priority value *currently waiting* in the stack. If we pop a larger non-priority value, we confirm a priority value is still waiting, which violates the ordering rule.

## Interview Extensions

1.  **Multiple Priority Levels**: What if priority is 1-10?
    -   *Hint*: "Higher priority popped before lower priority". Similar logic, check `max_priority_below > current_priority`.
2.  **Online Validation**: Stream of operations.
    -   *Hint*: Same logic works online.

### Common Mistakes

-   **Min Stack Update**: Forgetting to pop from `minPriorityStack` when popping from main stack.
-   **Priority Logic**: Checking `val > minP` for *priority* elements too (only non-priority are restricted).
-   **Time Units**: Mixing up push/pop times.
