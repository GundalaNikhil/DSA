---
problem_id: GRB_MST_PRIM__9142
display_id: GRB-008
slug: mst-prim
title: "MST Prim"
difficulty: Medium
difficulty_score: 42
topics:
  - Graphs
  - MST
  - Priority Queue
tags:
  - graphs-basics
  - mst
  - prim
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-008: MST Prim

## Problem Statement

Given a connected, undirected weighted graph, compute the total weight of its minimum spanning tree (MST) using Prim's algorithm.

![Problem Illustration](../images/GRB-008/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v w` describing an undirected edge with weight `w`

## Output Format

- Single integer: the total weight of the MST

## Constraints

- `1 <= n <= 100000`
- `n-1 <= m <= 200000`
- `0 <= w <= 10^9`
- The graph is connected

## Example

**Input:**

```
3 3
0 1 1
1 2 2
0 2 3
```

**Output:**

```
3
```

**Explanation:**

Prim's algorithm selects edges with weights 1 and 2 for total 3.

![Example Visualization](../images/GRB-008/example-1.png)

## Notes

- Use a min-heap keyed by edge weight.
- Track visited nodes to avoid cycles.
- Total MST weight fits in 64-bit integers.

## Related Topics

Minimum Spanning Tree, Prim, Priority Queue

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long mstPrim(int n, List<List<int[]>> adj) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();
            adj.get(u).add(new int[]{v, w});
            adj.get(v).add(new int[]{u, w});
        }

        Solution solution = new Solution();
        System.out.println(solution.mstPrim(n, adj));
        sc.close();
    }
}
```

### Python

```python
import sys
import heapq

def mst_prim(n: int, adj: list[list[tuple[int, int]]]) -> int:
    return 0
def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            adj[u].append((v, w))
            adj[v].append((u, w))
            
        print(mst_prim(n, adj))
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
#include <tuple>

using namespace std;

class Solution {
public:
    long long mstPrim(int n, const vector<vector<pair<int, int>>>& adj) {
        long long mstWeight = 0;
        vector<bool> visited(n, false);
        
        // Min-heap: {weight, node}
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        pq.push({0, 0});
        
        int nodesCount = 0;
        
        while (!pq.empty()) {
            int w = pq.top().first;
            int u = pq.top().second;
            pq.pop();
            
            if (visited[u]) continue;
            
            visited[u] = true;
            mstWeight += w;
            nodesCount++;
            
            if (nodesCount == n) break;
            
            for (auto& edge : adj[u]) {
                int v = edge.first;
                int weight = edge.second;
                if (!visited[v]) {
                    pq.push({weight, v});
                }
            }
        }
        
        return mstWeight;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<vector<pair<int, int>>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    Solution solution;
    cout << solution.mstPrim(n, adj) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class MinPriorityQueue {
  constructor() {
    this.heap = [];
  }
  push(val) {
    this.heap.push(val);
    this.bubbleUp(this.heap.length - 1);
  }
  pop() {
    if (this.heap.length === 0) return null;
    const min = this.heap[0];
    const end = this.heap.pop();
    if (this.heap.length > 0) {
      this.heap[0] = end;
      this.sinkDown(0);
    }
    return min;
  }
  isEmpty() { return this.heap.length === 0; }
  bubbleUp(idx) {
    const element = this.heap[idx];
    while (idx > 0) {
      let parentIdx = Math.floor((idx - 1) / 2);
      let parent = this.heap[parentIdx];
      if (element.w >= parent.w) break;
      this.heap[parentIdx] = element;
      this.heap[idx] = parent;
      idx = parentIdx;
    }
  }
  sinkDown(idx) {
    const length = this.heap.length;
    const element = this.heap[idx];
    while (true) {
      let leftChildIdx = 2 * idx + 1;
      let rightChildIdx = 2 * idx + 2;
      let swap = null;
      if (leftChildIdx < length) {
        let leftChild = this.heap[leftChildIdx];
        if (leftChild.w < element.w) swap = leftChildIdx;
      }
      if (rightChildIdx < length) {
        let rightChild = this.heap[rightChildIdx];
        if ((swap === null && rightChild.w < element.w) || (swap !== null && rightChild.w < this.heap[swap].w)) {
          swap = rightChildIdx;
        }
      }
      if (swap === null) break;
      this.heap[idx] = this.heap[swap];
      this.heap[swap] = element;
      idx = swap;
    }
  }
}

class Solution {
  mstPrim(n, adj) {
    return 0;
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
  const m = parseInt(data[idx++], 10);
  
  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const w = parseInt(data[idx++], 10);
    adj[u].push([v, w]);
    adj[v].push([u, w]);
  }

  const solution = new Solution();
  console.log(solution.mstPrim(n, adj));
});
```

