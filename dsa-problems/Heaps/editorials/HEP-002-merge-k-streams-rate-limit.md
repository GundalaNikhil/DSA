---
problem_id: HEP_MERGE_K_STREAMS_RATE_LIMIT__9034
display_id: HEP-002
slug: merge-k-streams-rate-limit
title: "Merge K Streams with Rate Limit"
difficulty: Medium
difficulty_score: 52
topics:
  - Heaps
  - K-Way Merge
  - Streaming
tags:
  - heaps
  - k-way-merge
  - rate-limit
  - medium
premium: true
subscription_tier: basic
---

# HEP-002: Merge K Streams with Rate Limit

## 📋 Problem Summary

You have `k` sorted streams of numbers.
You need to merge them into a single sorted sequence, but with a twist:
- In each "round", a stream can contribute at most `r` elements.
- Once a stream hits this limit for the round, it's "blocked" until the next round.
- Within a round, you always pick the smallest available number from unblocked streams.
- A new round starts only when **all** streams are either blocked or empty (wait, let's re-read carefully).
  - "After a stream has contributed `r` elements in the current round, it is blocked until the next round."
  - "Within a round, always output the smallest available element among the unblocked streams."
  - Implicitly: A round ends when no stream can contribute anymore (all are blocked or empty). Then all non-empty streams unblock, and a new round begins.

## 🌍 Real-World Scenario

**Scenario Title:** Fair Bandwidth Scheduling

Imagine a network router merging packets from `k` different users.
- To prevent one heavy user from hogging the bandwidth, the router enforces a **Quota** (`r`).
- Each user can send up to `r` packets in a cycle.
- The router picks the earliest timestamped packet (smallest value) from users who haven't used up their quota yet.
- Once everyone is capped or done, the quotas reset for the next cycle.

![Real-World Application](../images/HEP-002/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Round-Robin Merging

Streams:
S1: `[1, 5, 10]`
S2: `[2, 3, 6]`
Limit `r = 1`.

**Round 1:**
- Candidates: S1(1), S2(2). Both unblocked.
- Smallest: 1 (from S1). Output `1`.
- S1 usage: 1/1. **S1 Blocked**.
- Candidates: S2(2).
- Smallest: 2 (from S2). Output `2`.
- S2 usage: 1/1. **S2 Blocked**.
- No candidates left. End Round 1.

**Round 2:** (Reset usage)
- Candidates: S1(5), S2(3).
- Smallest: 3 (from S2). Output `3`.
- S2 usage: 1/1. **S2 Blocked**.
- Candidates: S1(5).
- Smallest: 5 (from S1). Output `5`.
- S1 usage: 1/1. **S1 Blocked**.
- No candidates left. End Round 2.

**Round 3:**
- Candidates: S1(10), S2(6).
- Smallest: 6 (from S2). Output `6`.
- S2 usage: 1/1. **S2 Blocked**.
- Candidates: S1(10).
- Smallest: 10 (from S1). Output `10`.
- S1 usage: 1/1. **S1 Blocked**.

Result: `1, 2, 3, 5, 6, 10`.

### Key Concept: Min-Heap with State Tracking

We use a **Min-Heap** to store the current head of each stream.
- Heap Element: `(value, stream_index)`.
- We also maintain an array `usage[k]` to track how many elements stream `i` has output in the current round.
- **Critical Logic:**
  - When we pop `(val, i)` from heap:
    - Output `val`.
    - Increment `usage[i]`.
    - If `usage[i] < r` and stream `i` has more elements, push next element from stream `i` into heap immediately.
    - If `usage[i] == r`, **do not push** next element yet. Stream `i` is blocked for this round.
  - When heap becomes empty but streams are not exhausted:
    - **End of Round.**
    - Reset `usage` for all streams.
    - Push the next available element from every non-empty stream that was blocked (or just iterate all streams and push their current head if not already in heap).
    - Actually, simpler: Keep a separate list of "blocked streams". When heap empty, move all from blocked list to heap.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** `k` streams, limit `r`.
- **Output:** Merged list.
- **Constraints:** Total elements $N \le 200,000$. $k \le 10^5$.
- **Edge Case:** Some streams might be empty initially.

## Naive Approach

### Intuition

Simulate rounds. In each round, collect available heads, sort them, pick smallest, update.

### Time Complexity

- **O(N * k)**: If we scan all streams every step.

## Optimal Approach

### Key Insight

Use a **Min-Heap** for active streams and a **List** for blocked streams.
1. Initialize heap with first element of all streams.
2. While heap is not empty:
   - Pop min `(val, idx)`.
   - Add to result.
   - Increment `usage[idx]`.
   - If `usage[idx] < r`:
     - If stream `idx` has more, push next to heap.
   - Else (`usage[idx] == r`):
     - Add `idx` to `blocked_queue`.
   - If heap is empty and `blocked_queue` is not empty:
     - **New Round**:
     - Reset `usage` (conceptually).
     - For every `idx` in `blocked_queue`:
       - If stream `idx` has more, push next to heap.
     - Clear `blocked_queue`.

### Algorithm

1. `minHeap` stores `(value, stream_index)`.
2. `blocked` list stores indices of streams that hit limit `r`.
3. `usage` array (or map) tracks count for current round. Actually, since we reset every round, we can just reset the array or use a generation counter. Since we process blocked queue explicitly, we effectively reset usage for those streams.
   - Wait, `usage` needs to track count *within* round.
   - When a stream comes back from `blocked`, its usage is 0.
   - When a stream stays in heap, its usage increments.
   - So, we can store `(value, stream_index, current_round_usage)` in heap? No, usage is per stream.
   - Just `usage[stream_index]` is fine. Reset it when moving from blocked to heap?
   - Yes: When moving `idx` from `blocked` to `heap`, set `usage[idx] = 0`.
   - What about streams that didn't hit limit but round ended?
     - "Round ends when heap is empty". This implies *all* active streams hit limit or ran out.
     - So *every* stream in the next round starts fresh.
     - Correct.

### Time Complexity

- **O(N log k)**.

### Space Complexity

- **O(k)**.

![Algorithm Visualization](../images/HEP-002/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    static class Element implements Comparable<Element> {
        int val;
        int streamIdx;
        
        public Element(int val, int streamIdx) {
            this.val = val;
            this.streamIdx = streamIdx;
        }
        
        @Override
        public int compareTo(Element other) {
            return Integer.compare(this.val, other.val);
        }
    }
    
    public List<Integer> mergeStreams(List<List<Integer>> streams, int r) {
        PriorityQueue<Element> pq = new PriorityQueue<>();
        int k = streams.size();
        int[] indices = new int[k]; // Current index in each stream
        int[] usage = new int[k];   // Usage in current round
        
        // Initial population
        for (int i = 0; i < k; i++) {
            if (!streams.get(i).isEmpty()) {
                pq.offer(new Element(streams.get(i).get(0), i));
                indices[i]++;
            }
        }
        
        List<Integer> result = new ArrayList<>();
        List<Integer> blocked = new ArrayList<>();
        
        while (!pq.isEmpty()) {
            Element curr = pq.poll();
            result.add(curr.val);
            
            int sIdx = curr.streamIdx;
            usage[sIdx]++;
            
            if (usage[sIdx] < r) {
                // Can still contribute to this round
                if (indices[sIdx] < streams.get(sIdx).size()) {
                    pq.offer(new Element(streams.get(sIdx).get(indices[sIdx]), sIdx));
                    indices[sIdx]++;
                }
            } else {
                // Blocked for this round
                blocked.add(sIdx);
            }
            
            // End of round check
            if (pq.isEmpty() && !blocked.isEmpty()) {
                // Start new round
                for (int idx : blocked) {
                    usage[idx] = 0; // Reset usage
                    if (indices[idx] < streams.get(idx).size()) {
                        pq.offer(new Element(streams.get(idx).get(indices[idx]), idx));
                        indices[idx]++;
                    }
                }
                blocked.clear();
            }
        }
        
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int k = sc.nextInt();
            int r = sc.nextInt();
            List<List<Integer>> streams = new ArrayList<>();
            for (int i = 0; i < k; i++) {
                int m = sc.nextInt();
                List<Integer> stream = new ArrayList<>();
                for (int j = 0; j < m; j++) {
                    stream.add(sc.nextInt());
                }
                streams.add(stream);
            }
            
            Solution solution = new Solution();
            List<Integer> result = solution.mergeStreams(streams, r);
            for (int i = 0; i < result.size(); i++) {
                System.out.print(result.get(i));
                if (i < result.size() - 1) System.out.print(" ");
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
import heapq

class Solution:
    def merge_streams(self, streams: list, r: int) -> list:
        k = len(streams)
        indices = [0] * k
        usage = [0] * k
        
        # Min-heap stores (value, stream_index)
        pq = []
        
        # Initial population
        for i in range(k):
            if streams[i]:
                heapq.heappush(pq, (streams[i][0], i))
                indices[i] += 1
                
        result = []
        blocked = []
        
        while pq:
            val, s_idx = heapq.heappop(pq)
            result.append(val)
            
            usage[s_idx] += 1
            
            if usage[s_idx] < r:
                # Still active in round
                if indices[s_idx] < len(streams[s_idx]):
                    next_val = streams[s_idx][indices[s_idx]]
                    heapq.heappush(pq, (next_val, s_idx))
                    indices[s_idx] += 1
            else:
                # Blocked
                blocked.append(s_idx)
                
            # Check if round ended
            if not pq and blocked:
                # Start new round
                for idx in blocked:
                    usage[idx] = 0
                    if indices[idx] < len(streams[idx]):
                        next_val = streams[idx][indices[idx]]
                        heapq.heappush(pq, (next_val, idx))
                        indices[idx] += 1
                blocked = []
                
        return result

def merge_streams(streams: list, r: int) -> list:
    solver = Solution()
    return solver.merge_streams(streams, r)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        k = int(next(it))
        r = int(next(it))
        streams = []
        for _ in range(k):
            m = int(next(it))
            stream = []
            for _ in range(m):
                stream.append(int(next(it)))
            streams.append(stream)
            
        result = merge_streams(streams, r)
        print(" ".join(map(str, result)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> mergeStreams(const vector<vector<int>>& streams, int r) {
        int k = streams.size();
        vector<int> indices(k, 0);
        vector<int> usage(k, 0);
        
        // Min-heap: {value, stream_index}
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        
        for (int i = 0; i < k; i++) {
            if (!streams[i].empty()) {
                pq.push({streams[i][0], i});
                indices[i]++;
            }
        }
        
        vector<int> result;
        vector<int> blocked;
        
        while (!pq.empty()) {
            auto [val, sIdx] = pq.top();
            pq.pop();
            result.push_back(val);
            
            usage[sIdx]++;
            
            if (usage[sIdx] < r) {
                if (indices[sIdx] < streams[sIdx].size()) {
                    pq.push({streams[sIdx][indices[sIdx]], sIdx});
                    indices[sIdx]++;
                }
            } else {
                blocked.push_back(sIdx);
            }
            
            if (pq.empty() && !blocked.empty()) {
                for (int idx : blocked) {
                    usage[idx] = 0;
                    if (indices[idx] < streams[idx].size()) {
                        pq.push({streams[idx][indices[idx]], idx});
                        indices[idx]++;
                    }
                }
                blocked.clear();
            }
        }
        
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int k, r;
    if (cin >> k >> r) {
        vector<vector<int>> streams(k);
        for (int i = 0; i < k; i++) {
            int m;
            cin >> m;
            streams[i].resize(m);
            for (int j = 0; j < m; j++) {
                cin >> streams[i][j];
            }
        }
        
        Solution solution;
        vector<int> result = solution.mergeStreams(streams, r);
        for (size_t i = 0; i < result.size(); i++) {
            if (i > 0) cout << " ";
            cout << result[i];
        }
        cout << "\n";
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
  mergeStreams(streams, r) {
    const k = streams.length;
    const indices = new Array(k).fill(0);
    const usage = new Array(k).fill(0);
    
    // Min heap: {val, idx}
    const pq = new PriorityQueue((a, b) => a.val - b.val);
    
    for (let i = 0; i < k; i++) {
      if (streams[i].length > 0) {
        pq.push({ val: streams[i][0], idx: i });
        indices[i]++;
      }
    }
    
    const result = [];
    let blocked = [];
    
    while (!pq.isEmpty()) {
      const { val, idx } = pq.pop();
      result.push(val);
      
      usage[idx]++;
      
      if (usage[idx] < r) {
        if (indices[idx] < streams[idx].length) {
          pq.push({ val: streams[idx][indices[idx]], idx: idx });
          indices[idx]++;
        }
      } else {
        blocked.push(idx);
      }
      
      if (pq.isEmpty() && blocked.length > 0) {
        for (const bIdx of blocked) {
          usage[bIdx] = 0;
          if (indices[bIdx] < streams[bIdx].length) {
            pq.push({ val: streams[bIdx][indices[bIdx]], idx: bIdx });
            indices[bIdx]++;
          }
        }
        blocked = [];
      }
    }
    
    return result;
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
  const k = parseInt(data[idx++]);
  const r = parseInt(data[idx++]);
  const streams = [];
  for (let i = 0; i < k; i++) {
    const m = parseInt(data[idx++]);
    const stream = [];
    for (let j = 0; j < m; j++) {
      stream.push(parseInt(data[idx++]));
    }
    streams.push(stream);
  }
  
  const solution = new Solution();
  const result = solution.mergeStreams(streams, r);
  console.log(result.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:** `k=2, r=1`. S1: `[1, 4]`, S2: `[2, 3, 5]`.

**Init:** Heap: `{(1, S1), (2, S2)}`. Blocked: `[]`.

**Step 1:** Pop `(1, S1)`. Res: `[1]`.
- Usage S1: 1. Limit reached.
- Blocked: `[S1]`. Heap: `{(2, S2)}`.

**Step 2:** Pop `(2, S2)`. Res: `[1, 2]`.
- Usage S2: 1. Limit reached.
- Blocked: `[S1, S2]`. Heap: `{}`.

**Round End:** Heap empty. Blocked `[S1, S2]`.
- Reset usage.
- S1 next: `4`. Push `(4, S1)`.
- S2 next: `3`. Push `(3, S2)`.
- Heap: `{(3, S2), (4, S1)}`. Blocked: `[]`.

**Step 3:** Pop `(3, S2)`. Res: `[1, 2, 3]`.
- Usage S2: 1. Blocked: `[S2]`. Heap: `{(4, S1)}`.

**Step 4:** Pop `(4, S1)`. Res: `[1, 2, 3, 4]`.
- Usage S1: 1. Blocked: `[S2, S1]`. Heap: `{}`.

**Round End:** Heap empty. Blocked `[S2, S1]`.
- S2 next: `5`. Push `(5, S2)`.
- S1 next: None.
- Heap: `{(5, S2)}`.

**Step 5:** Pop `(5, S2)`. Res: `[1, 2, 3, 4, 5]`.
- Usage S2: 1. Blocked: `[S2]`. Heap: `{}`.

**Round End:** Heap empty. Blocked `[S2]`.
- S2 next: None.
- Heap: `{}`. Blocked: `[]`.

**Finish.**

## ✅ Proof of Correctness

### Invariant
- The heap always contains the smallest available element from every *unblocked* stream.
- By picking the min from the heap, we satisfy the "smallest available" condition.
- The blocking mechanism strictly enforces the rate limit `r`.
- The round reset mechanism ensures fairness cycles.

## 💡 Interview Extensions

- **Extension 1:** Weighted Round Robin?
  - *Answer:* Give each stream a different `r_i`.
- **Extension 2:** Infinite Streams?
  - *Answer:* Generator-based approach, yield one by one.

## Common Mistakes to Avoid

1. **Premature Round Reset**
   - ❌ Wrong: Resetting when *any* stream gets blocked.
   - ✅ Correct: Reset only when *all* active streams are blocked (heap empty).
2. **Usage Counter**
   - ❌ Wrong: Forgetting to reset usage counters.
   - ✅ Correct: Reset to 0 at the start of each new round.

## Related Concepts

- **K-Way Merge:** Standard algorithm (Merge Sort).
- **Leaky Bucket:** Rate limiting algorithm.
