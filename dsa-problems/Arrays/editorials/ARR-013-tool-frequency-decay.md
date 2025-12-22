---
problem_id: ARR_FREQ_DECAY__E31B
display_id: ARR-013
slug: tool-frequency-decay
title: "Tool Frequency Top K with Recency Decay"
difficulty: Medium
difficulty_score: 50
topics:
  - Array
  - Hash Map
  - Sorting
  - Mathematics
  - Exponential Decay
tags:
  - arrays
  - hashmap
  - sorting
  - medium
premium: true
subscription_tier: basic
---

# Tool Frequency Top K with Recency Decay

![Problem Header](../images/ARR-013/header.png)

---

## Problem Summary

Find top K values based on frequency with exponential time decay - recent occurrences count more than old ones.

## Real-World Scenario

Imagine you're building an IDE's autocomplete feature that suggests the most relevant tools/functions. Recent usage should count more than old usage (yesterday's work is more relevant than last month's). Each time a tool is used, it gets a "decayed score" based on how long ago it was used. The formula `e^(-Δt/D)` gives higher weight to recent events and lower weight to old events, where D controls decay speed.

---

## Detailed Explanation

### Why Exponential Decay?

**Problem with simple frequency**:

- Tool A: used 100 times (all 6 months ago)
- Tool B: used 50 times (all this week)
- Simple count: A wins, but B is actually more relevant!

**Exponential decay solution**:

- Recent events get score ≈ 1.0
- Old events get score ≈ 0.0
- Formula: `score = e^(-(now - timestamp) / D)`

where:

- `now` = current time
- `timestamp` = when event occurred
- `D` = decay constant (controls how fast scores decrease)

### Decay Examples

```
If D = 10:
  Δt = 0:  score = e^0 = 1.00    (just happened!)
  Δt = 5:  score = e^-0.5 ≈ 0.61
  Δt = 10: score = e^-1 ≈ 0.37    (half-life ish)
  Δt = 20: score = e^-2 ≈ 0.14
  Δt = 50: score = e^-5 ≈ 0.007   (ancient history)
```

---

## Approach 1: Naive Solution

### Idea

For each unique value, iterate through ALL events to compute its total decayed score, then sort.

```
for each unique value v:
    score = 0
    for each event:
        if event.value == v:
            score += exp(-(now - event.time) / D)
    store (v, score)
sort by score descending
return top K
```

### Why is this inefficient?

For each of V unique values, we scan all E events → O(V × E)
Then sort V values → O(V log V)
Total: **O(V × E + V log V)** ≈ **O(E²)** when V ≈ E

### Complexity Analysis

**Time Complexity**: O(E² + E log E) where E is number of events

- **Why?** If every event has a unique value, V = E, so V × E = E²
- Sorting adds O(E log E)

**Space Complexity**: O(V) where V is distinct values

- Storing score for each unique value

---

## Approach 2: Optimal Solution ⭐

### Key Insight

Process events **once** in a single pass! For each event, immediately add its decayed score to the value's total.

Instead of:

```
For each value → scan all events → compute score
```

Do:

```
For each event → compute decay → add to value's running score
```

This is just **rearranging the order of iteration**!

### Algorithm

1. Create hash map: `value → totalScore`
2. For each event `(value, timestamp)`:
   - Compute `decay = e^(-(now - timestamp) / D)`
   - Add decay to `scores[value]`
3. Convert map to list of (value, score) pairs
4. Sort by score (descending), then by value (ascending) for ties
5. Return first K values

### Complexity Analysis

**Time Complexity**: O(E + V log V)

- **Why?** Process E events once (O(E)), then sort V unique values (O(V log V))
- **Typical case**: V << E (many repeated values), so dominated by O(E)

**Space Complexity**: O(V)

- Hash map stores one entry per unique value

---

## Visual Representation

### Example: Find Top 2 Tools

```
Events: [(tool=5, time=10), (tool=3, time=15), (tool=5, time=18), (tool=3, time=20)]
Now = 25, D = 10

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Event 1: tool=5, time=10
  Δt = 25 - 10 = 15
  decay = e^(-15/10) = e^(-1.5) ≈ 0.223
  scores[5] = 0.223

Event 2: tool=3, time=15
  Δt = 25 - 15 = 10
  decay = e^(-10/10) = e^(-1) ≈ 0.368
  scores[3] = 0.368

Event 3: tool=5, time=18
  Δt = 25 - 18 = 7
  decay = e^(-7/10) = e^(-0.7) ≈ 0.497
  scores[5] = 0.223 + 0.497 = 0.720

Event 4: tool=3, time=20
  Δt = 25 - 20 = 5
  decay = e^(-5/10) = e^(-0.5) ≈ 0.607
  scores[3] = 0.368 + 0.607 = 0.975

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Final Scores:
  tool 3: 0.975 ← Winner! (more recent usage)
  tool 5: 0.720

Top 2: [3, 5]
```

### Decay Visualization

```
Time axis (now = 25):
─────────────────────────────────────────────────────→
0    5    10   15   20   25

Tool 5: ●────────────●───────
       t=10          t=18
       old (0.223)   newer (0.497)
       Total: 0.720

Tool 3:         ●──────────●
               t=15       t=20
               (0.368)    recent! (0.607)
               Total: 0.975 ← Higher score!

Decay curves (e^(-Δt/10)):
1.0 |●
0.8 | ●
0.6 |  ●  ●
0.4 |   ●   ●
0.2 |    ●●   ●●
0.0 |________________●___________
    0  5  10  15  20  25  30
       Δt (time ago)
```

---

## Test Case Walkthrough

### Input:

```
events = [[7,1], [7,3], [3,5], [3,6], [7,8]]
now = 10, D = 5, k = 2
```

```
Step-by-step:

Event: [7, 1]
  Δt = 10-1 = 9
  decay = e^(-9/5) = e^(-1.8) ≈ 0.165
  scores = {7: 0.165}

Event: [7, 3]
  Δt = 10-3 = 7
  decay = e^(-7/5) = e^(-1.4) ≈ 0.247
  scores = {7: 0.165 + 0.247 = 0.412}

Event: [3, 5]
  Δt = 10-5 = 5
  decay = e^(-5/5) = e^(-1) ≈ 0.368
  scores = {7: 0.412, 3: 0.368}

Event: [3, 6]
  Δt = 10-6 = 4
  decay = e^(-4/5) = e^(-0.8) ≈ 0.449
  scores = {7: 0.412, 3: 0.368 + 0.449 = 0.817}

Event: [7, 8]
  Δt = 10-8 = 2
  decay = e^(-2/5) = e^(-0.4) ≈ 0.670
  scores = {7: 0.412 + 0.670 = 1.082, 3: 0.817}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Final Scores:
  7: 1.082 ← Most recent/frequent
  3: 0.817

Sorted (desc by score): [(7, 1.082), (3, 0.817)]
Top 2: [7, 3]
```

---

### Common Mistakes & Pitfalls

### 1. Recomputing Decay Multiple Times ⚠️

- ❌ For each value, loop through all events again
- ✅ Compute decay once per event and add to running total

### 2. Wrong Sort Order ⚠️

- ❌ Sorting by value instead of score
- ❌ Sorting ascending instead of descending
- ✅ Sort by score (descending), then value (ascending) for ties

### 3. Forgetting Tie-Breaking ⚠️

- ❌ When two values have same score, arbitrary order
- ✅ Use value itself as tiebreaker (smaller value first)

### 4. Mathematical Errors ⚠️

- ❌ Using `exp((now - timestamp) / D)` (positive exponent - grows!)
- ✅ Use `exp(-(now - timestamp) / D)` (negative exponent - decays!)

### 5. Integer Division ⚠️

- ❌ Using integer division: `-(now - timestamp) / D` in some languages
- ✅ Ensure floating-point division: `-(double)(now - timestamp) / D`

### 6. Not Handling K > Unique Values ⚠️

- ❌ Assuming K values always exist
- ✅ Return `min(k, scores.size())` values

---

## Implementations

### Java

```java
class Solution {
    public int[] topKWithDecay(int[][] values, int now, int D, int k) {
        Map<Integer, Double> scores = new HashMap<>();

        // Compute decayed score for each event
        for (int[] event : values) {
            int val = event[0];
            int timestamp = event[1];
            double decay = Math.exp(-(double)(now - timestamp) / D);
            scores.put(val, scores.getOrDefault(val, 0.0) + decay);
        }

        // Convert to list and sort
        List<Map.Entry<Integer, Double>> entries = new ArrayList<>(scores.entrySet());
        entries.sort((a, b) -> {
            // First by score (descending)
            int cmp = Double.compare(b.getValue(), a.getValue());
            if (cmp != 0) return cmp;
            // Then by value (ascending) for ties
            return Integer.compare(a.getKey(), b.getKey());
        });

        // Extract top k values
        int[] result = new int[Math.min(k, entries.size())];
        for (int i = 0; i < result.length; i++) {
            result[i] = entries.get(i).getKey();
        }

        return result;
    }
}
```

### Python

```python
import math

def top_k_with_decay(values, now, D, k):
    scores = {}

    # Compute decayed score for each event
    for val, timestamp in values:
        decay = math.exp(-(now - timestamp) / D)
        scores[val] = scores.get(val, 0.0) + decay

    # Sort by score (descending), then by value (ascending)
    sorted_values = sorted(scores.items(), key=lambda x: (-x[1], x[0]))

    # Return top k values
    return [val for val, _ in sorted_values[:k]]
```

### C++

```cpp
class Solution {
public:
    vector<int> topKWithDecay(vector<vector<int>>& values, int now, int D, int k) {
        unordered_map<int, double> scores;

        // Compute decayed score for each event
        for (auto& event : values) {
            int val = event[0];
            int timestamp = event[1];
            double decay = exp(-(double)(now - timestamp) / D);
            scores[val] += decay;
        }

        // Convert to vector and sort
        vector<pair<int, double>> entries(scores.begin(), scores.end());
        sort(entries.begin(), entries.end(), [](const auto& a, const auto& b) {
            // First by score (descending)
            if (abs(a.second - b.second) > 1e-9) {
                return a.second > b.second;
            }
            // Then by value (ascending) for ties
            return a.first < b.first;
        });

        // Extract top k values
        vector<int> result;
        for (int i = 0; i < min(k, (int)entries.size()); i++) {
            result.push_back(entries[i].first);
        }

        return result;
    }
};
```

### JavaScript

```javascript
/**
 * @param {number[][]} values
 * @param {number} now
 * @param {number} D
 * @param {number} k
 * @return {number[]}
 */
var topKWithDecay = function(values, now, D, k) {
    const scores = new Map();

    // Compute decayed score for each event
    for (const [val, timestamp] of values) {
        const decay = Math.exp(-(now - timestamp) / D);
        scores.set(val, (scores.get(val) || 0) + decay);
    }

    // Convert to array and sort
    const entries = Array.from(scores.entries());
    entries.sort((a, b) => {
        // First by score (descending)
        if (Math.abs(a[1] - b[1]) > 1e-9) {
            return b[1] - a[1];
        }
        // Then by value (ascending) for ties
        return a[0] - b[0];
    });

    // Extract top k values
    const result = [];
    for (let i = 0; i < Math.min(k, entries.length); i++) {
        result.push(entries[i][0]);
    }

    return result;
};

// Time: O(E + V log V), Space: O(V)
```

---

## Quick Comparison Table

| Aspect              | Naive O(E²)      | Optimal O(E + V log V) |
| ------------------- | ---------------- | ---------------------- |
| For E=1000, V=100   | ~1,000,000 ops   | ~1,700 ops             |
| For E=10000, V=1000 | ~100,000,000 ops | ~20,000 ops            |
| Space               | O(V)             | O(V)                   |
| Decay computations  | V × E times      | E times                |
| Sorting             | O(V log V)       | O(V log V)             |
| Typical performance | Very slow        | Fast                   |

---
