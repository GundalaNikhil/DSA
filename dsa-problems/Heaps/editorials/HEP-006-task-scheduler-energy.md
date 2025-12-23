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

### Key Concept: Positive vs Negative Net Gain

Split tasks into:
- **Positive tasks** (`gain >= duration`): executing them never decreases energy.
- **Negative tasks** (`gain < duration`): executing them decreases energy by
  `loss = duration - gain`.

#### Positive tasks
Sort by duration ascending and execute while possible. If the smallest-duration
positive task is not feasible, no other positive task is feasible and energy
cannot increase further from positives.

#### Negative tasks
Let `E_peak` be the energy after all feasible positive tasks.
For negative tasks, an optimal execution order is by **gain descending**.
In that order, before task `i` the energy is
`E_peak - sum_loss_prev`, so feasibility requires:
```
E_peak >= gain_i + sum_loss_prefix
```
where `sum_loss_prefix` includes the current task's loss.

To maximize the number of negative tasks, keep `sum_loss_prefix` as small as
possible:
- Iterate negative tasks by gain descending.
- Add each loss to a max-heap and to `sum_loss`.
- If `sum_loss + gain_i > E_peak`, remove the task with the **largest loss**.

The heap size after processing all negatives is the maximum number of negative
tasks that can be scheduled.

### Algorithm

1. Split tasks into positive and negative.
2. Sort positive by duration ascending and execute while feasible.
3. Let `E_peak` be the resulting energy.
4. Sort negative by gain descending.
5. Max-heap of losses and running `sum_loss`:
   - Add `loss`.
   - If `sum_loss + gain_i > E_peak`, remove the largest loss.
6. Answer = `positive_count + heap_size`.

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
        
        long peakE = currentE;

        // 2. Process Negative: Sort by gain descending
        Collections.sort(negative, (a, b) -> Integer.compare(b.g, a.g));
        
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        long currentLossSum = 0;
        
        for (Task t : negative) {
            int loss = t.d - t.g;
            currentLossSum += loss;
            pq.offer(loss);
            if (currentLossSum + t.g > peakE) {
                currentLossSum -= pq.poll();
            }
        }
        
        return count + pq.size();
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
                
        peak_e = current_e

        # Negative: Sort by gain desc
        negative.sort(key=lambda x: x[1], reverse=True)
        
        # Max heap for losses (use negative values for min-heap to simulate max-heap)
        pq = []
        current_loss_sum = 0
        
        for d, g in negative:
            loss = d - g
            current_loss_sum += loss
            heapq.heappush(pq, -loss)
            if current_loss_sum + g > peak_e:
                current_loss_sum += heapq.heappop(pq)
                
        return count + len(pq)

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

        long long peakE = E;
        
        sort(negative.begin(), negative.end(), [](const Task& a, const Task& b) {
            return a.g > b.g;
        });
        
        priority_queue<int> pq; // Max heap for losses
        long long currentLossSum = 0;
        
        for (const auto& t : negative) {
            int loss = t.d - t.g;
            currentLossSum += loss;
            pq.push(loss);
            if (currentLossSum + t.g > peakE) {
                currentLossSum -= pq.top();
                pq.pop();
            }
        }
        
        return count + (int)pq.size();
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
    
    const peakE = currentE;

    negative.sort((a, b) => b.g - a.g);
    
    // Max heap for losses
    const pq = new PriorityQueue((a, b) => b - a);
    let currentLossSum = 0n;
    
    for (const t of negative) {
      const loss = BigInt(t.d - t.g);
      currentLossSum += loss;
      pq.push(Number(loss));
      if (currentLossSum + BigInt(t.g) > peakE) {
        currentLossSum -= BigInt(pq.pop());
      }
    }
    
    return count + pq.size();
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
   - `3 >= 2`. Do it.
   - `E = 3 - 2 + 3 = 4`. Count = 1.
2. **Negative:** `(3,1)`. Loss = 2.
   - Sort by gain desc: `(3,1)` (gain 1).
   - Check: `4 >= 1 + 0 + 2 = 3`.
   - Yes. Do it.
   - Count = 2.

**Result:** 2.

**Input:** E=10. Negatives: `(10, 5)`, `(15, 10)`.
- Sorted by gain: `(15, 10)` (gain 10), `(10, 5)` (gain 5).
- T1 (15, 10): Loss 5.
  - Sum loss = 5. Check `5 + 10 > 10`. Remove loss 5.
- T2 (10, 5): Loss 5.
  - Sum loss = 5. Check `5 + 5 <= 10`. Keep.
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
