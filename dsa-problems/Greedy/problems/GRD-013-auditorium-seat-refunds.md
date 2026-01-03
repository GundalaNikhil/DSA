---
problem_id: GRD_AUDITORIUM_SEAT_REFUNDS__2841
display_id: GRD-013
slug: auditorium-seat-refunds
title: "Auditorium Seat Refunds"
difficulty: Easy-Medium
difficulty_score: 35
topics:
  - Greedy Algorithms
  - Heap
  - Priority Queue
tags:
  - greedy
  - heap
  - priority-queue
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-013: Auditorium Seat Refunds

## Problem Statement

An auditorium has seats organized in rows numbered 1 to `r`. Initially, all rows are fully occupied with `capacity[i]` seats in row `i`.

You receive `n` refund requests, where each request specifies a seat ID that includes the row number. When processing refunds, you want to minimize the highest occupied row index remaining after all refunds.

Return the highest occupied row number after processing all refund requests.

![Problem Illustration](../images/GRD-013/problem-illustration.png)

## Input Format

- First line: two integers `r n` (number of rows and number of refund requests)
- Second line: `r` space-separated integers representing initial capacity of each row
- Next `n` lines: two integers `row seat_id` representing each refund request

## Output Format

- Single integer: highest occupied row number (1-indexed) after all refunds

## Constraints

- `1 <= r <= 10^5`
- `1 <= capacity[i] <= 10^5`
- `0 <= n <= sum(capacity[i])`
- `1 <= row <= r`

## Example

**Input:**

```
3 3
5 4 3
3 1
3 2
2 1
```

**Output:**

```
2
```

**Explanation:**

Initial state:

- Row 1: 5 seats occupied
- Row 2: 4 seats occupied
- Row 3: 3 seats occupied

Refund requests:

1. Refund seat 1 from row 3 → Row 3 now has 2 seats
2. Refund seat 2 from row 3 → Row 3 now has 1 seat
3. Refund seat 1 from row 2 → Row 2 now has 3 seats

After processing:

- Row 1: 5 seats (still occupied)
- Row 2: 3 seats (still occupied)
- Row 3: 0 seats (completely empty after processing all refunds)

Since row 3 is completely empty, the highest occupied row is row 2.

The greedy strategy processes refunds from the highest rows first to minimize the highest occupied row number after all refunds are processed.

![Example Visualization](../images/GRD-013/example-1.png)

## Notes

- Track the occupancy count for each row
- Use a max-heap to efficiently track the highest occupied row
- After each refund, decrement the row's count
- If a row becomes empty (count = 0), it's no longer occupied
- Time complexity: O(n log r) for heap operations

## Related Topics

Greedy Algorithms, Heap, Priority Queue, State Management, Optimization

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int highestOccupiedRow(int r, int[] capacities, int[][] refunds) {
        //Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int r = sc.nextInt();
        int n = sc.nextInt();
        
        int[] capacities = new int[r];
        for (int i = 0; i < r; i++) {
            capacities[i] = sc.nextInt();
        }
        
        int[][] refunds = new int[n][2];
        for (int i = 0; i < n; i++) {
            refunds[i][0] = sc.nextInt();
            refunds[i][1] = sc.nextInt();
        }
        
        Solution solution = new Solution();
        System.out.println(solution.highestOccupiedRow(r, capacities, refunds));
        sc.close();
    }
}
```

### Python

```python
import sys

def highest_occupied_row(r: int, capacities: list, refunds: list) -> int:
    # //Implement here
    return 0

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    r = int(next(iterator))
    n = int(next(iterator))
    
    capacities = []
    for _ in range(r):
        capacities.append(int(next(iterator)))
        
    # Skip refunds details as we only need count
    # But we must consume the input
    for _ in range(n):
        next(iterator) # row
        next(iterator) # seat
        
    # Note: refunds list in function signature is just for compatibility with template
    # We can pass a dummy list or just use n
    print(highest_occupied_row(r, capacities, [0]*n))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    int highestOccupiedRow(int r, vector<int>& capacities, vector<pair<int,int>>& refunds) {
        //Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int r, n;
    if (!(cin >> r >> n)) return 0;

    vector<int> capacities(r);
    for (int i = 0; i < r; i++) {
        cin >> capacities[i];
    }

    vector<pair<int,int>> refunds(n);
    for (int i = 0; i < n; i++) {
        cin >> refunds[i].first >> refunds[i].second;
    }

    Solution solution;
    cout << solution.highestOccupiedRow(r, capacities, refunds) << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  highestOccupiedRow(r, capacities, refunds) {
    //Implement here
    return 0;
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
  const [r, n] = data[ptr++].split(" ").map(Number);
  const capacities = data[ptr++].split(" ").map(Number);
  
  const refunds = [];
  for (let i = 0; i < n; i++) {
    const [row, seatId] = data[ptr++].split(" ").map(Number);
    refunds.push([row, seatId]);
  }

  const solution = new Solution();
  console.log(solution.highestOccupiedRow(r, capacities, refunds));
});
```

