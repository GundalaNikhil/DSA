---
problem_id: GRD_FESTIVAL_BANDWIDTH_SPLIT__9163
display_id: GRD-014
slug: festival-bandwidth-split
title: "Festival Bandwidth Split"
difficulty: Medium
difficulty_score: 45
topics:
  - Greedy Algorithms
  - Knapsack
  - Optimization
tags:
  - greedy
  - knapsack
  - optimization
  - medium
premium: true
subscription_tier: basic
---

# GRD-014: Festival Bandwidth Split

## 📋 Problem Summary

You have `n` stages, each requiring a minimum bandwidth `b[i]`. You have a total bandwidth budget `B`. You want to maximize the **count** of stages that can run. As a secondary goal, minimize wasted bandwidth.

## 🌍 Real-World Scenario

**Scenario Title:** Packing a Lunchbox

Imagine you have a small lunchbox (Capacity `B`) and many different snacks (Items).
- Each snack has a size `b[i]`.
- You want to fit as many *different* snacks as possible into the box to have variety.
- You don't care about the total calories (sum of sizes), just the *number* of items.
- If you have space left over, you'd prefer to fill it tightly, but your main goal is "More Items".

To fit the most items, you should obviously pack the smallest ones first! Putting a giant watermelon in the box takes up space that could hold 10 grapes.

**Why This Problem Matters:**

- **Resource Allocation:** Maximizing the number of customers served (throughput) when resources are limited.
- **Budgeting:** Buying as many items as possible with a fixed amount of money.

![Real-World Application](../images/GRD-014/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: The Greedy Choice

Items: [5, 2, 4]. Budget: 7.

Sorted: [2, 4, 5].

```text
Step 1: Pick smallest (2).
   Remaining Budget: 7 - 2 = 5.
   Count: 1.

Step 2: Pick next smallest (4).
   Remaining Budget: 5 - 4 = 1.
   Count: 2.

Step 3: Pick next smallest (5).
   Remaining Budget: 1 - 5 = -4 (Impossible).
   Stop.

Result: 2 items.
```

If we picked 5 first:
   Remaining: 2.
   Pick 2: Remaining 0. Count 2.
   Pick 4: Impossible.
   Result: 2 items.

Both give 2 items. But picking smallest first guarantees we never "block" a future small item with a large one unnecessarily.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Maximize Count:** This is the primary objective.
- **Minimize Waste:** This is secondary. The greedy strategy of "smallest first" naturally handles this because by picking smaller items, we leave more room (or use less space for the same count). Wait, actually, if we pick [2, 4] (Sum 6, Waste 1) vs [2, 5] (Sum 7, Waste 0), both have count 2.
- **Does Greedy Minimize Waste?**
  - The problem asks to minimize waste *among solutions with maximum stages*.
  - Greedy picks [2, 4] -> Sum 6. Waste 1.
  - Alternative [2, 5] -> Sum 7. Waste 0.
  - The problem example says: "Best choice: Stages 0 + 1 (waste = 0)". Wait.
  - Example Input: `5 2 4`. Budget 7.
  - Greedy (Sorted: 2, 4, 5): Picks 2, then 4. Sum 6. Waste 1.
  - Example Explanation says: "Best choice: Stages 0 + 1 (waste = 0)". (5 + 2 = 7).
  - **CRITICAL:** The example explanation contradicts the standard "Maximize Count" greedy logic if "Minimize Waste" implies *maximizing used bandwidth*.
  - Usually "Minimize Waste" means "Maximize Used".
  - If we strictly follow "Smallest First", we get Count 2, Used 6.
  - If we pick {5, 2}, we get Count 2, Used 7.
  - Both have Count 2. But {5, 2} has less waste.
  - **Does the Greedy Strategy fail the secondary goal?**
    - Yes, simple sorting fails the secondary goal.
    - However, the Note says: "To minimize waste among solutions with same stage count, this greedy approach already achieves it".
    - This note in the problem description is **incorrect** based on the example explanation provided in the same file!
    - The example explanation explicitly prefers {5, 2} (Waste 0) over {2, 4} (Waste 1).
    - But the standard greedy approach picks {2, 4}.
    - **What should we do?**
    - The problem asks to return "Single integer: maximum number of stages".
    - It does **NOT** ask to return the waste or the specific set.
    - So the secondary goal is irrelevant for the *Output Format*.
    - The output is just the count.
    - Both strategies yield Count 2.
    - Therefore, for the purpose of the *Output*, the simple Greedy (Smallest First) is sufficient and correct.
    - I will stick to the simple Greedy because calculating the optimal waste for a fixed count is a subset sum problem (NP-Hard). Given $N=10^5$, we cannot solve Subset Sum.
    - Thus, the "Secondary Goal" text in the problem is likely flavor text or a misunderstanding in the problem writing, given the constraints.
    - I will focus on the Primary Goal.

## Naive Approach

### Intuition

Try all subsets.

### Algorithm

1. Generate $2^N$ subsets.
2. Filter those with Sum $\le B$.
3. Pick max size.

### Time Complexity

- **O(2^N)**: Impossible.

## Optimal Approach

### Key Insight

To maximize the *number* of items with a fixed budget, we should always buy the cheapest items.
Proof: Suppose an optimal solution $S$ does not include the smallest item $x$, but includes a larger item $y$. We can swap $y$ for $x$. The count remains the same, but the total sum decreases (or stays same), so the budget constraint is still satisfied. We can repeat this until $S$ consists of the $k$ smallest items.

### Algorithm

1. Sort `bandwidths` in ascending order.
2. Iterate and sum up values.
3. Stop when `current_sum + next_val > B`.
4. Return the count.

### Time Complexity

- **O(N log N)**: Sorting.

### Space Complexity

- **O(1)**: (ignoring sort space).

![Algorithm Visualization](../images/GRD-014/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int maxStages(int n, long B, long[] bandwidths) {
        Arrays.sort(bandwidths);
        
        long currentSum = 0;
        int count = 0;
        
        for (long b : bandwidths) {
            if (currentSum + b <= B) {
                currentSum += b;
                count++;
            } else {
                break;
            }
        }
        
        return count;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        long B = sc.nextLong();
        
        long[] bandwidths = new long[n];
        for (int i = 0; i < n; i++) {
            bandwidths[i] = sc.nextLong();
        }
        
        Solution solution = new Solution();
        System.out.println(solution.maxStages(n, B, bandwidths));
        sc.close();
    }
}
```

### Python

```python
import sys

def max_stages(n: int, B: int, bandwidths: list) -> int:
    bandwidths.sort()
    
    current_sum = 0
    count = 0
    
    for b in bandwidths:
        if current_sum + b <= B:
            current_sum += b
            count += 1
        else:
            break
            
    return count

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    n = int(next(iterator))
    B = int(next(iterator))
    
    bandwidths = []
    for _ in range(n):
        bandwidths.append(int(next(iterator)))

    result = max_stages(n, B, bandwidths)
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
    int maxStages(int n, long long B, vector<long long>& bandwidths) {
        sort(bandwidths.begin(), bandwidths.end());
        
        long long currentSum = 0;
        int count = 0;
        
        for (long long b : bandwidths) {
            if (currentSum + b <= B) {
                currentSum += b;
                count++;
            } else {
                break;
            }
        }
        
        return count;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long B;
    if (!(cin >> n >> B)) return 0;

    vector<long long> bandwidths(n);
    for (int i = 0; i < n; i++) {
        cin >> bandwidths[i];
    }

    Solution solution;
    cout << solution.maxStages(n, B, bandwidths) << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxStages(n, B, bandwidths) {
    // Sort numerically!
    bandwidths.sort((a, b) => a - b);
    
    let currentSum = 0;
    let count = 0;
    
    for (const b of bandwidths) {
      if (currentSum + b <= B) {
        currentSum += b;
        count++;
      } else {
        break;
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
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  
  let ptr = 0;
  const [n, B] = data[ptr++].split(" ").map(Number);
  const bandwidths = data[ptr++].split(" ").map(Number);

  const solution = new Solution();
  console.log(solution.maxStages(n, B, bandwidths));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3 7
5 2 4
```

**Step 1:** Sort `[2, 4, 5]`.
**Step 2:**
- Pick 2. Sum 2. Count 1.
- Pick 4. Sum 6. Count 2.
- Pick 5. Sum 6+5=11 > 7. Break.

**Result:** 2.

![Example Visualization](../images/GRD-014/example-1.png)

## ✅ Proof of Correctness

### Invariant
The set of $k$ smallest elements has the minimum possible sum of any subset of size $k$.
Therefore, if any subset of size $k$ fits in budget $B$, the subset of the $k$ smallest elements also fits.
This implies that we can simply check sizes $k=1, 2, ...$ using the smallest elements until we fail.

## 💡 Interview Extensions

- **Extension 1:** What if we want to maximize the *total bandwidth used* (Knapsack)?
  - *Answer:* This is 0/1 Knapsack (NP-Hard). Solvable with DP if $B$ is small.
- **Extension 2:** What if we can use fractions of a stage?
  - *Answer:* Fractional Knapsack (Greedy by value/weight ratio). Here value=1, weight=b. Ratio = $1/b$. Best ratio = smallest $b$. Same logic.

## Common Mistakes to Avoid

1. **Sorting Strings**
   - ❌ Wrong: In JS, `sort()` sorts alphabetically ("10" < "2").
   - ✅ Correct: `sort((a,b) => a-b)`.

2. **Integer Overflow**
   - ❌ Wrong: Using `int` for sum if $B$ is large ($10^{12}$).
   - ✅ Correct: Use `long` / `long long`.

## Related Concepts

- **Knapsack Problem:** The general family.
- **Sorting:** The key operation.
