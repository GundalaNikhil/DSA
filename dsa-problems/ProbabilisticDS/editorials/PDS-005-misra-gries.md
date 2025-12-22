---
problem_id: PDS_MISRA_GRIES__9624
display_id: PDS-005
slug: misra-gries
title: "Frequent Items with Misra-Gries"
difficulty: Medium
difficulty_score: 52
topics:
  - Probabilistic Data Structures
  - Streaming
  - Frequency Estimation
tags:
  - probabilistic-ds
  - misra-gries
  - streaming
  - medium
premium: true
subscription_tier: basic
---

# PDS-005: Frequent Items with Misra-Gries

## 📋 Problem Summary

We need to identify all elements in a stream of $n$ items that appear more than $n/k$ times.
- We must use the **Misra-Gries** algorithm.
- We are allowed to maintain at most $k-1$ counters.
- The output should be the set of candidate items remaining in the counters after processing the stream.

## 🌍 Real-World Scenario

**Scenario Title:** Real-Time Traffic Analysis

Imagine you are monitoring a high-speed network link (100 Gbps).
- You want to identify IP addresses that are consuming a significant portion of the bandwidth (e.g., > 1%).
- There are billions of possible IP addresses, so you can't store a counter for each one.
- However, you know that there can be at most 99 IPs that consume > 1% of the bandwidth.
- **Misra-Gries** allows you to track these "heavy hitters" using a very small amount of memory (just 99 counters) with a guarantee that you won't miss any true heavy hitter.

**Why This Problem Matters:**

- **DDoS Detection:** Identifying IPs sending a flood of packets.
- **Search Trends:** Finding the most popular queries in a stream.
- **Financial Trading:** Identifying stocks with unusually high trade volume.

![Real-World Application](../images/PDS-005/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Misra-Gries Logic

Stream: `A B A C A D` ($k=3$, so we keep $k-1=2$ counters).

1. **Read A:** Counters: `{A:1}`
2. **Read B:** Counters: `{A:1, B:1}` (Full)
3. **Read A:** Increment A. Counters: `{A:2, B:1}`
4. **Read C:** C is not in counters, and counters are full.
   - Decrement ALL counters.
   - `{A:1, B:0}` -> Remove B.
   - Counters: `{A:1}`
5. **Read A:** Increment A. Counters: `{A:2}`
6. **Read D:** Counters: `{A:2, D:1}`

Result Candidates: `{A, D}`.
Note: A appeared 3 times (50% of 6). D appeared 1 time.
Threshold $n/k = 6/3 = 2$. A is a true heavy hitter. D is a false positive candidate (which is allowed).

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:**
  - $n$: Stream length.
  - $k$: Parameter (threshold $n/k$).
  - Stream: List of integers.
- **Output:**
  - Sorted list of keys remaining in the map.
- **Algorithm:**
  - Maintain a map of size at most $k-1$.
  - If item $x$ in map: increment count.
  - Else if map size < $k-1$: add $x$ with count 1.
  - Else (map full): decrement ALL counts in map. Remove keys that drop to 0.

## Naive Approach

### Intuition

Store counts for ALL items in a hash map.

### Algorithm

1. Count everything.
2. Filter keys with count $> n/k$.

### Limitations

- **Space Complexity:** $O(N)$ unique items. If stream has 1 billion unique items, this crashes memory.
- Misra-Gries uses $O(k)$ space, which is tiny.

## Optimal Approach

### Key Insight

The Misra-Gries algorithm generalizes the Boyer-Moore Voting Algorithm (which finds a majority element $> n/2$).
- By decrementing $k$ distinct elements at once (the new one + the $k-1$ in the map), we "cancel out" groups of $k$ distinct items.
- If an item appears $> n/k$ times, it cannot be fully cancelled out.

### Algorithm

1. Initialize empty map `counts`.
2. For each item `x` in stream:
   - If `x` in `counts`: `counts[x]++`
   - Else if `counts.size() < k-1`: `counts[x] = 1`
   - Else:
     - Decrement all keys in `counts`.
     - Remove keys with value 0.
3. Extract keys from `counts`, sort them, and print.

### Time Complexity

- **O(n \cdot k)** if decrementing takes $O(k)$.
- Can be optimized to $O(n)$ with advanced data structures, but $O(n \cdot k)$ is acceptable since $k$ is small.

### Space Complexity

- **O(k)**.

![Algorithm Visualization](../images/PDS-005/algorithm-visualization.png)
![Algorithm Steps](../images/PDS-005/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public List<Integer> misraGries(int[] stream, int k) {
        Map<Integer, Integer> counts = new HashMap<>();
        
        for (int x : stream) {
            if (counts.containsKey(x)) {
                counts.put(x, counts.get(x) + 1);
            } else if (counts.size() < k - 1) {
                counts.put(x, 1);
            } else {
                // Decrement all
                List<Integer> toRemove = new ArrayList<>();
                for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
                    int val = entry.getValue() - 1;
                    if (val == 0) {
                        toRemove.add(entry.getKey());
                    } else {
                        entry.setValue(val);
                    }
                }
                for (int key : toRemove) {
                    counts.remove(key);
                }
            }
        }
        
        List<Integer> res = new ArrayList<>(counts.keySet());
        Collections.sort(res);
        return res;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            int[] stream = new int[n];
            for (int i = 0; i < n; i++) {
                stream[i] = sc.nextInt();
            }
    
            Solution solution = new Solution();
            List<Integer> res = solution.misraGries(stream, k);
            for (int i = 0; i < res.size(); i++) {
                System.out.print(res.get(i));
                if (i + 1 < res.size()) System.out.print(" ");
            }
            System.out.println();
        }
        sc.close();
    }
}
```

### Python

```python
import sys
from collections import Counter

def misra_gries(stream, k):
    counts = Counter()
    
    for x in stream:
        if x in counts:
            counts[x] += 1
        elif len(counts) < k - 1:
            counts[x] = 1
        else:
            # Decrement all
            to_remove = []
            for key in counts:
                counts[key] -= 1
                if counts[key] == 0:
                    to_remove.append(key)
            for key in to_remove:
                del counts[key]
                
    return sorted(counts.keys())

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        k = int(next(iterator))
        stream = []
        for _ in range(n):
            stream.append(int(next(iterator)))
            
        res = misra_gries(stream, k)
        print(" ".join(str(x) for x in res))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> misraGries(const vector<int>& stream, int k) {
        map<int, int> counts;
        
        for (int x : stream) {
            if (counts.count(x)) {
                counts[x]++;
            } else if (counts.size() < k - 1) {
                counts[x] = 1;
            } else {
                // Decrement all
                vector<int> toRemove;
                for (auto& pair : counts) {
                    pair.second--;
                    if (pair.second == 0) {
                        toRemove.push_back(pair.first);
                    }
                }
                for (int key : toRemove) {
                    counts.erase(key);
                }
            }
        }
        
        vector<int> res;
        for (auto& pair : counts) {
            res.push_back(pair.first);
        }
        return res;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (cin >> n >> k) {
        vector<int> stream(n);
        for (int i = 0; i < n; i++) cin >> stream[i];
    
        Solution solution;
        vector<int> res = solution.misraGries(stream, k);
        for (int i = 0; i < (int)res.size(); i++) {
            if (i) cout << " ";
            cout << res[i];
        }
        cout << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function misraGries(stream, k) {
  const counts = new Map();
  
  for (const x of stream) {
    if (counts.has(x)) {
      counts.set(x, counts.get(x) + 1);
    } else if (counts.size < k - 1) {
      counts.set(x, 1);
    } else {
      // Decrement all
      const toRemove = [];
      for (const [key, val] of counts) {
        if (val - 1 === 0) {
          toRemove.push(key);
        } else {
          counts.set(key, val - 1);
        }
      }
      for (const key of toRemove) {
        counts.delete(key);
      }
    }
  }
  
  const res = Array.from(counts.keys()).sort((a, b) => a - b);
  return res;
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
  const k = parseInt(data[idx++], 10);
  const stream = [];
  for (let i = 0; i < n; i++) stream.push(parseInt(data[idx++], 10));
  const res = misraGries(stream, k);
  console.log(res.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `7 3`, Stream `1 2 1 3 1 2 4`
$k=3$, capacity=2.

1. `1`: `{1:1}`
2. `2`: `{1:1, 2:1}`
3. `1`: `{1:2, 2:1}`
4. `3`: Full. Decr all. `{1:1, 2:0}` -> `{1:1}`.
5. `1`: `{1:2}`
6. `2`: `{1:2, 2:1}`
7. `4`: Full. Decr all. `{1:1, 2:0}` -> `{1:1}`.

Step 4: `3` arrives. Map `{1:2, 2:1}`. Decrement: `{1:1, 2:0}`. Remove 2. Map `{1:1}`. Correct.
Step 5: `1` arrives. Map `{1:2}`.
Step 6: `2` arrives. Map `{1:2, 2:1}`.
Step 7: `4` arrives. Map `{1:2, 2:1}`. Decrement: `{1:1, 2:0}`. Remove 2. Map `{1:1}`.

Result: `1`.
The example explanation says "Misra-Gries keeps at most 2 counters".
Maybe the order of operations matters?
If I process `1 2 1 3 1 2 4`:
- `1`: `{1:1}`
- `2`: `{1:1, 2:1}`
- `1`: `{1:2, 2:1}`
- `3`: `{1:1}` (after decr)
- `1`: `{1:2}`
- `2`: `{1:2, 2:1}`
- `4`: `{1:1}` (after decr)

Why does example say `1 2`?
Ah, `1 2 1 3 1 2 4`.
Maybe my manual trace of step 7 is wrong?
`{1:2, 2:1}` + `4`.
Decrement 1 -> 1.
Decrement 2 -> 0.
So 2 is removed. 1 remains.
Is it possible the example logic is slightly different?
Or maybe I copied the stream wrong? `1 2 1 3 1 2 4`.
Let's check the code logic.
If `counts` has `x`, increment.
Else if space, add.
Else decrement all.

Maybe the example output `1 2` implies `2` survived?
Let's trace again.
`1`: {1:1}
`2`: {1:1, 2:1}
`1`: {1:2, 2:1}
`3`: {1:1} (2 removed)
`1`: {1:2}
`2`: {1:2, 2:1}
`4`: {1:1} (2 removed)

If the output is `1 2`, then `2` must be in the map.
Maybe the stream is different? No.
Maybe the capacity is different? $k=3$ means $k-1=2$ counters.
Variant: Insert `x` with count 1. If size > $k-1$, decrement all.
Let's try that variant.
1. `1`: {1:1}
2. `2`: {1:1, 2:1}
3. `1`: {1:2, 2:1}
4. `3`: {1:2, 2:1, 3:1} -> Decr all -> {1:1, 2:0, 3:0} -> {1:1}
5. `1`: {1:2}
6. `2`: {1:2, 2:1}
7. `4`: {1:2, 2:1, 4:1} -> Decr all -> {1:1, 2:0, 4:0} -> {1:1}
Still just 1.

Let's look at the example explanation again.
"Misra-Gries keeps at most 2 counters and returns {1,2} as candidates."
Maybe the example output is just illustrative of *possible* candidates?
Or maybe $k$ counters?
If $k$ counters (capacity 3):
1. `1`: {1:1}
2. `2`: {1:1, 2:1}
3. `1`: {1:2, 2:1}
4. `3`: {1:2, 2:1, 3:1}
5. `1`: {1:3, 2:1, 3:1}
6. `2`: {1:3, 2:2, 3:1}
7. `4`: {1:3, 2:2, 3:1, 4:1} -> Decr -> {1:2, 2:1, 3:0, 4:0} -> {1:2, 2:1}
Result {1, 2}.
Aha! The problem statement says "run the Misra-Gries algorithm with `k-1` counters".
But standard Misra-Gries for parameter $k$ (threshold $1/k$) uses $k-1$ counters.
However, some definitions say "maintain $k$ counters".
If the example output is {1, 2}, it strongly suggests capacity was effectively 3 (or the logic allowed 3 items temporarily).
But the problem says "with `k-1` counters".
Let's stick to the problem statement "k-1 counters".
If my trace says {1}, and example says {1, 2}, maybe I should check if I missed something.
Frequencies: 1:3, 2:2, 3:1, 4:1.
Only 1 is > 2.33. So {1} is the only *true* heavy hitter.
{2} is a false positive.
The algorithm is allowed to return false positives.
If I use capacity $k-1=2$, I get {1}.
If I use capacity $k=3$, I get {1, 2}.
Given the explicit instruction "with `k-1` counters", I will implement that. The example output might be from a slightly different run or implementation detail (e.g., order of keys in map affecting decrement?). No, decrement affects all.
I will trust the "k-1 counters" instruction.

## ✅ Proof of Correctness

### Invariant
At any point, if we have processed $m$ items and the counters are $C$, then for any item $j$ with true frequency $f_j$, $f_j \le C[j] + D$, where $D$ is the total amount of decrements performed.
Also $D \le (m - \sum C)/k$.
This guarantees $f_j - C[j] \le m/k$.
If $f_j > m/k$, then $C[j] > 0$.

### Why the approach is correct
Standard Misra-Gries logic.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Space Saving Algorithm?
  - *Hint:* Similar to Misra-Gries but keeps the item with min count and replaces it. Better accuracy in practice.
- **Extension 2:** Distributed Heavy Hitters?
  - *Hint:* Merge summaries from multiple nodes. (Merge counters by adding).
- **Extension 3:** Weighted updates?
  - *Hint:* Generalizes naturally.

### Common Mistakes to Avoid

1. **Off-by-one**
   - ❌ Wrong: Using $k$ counters when asked for $k-1$.
   - ✅ Correct: Capacity $k-1$.
2. **Decrement Logic**
   - ❌ Wrong: Decrementing only the new item.
   - ✅ Correct: Decrement ALL items (including the virtual new one, which effectively means ignoring the new one and decrementing existing ones).

## Related Concepts

- **Majority Element:** Special case where $k=2$.
- **Frequent Directions:** Matrix sketching.
