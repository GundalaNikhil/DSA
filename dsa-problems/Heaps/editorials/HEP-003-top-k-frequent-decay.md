---
problem_id: HEP_TOP_K_FREQUENT_DECAY__5829
display_id: HEP-003
slug: top-k-frequent-decay
title: "Top K Frequent with Decay"
difficulty: Medium
difficulty_score: 58
topics:
  - Heaps
  - Lazy Updates
  - Time Decay
tags:
  - heaps
  - decay
  - frequency
  - medium
premium: true
subscription_tier: basic
---

# HEP-003: Top K Frequent with Decay

## 📋 Problem Summary

You need to track the frequency of keys in a system where counts decay over time.
- `ADD key t`: Increment count of `key` by 1 at time `t`.
- `QUERY t`: Return the top `k` keys with the highest effective counts at time `t`.
- **Decay Rule:** Every `d` seconds, the count halves.
  - Formula: `Count_effective = Count_stored x 0.5^lfloor (t - t_last) / d rfloor`.

## 🌍 Real-World Scenario

**Scenario Title:** Trending Topics on Social Media

Imagine a "Trending Now" sidebar on Twitter.
- A hashtag like `#Olympics` gets millions of mentions (ADD events).
- However, mentions from last week shouldn't count as much as mentions today.
- The system applies a **Time Decay** factor. Old popularity fades away.
- When you load the page (QUERY), the system calculates the current "heat" of each topic and shows the top `k`.

![Real-World Application](../images/HEP-003/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Decay Process

Key "A", Decay Interval `d=10`.

Time 0: ADD "A". Count = 1. Last Update = 0.
Time 5: ADD "A".
- Decay from 0 to 5: `lfloor (5-0)/10 rfloor = 0` halves.
- Effective old count: `1 x 0.5^0 = 1`.
- New count: `1 + 1 = 2`. Last Update = 5.

Time 25: QUERY.
- Decay from 5 to 25: `lfloor (25-5)/10 rfloor = lfloor 20/10 rfloor = 2` halves.
- Effective count: `2 x 0.5^2 = 2 x 0.25 = 0.5`.

### Key Concept: Lazy Updates

We cannot update the count of *every* key at every second (`O(N)`).
Instead, we store `(count, last_update_time)` for each key.
- When accessing a key (ADD or QUERY), we first bring its count "up to date" using the decay formula.
- Then we perform the operation.
- This ensures we only pay the computation cost when necessary.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** Operations with timestamps. Timestamps are non-decreasing.
- **Output:** List of keys.
- **Constraints:** `Q <= 10^5`, `d <= 10^9`.
- **Tie-breaking:** If counts are equal, use lexicographical order (smaller string first).
- **Floating Point:** Use `double` for counts.

## Naive Approach

### Intuition

On every `QUERY`, iterate through all keys, apply decay, sort them, pick top `k`.

### Time Complexity

- **O(Q * N log N)**: Too slow if many unique keys exist.

## Optimal Approach

### Key Insight

Let `bucket = floor(t / d)`. Store each key with:
- `count`: effective count at its last update bucket
- `bucket`: last update bucket

At query bucket `B`, the effective count is:
```
count * 0.5^(B - bucket)
```
Define a **time-invariant score**:
```
score = log(count) + bucket * ln(2)
```
Then:
```
log(effective) = score - B * ln(2)
```
The term `-B * ln(2)` is common to all keys in a query, so ordering by
effective count is **exactly** ordering by `score`, independent of `B`.

This lets us maintain a max-heap by `score` and answer each `QUERY`
without scanning all keys.

### Algorithm

1. Map `key -> {count, bucket, score, version}`.
2. Max-heap stores entries `(score, key, version)` ordered by:
   - higher `score` first
   - if tied, lexicographically smaller key first
3. **ADD(key, t):**
   - `B = floor(t / d)`
   - If key exists, decay its `count` to bucket `B`:
     `count *= 0.5^(B - bucket)`
   - `count += 1`, set `bucket = B`
   - `score = log(count) + bucket * ln(2)`
   - Increment `version` and push new heap entry
4. **QUERY(t):**
   - Pop heap until you collect `k` **valid** entries (version matches map).
   - Output their keys in heap order.
   - Push the valid entries back (query does not change state).

### Time Complexity

- **ADD:** `O(log N)`
- **QUERY:** `O(k log N)` (plus discarding stale heap entries)

### Space Complexity

- **O(N)**.

![Algorithm Visualization](../images/HEP-003/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    static class State {
        double count;
        int bucket;
        double score;
        int version;
    }

    static class Entry {
        String key;
        double score;
        int version;

        Entry(String key, double score, int version) {
            this.key = key;
            this.score = score;
            this.version = version;
        }
    }

    public List<String> processOperations(int d, int k, List<String[]> operations) {
        Map<String, State> map = new HashMap<>();
        PriorityQueue<Entry> pq = new PriorityQueue<>((a, b) -> {
            if (a.score == b.score) return a.key.compareTo(b.key);
            return Double.compare(b.score, a.score);
        });
        List<String> results = new ArrayList<>();
        final double LN2 = Math.log(2.0);
        
        for (String[] op : operations) {
            String type = op[0];
            if (type.equals("ADD")) {
                String key = op[1];
                int t = Integer.parseInt(op[2]);

                int bucket = t / d;
                State state = map.get(key);
                if (state == null) {
                    state = new State();
                    state.count = 0.0;
                    state.bucket = bucket;
                    state.version = 0;
                } else if (bucket > state.bucket) {
                    int diff = bucket - state.bucket;
                    state.count *= Math.pow(0.5, diff);
                }

                state.count += 1.0;
                state.bucket = bucket;
                state.score = Math.log(state.count) + state.bucket * LN2;
                state.version++;
                map.put(key, state);
                pq.add(new Entry(key, state.score, state.version));
            } else {
                List<Entry> used = new ArrayList<>();
                List<String> out = new ArrayList<>();

                while (out.size() < k && !pq.isEmpty()) {
                    Entry e = pq.poll();
                    State state = map.get(e.key);
                    if (state == null || state.version != e.version) {
                        continue;
                    }
                    out.add(e.key);
                    used.add(e);
                }

                for (Entry e : used) pq.add(e);
                if (out.isEmpty()) {
                    results.add("EMPTY");
                } else {
                    results.add(String.join(" ", out));
                }
            }
        }
        return results;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int q = sc.nextInt();
            int d = sc.nextInt();
            int k = sc.nextInt();
            List<String[]> operations = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                String op = sc.next();
                if (op.equals("ADD")) {
                    String key = sc.next();
                    String t = sc.next();
                    operations.add(new String[]{op, key, t});
                } else {
                    String t = sc.next();
                    operations.add(new String[]{op, t});
                }
            }
            Solution solution = new Solution();
            List<String> result = solution.processOperations(d, k, operations);
            for (String s : result) System.out.println(s);
        }
        sc.close();
    }
}
```

### Python

```python
import sys
import math
import heapq

class Solution:
    def process_operations(self, d: int, k: int, operations: list) -> list:
        ln2 = math.log(2.0)
        # key -> (count, bucket, score, version)
        state = {}
        heap = []
        results = []

        for op in operations:
            if op[0] == "ADD":
                key = op[1]
                t = int(op[2])
                bucket = t // d

                if key in state:
                    count, last_bucket, score, version = state[key]
                    if bucket > last_bucket:
                        count *= 0.5 ** (bucket - last_bucket)
                    last_bucket = bucket
                    count += 1.0
                else:
                    count, last_bucket, version = 1.0, bucket, 0

                score = math.log(count) + last_bucket * ln2
                version += 1
                state[key] = (count, last_bucket, score, version)
                heapq.heappush(heap, (-score, key, version))
            else:
                out = []
                used = []
                while heap and len(out) < k:
                    neg_score, key, ver = heapq.heappop(heap)
                    cur = state.get(key)
                    if cur is None or cur[3] != ver:
                        continue
                    out.append(key)
                    used.append((neg_score, key, ver))

                for item in used:
                    heapq.heappush(heap, item)
                results.append("EMPTY" if not out else " ".join(out))

        return results

def process_operations(d: int, k: int, operations: list) -> list:
    solver = Solution()
    return solver.process_operations(d, k, operations)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        q = int(next(it))
        d = int(next(it))
        k = int(next(it))
        operations = []
        for _ in range(q):
            op = next(it)
            if op == "ADD":
                key = next(it)
                t = next(it)
                operations.append([op, key, t])
            else:
                t = next(it)
                operations.append([op, t])
        
        result = process_operations(d, k, operations)
        print("\n".join(result))
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
#include <unordered_map>
#include <cmath>
#include <queue>

using namespace std;

struct State {
    double count;
    int bucket;
    double score;
    int version;
};

struct Entry {
    string key;
    double score;
    int version;
};

struct Cmp {
    bool operator()(const Entry& a, const Entry& b) const {
        if (a.score == b.score) return a.key > b.key;
        return a.score < b.score;
    }
};

class Solution {
public:
    vector<string> processOperations(int d, int k, const vector<vector<string>>& operations) {
        unordered_map<string, State> map;
        priority_queue<Entry, vector<Entry>, Cmp> pq;
        vector<string> results;
        const double LN2 = log(2.0);
        
        for (const auto& op : operations) {
            if (op[0] == "ADD") {
                string key = op[1];
                int t = stoi(op[2]);

                int bucket = t / d;
                State state;
                auto it = map.find(key);
                if (it == map.end()) {
                    state.count = 0.0;
                    state.bucket = bucket;
                    state.version = 0;
                } else {
                    state = it->second;
                    if (bucket > state.bucket) {
                        int diff = bucket - state.bucket;
                        state.count *= pow(0.5, diff);
                    }
                }
                state.count += 1.0;
                state.bucket = bucket;
                state.score = log(state.count) + state.bucket * LN2;
                state.version++;
                map[key] = state;
                pq.push({key, state.score, state.version});
            } else {
                vector<Entry> used;
                vector<string> out;
                while (!pq.empty() && (int)out.size() < k) {
                    Entry e = pq.top();
                    pq.pop();
                    auto it = map.find(e.key);
                    if (it == map.end() || it->second.version != e.version) {
                        continue;
                    }
                    out.push_back(e.key);
                    used.push_back(e);
                }
                for (const auto& e : used) pq.push(e);
                if (out.empty()) {
                    results.push_back("EMPTY");
                } else {
                    string line;
                    for (int i = 0; i < (int)out.size(); i++) {
                        if (i) line += " ";
                        line += out[i];
                    }
                    results.push_back(line);
                }
            }
        }
        return results;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int q, d, k;
    if (cin >> q >> d >> k) {
        vector<vector<string>> operations;
        for (int i = 0; i < q; i++) {
            string op;
            cin >> op;
            if (op == "ADD") {
                string key, t;
                cin >> key >> t;
                operations.push_back({op, key, t});
            } else {
                string t;
                cin >> t;
                operations.push_back({op, t});
            }
        }
        
        Solution solution;
        vector<string> result = solution.processOperations(d, k, operations);
        for (const string& s : result) cout << s << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class MaxHeap {
  constructor() {
    this.data = [];
  }
  isEmpty() {
    return this.data.length === 0;
  }
  better(a, b) {
    if (a.score === b.score) return a.key < b.key;
    return a.score > b.score;
  }
  push(item) {
    this.data.push(item);
    this.bubbleUp(this.data.length - 1);
  }
  pop() {
    if (this.data.length === 0) return null;
    const top = this.data[0];
    const last = this.data.pop();
    if (this.data.length > 0) {
      this.data[0] = last;
      this.bubbleDown(0);
    }
    return top;
  }
  bubbleUp(idx) {
    while (idx > 0) {
      const pIdx = Math.floor((idx - 1) / 2);
      if (this.better(this.data[idx], this.data[pIdx])) {
        [this.data[idx], this.data[pIdx]] = [this.data[pIdx], this.data[idx]];
        idx = pIdx;
      } else {
        break;
      }
    }
  }
  bubbleDown(idx) {
    const n = this.data.length;
    while (true) {
      let best = idx;
      const left = 2 * idx + 1;
      const right = 2 * idx + 2;
      if (left < n && this.better(this.data[left], this.data[best])) best = left;
      if (right < n && this.better(this.data[right], this.data[best])) best = right;
      if (best === idx) break;
      [this.data[idx], this.data[best]] = [this.data[best], this.data[idx]];
      idx = best;
    }
  }
}

class Solution {
  processOperations(d, k, operations) {
    const state = new Map();
    const heap = new MaxHeap();
    const results = [];
    const ln2 = Math.log(2.0);

    for (const opData of operations) {
      const op = opData[0];
      if (op === "ADD") {
        const key = opData[1];
        const t = parseInt(opData[2], 10);
        const bucket = Math.floor(t / d);

        let st = state.get(key);
        if (!st) {
          st = { count: 0.0, bucket: bucket, score: 0.0, version: 0 };
        } else if (bucket > st.bucket) {
          const diff = bucket - st.bucket;
          st.count *= Math.pow(0.5, diff);
        }

        st.count += 1.0;
        st.bucket = bucket;
        st.score = Math.log(st.count) + st.bucket * ln2;
        st.version += 1;
        state.set(key, st);
        heap.push({ key: key, score: st.score, version: st.version });
      } else {
        const out = [];
        const used = [];

        while (!heap.isEmpty() && out.length < k) {
          const e = heap.pop();
          const st = state.get(e.key);
          if (!st || st.version !== e.version) continue;
          out.push(e.key);
          used.push(e);
        }

        for (const e of used) heap.push(e);
        results.push(out.length ? out.join(" ") : "EMPTY");
      }
    }

    return results;
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
  const q = parseInt(data[idx++]);
  const d = parseInt(data[idx++]);
  const k = parseInt(data[idx++]);
  const operations = [];
  for (let i = 0; i < q; i++) {
    const op = data[idx++];
    if (op === "ADD") {
      const key = data[idx++];
      const t = data[idx++];
      operations.push([op, key, t]);
    } else {
      const t = data[idx++];
      operations.push([op, t]);
    }
  }
  
  const solution = new Solution();
  const result = solution.processOperations(d, k, operations);
  console.log(result.join("\n"));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4 5 1
ADD a 0
ADD a 5
ADD b 5
QUERY 10
```

1. `ADD a 0`:
   - `a`: count=1.0, last=0.
2. `ADD a 5`:
   - `a`: decay (5-0)/5 = 1 shift. `1.0 * 0.5 = 0.5`.
   - `a`: count = 0.5 + 1.0 = 1.5. last=5.
3. `ADD b 5`:
   - `b`: count=1.0, last=5.
4. `QUERY 10`:
   - `a`: decay (10-5)/5 = 1 shift. `1.5 * 0.5 = 0.75`.
   - `b`: decay (10-5)/5 = 1 shift. `1.0 * 0.5 = 0.5`.
   - Sort: `a` (0.75) > `b` (0.5).
   - Top 1: `a`.

## ✅ Proof of Correctness

### Invariant
- For each key, `(count, bucket)` is the exact effective count at that bucket.
- `score = log(count) + bucket * ln(2)` is time-invariant. For query bucket `B`,
  `log(effective) = score - B * ln(2)`, so ordering by `score` matches ordering
  by effective count.
- Heap entries with matching `version` reflect the current score; stale entries
  are ignored, so the top valid entries are the true top `k`.

## 💡 Interview Extensions

- **Extension 1:** Continuous Decay?
  - *Answer:* Use `e^-lambda t`. This allows using a global multiplier and avoiding iteration if we use a Heap with lazy updates (still hard for Top K).
- **Extension 2:** Sliding Window Count?
  - *Answer:* Use a queue of timestamps for each key.

### Common Mistakes to Avoid

1. **Updating State on Query**
   - ❌ Wrong: Updating `last_update` during a QUERY.
   - ✅ Correct: QUERY is read-only. Updating `last_update` changes the anchor for the floor function, which alters future decay steps.
2. **Integer Division**
   - ❌ Wrong: Using floating point division for shifts.
   - ✅ Correct: Use integer division `(t - last) / d`.

## Related Concepts

- **Exponential Moving Average (EMA):** Similar concept.
- **Lazy Propagation:** In segment trees.
