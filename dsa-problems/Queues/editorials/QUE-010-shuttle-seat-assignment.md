---
problem_id: QUE_SHUTTLE_SEAT_ASSIGNMENT__4407
display_id: QUE-010
slug: shuttle-seat-assignment
title: "Shuttle Seat Assignment"
difficulty: Medium
difficulty_score: 46
topics:
  - Scheduling
  - Priority Queue
  - Queue
tags:
  - scheduling
  - min-heap
  - queue
  - medium
premium: true
subscription_tier: basic
---

# QUE-010: Shuttle Seat Assignment

## 📋 Problem Summary

We are given $N$ intervals `[arrival, departure)`. Each interval represents a passenger needing a seat. We need to find the minimum number of seats required to accommodate all passengers simultaneously.
- A seat is occupied from `arrival` to `departure`.
- At `departure` time, the seat becomes free.

## 🌍 Real-World Scenario

**Scenario Title:** Conference Room Booking

Imagine a co-working space with multiple meeting rooms.
- You have a list of meeting requests: `[9:00-10:00]`, `[9:30-10:30]`, `[10:00-11:00]`.
- You want to know the **minimum number of physical rooms** needed to host all meetings.
- If Meeting A ends at 10:00 and Meeting C starts at 10:00, they can share the same room.
- If Meeting A and B overlap, they need separate rooms.
- This is identical to the "Shuttle Seat" problem.

**Why This Problem Matters:**

- **Resource Allocation:** Determining hardware requirements (servers, ports, threads).
- **Logistics:** Fleet sizing for delivery trucks.

![Real-World Application](../images/QUE-010/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Interval Overlap

Intervals:
1. `[0, 5)`
2. `[4, 5)`
3. `[4, 9)`

Timeline:
```
Time: 0   1   2   3   4   5   6   7   8   9
P1:   [===================)
P2:                   [===)
P3:                   [===================)
```

- At time 0: P1 arrives. Seats: 1 (P1).
- At time 4: P2 arrives. P1 is still there. Seats: 2 (P1, P2).
- At time 4: P3 arrives. P1, P2 are there. Seats: 3?
  - Wait, P1 ends at 5. P2 ends at 5.
  - Actually, let's trace carefully.
  - P1 occupies `[0, 5)`.
  - P2 occupies `[4, 5)`.
  - P3 occupies `[4, 9)`.
  - At $t=4$, P1 is active. P2 starts. P3 starts.
  - Total overlap at $t=4$ is 3?
  - No, the example says 2. Why?
  - Ah, the input example says `0 4 4` arrivals and `5 5 9` departures.
  - P1: `0-5`. P2: `4-5`. P3: `4-9`.
  - At $t=4$, P1 is active. P2 starts. P3 starts.
  - Wait, if P2 starts at 4 and P3 starts at 4, and P1 is still there (ends at 5), then at $t=4$, all three are present.
  - Let's re-read the example explanation. "At time 4, two passengers overlap: Passenger 1 and Passenger 2... wait."
  - The example output is 2.
  - Let's check the intervals again.
  - P1: 0-5.
  - P2: 4-5.
  - P3: 4-9.
  - Maybe P2 reuses P1's seat? No, P1 ends at 5. P2 starts at 4. Overlap.
  - Maybe P3 reuses P1's seat? No, P3 starts at 4.
  - Is it possible the example explanation implies something else?
  - "Passenger 1: [0, 5), Passenger 2: [4, 5), Passenger 3: [4, 9)".
  - At $t=4$, P1 is active. P2 is active. P3 is active.
  - That requires 3 seats.
  - Why does the example say 2?
  - Let's look at the input again.
  - `0 4 4` arrivals. `5 5 9` departures.
  - Maybe the input isn't sorted? P1: `0-5`. P2: `4-5`. P3: `4-9`.
  - Is there a mistake in my understanding or the example?
  - If the output is 2, then one of them must not overlap.
  - Maybe P2 is `4-5` and P3 is `4-9`.
  - Wait, if P1 ends at 5, and P2 starts at 4. They overlap.
  - If P1 ends at 5, and P3 starts at 4. They overlap.
  - If P2 ends at 5, and P3 starts at 4. They overlap.
  - All 3 overlap at interval `[4, 5)`.
  - **Correction:** The example explanation says "At time 4, two passengers overlap".
  - This implies P3 might not be overlapping?
  - Or maybe the input pairs are different?
  - `arrivals`: `0 4 4`. `departures`: `5 5 9`.
  - Usually inputs are paired by index. P1: (0,5), P2: (4,5), P3: (4,9).
  - Unless the lists are independent? No, "list of passenger arrival and departure times".
  - Let's assume the standard "Meeting Rooms II" logic.
  - Events:
    - `(0, +1)`
    - `(4, +1)`
    - `(4, +1)`
    - `(5, -1)`
    - `(5, -1)`
    - `(9, -1)`
  - Sort events:
    - `0: +1` (cnt=1)
    - `4: +1` (cnt=2)
    - `4: +1` (cnt=3)
    - `5: -1` (cnt=2)
    - `5: -1` (cnt=1)
    - `9: -1` (cnt=0)
  - Max overlap is 3.
  - Why is the example output 2?
  - **Hypothesis:** The example input might be `0 5`, `4 5`, `4 9`? No.
  - Maybe the example explanation text "Passenger 1... Passenger 2... Passenger 3" has a typo in the intervals?
  - Let's check the provided example text again.
  - "Passenger 1: [0, 5), Passenger 2: [4, 5), Passenger 3: [4, 9)".
  - This definitely overlaps 3 deep.
  - **Wait!** Maybe the input `arrivals` and `departures` are NOT paired by index?
  - "A shuttle service has a list of passenger arrival and departure times."
  - Usually this implies `(arr[i], dep[i])`.
  - However, if the problem is "Minimum Platforms", we just sort both arrays independently.
  - If we sort arrivals: `0, 4, 4`.
  - If we sort departures: `5, 5, 9`.
  - Logic:
    - `0` arrives. Need 1.
    - `4` arrives. Need 2.
    - `4` arrives. Need 3.
    - `5` departs. Need 2.
  - Still 3.
  - Is it possible the example output is wrong in the problem description? Or maybe I'm missing a constraint like "seats can be shared if...".
  - Let's look at the image or standard problems.
  - LeetCode 253 (Meeting Rooms II).
  - Input: `[[0, 30],[5, 10],[15, 20]]`. Output: 2.
  - My trace: `0-30`, `5-10`, `15-20`.
    - `0`: +1 (1).
    - `5`: +1 (2).
    - `10`: -1 (1).
    - `15`: +1 (2).
    - `20`: -1 (1).
    - `30`: -1 (0). Max 2. Correct.
  - Back to this problem.
  - `0-5`, `4-5`, `4-9`.
  - Overlap is `[4, 5)`. All 3 are present.
  - **Maybe the example output IS 3 and the text "2" is a typo?**
  - **OR** maybe the input is `0 4 9` and `5 5 10`?
  - Let's assume the standard algorithm (Meeting Rooms II) is correct and the example might be slightly off, or I should stick to the algorithm.
  - **Wait**, let's re-read carefully. "Minimum number of seats required so that no passenger has to wait."
  - Is it possible `4` is inclusive and `5` is exclusive? Yes `[4, 5)`.
  - Is it possible `4` arrival means they arrive AT 4? Yes.
  - Is it possible `5` departure means they leave AT 5? Yes.
  - So `[4, 5)` overlaps with `[0, 5)`.
  - Okay, I will proceed with the standard "Meeting Rooms II" solution (Min Heap or Line Sweep) as it's the canonical solution for this problem type. I will note the discrepancy or assume the standard logic holds.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** Two arrays, `arrivals` and `departures`.
- **Output:** Integer (max concurrent intervals).
- **Intervals:** `[start, end)`. Start is inclusive, End is exclusive.
- **Tie-breaking:** If one arrives at X and another departs at X, process departure first (seat frees up before new one takes it).

## Naive Approach

### Intuition

For each time point where someone arrives, count how many people are currently active.

### Algorithm

1. Collect all time points.
2. For each point, check all intervals.
3. Max count is answer.

### Limitations

- **Time Complexity:** $O(N^2)$.
- With $N=100,000$, too slow.

## Optimal Approach

### Key Insight

We can process events in chronological order.
- **Arrival:** +1 seat needed.
- **Departure:** -1 seat needed.
- Sort all events. Iterate and track max `count`.

Alternatively, use a **Min-Heap** to track end times of currently occupied seats.
1. Sort intervals by start time.
2. Min-Heap stores end times of active meetings.
3. For each new meeting `[start, end)`:
   - Free up seats: Remove all elements from heap where `heap.min() <= start`.
   - Occupy seat: Add `end` to heap.
   - `max_seats = max(max_seats, heap.size())`.

### Algorithm (Min-Heap)

1. Pair `(arrival[i], departure[i])` and sort by arrival.
2. Initialize `PriorityQueue` (Min-Heap).
3. Loop through sorted intervals:
   - While `!pq.isEmpty() && pq.peek() <= current.start`: `pq.poll()`.
   - `pq.offer(current.end)`.
   - `max = Math.max(max, pq.size())`.

### Time Complexity

- **O(N log N)** due to sorting. Heap operations are also bounded by $N \log N$.

### Space Complexity

- **O(N)** for heap and storage.

![Algorithm Visualization](../images/QUE-010/algorithm-visualization.png)
![Algorithm Steps](../images/QUE-010/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int minSeats(int[] arrivals, int[] departures) {
        int n = arrivals.length;
        int[][] intervals = new int[n][2];
        for (int i = 0; i < n; i++) {
            intervals[i][0] = arrivals[i];
            intervals[i][1] = departures[i];
        }
        
        // Sort by arrival time
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        
        // Min-heap stores departure times
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int maxSeats = 0;
        
        for (int[] interval : intervals) {
            int start = interval[0];
            int end = interval[1];
            
            // Free up seats that have ended by 'start'
            while (!pq.isEmpty() && pq.peek() <= start) {
                pq.poll();
            }
            
            pq.offer(end);
            maxSeats = Math.max(maxSeats, pq.size());
        }
        
        return maxSeats;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] arrivals = new int[n];
            int[] departures = new int[n];
            for (int i = 0; i < n; i++) {
                arrivals[i] = sc.nextInt();
            }
            for (int i = 0; i < n; i++) {
                departures[i] = sc.nextInt();
            }
    
            Solution solution = new Solution();
            int result = solution.minSeats(arrivals, departures);
            System.out.println(result);
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List
import heapq
import sys

def min_seats(arrivals: List[int], departures: List[int]) -> int:
    intervals = sorted(zip(arrivals, departures))
    min_heap = [] # Stores departure times
    max_seats = 0
    
    for start, end in intervals:
        # Free up seats
        while min_heap and min_heap[0] <= start:
            heapq.heappop(min_heap)
            
        heapq.heappush(min_heap, end)
        max_seats = max(max_seats, len(min_heap))
        
    return max_seats

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        arrivals = [int(next(iterator)) for _ in range(n)]
        departures = [int(next(iterator)) for _ in range(n)]
        
        result = min_seats(arrivals, departures)
        print(result)
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

class Solution {
public:
    int minSeats(const vector<int>& arrivals, const vector<int>& departures) {
        int n = arrivals.size();
        vector<pair<int, int>> intervals(n);
        for (int i = 0; i < n; i++) {
            intervals[i] = {arrivals[i], departures[i]};
        }
        
        sort(intervals.begin(), intervals.end());
        
        priority_queue<int, vector<int>, greater<int>> pq; // Min-heap
        int maxSeats = 0;
        
        for (const auto& interval : intervals) {
            int start = interval.first;
            int end = interval.second;
            
            while (!pq.empty() && pq.top() <= start) {
                pq.pop();
            }
            
            pq.push(end);
            maxSeats = max(maxSeats, (int)pq.size());
        }
        return maxSeats;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (cin >> n) {
        vector<int> arrivals(n), departures(n);
        for (int i = 0; i < n; i++) {
            cin >> arrivals[i];
        }
        for (int i = 0; i < n; i++) {
            cin >> departures[i];
        }
    
        Solution solution;
        cout << solution.minSeats(arrivals, departures) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class MinHeap {
  constructor() {
    this.data = [];
  }
  push(val) {
    this.data.push(val);
    this.bubbleUp(this.data.length - 1);
  }
  pop() {
    if (this.data.length === 0) return null;
    const top = this.data[0];
    const bottom = this.data.pop();
    if (this.data.length > 0) {
      this.data[0] = bottom;
      this.bubbleDown(0);
    }
    return top;
  }
  peek() {
    return this.data.length > 0 ? this.data[0] : null;
  }
  size() { return this.data.length; }
  
  bubbleUp(idx) {
    while (idx > 0) {
      const p = Math.floor((idx - 1) / 2);
      if (this.data[idx] < this.data[p]) {
        [this.data[idx], this.data[p]] = [this.data[p], this.data[idx]];
        idx = p;
      } else break;
    }
  }
  bubbleDown(idx) {
    while (true) {
      const left = 2 * idx + 1;
      const right = 2 * idx + 2;
      let swap = idx;
      if (left < this.data.length && this.data[left] < this.data[swap]) swap = left;
      if (right < this.data.length && this.data[right] < this.data[swap]) swap = right;
      if (swap !== idx) {
        [this.data[idx], this.data[swap]] = [this.data[swap], this.data[idx]];
        idx = swap;
      } else break;
    }
  }
}

class Solution {
  minSeats(arrivals, departures) {
    const n = arrivals.length;
    const intervals = [];
    for (let i = 0; i < n; i++) {
      intervals.push([arrivals[i], departures[i]]);
    }
    
    intervals.sort((a, b) => a[0] - b[0]);
    
    const pq = new MinHeap();
    let maxSeats = 0;
    
    for (const [start, end] of intervals) {
      while (pq.size() > 0 && pq.peek() <= start) {
        pq.pop();
      }
      pq.push(end);
      maxSeats = Math.max(maxSeats, pq.size());
    }
    return maxSeats;
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
  const n = parseInt(data[idx++], 10);
  const arrivals = [];
  const departures = [];
  for (let i = 0; i < n; i++) {
    arrivals.push(parseInt(data[idx++], 10));
  }
  for (let i = 0; i < n; i++) {
    departures.push(parseInt(data[idx++], 10));
  }

  const solution = new Solution();
  const result = solution.minSeats(arrivals, departures);
  console.log(result);
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `0 4 4` (Arr), `5 5 9` (Dep).
Intervals: `(0,5), (4,5), (4,9)`. Sorted.

1. `(0,5)`:
   - PQ empty.
   - Push 5. PQ `[5]`. Max=1.
2. `(4,5)`:
   - Peek 5. $5 \le 4$? No.
   - Push 5. PQ `[5, 5]`. Max=2.
3. `(4,9)`:
   - Peek 5. $5 \le 4$? No.
   - Push 9. PQ `[5, 5, 9]`. Max=3.

Result: 3. (Note: The example output in problem description said 2, but standard logic yields 3. In interview, clarify if endpoints are exclusive/inclusive. If `[start, end)` and `end` is exclusive, then `5 <= 4` is false. If `end` is inclusive, still false. The only way to get 2 is if `(4,5)` reuses `(0,5)`'s seat, which implies `(0,5)` ended before 4? No. Or `(4,5)` starts AFTER `(0,5)` ends? No. The only explanation for 2 is if the input was different or "wait" implies something else.)

**Correction:** If we use the "Line Sweep" method (sort start/end independently):
Starts: `0, 4, 4`. Ends: `5, 5, 9`.
- `0`: +1 (1)
- `4`: +1 (2)
- `4`: +1 (3)
- `5`: -1 (2)
- ...
Still 3.

## ✅ Proof of Correctness

### Invariant
The Min-Heap contains the departure times of all currently active passengers. The size of the heap represents the number of seats currently occupied.

### Why the approach is correct
By processing intervals in order of arrival and removing those that have finished, we accurately simulate the timeline and track peak occupancy.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Weighted Intervals?
  - *Hint:* If each passenger needs $W$ seats? Just add $W$ to current load.
- **Extension 2:** Max $K$ seats available?
  - *Hint:* Check if `heap.size() < K`. If not, can we delay? (Different problem: Scheduling).

## Common Mistakes to Avoid

1. **Sorting only by Start**
   - ❌ Wrong: Sorting intervals but not using a heap/sweep line to track ends.
   - ✅ Correct: Must track when intervals *end* to free resources.
2. **Edge Cases**
   - ❌ Wrong: `start == end` (0 duration).
   - ✅ Correct: Logic should handle it (push then pop immediately or never push).

## Related Concepts

- **Meeting Rooms II:** The classic LeetCode equivalent.
- **Line Sweep:** Alternative $O(N \log N)$ approach.
