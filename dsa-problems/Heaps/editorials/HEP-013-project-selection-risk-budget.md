---
problem_id: HEP_PROJECT_SELECTION_RISK_BUDGET__2917
display_id: HEP-013
slug: project-selection-risk-budget
title: "Project Selection with Risk Budget"
difficulty: Medium
difficulty_score: 60
topics:
  - Heaps
  - Greedy
  - Finance
tags:
  - heaps
  - greedy
  - risk-budget
  - medium
premium: true
subscription_tier: basic
---

# HEP-013: Project Selection with Risk Budget

## 📋 Problem Summary

You have `n` projects, each with:
- `cost`: Minimum capital required to start.
- `profit`: Capital gained after completion.
- `risk`: Risk incurred.

You start with initial capital `C` and risk budget `R`.
You can select at most `k` projects.
Constraints to select a project:
1. `current_capital >= cost`
2. `current_risk + risk <= R`

Goal: Maximize final capital.
Note: Capital increases by `profit`. Risk increases by `risk`.

## 🌍 Real-World Scenario

**Scenario Title:** Venture Capital Investment

A VC firm has a fund `C` and a strict risk tolerance `R`.
- Startups pitch for funding (`cost`).
- If successful, they return `profit`.
- Each investment adds exposure (`risk`) to the portfolio.
- The firm wants to reinvest returns into new startups to maximize the fund's value after `k` rounds of investment, without exceeding the risk limit.

![Real-World Application](../images/HEP-013/real-world-scenario.png)

## Detailed Explanation

### Key Idea

This is the IPO selection pattern with an extra risk budget.
- Capital only increases, so once a project is affordable by cost, it stays
  affordable.
- Remaining risk only decreases, so a project that is too risky now will never
  become feasible later.

We sort projects by cost and maintain a max-heap by profit for the projects that
are currently affordable. For each selection, we pop the most profitable project
that fits the remaining risk budget.

### Example

Input:
```
3 2 1 3
1 2 1
2 2 2
3 5 2
```
- Start: capital=1, remaining risk=3.
- Pick project 1 (cost 1, profit 2, risk 1): capital=3, remaining risk=2.
- Projects 2 and 3 are affordable; pick project 3 (profit 5, risk 2).
- Final capital = 8.

### Algorithm

1. Sort projects by cost ascending.
2. Max-heap by profit for all projects with `cost <= current capital`.
3. Repeat up to `k` times:
   - Push all newly affordable projects into the heap.
   - Pop from the heap until you find a project with `risk <= remaining risk`.
     If none exist, stop.
   - Take the project: `capital += profit`, `remaining risk -= risk`.
4. Return the final capital.

### Time Complexity

- **O(N log N)**.

### Space Complexity

- **O(N)**.

![Algorithm Visualization](../images/HEP-013/algorithm-visualization.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    static class Project {
        long c, p, r;
        public Project(long c, long p, long r) {
            this.c = c;
            this.p = p;
            this.r = r;
        }
    }
    
    public long maximizeCapital(int k, long C, long R, long[] cost, long[] profit, long[] risk) {
        int n = cost.length;
        Project[] projects = new Project[n];
        for (int i = 0; i < n; i++) {
            projects[i] = new Project(cost[i], profit[i], risk[i]);
        }
        
        // Sort by cost
        Arrays.sort(projects, (a, b) -> Long.compare(a.c, b.c));
        
        // Max-Heap by profit
        PriorityQueue<Project> pq = new PriorityQueue<>((a, b) -> Long.compare(b.p, a.p));
        
        int ptr = 0;
        long currentC = C;
        long remainingR = R;
        
        for (int i = 0; i < k; i++) {
            // Add affordable projects
            while (ptr < n && projects[ptr].c <= currentC) {
                pq.offer(projects[ptr]);
                ptr++;
            }
            
            // Pick best valid
            boolean picked = false;
            while (!pq.isEmpty()) {
                Project p = pq.peek();
                if (p.r <= remainingR) {
                    // Valid
                    pq.poll();
                    currentC += p.p;
                    remainingR -= p.r;
                    picked = true;
                    break;
                } else {
                    // Too risky, will never be valid
                    pq.poll();
                }
            }
            
            if (!picked) break;
        }
        
        return currentC;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            long C = sc.nextLong();
            long R = sc.nextLong();
            long[] cost = new long[n];
            long[] profit = new long[n];
            long[] risk = new long[n];
            for (int i = 0; i < n; i++) {
                cost[i] = sc.nextLong();
                profit[i] = sc.nextLong();
                risk[i] = sc.nextLong();
            }
            
            Solution solution = new Solution();
            System.out.println(solution.maximizeCapital(k, C, R, cost, profit, risk));
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
    def maximize_capital(self, k: int, C: int, R: int, cost: list, profit: list, risk: list) -> int:
        n = len(cost)
        projects = []
        for i in range(n):
            projects.append((cost[i], profit[i], risk[i]))
            
        # Sort by cost
        projects.sort(key=lambda x: x[0])
        
        # Max-Heap (store -profit)
        pq = []
        ptr = 0
        current_c = C
        remaining_r = R
        
        for _ in range(k):
            # Add affordable
            while ptr < n and projects[ptr][0] <= current_c:
                # Push (-profit, risk)
                heapq.heappush(pq, (-projects[ptr][1], projects[ptr][2]))
                ptr += 1
                
            # Pick best
            picked = False
            while pq:
                p, r = pq[0] # Peek
                p = -p
                
                if r <= remaining_r:
                    heapq.heappop(pq)
                    current_c += p
                    remaining_r -= r
                    picked = True
                    break
                else:
                    # Too risky
                    heapq.heappop(pq)
            
            if not picked:
                break
                
        return current_c

def maximize_capital(k: int, C: int, R: int, cost: list, profit: list, risk: list) -> int:
    solver = Solution()
    return solver.maximize_capital(k, C, R, cost, profit, risk)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        k = int(next(it))
        C = int(next(it))
        R = int(next(it))
        cost = []
        profit = []
        risk = []
        for _ in range(n):
            cost.append(int(next(it)))
            profit.append(int(next(it)))
            risk.append(int(next(it)))
            
        print(maximize_capital(k, C, R, cost, profit, risk))
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

struct Project {
    long long c, p, r;
};

struct CompareProfit {
    bool operator()(const Project& a, const Project& b) {
        return a.p < b.p; // Max heap
    }
};

class Solution {
public:
    long long maximizeCapital(int k, long long C, long long R, const vector<long long>& cost,
                              const vector<long long>& profit, const vector<long long>& risk) {
        int n = cost.size();
        vector<Project> projects(n);
        for (int i = 0; i < n; i++) {
            projects[i] = {cost[i], profit[i], risk[i]};
        }
        
        sort(projects.begin(), projects.end(), [](const Project& a, const Project& b) {
            return a.c < b.c;
        });
        
        priority_queue<Project, vector<Project>, CompareProfit> pq;
        int ptr = 0;
        long long currentC = C;
        long long remainingR = R;
        
        for (int i = 0; i < k; i++) {
            while (ptr < n && projects[ptr].c <= currentC) {
                pq.push(projects[ptr]);
                ptr++;
            }
            
            bool picked = false;
            while (!pq.empty()) {
                Project top = pq.top();
                if (top.r <= remainingR) {
                    pq.pop();
                    currentC += top.p;
                    remainingR -= top.r;
                    picked = true;
                    break;
                } else {
                    pq.pop();
                }
            }
            
            if (!picked) break;
        }
        
        return currentC;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, k;
    long long C, R;
    if (cin >> n >> k >> C >> R) {
        vector<long long> cost(n), profit(n), risk(n);
        for (int i = 0; i < n; i++) cin >> cost[i] >> profit[i] >> risk[i];
        
        Solution solution;
        cout << solution.maximizeCapital(k, C, R, cost, profit, risk) << "\n";
    }
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class PriorityQueue {
  constructor(compare) {
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
  maximizeCapital(k, C, R, cost, profit, risk) {
    const n = cost.length;
    const projects = [];
    for (let i = 0; i < n; i++) {
      projects.push({ c: BigInt(cost[i]), p: BigInt(profit[i]), r: BigInt(risk[i]) });
    }
    
    projects.sort((a, b) => {
      if (a.c < b.c) return -1;
      if (a.c > b.c) return 1;
      return 0;
    });
    
    const pq = new PriorityQueue((a, b) => {
      if (a.p > b.p) return -1;
      if (a.p < b.p) return 1;
      return 0;
    });
    
    let ptr = 0;
    let currentC = BigInt(C);
    let remainingR = BigInt(R);
    
    for (let i = 0; i < k; i++) {
      while (ptr < n && projects[ptr].c <= currentC) {
        pq.push(projects[ptr]);
        ptr++;
      }
      
      let picked = false;
      while (!pq.isEmpty()) {
        const top = pq.peek();
        if (top.r <= remainingR) {
          pq.pop();
          currentC += top.p;
          remainingR -= top.r;
          picked = true;
          break;
        } else {
          pq.pop();
        }
      }
      
      if (!picked) break;
    }
    
    return currentC.toString();
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
  const k = parseInt(data[idx++]);
  const C = parseInt(data[idx++]);
  const R = parseInt(data[idx++]);
  const cost = [];
  const profit = [];
  const risk = [];
  for (let i = 0; i < n; i++) {
    cost.push(parseInt(data[idx++]));
    profit.push(parseInt(data[idx++]));
    risk.push(parseInt(data[idx++]));
  }
  
  const solution = new Solution();
  console.log(solution.maximizeCapital(k, C, R, cost, profit, risk));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3 2 1 3
1 2 1
2 2 2
3 5 2
```
Sorted by cost: P1 (1,2,1), P2 (2,2,2), P3 (3,5,2).

1. **Step 1:**
   - Affordable: P1.
   - Pick P1. Capital = 3, Remaining risk = 2.
2. **Step 2:**
   - Affordable: P2, P3.
   - Pick P3 (profit 5, risk 2).
   - Capital = 8, Remaining risk = 0.

**Result:** 8.

## ✅ Proof of Correctness

### Invariant
- The set of cost-affordable projects only grows as capital increases, so every
  project is pushed to the heap at most once.
- Remaining risk only decreases. If a project is too risky now, it will never
  become feasible later, so discarding it is safe.
- Choosing the feasible project with maximum profit maximizes the next capital
  and cannot reduce future affordability.

## 💡 Interview Extensions

- **Extension 1:** Capital consumed?
  - *Answer:* Then it becomes Knapsack-like (Cost/Profit trade-off).
- **Extension 2:** Risk decreases?
  - *Answer:* Then valid set grows.

### Common Mistakes to Avoid

1. **Risk Check Timing**
   - ❌ Wrong: Checking risk only when adding to heap.
   - ✅ Correct: Check risk when popping, because budget decreases.
2. **Capital Consumption**
   - ❌ Wrong: Subtracting cost from capital.
   - ✅ Correct: Capital only increases.

## Related Concepts

- **Greedy:** Standard approach.
