---
problem_id: HEP_TASK_SCHEDULER_ENERGY__9471
display_id: HEP-006
slug: task-scheduler-energy
title: "Task Scheduler with Energy"
difficulty: Medium
difficulty_score: 56
topics:
  - Heaps
  - Greedy
  - Scheduling
tags:
  - heaps
  - greedy
  - energy
  - medium
premium: true
subscription_tier: basic
---

# HEP-006: Task Scheduler with Energy

## 📋 Problem Summary

You have `n` tasks, each with a `duration` (cost) and a `gain` (reward).
You start with energy `E`.
To start a task, you need `E >= duration`.
After finishing, `E = E - duration + gain`.
Find the maximum number of tasks you can complete.

## 🌍 Real-World Scenario

**Scenario Title:** RPG Quest Progression

In a Role-Playing Game, you have a Stamina bar.
- Quests require a minimum Stamina to start (e.g., "Climb the Mountain" needs 50 Stamina).
- Completing the quest consumes Stamina but also rewards you with a Stamina Potion or boost.
- Some quests are net positive (gain > cost), increasing your capacity for harder quests.
- Some are net negative (gain < cost), draining you.
- You want to complete as many quests as possible.

![Real-World Application](../images/HEP-006/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Energy Flow

Start E = 10.
Tasks:
A: Cost 5, Gain 10 (Net +5).
B: Cost 15, Gain 20 (Net +5).
C: Cost 8, Gain 2 (Net -6).

Strategy:
1. Do A first? Need 5. Have 10. OK.
   - E = 10 - 5 + 10 = 15.
2. Now have 15. Can do B (Need 15).
   - E = 15 - 15 + 20 = 20.
3. Now have 20. Can do C (Need 8).
   - E = 20 - 8 + 2 = 14.
Total: 3 tasks.

If we tried B first: Need 15. Have 10. Impossible.

### Key Concept: Split into Two Groups

1. **Net Positive Tasks ($gain \ge duration$):**
   - These increase (or maintain) your energy.
   - You should always do these if you can.
   - Order matters! To maximize the chance of doing all, do the ones with **smallest duration** first. This "unlocks" energy for harder tasks.
2. **Net Negative Tasks ($gain < duration$):**
   - These decrease your energy.
   - You should do these *after* all possible positive tasks, when your energy is highest.
   - Order matters! This is trickier. It's like the "Knapsack-like" or "Reverse Greedy" problem.
   - Standard strategy for negative tasks: Sort by `gain` descending (or `end_energy` descending)?
   - Let's verify: Suppose we have E=20.
     - T1: Cost 10, Gain 5 (Net -5). Needs 10.
     - T2: Cost 15, Gain 10 (Net -5). Needs 15.
     - If T1 then T2:
       - Start T1 (20 >= 10). E -> 15.
       - Start T2 (15 >= 15). E -> 10.
       - Both done.
     - If T2 then T1:
       - Start T2 (20 >= 15). E -> 15.
       - Start T1 (15 >= 10). E -> 10.
       - Both done.
   - What if:
     - T1: Cost 10, Gain 2 (Net -8).
     - T2: Cost 10, Gain 8 (Net -2).
     - E = 15.
     - T1 then T2: 15->7. T2 needs 10. Fail.
     - T2 then T1: 15->13. T1 needs 10. OK. 13->5.
     - We preferred T2 (higher gain).
   - Correct greedy for negative tasks: Sort by `gain` descending? Or `gain`? Or `max(gain, duration)`?
   - Let's check the standard "Job Sequencing with Deadlines" or similar.
   - For tasks where $gain < cost$, let $net = cost - gain$ (loss).
   - We want to process tasks with **higher gain** (or larger `gain`) first?
   - Yes, sort by `gain` descending (or equivalently `return_energy` descending).

If we sort by `gain` descending (largest return first), we maximize intermediate energy.
Example: E=15.
A: Cost 10, Gain 9.
B: Cost 10, Gain 2.
A then B: 15 -> 14 -> 6. (OK)
B then A: 15 -> 7. A needs 10. Fail.
So `gain` descending is correct.

For positive tasks: Sort by `cost` ascending.
For negative tasks: Sort by `gain` descending?
Is it guaranteed we can do *all* negative tasks? No.
For positive tasks, we just do them if we can.
For negative tasks, we might not be able to do all. It becomes a selection problem.
"Max number of tasks".
This part is actually a **Priority Queue** problem.
We iterate through the sorted negative tasks.
We maintain a Max-Heap of "costs" (or losses) of tasks we have "committed" to.
If we can't afford a task, we might "undo" a previous task if the new one is "cheaper" or "better"?
"Start with E_max. Select max subset of tasks."
This looks like the "Course Schedule III" (LC 630) or similar.
But here we have `gain`.
Let's refine the negative part.
We have reached a peak energy $E_{peak}$ after all positive tasks.
Now we want to pick a subset of negative tasks.
Each negative task $i$ has $cost_i$ and $gain_i$.
Condition: $E_{curr} \ge cost_i$. Update $E_{curr} \leftarrow E_{curr} - (cost_i - gain_i)$.
Since $cost_i > gain_i$, energy decreases.
We want to maximize count.
This is exactly the "constrained subset sum" or similar?
Let's try the standard approach for this specific variant (often called "Quest" or "Dungeon Game" variant).
1. Process positive tasks: Greedy (sort by cost).
2. Process negative tasks:
   - This is hard.
   - Start from 0 energy at end. Add tasks in reverse?
   - Reverse of "Cost C, Gain G" is "Cost G, Gain C".
   - Net change is positive!
   - But constraint is: $E_{before} \ge C \implies E_{after} + (C-G) \ge C \implies E_{after} \ge G$.
   - So in reverse: "Start with 0. Task needs $G$. Becomes $E+C-G$."
   - This transforms negative tasks ($C > G$) into positive tasks in reverse ($G < C$ means net gain in reverse).
   - So for negative tasks, we can treat them as positive tasks in reverse?
   - We want to end with $\ge 0$ energy.
   - So we start with 0 (or any valid end state) and go backwards to $E_{peak}$.
   - We want to fit max tasks.
   - In reverse: Start $E=0$. Task requires $gain$. Adds $cost - gain$.
   - We want to reach $\le E_{peak}$.
   - Maximize count.
   - This is exactly the same as the positive case!
   - Sort negative tasks by `gain` descending (which is "cost" in reverse).
   - So sort by `gain` descending.
   - Iterate. If we can afford (current reverse energy $\le$ actual peak? No).
   - In reverse, we start with 0. We "gain" energy. We want to keep total required energy $\le E_{peak}$.
   - Use a Max-Heap to track "costs" (losses) of taken tasks.
   - Iterate negative tasks sorted by `gain` descending?
   - Let's verify the reverse logic.
   - Forward: $E_{peak} \xrightarrow{T1} E_1 \xrightarrow{T2} E_2 \dots \ge 0$.
   - Reverse: $E_{final} (\ge 0) \xrightarrow{T_{last}} \dots \xrightarrow{T1} E_{peak}$.
   - Reverse step: $E_{prev} = E_{next} - gain + cost$.
   - Constraint: $E_{prev} \ge cost \implies E_{next} - gain + cost \ge cost \implies E_{next} \ge gain$.
   - So in reverse: We need $E \ge gain$. We add $cost - gain$.
   - We want to pick max tasks such that final $E \le E_{peak}$.
   - This is: Start $E=0$. Tasks have "threshold" $gain$ and "delta" $cost-gain$.
   - We want to pick max tasks such that we can execute them (threshold constraint) and total sum is $\le E_{peak}$? No.
   - The constraint is sequential.
   - But since "delta" is positive, energy grows.
   - If we sort by "threshold" (gain) ascending?
   - In reverse, we want to do tasks with small thresholds first?
   - Yes, "Smallest `gain` first" in reverse means "Largest `gain` last" in forward.
   - So in forward: Sort by `gain` descending.
   - This matches our earlier intuition.
   - Now, how to select max subset?
   - We have a sequence of tasks sorted by `gain` descending.
   - We iterate. Maintain a Max-Heap of "costs" (actual costs? or net losses?).
     "Iterate tasks. If can do, do it. Else, if this task is 'cheaper' than the most expensive task we already did, swap."
     Cheaper in terms of what?
     We want to save energy.
     The "cost" we pay is the net loss ($cost - gain$).
     If we swap, we need to ensure validity.
     This specific greedy-with-heap works for "Deadline" problems.
     Here the constraint is capacity.
     Let's look at the "Reverse" strategy again.
     Reverse Problem:
     - Start $E=0$.
     - Tasks: Require $gain$. Provide $cost - gain$ (net positive).
     - Maximize count such that final $E \le E_{peak}$.
     - The constraint is simply that we can perform the sequence starting from $E_{peak}$ in forward.
     - In reverse, it means we generate enough energy to reach $E_{peak}$.
     - No, in reverse, we *gain* energy. The constraint is $E_{curr} \ge gain$.
     - And we want to end up with a state that was reachable from $E_{peak}$.
     - Since in reverse they are "positive" tasks (net gain), we should just do them if we can?
     - But we have a "budget" of $E_{peak}$.
       - We have "Reverse Capacity" $E_{peak}$.
       - Tasks consume capacity? No, they produce.
     - Let's stick to Forward.
     - Sort negative tasks by `gain` descending.
     - Iterate.
     - If $E \ge cost$: Do it. Push to Max-Heap (by cost? or net loss?).
     - Else: Can we swap?
       - If $E + \text{max\_heap\_top} \ge cost$?
       - No, swapping means we undo a previous task to do this one.
       - We undo if the previous task was "worse".
       - "Worse" means it consumed more energy?
       - But tasks have different requirements ($cost$) and different net losses.
       - This is complex.

**Correct Approach for Negative Tasks:**
1. Positive tasks: Sort by `cost` ascending. Do all possible.
2. Negative tasks:
   - Sort by `gain + cost` descending? Or `gain` descending?
   - But for selection?
   - Let's use the **Reverse Strategy** properly.
   - We have $E_{peak}$.
   - We want to select a subset of negative tasks.
   - Let's consider the "gap" $cost - gain$.
   - In reverse, we start with $E_{curr} = 0$.
   - We consider tasks. Task $i$ requires $gain_i$ energy to be "finished" (in reverse start).
   - And it provides $cost_i - gain_i$ energy.
   - We want to pick max tasks such that we never drop below 0? No.
   - We want to pick max tasks such that total required $\le E_{peak}$.
     - Treat negative tasks as: "Requires `gain`, gives `cost`".
     - We start with 0.
     - We want to reach $\le E_{peak}$? No.
     - We want to find max subset that can be chained from $E_{peak}$.
     - This is equivalent to:
       - Start with $E_{current} = E_{peak}$.
       - We want to absorb "losses".
       - Task $i$ has loss $L_i = cost_i - gain_i$.
       - Constraint: $E_{current} \ge cost_i$.
       - Update: $E_{current} -= L_i$.
       - We want to maximize count.
       - Sort tasks by `gain` descending. (This is the "latest deadline" equivalent).
       - Iterate.
       - If $E_{current} \ge cost_i$: Take it. Push $cost_i$ (or $L_i$?) to Heap.
       - Else:
         - We can't take it.
         - Can we swap?
         - We want to minimize the "barrier" to continue?
           - Sort by `gain` descending.
           - Use a Max-Heap to store `cost` (requirement).
           - High gain = Low requirement in reverse.
           - Let's try:
             - Max-Heap stores `cost`.
             - Iterate tasks by `gain` descending.
             - Add task to heap. $count++$.
             - $E_{needed} += (cost - gain)$? No.
             - Let's go back to the "Positive in Reverse" idea.
             - Reverse Tasks: $R_i$. Cost $G_i$. Gain $C_i$. Net $+ (C_i - G_i)$.
             - We start with $E=0$.
             - We want to do max tasks such that final $E \le E_{peak}$.
             - AND intermediate constraints $E \ge G_i$ are met.
             - Since they are net positive, we should sort by $G_i$ ascending (Smallest requirement first).
             - Iterate.
             - If $E \ge G_i$: Do it. $E += (C_i - G_i)$.
             - But we have a "limit" $E_{peak}$.
             - We want to stop when $E > E_{peak}$? No.
             - We want to select a subset.
             - No, because we are limited by $E_{peak}$ at the end of the chain.
             - The chain in reverse builds up energy.
             - $0 \to E_1 \to E_2 \dots \to E_{final}$.
             - We need $E_{final} \le E_{peak}$.
             - So we want to pick tasks that "add up" to $\le E_{peak}$ while satisfying local constraints.
             - Since they add energy, we want to pick tasks that add *least* energy?
             - Or satisfy constraints easily?
             - This is a Priority Queue problem!
             - Sort by $G_i$ ascending (Reverse Cost).
             - Iterate.
             - Add task. $E_{curr} += (C_i - G_i)$.
             - Push $(C_i - G_i)$ to Max-Heap.
             - Let's trace carefully.
             - Forward: $E_{peak} \ge C_1 \to E_1 \ge C_2 \dots$
             - $E_1 = E_{peak} - (C_1 - G_1)$.
             - $E_2 = E_1 - (C_2 - G_2) = E_{peak} - \sum (C_k - G_k)$.
             - Constraint: $E_{i-1} \ge C_i \implies E_{peak} - \sum_{k<i} (C_k - G_k) \ge C_i$.
             - $E_{peak} \ge C_i + \sum_{k<i} (C_k - G_k)$.
             - $E_{peak} \ge G_i + (C_i - G_i) + \sum_{k<i} (C_k - G_k)$.
             - $E_{peak} \ge G_i + \sum_{k \le i} (C_k - G_k)$.
             - Let $Loss_k = C_k - G_k$.
             - $E_{peak} \ge G_i + \sum_{k \le i} Loss_k$.
             - We want to pick max tasks satisfying this for all $i$.
             - If we process in order of `gain` descending (so $G_i$ is decreasing), the term $G_i$ becomes easier.
             - But the sum $\sum Loss_k$ grows.
             - So:
               1. Sort negative tasks by `gain` descending.
               2. Iterate.
               3. Maintain `current_loss_sum`.
               4. Check if $E_{peak} \ge G_i + current\_loss\_sum + Loss_i$.
               5. If yes: Take it. Add $Loss_i$ to Max-Heap. `current_loss_sum += Loss_i`.
               6. If no:
                  - Can we swap?
                  - We want to minimize `current_loss_sum`.
                  - If $Loss_i < max\_heap\_top$:
                    - Swap!
                    - Remove max loss. Add $Loss_i$.
                    - `current_loss_sum` decreases.
                    - Validity?
                    - Since we process by $G_i$ descending, the previous tasks had $G_k \ge G_i$.
                    - Their condition was $E_{peak} \ge G_k + Sum_{prev}$.
                    - Now we reduce sum. So previous tasks remain valid!
                    - What about current task?
                    - We need $E_{peak} \ge G_i + NewSum$.
                    - Since we swapped, $NewSum < OldSum$.
                    - If we couldn't satisfy $G_i + OldSum$, maybe we can satisfy $G_i + NewSum$?
                    - We only do this if it helps (reduces loss).
                    - Does it satisfy current?
                    - We check $E_{peak} \ge G_i + (Sum - Max + Loss_i)$.
                    - If yes, we swap.
                    - If no, we ignore current.

This looks solid.

### Algorithm

1. Separate tasks into `Positive` ($gain \ge duration$) and `Negative` ($gain < duration$).
2. **Positive:**
   - Sort by `duration` ascending.
   - Iterate. If $E \ge duration$, do it. $E += gain - duration$. Count++.
   - Else, stop? (Since sorted by duration, if we can't do this, we can't do any subsequent ones? Yes, because $E$ only grows).
3. **Negative:**
   - Sort by `gain` descending.
   - Max-Heap `pq` stores `loss` ($duration - gain$) of accepted tasks.
   - `current_loss_sum = 0`.
   - Iterate.
   - `loss = duration - gain`.
   - Condition: $E_{peak} \ge gain + current\_loss\_sum + loss$.
   - If valid:
     - Add to `pq`. `current_loss_sum += loss`. Count++.
   - Else:
     - If `!pq.empty()` and `pq.top() > loss`:
       - Check if swap is valid: $E_{peak} \ge gain + current\_loss\_sum - pq.top() + loss$.
       - If valid, swap. `current_loss_sum -= (pq.top() - loss)`. Pop, Push.
       - Note: Count stays same. We just optimized sum for future tasks.
4. Return total count.

### Time Complexity

- **O(N log N)**.

### Space Complexity

- **O(N)**.

![Algorithm Visualization](../images/HEP-006/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    static class Task {
        int d, g;
        public Task(int d, int g) {
            this.d = d;
            this.g = g;
        }
    }
    
    public int maxTasks(int E, int[] duration, int[] gain) {
        List<Task> positive = new ArrayList<>();
        List<Task> negative = new ArrayList<>();
        
        for (int i = 0; i < duration.length; i++) {
            if (gain[i] >= duration[i]) {
                positive.add(new Task(duration[i], gain[i]));
            } else {
                negative.add(new Task(duration[i], gain[i]));
            }
        }
        
        // 1. Process Positive: Sort by duration ascending
        Collections.sort(positive, (a, b) -> Integer.compare(a.d, b.d));
        
        int count = 0;
        long currentE = E;
        
        for (Task t : positive) {
            if (currentE >= t.d) {
                currentE += (t.g - t.d);
                count++;
            } else {
                // Cannot process this task. Since sorted by duration, can't process any further?
                break;
            }
        }
        
        // 2. Process Negative: Sort by gain descending
        Collections.sort(negative, (a, b) -> Integer.compare(b.g, a.g));
        
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        long currentLossSum = 0;
        
        for (Task t : negative) {
            int loss = t.d - t.g;
            // Condition: currentE >= t.g + currentLossSum + loss
            // Because E_start >= G_i + Sum(Loss_k)
            
            if (currentE >= t.g + currentLossSum + loss) {
                pq.offer(loss);
                currentLossSum += loss;
                count++;
            } else {
                if (!pq.isEmpty() && pq.peek() > loss) {
                    // Try swap
                    long newLossSum = currentLossSum - pq.peek() + loss;
                    if (currentE >= t.g + newLossSum) {
                        currentLossSum = newLossSum;
                        pq.poll();
                        pq.offer(loss);
                    }
                }
            }
        }
        
        return count;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int E = sc.nextInt();
            int[] duration = new int[n];
            int[] gain = new int[n];
            for (int i = 0; i < n; i++) {
                duration[i] = sc.nextInt();
                gain[i] = sc.nextInt();
            }
            
            Solution solution = new Solution();
            System.out.println(solution.maxTasks(E, duration, gain));
        }
        sc.close();
    }
}
```

### Python

```python
import sys
import heapq

class Solution:
    def max_tasks(self, E: int, duration: list, gain: list) -> int:
        positive = []
        negative = []
        
        for d, g in zip(duration, gain):
            if g >= d:
                positive.append((d, g))
            else:
                negative.append((d, g))
                
        # Positive: Sort by duration asc
        positive.sort(key=lambda x: x[0])
        
        count = 0
        current_e = E
        
        for d, g in positive:
            if current_e >= d:
                current_e += (g - d)
                count += 1
            else:
                break
                
        # Negative: Sort by gain desc
        negative.sort(key=lambda x: x[1], reverse=True)
        
        # Max heap for losses (use negative values for min-heap to simulate max-heap)
        pq = []
        current_loss_sum = 0
        
        for d, g in negative:
            loss = d - g
            # Check if we can add this task
            # Condition: current_e >= g + current_loss_sum + loss
            
            if current_e >= g + current_loss_sum + loss:
                heapq.heappush(pq, -loss)
                current_loss_sum += loss
                count += 1
            else:
                if pq and -pq[0] > loss:
                    # Try swap
                    max_loss = -pq[0]
                    new_loss_sum = current_loss_sum - max_loss + loss
                    if current_e >= g + new_loss_sum:
                        heapq.heappop(pq)
                        heapq.heappush(pq, -loss)
                        current_loss_sum = new_loss_sum
                        
        return count

def max_tasks(E: int, duration: list, gain: list) -> int:
    solver = Solution()
    return solver.max_tasks(E, duration, gain)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        E = int(next(it))
        duration = []
        gain = []
        for _ in range(n):
            duration.append(int(next(it)))
            gain.append(int(next(it)))
            
        print(max_tasks(E, duration, gain))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

struct Task {
    int d, g;
};

class Solution {
public:
    int maxTasks(long long E, const vector<int>& duration, const vector<int>& gain) {
        vector<Task> positive, negative;
        for (size_t i = 0; i < duration.size(); i++) {
            if (gain[i] >= duration[i]) {
                positive.push_back({duration[i], gain[i]});
            } else {
                negative.push_back({duration[i], gain[i]});
            }
        }
        
        sort(positive.begin(), positive.end(), [](const Task& a, const Task& b) {
            return a.d < b.d;
        });
        
        int count = 0;
        for (const auto& t : positive) {
            if (E >= t.d) {
                E += (t.g - t.d);
                count++;
            } else {
                break;
            }
        }
        
        sort(negative.begin(), negative.end(), [](const Task& a, const Task& b) {
            return a.g > b.g;
        });
        
        priority_queue<int> pq; // Max heap for losses
        long long currentLossSum = 0;
        
        for (const auto& t : negative) {
            int loss = t.d - t.g;
            if (E >= t.g + currentLossSum + loss) {
                pq.push(loss);
                currentLossSum += loss;
                count++;
            } else {
                if (!pq.empty() && pq.top() > loss) {
                    long long newLossSum = currentLossSum - pq.top() + loss;
                    if (E >= t.g + newLossSum) {
                        currentLossSum = newLossSum;
                        pq.pop();
                        pq.push(loss);
                    }
                }
            }
        }
        
        return count;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    long long E;
    if (cin >> n >> E) {
        vector<int> duration(n), gain(n);
        for (int i = 0; i < n; i++) cin >> duration[i] >> gain[i];
        
        Solution solution;
        cout << solution.maxTasks(E, duration, gain) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class PriorityQueue {
  constructor(compare = (a, b) => a - b) {
    this.heap = [];
    this.compare = compare;
  }
  size() { return this.heap.length; }
  isEmpty() { return this.heap.length === 0; }
  peek() { return this.heap[0]; }
  push(val) {
    this.heap.push(val);
    this.bubbleUp(this.heap.length - 1);
  }
  pop() {
    if (this.size() === 0) return null;
    const top = this.heap[0];
    const bottom = this.heap.pop();
    if (this.size() > 0) {
      this.heap[0] = bottom;
      this.bubbleDown(0);
    }
    return top;
  }
  bubbleUp(idx) {
    while (idx > 0) {
      const pIdx = Math.floor((idx - 1) / 2);
      if (this.compare(this.heap[idx], this.heap[pIdx]) < 0) {
        [this.heap[idx], this.heap[pIdx]] = [this.heap[pIdx], this.heap[idx]];
        idx = pIdx;
      } else break;
    }
  }
  bubbleDown(idx) {
    while (true) {
      const left = 2 * idx + 1;
      const right = 2 * idx + 2;
      let swap = null;
      if (left < this.size() && this.compare(this.heap[left], this.heap[idx]) < 0) swap = left;
      if (right < this.size() && this.compare(this.heap[right], swap === null ? this.heap[idx] : this.heap[swap]) < 0) swap = right;
      if (swap === null) break;
      [this.heap[idx], this.heap[swap]] = [this.heap[swap], this.heap[idx]];
      idx = swap;
    }
  }
}

class Solution {
  maxTasks(E, duration, gain) {
    const positive = [];
    const negative = [];
    
    for (let i = 0; i < duration.length; i++) {
      if (gain[i] >= duration[i]) {
        positive.push({ d: duration[i], g: gain[i] });
      } else {
        negative.push({ d: duration[i], g: gain[i] });
      }
    }
    
    positive.sort((a, b) => a.d - b.d);
    
    let count = 0;
    let currentE = BigInt(E);
    
    for (const t of positive) {
      if (currentE >= BigInt(t.d)) {
        currentE += BigInt(t.g - t.d);
        count++;
      } else {
        break;
      }
    }
    
    negative.sort((a, b) => b.g - a.g);
    
    // Max heap for losses
    const pq = new PriorityQueue((a, b) => b - a);
    let currentLossSum = 0n;
    
    for (const t of negative) {
      const loss = BigInt(t.d - t.g);
      const g = BigInt(t.g);
      
      if (currentE >= g + currentLossSum + loss) {
        pq.push(Number(loss));
        currentLossSum += loss;
        count++;
      } else {
        if (!pq.isEmpty() && BigInt(pq.peek()) > loss) {
          const maxLoss = BigInt(pq.peek());
          const newLossSum = currentLossSum - maxLoss + loss;
          if (currentE >= g + newLossSum) {
            currentLossSum = newLossSum;
            pq.pop();
            pq.push(Number(loss));
          }
        }
      }
    }
    
    return count;
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
  const E = parseInt(data[idx++]);
  const duration = [];
  const gain = [];
  for (let i = 0; i < n; i++) {
    duration.push(parseInt(data[idx++]));
    gain.push(parseInt(data[idx++]));
  }
  
  const solution = new Solution();
  console.log(solution.maxTasks(E, duration, gain));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:** E=3. Tasks: `(2,3)`, `(3,1)`.

1. **Positive:** `(2,3)`.
   - $3 \ge 2$. Do it.
   - $E = 3 - 2 + 3 = 4$. Count = 1.
2. **Negative:** `(3,1)`. Loss = 2.
   - Sort by gain desc: `(3,1)` (gain 1).
   - Check: $4 \ge 1 + 0 + 2 = 3$.
   - Yes. Do it.
   - Count = 2.

**Result:** 2.

**Input:** E=10. Negatives: `(10, 5)`, `(15, 10)`.
- Sorted by gain: `(15, 10)` (gain 10), `(10, 5)` (gain 5).
- T1 (15, 10): Loss 5.
  - $10 \ge 10 + 0 + 5 = 15$. No.
  - Swap? Heap empty.
- T2 (10, 5): Loss 5.
  - $10 \ge 5 + 0 + 5 = 10$. Yes.
  - Do it. Count = 1.
- Result 1. (Correct: 10->5. Can't do 15).

## ✅ Proof of Correctness

### Invariant
- Positive tasks increase capacity, so doing them first (cheapest first) maximizes peak energy.
- Negative tasks decrease capacity. Sorting by gain descending ensures we satisfy the tightest "end constraints" first (in reverse logic).
- The heap ensures we pick the subset with minimal total loss that fits in the budget.

## 💡 Interview Extensions

- **Extension 1:** What if tasks have deadlines?
  - *Answer:* Combine with "Job Sequencing" (sort by deadline).
- **Extension 2:** Maximize total gain instead of count?
  - *Answer:* DP (Knapsack).

### Common Mistakes to Avoid

1. **Mixing Positive/Negative**
   - ❌ Wrong: Sorting all tasks together.
   - ✅ Correct: Positive tasks must be done first to build energy.
2. **Sorting Negative Tasks**
   - ❌ Wrong: Sorting by cost or loss.
   - ✅ Correct: Sort by `gain` descending.

## Related Concepts

- **Greedy:** Standard approach for scheduling.
- **Priority Queue:** For optimizing selections with constraints.
