---
problem_id: HEP_SCHEDULER_COOLING_PRIORITY__5382
display_id: HEP-014
slug: scheduler-cooling-priority
title: "Scheduler With Cooling and Priority"
difficulty: Medium
difficulty_score: 57
topics:
  - Heaps
  - Scheduling
  - Greedy
tags:
  - heaps
  - cooldown
  - scheduling
  - medium
premium: true
subscription_tier: basic
---

# HEP-014: Scheduler With Cooling and Priority

## 📋 Problem Summary

You have `m` task types. Each has a `count` (available units) and a `priority` (score per unit).
You have `T` time slots.
In each slot, you can run one task or idle.
Constraint: If you run task type `X` at time `t`, you cannot run `X` again until `t + k + 1`.
Goal: Maximize total priority score within `T` slots.

## 🌍 Real-World Scenario

**Scenario Title:** High-Performance Computing Job Dispatch

A supercomputer scheduler receives jobs of different types (e.g., Physics Sim, AI Training).
- Each job type has a value (priority) and a limited number of pending requests (count).
- Running a job of type `X` heats up a specific hardware component.
- The component needs `k` cycles to cool down before it can run type `X` again.
- You have a fixed time window `T` to maximize the value of completed jobs.

![Real-World Application](../images/HEP-014/real-world-scenario.png)

## Detailed Explanation

### Feasibility of counts

Let `x_i` be how many times task type `i` is executed, with `0 <= x_i <= count_i`.
A schedule exists in `T` slots with cooldown `k` iff:
```
L = max(sum_x, (max_x - 1) * (k + 1) + n_max) <= T
```
where `sum_x = sum x_i`, `max_x = max x_i`, and `n_max` is the number of task
types that achieve `max_x`. This is the standard Task Scheduler bound and is
always tight.

So the problem reduces to choosing `x_i` to maximize:
```
score = sum(x_i * priority_i)
```
subject to the feasibility constraint above.

### Greedy reduction to maximize score

1. **Per-task cap:** A single task type cannot exceed
   `limit = floor((T + k) / (k + 1))`, so clamp
   `x_i = min(count_i, limit)`.
2. **Schedule constraint:** While
   `(max_x - 1) * (k + 1) + n_max > T`, only tasks at `max_x` can reduce the
   bound. Keep the `Y = T - (max_x - 1) * (k + 1)` highest-priority tasks at
   `max_x` and decrement the rest by 1.
3. **Sum constraint:** If `sum_x > T`, remove units from the lowest-priority
   tasks until `sum_x = T`. This never violates the schedule bound because
   decreasing counts only makes it easier to schedule.

### Algorithm

1. Initialize `x_i = min(count_i, limit)` for all tasks.
2. Fix the schedule bound by repeatedly demoting the lowest-priority tasks among
   those at `max_x`.
3. Fix the sum bound by removing units from lowest-priority tasks until
   `sum_x <= T`.
4. Return `sum(x_i * priority_i)`.

### Time Complexity

- **O(m^2 log m)** (with `m <= 26`, this is tiny).

### Space Complexity

- **O(m)**.

![Algorithm Visualization](../images/HEP-014/algorithm-visualization.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    static class Task {
        String id;
        int count;
        long priority;
        int x; // assigned count
        
        public Task(String id, int count, long priority) {
            this.id = id;
            this.count = count;
            this.priority = priority;
            this.x = count;
        }
    }
    
    public long maxPriority(int T, int cooldown, String[] ids, int[] count, long[] priority) {
        int m = ids.length;
        List<Task> tasks = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            tasks.add(new Task(ids[i], count[i], priority[i]));
        }
        
        // 1. Clamp
        int limit = (T + cooldown) / (cooldown + 1);
        for (Task t : tasks) {
            t.x = Math.min(t.count, limit);
        }
        
        // 2. Satisfy Schedule Constraint
        while (true) {
            int maxX = 0;
            for (Task t : tasks) maxX = Math.max(maxX, t.x);
            
            if (maxX == 0) break;
            
            List<Task> atMax = new ArrayList<>();
            for (Task t : tasks) {
                if (t.x == maxX) atMax.add(t);
            }
            
            long required = (long)(maxX - 1) * (cooldown + 1) + atMax.size();
            
            if (required <= T) break;
            
            // Too many at maxX. Allowed?
            long allowed = T - (long)(maxX - 1) * (cooldown + 1);
            // allowed can be negative if T is very small, but clamp handles basic bounds.
            // If allowed < 0, it means even 1 task at maxX is too much?
            // (maxX-1)(k+1) + 1 > T.
            // This implies maxX is too high.
            // But we clamped maxX <= (T+k)/(k+1).
            // So (maxX-1)(k+1) + 1 <= T is guaranteed for a SINGLE task.
            // So allowed >= 1.
            
            // Sort atMax by Priority Descending (Keep high priority)
            atMax.sort((a, b) -> Long.compare(b.priority, a.priority));
            
            // Keep top 'allowed', demote others
            for (int i = (int)allowed; i < atMax.size(); i++) {
                atMax.get(i).x--;
            }
        }
        
        // 3. Satisfy Sum Constraint
        long sumX = 0;
        for (Task t : tasks) sumX += t.x;
        
        if (sumX > T) {
            long toRemove = sumX - T;
            // Sort by Priority Ascending (Remove low priority)
            tasks.sort((a, b) -> Long.compare(a.priority, b.priority));
            
            for (Task t : tasks) {
                if (toRemove <= 0) break;
                int remove = (int)Math.min(t.x, toRemove);
                t.x -= remove;
                toRemove -= remove;
            }
        }
        
        long totalScore = 0;
        for (Task t : tasks) totalScore += t.x * t.priority;
        
        return totalScore;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int m = sc.nextInt();
            int cooldown = sc.nextInt();
            int T = sc.nextInt();
            String[] ids = new String[m];
            int[] count = new int[m];
            long[] priority = new long[m];
            for (int i = 0; i < m; i++) {
                ids[i] = sc.next();
                count[i] = sc.nextInt();
                priority[i] = sc.nextLong();
            }
            
            Solution solution = new Solution();
            System.out.println(solution.maxPriority(T, cooldown, ids, count, priority));
        }
        sc.close();
    }
}
```

### Python
```python
import sys

class Task:
    def __init__(self, tid, count, priority):
        self.id = tid
        self.count = count
        self.priority = priority
        self.x = count

class Solution:
    def max_priority(self, T: int, cooldown: int, ids: list, count: list, priority: list) -> int:
        tasks = []
        for i in range(len(ids)):
            tasks.append(Task(ids[i], count[i], priority[i]))
            
        # 1. Clamp
        limit = (T + cooldown) // (cooldown + 1)
        for t in tasks:
            t.x = min(t.count, limit)
            
        # 2. Schedule Constraint
        while True:
            max_x = 0
            for t in tasks:
                max_x = max(max_x, t.x)
            
            if max_x == 0:
                break
                
            at_max = [t for t in tasks if t.x == max_x]
            required = (max_x - 1) * (cooldown + 1) + len(at_max)
            
            if required <= T:
                break
                
            allowed = T - (max_x - 1) * (cooldown + 1)
            # Sort by priority desc
            at_max.sort(key=lambda x: x.priority, reverse=True)
            
            for i in range(int(allowed), len(at_max)):
                at_max[i].x -= 1
                
        # 3. Sum Constraint
        sum_x = sum(t.x for t in tasks)
        if sum_x > T:
            to_remove = sum_x - T
            # Sort by priority asc
            tasks.sort(key=lambda x: x.priority)
            
            for t in tasks:
                if to_remove <= 0:
                    break
                rem = min(t.x, to_remove)
                t.x -= rem
                to_remove -= rem
                
        return sum(t.x * t.priority for t in tasks)

def max_priority(T: int, cooldown: int, ids: list, count: list, priority: list) -> int:
    solver = Solution()
    return solver.max_priority(T, cooldown, ids, count, priority)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        m = int(next(it))
        cooldown = int(next(it))
        T = int(next(it))
        ids = []
        count = []
        priority = []
        for _ in range(m):
            ids.append(next(it))
            count.append(int(next(it)))
            priority.append(int(next(it)))
            
        print(max_priority(T, cooldown, ids, count, priority))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>

using namespace std;

struct Task {
    string id;
    int count;
    long long priority;
    int x;
};

class Solution {
public:
    long long maxPriority(int T, int cooldown, const vector<string>& ids,
                          const vector<int>& count, const vector<long long>& priority) {
        int m = ids.size();
        vector<Task> tasks;
        for (int i = 0; i < m; i++) {
            tasks.push_back({ids[i], count[i], priority[i], count[i]});
        }
        
        // 1. Clamp
        int limit = (T + cooldown) / (cooldown + 1);
        for (auto& t : tasks) {
            t.x = min(t.count, limit);
        }
        
        // 2. Schedule Constraint
        while (true) {
            int maxX = 0;
            for (const auto& t : tasks) maxX = max(maxX, t.x);
            
            if (maxX == 0) break;
            
            vector<Task*> atMax;
            for (auto& t : tasks) {
                if (t.x == maxX) atMax.push_back(&t);
            }
            
            long long required = (long long)(maxX - 1) * (cooldown + 1) + atMax.size();
            
            if (required <= T) break;
            
            long long allowed = T - (long long)(maxX - 1) * (cooldown + 1);
            
            sort(atMax.begin(), atMax.end(), [](Task* a, Task* b) {
                return a->priority > b->priority;
            });
            
            for (size_t i = allowed; i < atMax.size(); i++) {
                atMax[i]->x--;
            }
        }
        
        // 3. Sum Constraint
        long long sumX = 0;
        for (const auto& t : tasks) sumX += t.x;
        
        if (sumX > T) {
            long long toRemove = sumX - T;
            sort(tasks.begin(), tasks.end(), [](const Task& a, const Task& b) {
                return a.priority < b.priority;
            });
            
            for (auto& t : tasks) {
                if (toRemove <= 0) break;
                int rem = min((long long)t.x, toRemove);
                t.x -= rem;
                toRemove -= rem;
            }
        }
        
        long long totalScore = 0;
        for (const auto& t : tasks) totalScore += (long long)t.x * t.priority;
        
        return totalScore;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int m, cooldown, T;
    if (cin >> m >> cooldown >> T) {
        vector<string> ids(m);
        vector<int> count(m);
        vector<long long> priority(m);
        for (int i = 0; i < m; i++) cin >> ids[i] >> count[i] >> priority[i];
        
        Solution solution;
        cout << solution.maxPriority(T, cooldown, ids, count, priority) << "\n";
    }
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class Solution {
  maxPriority(T, cooldown, ids, count, priority) {
    const m = ids.length;
    const tasks = [];
    for (let i = 0; i < m; i++) {
      tasks.push({
        id: ids[i],
        count: count[i],
        priority: BigInt(priority[i]),
        x: count[i]
      });
    }
    
    // 1. Clamp
    const limit = Math.floor((T + cooldown) / (cooldown + 1));
    for (const t of tasks) {
      t.x = Math.min(t.count, limit);
    }
    
    // 2. Schedule Constraint
    while (true) {
      let maxX = 0;
      for (const t of tasks) maxX = Math.max(maxX, t.x);
      
      if (maxX === 0) break;
      
      const atMax = tasks.filter(t => t.x === maxX);
      const required = (maxX - 1) * (cooldown + 1) + atMax.length;
      
      if (required <= T) break;
      
      const allowed = T - (maxX - 1) * (cooldown + 1);
      
      atMax.sort((a, b) => {
        if (a.priority > b.priority) return -1;
        if (a.priority < b.priority) return 1;
        return 0;
      });
      
      for (let i = allowed; i < atMax.length; i++) {
        atMax[i].x--;
      }
    }
    
    // 3. Sum Constraint
    let sumX = 0;
    for (const t of tasks) sumX += t.x;
    
    if (sumX > T) {
      let toRemove = sumX - T;
      tasks.sort((a, b) => {
        if (a.priority < b.priority) return -1;
        if (a.priority > b.priority) return 1;
        return 0;
      });
      
      for (const t of tasks) {
        if (toRemove <= 0) break;
        const rem = Math.min(t.x, toRemove);
        t.x -= rem;
        toRemove -= rem;
      }
    }
    
    let totalScore = 0n;
    for (const t of tasks) {
      totalScore += BigInt(t.x) * t.priority;
    }
    
    return totalScore.toString();
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
  const m = parseInt(data[idx++]);
  const cooldown = parseInt(data[idx++]);
  const T = parseInt(data[idx++]);
  const ids = [];
  const count = [];
  const priority = [];
  for (let i = 0; i < m; i++) {
    ids.push(data[idx++]);
    count.push(parseInt(data[idx++]));
    priority.push(parseInt(data[idx++]));
  }
  
  const solution = new Solution();
  console.log(solution.maxPriority(T, cooldown, ids, count, priority));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:** `2 1 3`. A: `2 3`. B: `1 5`.
1. Clamp: `limit = (3+1)/2 = 2`.
   - `x_A = min(2, 2) = 2`.
   - `x_B = min(1, 2) = 1`.
2. Schedule Check:
   - `maxX = 2`. `atMax = [A]`.
   - `req = (2-1)*2 + 1 = 3`.
   - `3 <= 3`. OK.
3. Sum Check:
   - `sum = 2 + 1 = 3`.
   - `3 <= 3`. OK.
4. Score: `2*3 + 1*5 = 11`.

**Input:** `2 0 5`. A: `10 10`. B: `10 5`.
1. Clamp: `limit = 5`. `x_A=5, x_B=5`.
2. Schedule: `maxX=5`. `atMax=[A, B]`.
   - `req = 4*1 + 2 = 6`.
   - `6 > 5`. Fail.
   - `allowed = 5 - 4 = 1`.
   - Keep top 1 (A). Demote B to 4.
   - `x_A=5, x_B=4`.
   - Loop: `maxX=5`. `atMax=[A]`. `req=5`. OK.
3. Sum: `5+4=9`. `9 > 5`.
   - Remove 4.
   - Low prio is B. `x_B` becomes 0.
   - `x_A=5, x_B=0`.
4. Score: `50`.

## ✅ Proof of Correctness

### Invariant
- Feasibility depends only on `L = max(sum_x, (max_x - 1)(k + 1) + n_max)` and
  is achievable whenever `L <= T` (Task Scheduler bound).
- If `L > T`, only tasks at `max_x` can reduce the bound. Demoting the
  lowest-priority tasks among those at `max_x` preserves feasibility while
  losing the least score.
- Once `L <= T`, the only remaining restriction is `sum_x <= T`. Removing units
  from the lowest-priority tasks maximizes the total score.

## 💡 Interview Extensions

- **Extension 1:** Infinite T?
  - *Answer:* Just sum all priorities.
- **Extension 2:** Dynamic priorities?
  - *Answer:* Much harder, needs global optimization.

### Common Mistakes to Avoid

1. **Simple Greedy**
   - ❌ Wrong: Picking max priority at each step (simulation).
   - ✅ Correct: Global optimization of counts.
2. **Ignoring Cooldown**
   - ❌ Wrong: Only checking sum constraint.
   - ✅ Correct: Must check `(max-1)(k+1) + n_max`.

## Related Concepts

- **Task Scheduler (LC 621):** Core logic.
- **Greedy:** Global vs Local.
