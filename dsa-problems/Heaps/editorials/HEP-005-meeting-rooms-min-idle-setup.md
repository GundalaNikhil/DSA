---
problem_id: HEP_MEETING_ROOMS_MIN_IDLE_SETUP__3108
display_id: HEP-005
slug: meeting-rooms-min-idle-setup
title: "Meeting Rooms Min Idle with Setup Time"
difficulty: Medium
difficulty_score: 54
topics:
  - Heaps
  - Scheduling
  - Intervals
tags:
  - heaps
  - scheduling
  - intervals
  - medium
premium: true
subscription_tier: basic
---

# HEP-005: Meeting Rooms Min Idle with Setup Time

## 📋 Problem Summary

You have `k` rooms and `n` meetings. Each meeting has a start and end time.
After a meeting ends, a room needs `s` setup time.
If a room finishes meeting `i` at `end_i`, it is ready at `end_i + s`.
If it takes meeting `j` starting at `start_j`, the **slack** is `start_j - (end_i + s)`.
Goal: Assign meetings to rooms to minimize total slack.
Input guarantees a valid schedule exists.

## 🌍 Real-World Scenario

**Scenario Title:** Conference Center Optimization

You manage a conference center with `k` halls.
- Between events, cleaning crews need `s` minutes to prep the room.
- If a room sits empty after cleaning, that's wasted potential (slack).
- You want to schedule events such that rooms are "back-to-back" as much as possible to maximize efficiency (or minimize idle time).

![Real-World Application](../images/HEP-005/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Slack Calculation

Room 1 Timeline:
`[Meeting A: 0-10] --Setup(1)-- [Ready at 11] ....... [Meeting B: 15-20]`

Slack = Start(B) - Ready(A) = 15 - 11 = 4.

If we assigned Meeting C (12-14) instead:
`[Meeting A: 0-10] --Setup(1)-- [Ready at 11] . [Meeting C: 12-14]`
Slack = 12 - 11 = 1. Better!

### Key Concept: Best-Fit Strategy

We process meetings in order of their **start times**.
For the current meeting starting at `T_start`, we need a room that is free by `T_start`.
Among all rooms free `<= T_start`, which one should we pick?
- To minimize slack (`T_start - T_free`), we should pick the room with the **largest** `T_free` that is still `<= T_start`.
- This is a "Best Fit" strategy. We want the "tightest" fit.

Why largest `T_free`?
- Suppose rooms are free at 5, 8, 10. Meeting starts at 12.
- Slacks: `12-5=7`, `12-8=4`, `12-10=2`.
- Picking 10 gives min slack.
- Also, picking 10 leaves 5 and 8 available for potential earlier meetings (though we process by start time, so future meetings start `>= 12`).
- So, picking the latest possible valid room is locally and globally optimal.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** Meetings list, `k`, `s`.
- **Output:** Total slack.
- **Constraints:** `N <= 10^5`, `K <= N`.
- **Guarantee:** A valid schedule exists (so we don't need to check if `K` is sufficient, just optimize assignment).

## Naive Approach

### Intuition

For each meeting, iterate all `K` rooms to find the best one.

### Time Complexity

- **O(N * K)**: Slow if `K` is large.

## Optimal Approach

### Key Insight

We need to efficiently query: "Find max `T_free <= T_start`" among rooms that have already hosted a meeting.
We track:
- **Used rooms**: a multiset of their next free times.
- **Unused rooms**: a counter. The first meeting in a room has **0 slack** by definition.

For each meeting in start-time order:
- If a used room is free by `start`, assign the meeting to the used room with the **latest** free time (minimizes this meeting's slack).
- Otherwise, open a new room (if any unused remain) and add **0 slack**.

Then update that room's next free time to `end + s`.

### Algorithm

1. Sort meetings by start time.
2. Initialize a Multiset for **used** rooms (empty) and `unused = k`.
3. `totalSlack = 0`.
4. For each meeting `[start, end]`:
   - Find `roomEnd` = largest value in Multiset `<= start`.
   - If found, `slack = start - roomEnd`, remove `roomEnd`.
   - If not found, use an unused room (`unused--`) and add `slack = 0`.
   - Insert `end + s` into Multiset (room is now used).
5. Return `totalSlack`.

### Time Complexity

- **O(N log K)**: Sorting + Multiset operations.

### Space Complexity

- **O(K)**: Multiset size.

![Algorithm Visualization](../images/HEP-005/algorithm-visualization.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    public long minTotalSlack(int[][] meetings, int k, int s) {
        Arrays.sort(meetings, (a, b) -> Integer.compare(a[0], b[0]));
        
        // TreeMap to store <FreeTime, Count> for rooms already used
        TreeMap<Integer, Integer> rooms = new TreeMap<>();
        int unused = k;
        
        long totalSlack = 0;
        
        for (int[] meeting : meetings) {
            int start = meeting[0];
            int end = meeting[1];
            
            // Find largest free time <= start among used rooms
            Map.Entry<Integer, Integer> entry = rooms.floorEntry(start);

            if (entry != null) {
                int freeTime = entry.getKey();
                int count = entry.getValue();
                
                totalSlack += (long)(start - freeTime);
                
                if (count == 1) rooms.remove(freeTime);
                else rooms.put(freeTime, count - 1);
                
            } else {
                // Use a fresh room; first meeting in a room has 0 slack.
                // Valid schedule is guaranteed, so unused > 0 here.
                unused--;
            }

            int nextFree = end + s;
            rooms.put(nextFree, rooms.getOrDefault(nextFree, 0) + 1);
        }
        
        return totalSlack;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            int s = sc.nextInt();
            int[][] meetings = new int[n][2];
            for (int i = 0; i < n; i++) {
                meetings[i][0] = sc.nextInt();
                meetings[i][1] = sc.nextInt();
            }
            
            Solution solution = new Solution();
            System.out.println(solution.minTotalSlack(meetings, k, s));
        }
        sc.close();
    }
}
```

### Python
```python
import sys
from bisect import bisect_right

class Solution:
    def min_total_slack(self, meetings: list, k: int, s: int) -> int:
        meetings.sort(key=lambda x: x[0])
        unused = k

        # Coordinate-compress possible free times (end + s).
        coords = sorted({end + s for _, end in meetings})
        rank = {val: i for i, val in enumerate(coords)}
        n = len(coords)
        tree = [0] * (4 * n)

        def update(node, left, right, idx, delta):
            if left == right:
                tree[node] += delta
                return
            mid = (left + right) // 2
            if idx <= mid:
                update(node * 2, left, mid, idx, delta)
            else:
                update(node * 2 + 1, mid + 1, right, idx, delta)
            tree[node] = tree[node * 2] + tree[node * 2 + 1]

        def query_rightmost(node, left, right, r_limit):
            if left > r_limit or tree[node] == 0:
                return -1
            if left == right:
                return left
            mid = (left + right) // 2
            res = query_rightmost(node * 2 + 1, mid + 1, right, r_limit)
            if res != -1:
                return res
            return query_rightmost(node * 2, left, mid, r_limit)

        total_slack = 0
        for start, end in meetings:
            idx = bisect_right(coords, start) - 1
            best_rank = -1
            if idx >= 0:
                best_rank = query_rightmost(1, 0, n - 1, idx)

            if best_rank != -1:
                free_time = coords[best_rank]
                total_slack += start - free_time
                update(1, 0, n - 1, best_rank, -1)
            else:
                # Use a fresh room; first meeting in a room has 0 slack.
                unused -= 1

            update(1, 0, n - 1, rank[end + s], 1)

        return total_slack

def min_total_slack(meetings: list, k: int, s: int) -> int:
    solver = Solution()
    return solver.min_total_slack(meetings, k, s)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        k = int(next(it))
        s = int(next(it))
        meetings = []
        for _ in range(n):
            start = int(next(it))
            end = int(next(it))
            meetings.append([start, end])
        
        result = min_total_slack(meetings, k, s)
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
#include <map>

using namespace std;

class Solution {
public:
    long long minTotalSlack(vector<vector<int>>& meetings, int k, int s) {
        sort(meetings.begin(), meetings.end());
        
        map<int, int> rooms;
        int usedRooms = 0;
        
        long long totalSlack = 0;
        
        for (const auto& m : meetings) {
            int start = m[0];
            int end = m[1];
            
            auto it = rooms.upper_bound(start);
            if (it != rooms.begin()) {
                it--;
                int freeTime = it->first;
                totalSlack += (long long)(start - freeTime);
                
                if (it->second == 1) rooms.erase(it);
                else it->second--;
                
                rooms[end + s]++;
            } else {
                if (usedRooms < k) {
                    usedRooms++;
                    rooms[end + s]++;
                } else {
                    // Should not happen if k is sufficient as per problem constraints/guarantees?
                    // Or maybe we treat it as infinite slack/invalid? The problem implies K is sufficient.
                }
            }
        }
        
        return totalSlack;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, k, s;
    if (cin >> n >> k >> s) {
        vector<vector<int>> meetings(n, vector<int>(2));
        for (int i = 0; i < n; i++) {
            cin >> meetings[i][0] >> meetings[i][1];
        }
        
        Solution solution;
        cout << solution.minTotalSlack(meetings, k, s) << "\n";
    }
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

// Simple BST / TreeMap implementation for JS
class TreeMap {
  constructor() {
    // Sorted array + counts map for used rooms.
    this.keys = [];
    this.counts = {};
  }
  
  // Find largest key <= val
  floorKey(val) {
    if (this.keys.length === 0) return null;
    let l = 0, r = this.keys.length - 1;
    let res = null;
    while (l <= r) {
      const mid = Math.floor((l + r) / 2);
      if (this.keys[mid] <= val) {
        res = this.keys[mid];
        l = mid + 1;
      } else {
        r = mid - 1;
      }
    }
    return res;
  }
  
  removeOne(key) {
    if (this.counts[key] > 1) {
      this.counts[key]--;
    } else {
      delete this.counts[key];
      // Remove from keys array
      // Binary search to find index
      let l = 0, r = this.keys.length - 1;
      while (l <= r) {
        const mid = Math.floor((l + r) / 2);
        if (this.keys[mid] === key) {
          this.keys.splice(mid, 1);
          return;
        } else if (this.keys[mid] < key) {
          l = mid + 1;
        } else {
          r = mid - 1;
        }
      }
    }
  }
  
  addOne(key) {
    if (this.counts[key]) {
      this.counts[key]++;
    } else {
      this.counts[key] = 1;
      // Insert into keys array sorted
      // Find index
      let l = 0, r = this.keys.length - 1;
      let idx = this.keys.length;
      while (l <= r) {
        const mid = Math.floor((l + r) / 2);
        if (this.keys[mid] < key) {
          l = mid + 1;
        } else {
          idx = mid;
          r = mid - 1;
        }
      }
      this.keys.splice(idx, 0, key);
    }
  }
}

class Solution {
  minTotalSlack(meetings, k, s) {
    meetings.sort((a, b) => a[0] - b[0]);
    
    const rooms = new TreeMap();
    let unused = k;
    
    let totalSlack = 0n;
    
    for (const [start, end] of meetings) {
      const freeTime = rooms.floorKey(start);
      
      if (freeTime !== null) {
        totalSlack += BigInt(start - freeTime);
        rooms.removeOne(freeTime);
      } else {
        // Use a fresh room; first meeting in a room has 0 slack.
        unused--;
      }

      rooms.addOne(end + s);
    }
    
    return totalSlack.toString();
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
  const s = parseInt(data[idx++]);
  const meetings = [];
  for (let i = 0; i < n; i++) {
    const start = parseInt(data[idx++]);
    const end = parseInt(data[idx++]);
    meetings.push([start, end]);
  }
  
  const solution = new Solution();
  console.log(solution.minTotalSlack(meetings, k, s));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:** `3 2 1`. Meetings: `[0,10], [5,8], [13,20]`.
Sorted: `[0,10], [5,8], [13,20]`.

1. **Meeting [0,10]**:
   - Used rooms: empty, unused = 2.
   - No used room is free, so open a fresh room.
   - Slack: 0.
   - Add 10+1=11 to used rooms.

2. **Meeting [5,8]**:
   - Used rooms: `{11}` (not free by 5), unused = 1.
   - No used room is free, so open a fresh room.
   - Slack: 0.
   - Add 8+1=9 to used rooms.

3. **Meeting [13,20]**:
   - Used rooms: `{9, 11}`.
   - Floor(13) -> 11.
   - Slack: 13 - 11 = 2.
   - Replace 11 with 20+1=21.

Total Slack: 2.

This matches the example because slack is counted **only between consecutive meetings** in the same room.  
The first meeting assigned to a room contributes **0** slack.

## ✅ Proof of Correctness

### Invariant
- If a used room is available, choosing the latest available free time minimizes the current slack and keeps earlier free times available for future meetings.
- If no used room is available, the meeting must start a new room; by definition its slack is 0.
- Updating the chosen room’s next free time preserves feasibility for all later meetings (sorted by start).

## 💡 Interview Extensions

- **Extension 1:** Weighted Meetings?
  - *Answer:* DP or Max Flow.
- **Extension 2:** Maximize meetings instead of minimize slack?
  - *Answer:* Standard Activity Selection (sort by end time).

### Common Mistakes to Avoid

1. **Initial Slack**
   - ❌ Wrong: Counting `start - 0` as slack.
   - ✅ Correct: First meeting in a room has 0 slack.
2. **Set vs Multiset**
   - ❌ Wrong: Using a Set (ignoring duplicate free times).
   - ✅ Correct: Use Multiset/Map<Time, Count> because multiple rooms can be free at the same time.

## Related Concepts

- **Interval Partitioning:** Minimizing number of rooms.
- **Bin Packing:** Related but NP-hard (this is simpler).
