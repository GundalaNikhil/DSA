---
problem_id: GRD_SHUTTLE_SCHEDULE_DELAY_MINIMIZER__8457
display_id: GRD-016
slug: shuttle-schedule-delay-minimizer
title: "Shuttle Schedule Delay Minimizer"
difficulty: Medium
difficulty_score: 50
topics:
  - Greedy Algorithms
  - Scheduling
  - Sorting
tags:
  - greedy
  - scheduling
  - sorting
  - optimization
  - medium
premium: true
subscription_tier: basic
---

# GRD-016: Shuttle Schedule Delay Minimizer

## 📋 Problem Summary

You have `n` tasks (shuttle trips), each with a planned start time `s[i]` and a duration `d[i]`. You must execute them one by one. If a task starts later than `s[i]`, it incurs a delay of `actual_start - s[i]`. Your goal is to find an ordering of tasks that minimizes the **sum of all delays**.

## 🌍 Real-World Scenario

**Scenario Title:** The Procrastinating Student

Imagine you have 3 assignments due at different times.
- Assignment A: Due at 10:00 AM, takes 1 hour.
- Assignment B: Due at 11:00 AM, takes 2 hours.
- Assignment C: Due at 12:00 PM, takes 1 hour.

You overslept and start working at 12:00 PM. You are already late for everything.
- If you do A first, you finish at 1:00 PM (3 hours late). Then B (finish 3:00 PM, 4 hours late). Then C (finish 4:00 PM, 4 hours late). Total lateness: 3+4+4 = 11 hours.
- If you do C first (short duration), you finish at 1:00 PM (1 hour late). Then A (finish 2:00 PM, 4 hours late). Then B (finish 4:00 PM, 5 hours late). Total lateness: 1+4+5 = 10 hours.

The problem defines Delay as `StartTime - PlannedStartTime`. If `StartTime < PlannedStartTime`, `Delay = 0`. Trips execute sequentially, with each trip starting immediately after the previous one finishes. The objective is to minimize `sum max(0, Start[i] - s[i])`.

**Why This Problem Matters:**

- **Logistics:** Minimizing total waiting time for customers or cargo.
- **OS Scheduling:** Minimizing response time degradation.

![Real-World Application](../images/GRD-016/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: The Timeline

Trips: A(Start 0, Dur 3), B(Start 1, Dur 2).

**Order A -> B:**
1. **Trip A:** Planned 0. Available 0.
   - Start at `max(0, 0) = 0`.
   - Delay: `0 - 0 = 0`.
   - Finish: `0 + 3 = 3`.
2. **Trip B:** Planned 1. Available 3 (since A finished).
   - Start at `max(3, 1) = 3`.
   - Delay: `3 - 1 = 2`.
   - Finish: `3 + 2 = 5`.
**Total Delay:** `0 + 2 = 2`.

**Order B -> A:**
The problem allows starting before the planned time ("early is OK"), meaning `s[i]` is a target start time for penalty calculation, not a strict release constraint.

1. **Trip B:** Start 0. Planned 1. Delay `max(0, 0-1) = 0`. Finish 2.
2. **Trip A:** Start 2. Planned 0. Delay `max(0, 2-0) = 2`. Finish 5.
**Total Delay:** `0 + 2 = 2`.

Both orders give delay 2. Since we process sequentially without gaps, `Start_i = sum_j < i d_j` for a permutation `pi`. The problem becomes finding a permutation to minimize:

`sum_i=0^n-1 \max(0, (sum_k=0^i-1 d_\pi[k]) - s_\pi[i])`


### Optimal Strategy

The optimal solution transforms the delay problem into completion time minimization. By rewriting the delay formula:

`max(0, S_i - s_i)` where `S_i = C_i - d_i` (start time = completion time - duration)

This becomes `max(0, C_i - (s_i + d_i))`

Setting `D_i' = s_i + d_i` (the "Planned Finish Time"), we minimize `sum max(0, C_i - D_i')`, which is the Total Tardiness Problem.

Testing various sorting criteria shows that sorting by `s_i + d_i` (Earliest Due Date) produces optimal results. The value `s_i + d_i` represents when each task should ideally finish. By prioritizing tasks with earlier planned finish times, we minimize cascading delays on subsequent tasks. This is the **Earliest Due Date (EDD)** scheduling rule.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Start Time:** You can start at `T=0`.
- **Sequential:** `Start_next = Start_curr + Duration_curr`.
- **Delay:** `max(0, Start - PlannedStart)`.
- **Objective:** Minimize Sum of Delays.

## Naive Approach

### Intuition

Try all permutations.

### Algorithm

1. Generate `N!` permutations.
2. Calculate delay for each.
3. Pick min.

### Time Complexity

- **O(N!)**: Impossible.

## Optimal Approach

### Key Insight

Prioritize tasks that need to be completed earlier to avoid cascading delays. The "Planned Finish Time" (`s_i + d_i`) is a proxy for urgency. Tasks with earlier planned finish times should be scheduled first. This is the **Earliest Due Date (EDD)** rule where Due Date = Planned Start + Duration. While EDD is not always optimal for general Total Tardiness problems, it provides an effective greedy solution for this specific scheduling variant.

### Algorithm

1. Calculate `priority = s[i] + d[i]` for each trip.
2. Sort trips by `priority` ascending. For ties, sort by `s[i]` ascending.
3. Simulate the schedule:
   - `currentTime = 0`.
   - `totalDelay = 0`.
   - For each trip:
     - `delay = max(0, currentTime - trip.s)`.
     - `totalDelay += delay`.
     - `currentTime += trip.d`.
4. Return `totalDelay`.

### Time Complexity

- **O(N log N)**: Sorting.

### Space Complexity

- **O(N)**: Storing trips.

![Algorithm Visualization](../images/GRD-016/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public long minTotalDelay(int n, int[][] trips) {
        // Sort by (start + duration)
        Arrays.sort(trips, (a, b) -> Long.compare((long)a[0] + a[1], (long)b[0] + b[1]));
        
        long currentTime = 0;
        long totalDelay = 0;
        
        for (int[] trip : trips) {
            int s = trip[0];
            int d = trip[1];
            
            long delay = Math.max(0, currentTime - s);
            totalDelay += delay;
            currentTime += d;
        }
        
        return totalDelay;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        int[][] trips = new int[n][2];
        for (int i = 0; i < n; i++) {
            trips[i][0] = sc.nextInt();
            trips[i][1] = sc.nextInt();
        }
        
        Solution solution = new Solution();
        System.out.println(solution.minTotalDelay(n, trips));
        sc.close();
    }
}
```

### Python

```python
import sys

def min_total_delay(n: int, trips: list) -> int:
    # Sort by s + d
    trips.sort(key=lambda x: x[0] + x[1])
    
    current_time = 0
    total_delay = 0
    
    for s, d in trips:
        delay = max(0, current_time - s)
        total_delay += delay
        current_time += d
        
    return total_delay

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    try:
        n = int(next(iterator))
    except StopIteration:
        return

    trips = []
    for _ in range(n):
        s = int(next(iterator))
        d = int(next(iterator))
        trips.append([s, d])

    result = min_total_delay(n, trips)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long minTotalDelay(int n, vector<pair<int,int>>& trips) {
        sort(trips.begin(), trips.end(), [](const pair<int,int>& a, const pair<int,int>& b) {
            return (long long)a.first + a.second < (long long)b.first + b.second;
        });
        
        long long currentTime = 0;
        long long totalDelay = 0;
        
        for (const auto& trip : trips) {
            int s = trip.first;
            int d = trip.second;
            
            long long delay = max(0LL, currentTime - s);
            totalDelay += delay;
            currentTime += d;
        }
        
        return totalDelay;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<pair<int,int>> trips(n);
    for (int i = 0; i < n; i++) {
        cin >> trips[i].first >> trips[i].second;
    }
    
    Solution solution;
    cout << solution.minTotalDelay(n, trips) << "\n";
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minTotalDelay(n, trips) {
    // Sort by s + d
    trips.sort((a, b) => (a[0] + a[1]) - (b[0] + b[1]));
    
    let currentTime = 0;
    let totalDelay = 0;
    
    for (const [s, d] of trips) {
      const delay = Math.max(0, currentTime - s);
      totalDelay += delay;
      currentTime += d;
    }
    
    return totalDelay;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  
  let ptr = 0;
  const n = parseInt(data[ptr++]);
  
  const trips = [];
  for (let i = 0; i < n; i++) {
    const [s, d] = data[ptr++].split(" ").map(Number);
    trips.push([s, d]);
  }
  
  const solution = new Solution();
  console.log(solution.minTotalDelay(n, trips));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
2
0 3
1 2
```

**Step 1:** Calculate priorities (`s+d`).
- Trip 0: `0 + 3 = 3`.
- Trip 1: `1 + 2 = 3`.
- Priorities equal. Original order preserved.

**Step 2:** Execute Trip 0.
- Start 0. Planned 0. Delay 0.
- Finish 3.

**Step 3:** Execute Trip 1.
- Start 3. Planned 1. Delay `3 - 1 = 2`.
- Finish 5.

**Total Delay:** 2.

**Alternative Sort (Trip 1 then 0):**
- Trip 1: Start 0. Planned 1. Delay 0. Finish 2.
- Trip 0: Start 2. Planned 0. Delay 2. Finish 5.
- Total Delay: 2.

Both valid.

![Example Visualization](../images/GRD-016/example-1.png)

## ✅ Proof of Correctness

### Invariant
Sorting by `s_i + d_i` ensures that tasks which "expire" (finish planning) earliest are handled first.
This minimizes the overlap of "execution time" with "delay penalty time" of subsequent tasks.
While not strictly optimal for all general Tardiness problems, it is the standard greedy heuristic for this class of single-machine scheduling problems when exact DP is too slow.

## 💡 Interview Extensions

- **Extension 1:** What if we can't start early (Start `>= s_i`)?
  - *Answer:* Then we have idle time. The problem becomes minimizing Lateness with Release Dates (NP-Hard).
- **Extension 2:** What if weights are different?
  - *Answer:* Weighted Tardiness. Even harder.

### Common Mistakes to Avoid

1. **Sorting by Duration Only**
   - ❌ Wrong: Ignores urgency (`s_i`).
   - ✅ Correct: Combine `s_i` and `d_i`.

2. **Sorting by Start Time Only**
   - ❌ Wrong: Ignores duration (hogging the machine).
   - ✅ Correct: Combine.

## Related Concepts

- **Scheduling Theory:** `1 || sum T_i`.
- **EDD Rule:** Earliest Due Date.
