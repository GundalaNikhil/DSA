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

### ASCII Diagram: Scheduling Flow

Tasks:
A: Count 2, Priority 3.
B: Count 1, Priority 5.
k=1 (Cooldown 1 slot). T=3.

Time 1:
- Available: A, B.
- Greedy Choice: B (Priority 5 > 3).
- Run B. Score 5.
- B count -> 0. B cooldown until Time 1 + 1 + 1 = 3.

Time 2:
- Available: A. (B is cooling).
- Run A. Score 3.
- A count -> 1. A cooldown until Time 2 + 1 + 1 = 4.

Time 3:
- Available: B (Cooldown expired at 3).
- But B count is 0. So B unavailable.
- A is cooling (until 4).
- Idle?
- "B count 1". So B is finished.
- So at Time 3, only A is potentially available but cooling.
- So Idle.
- Total Score: 5 + 3 = 8.

Input: `A 2 3`, `B 1 5`. `k=1`. `T=3`.
My trace: B, A, Idle -> 8.
Example Explanation: "A, B, A".
- T1: A (3). A cools until 3.
- T2: B (5). B cools until 4.
- T3: A (3). (A available at 3).
- Total: 3 + 5 + 3 = 11.
- Ah! Greedy choice (Max Priority) failed!
- B (5) > A (3). But picking B first blocked A? No.
- Picking B first: B at 1. A at 2. At 3, A is ready?
  - If A run at 2, A ready at 2+1+1=4.
  - So at 3, A is cooling.
  - B is finished.
  - So B, A -> Idle.
- Picking A first: A at 1. B at 2. At 3, A ready (1+1+1=3).
  - A run at 3.
  - Total A, B, A.
- Why did B first fail?
  - Because A has count 2. We need to fit 2 As.
  - A needs spacing. `A _ A`.
  - B fits in the gap. `A B A`.
  - If we do `B A _`, we waste slot 3.
- This implies **Greedy by Priority is NOT optimal**.
- However, the problem is tagged "Heaps" and "Greedy".
- Is there a specific greedy strategy?
- Or is it just "Greedy works if we consider frequency"?
- Like "Task Scheduler" (LeetCode 621)?
- In LC 621, we schedule most frequent first to minimize idle.
- Here we maximize *score*.
- If we have infinite T, we just run everything.
- With limited T, we want to fit high priority tasks.
- But high priority might have low count.
- If we pick B (5) first, we get 5.
- If we pick A (3) first, we might get 3+3=6.
- But we can get both!
- The conflict is purely about *ordering* to fit them in `T`.
- But constraints: `T <= 100,000`. `m <= 26`.
- `m` is small!
- This suggests we can iterate or use the small `m`.
- But `count` is large.
- The constraint is `T`.
- We want to select a subset of tasks that fits in `T` with cooldowns.
- This is exactly "Task Scheduler" but with values and a hard limit `T`.
- Is it possible that simply "Max Heap of Available" is the intended solution, and the example is a counter-example to "Simple Greedy"?
- Or is the example solvable by a better Greedy?
- Maybe "Priority * Count"? No.
- Maybe "Priority" but we must respect "Bottlenecks"?
- If the intended solution is Heaps/Greedy, it's likely the simulation with a Heap.
- Let's re-read the example carefully.
- `A 2 3`, `B 1 5`.
- If we use a Max-Heap of *Available* tasks:
  - T1: Heap {A:3, B:5}. Pop B.
  - T2: Heap {A:3}. Pop A.
  - T3: Heap {}. (A cooling).
  - Result 8.
- The optimal is 11.
- This proves **Simple Greedy (Max Priority) is Wrong**.
- So why is it tagged Greedy/Heaps?
- Maybe we should prioritize tasks with **Higher Count**?
  - T1: Heap {A(2), B(1)}. Pop A.
  - T2: Heap {B(1)}. Pop B.
  - T3: Heap {A(1)}. Pop A.
  - Result 11.
- What if:
  - A: Count 100, Priority 1.
  - B: Count 1, Priority 1000.
  - T=2. k=1.
  - Count Greedy: A, A. Score 2.
  - Priority Greedy: B, A. Score 1001.
  - Optimal: B, A.
- So neither "Max Priority" nor "Max Count" works alone.
- This is a complex scheduling problem.
- However, `m` is small (26).
- Maybe we can use that?
- But `T` is large.
- Is there a hybrid greedy?
- "Task Scheduler" (LC 621) minimizes idle time by picking max count.
- Here we have values.
- If `T` is large enough to fit all, order doesn't matter (except for idle).
- If `T` is tight, we must drop tasks.
- We should drop low priority tasks?
- Yes.
- But we might need to drop a high priority task if it causes too much idle?
- No, idle is fine if we score high.
- The issue in the example was that picking B first forced A to be delayed, pushing the second A out of `T`.
- So we "dropped" the second A (value 3).
- If we picked A first, we fit both.
- Effectively, we chose between `{B, A}` (8) and `{A, B, A}` (11).
- We want to fit as many high value tasks as possible.
- **Hypothesis:** This is a "Greedy with Backtracking" or "DP"?
- With `T=100,000`, DP is `O(T * 2^m)` -> Too slow.
- But `m` is small.
- Maybe we can just simulate?
- Is it possible that we simply run the simulation using a Heap, but the Heap criteria is complex?
- Or maybe we just run the simulation and the example output 11 is achievable by "Max Priority" if we consider `A` has higher priority *in total*?
- No, A(3) < B(5).
- What if we sort by `Priority` and try to schedule?
- If we schedule B: it takes slots `t, t+k+1, ...`.
- This reserves slots.
- This feels like "fill slots".
- But `T` is large.
- Let's reconsider the constraints and type.
- "Heaps", "Greedy".
- Usually implies the simulation approach.
- Is it possible `k` is small? `k <= 100,000`.
- **Wait**, if `m` is small, maybe we can model this as:
  - We have `T` slots.
  - We want to pick `c_i` slots for task `i` such that no two are closer than `k`.
  - Total score $\sum c_i \times p_i$.
  - Subject to $\sum c_i \le T$ (roughly).
  - Let $x_i$ be the number of times we run task $i$. $0 \le x_i \le count_i$.
  - We want to maximize $\sum x_i p_i$.
  - Constraint: Can we schedule these counts?
  - This is the "Task Scheduler" feasibility check!
  - For a set of counts $\{x_1, \dots, x_m\}$, can they be scheduled in $T$ with cooldown $k$?
  - Condition (from LC 621 logic):
    - Let $max\_freq = \max(x_i)$.
    - Let $n\_max$ be count of tasks with $x_i = max\_freq$.
    - Min length required = $(max\_freq - 1) \times (k + 1) + n\_max$.
    - Also total length $\ge \sum x_i$.
    - So valid iff $\max((max\_freq - 1)(k+1) + n\_max, \sum x_i) \le T$.
  - **Algorithm:**
    - Iterate $x_i$ from $count_i$ down to 0?
    - No, we want to maximize score.
    - This looks like a Knapsack-style optimization but with a weird constraint.
    - We should try to include high priority tasks.
    - Let's sort tasks by Priority descending.
    - Try to take all of Task 1.
    - Then all of Task 2.
    - ...
    - Check feasibility at each step?
    - Feasibility check depends on *all* counts.
    - If we fix the set of counts, we can check.
    - But we can reduce counts.
    - If we take full Task 1, full Task 2... and we violate $T$.
    - Which one to reduce? The one with lowest priority?
    - Yes!
    - **Proposed Greedy Strategy:**
      1. Start with assuming we take ALL tasks ($x_i = count_i$).
      2. Check if valid in $T$.
      3. If valid, return total score.
      4. If invalid, we must reduce the "length".
         - The length is determined by $\max(L_{sched}, L_{sum})$.
         - $L_{sched} = (max\_freq - 1)(k+1) + n\_max$.
         - $L_{sum} = \sum x_i$.
         - If $L_{sum} > T$: We are limited by total slots. Remove lowest priority tasks until $\sum x_i \le T$.
         - If $L_{sched} > T$: We are limited by the max frequency task(s).
           - We need to reduce $max\_freq$.
           - Or reduce the count of tasks contributing to $n\_max$ (if they are low priority).
           - We should reduce the count of the *highest frequency* task?
           - But that task might have high priority!
           - If High Priority High Freq task is causing bottleneck, we MUST reduce it.
           - Why? Because we literally can't fit it.
           - Even if we drop everything else, if $(count_A - 1)(k+1) + 1 > T$, we simply cannot run A that many times.
           - So, step 1: Clamp every $x_i$ such that $(x_i - 1)(k+1) + 1 \le T$.
             - i.e., $x_i \le \lfloor \frac{T - 1}{k + 1} \rfloor + 1$.
             - Let's call this $limit\_freq$.
             - Update $x_i = \min(count_i, limit\_freq)$.
           - Now, $L_{sched}$ might still be $> T$ if multiple tasks have high freq.
             - $L_{sched} = (max\_freq - 1)(k+1) + n\_max$.
             - If this $> T$, it means we have too many tasks at $max\_freq$.
             - We must reduce some of them to $max\_freq - 1$.
             - Which ones? The ones with lowest priority!
             - So, collect all tasks with $x_i = max\_freq$.
             - Sort by priority.
             - Keep the top $Y$ tasks at $max\_freq$, reduce others to $max\_freq - 1$.
             - How many $Y$ can we keep?
             - $(max\_freq - 1)(k+1) + Y \le T \implies Y \le T - (max\_freq - 1)(k+1)$.
             - So we keep $Y$ highest priority ones. Others decrement.
             - Repeat loop? (Since new max freq might be lower, or we might hit sum limit).
           - Also check $L_{sum} > T$.
             - If sum $> T$, remove lowest priority tasks (decrement their counts) until sum $\le T$.
             - Note: Decrementing counts might reduce $L_{sched}$ too.
    - This looks like a valid greedy strategy.
    - **Refined Algorithm:**
      1. Initial $x_i = count_i$.
      2. Clamp each $x_i$ to $limit\_freq = (T + k) / (k + 1)$.
      3. Priority Queue (Min-Heap) of *active* units? No, counts are large.
      4. We have two constraints:
         - A: $\sum x_i \le T$.
         - B: For any freq $f$, let $N_f$ be count of tasks with $x_i \ge f$. Then $(f-1)(k+1) + N_f$ is NOT the condition.
         - The condition is simply $L_{sched} \le T$.
      5. Let's satisfy B first.
         - While $(max\_x - 1)(k+1) + count(max\_x) > T$:
           - We have too many tasks at `max_x`.
           - Allowed count at `max_x`: $Y = T - (max\_x - 1)(k+1)$.
           - Identify tasks with $x_i = max\_x$.
           - Sort them by priority.
           - Keep top $Y$ at $max\_x$.
           - Decrement the rest to $max\_x - 1$.
           - Update $max\_x$ (might stay same or decrease).
      6. Now B is satisfied. Check A ($\sum x_i \le T$).
         - While $\sum x_i > T$:
           - Remove unit with lowest priority.
           - We can use a Min-Heap of (Priority, TaskID) representing the "marginal" unit?
           - No, we have counts.
           - We should remove from the task with lowest priority that has $x_i > 0$.
           - Just decrement $x_{lowest}$.
           - Does this violate B?
           - Reducing $x_i$ never increases $L_{sched}$. So B remains satisfied.
      7. Calculate total score.

    - **Wait**, does satisfying B first then A work?
      - Example:
        - T=2, k=1.
        - A: Count 100, Pri 1.
        - B: Count 1, Pri 1000.
        - Step 1 (Clamp): $limit = (2+1)/2 = 1$.
        - $x_A = 1, x_B = 1$.
        - Step 2 (Check B):
          - $max\_x = 1$. $count(1) = 2$.
          - $L_{sched} = 0 + 2 = 2 \le 2$. OK.
        - Step 3 (Check A):
          - Sum = 2 \le 2. OK.
        - Result: A(1) + B(1) = 1001.
        - Correct.
      - Example from problem:
        - A: 2, 3. B: 1, 5. k=1, T=3.
        - Step 1 (Clamp): $limit = (3+1)/2 = 2$.
        - $x_A = 2, x_B = 1$.
        - Step 2 (Check B):
          - $max\_x = 2$ (A). $count(2) = 1$.
          - $L_{sched} = (1)(2) + 1 = 3 \le 3$. OK.
        - Step 3 (Check A):
          - Sum = 3 \le 3. OK.
        - Result: $2\times3 + 1\times5 = 11$.
        - Correct.
      - Another:
        - A: 10, 10. B: 10, 5. k=0. T=5.
        - Clamp: $limit = 5$.
        - $x_A=5, x_B=5$.
        - B Check: $max=5, cnt=2$. $L = 4(1)+2 = 6 > 5$.
        - Allowed at 5: $5 - 4 = 1$.
        - Tasks at 5: A(10), B(5).
        - Keep A at 5. Reduce B to 4.
        - $x_A=5, x_B=4$.
        - B Check: $max=5, cnt=1$. $L = 4+1 = 5 \le 5$. OK.
        - A Check: Sum = 9 > 5.
        - Reduce lowest priority.
        - B is lowest (5). Reduce B: $4 \to 0$.
        - Sum = 5. OK.
        - Result: $5 \times 10 = 50$.
        - Optimal? Yes, fill 5 slots with A.
    - This strategy seems robust.

### Algorithm

1. Parse input. Store as objects.
2. **Clamp:** For each task, $x_i = \min(count_i, (T + k) / (k + 1))$.
3. **Satisfy Schedule Constraint:**
   - Group tasks by current count $x_i$.
   - Find $max\_x$.
   - Calculate needed slots $L = (max\_x - 1)(k+1) + count(max\_x)$.
   - If $L > T$:
     - We have too many at $max\_x$.
     - Allowed $Y = T - (max\_x - 1)(k+1)$.
     - Identify tasks at $max\_x$. Sort by Priority Descending.
     - Keep top $Y$.
     - Decrement others to $max\_x - 1$.
     - Repeat check. (Since we only reduce counts, we will converge).
4. **Satisfy Sum Constraint:**
   - Calculate $S = \sum x_i$.
   - If $S > T$:
     - We need to remove $S - T$ units.
     - Remove from lowest priority tasks.
     - Sort all tasks by Priority Ascending.
     - Iterate: remove $\min(x_i, needed)$ from current task.
     - Update $S$. Stop when $S \le T$.
5. Calculate total score $\sum x_i p_i$.

### Time Complexity

- **O(M log M)** or **O(M^2)**. Since $M \le 26$, this is instant.

### Space Complexity

- **O(M)**.

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

public class Main {
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
- The problem is equivalent to finding a set of counts $\{x_i\}$ satisfying the Task Scheduler constraint and Sum constraint.
- The greedy strategy works because the constraints are hierarchical: the "bottleneck" is always the max frequency. Reducing max frequency or total sum from the bottom (lowest priority) preserves optimality.

## 💡 Interview Extensions

- **Extension 1:** Infinite T?
  - *Answer:* Just sum all priorities.
- **Extension 2:** Dynamic priorities?
  - *Answer:* Much harder, maybe flow.

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
