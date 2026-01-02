---
problem_id: GRB_DIJKSTRA_BINARY_HEAP__6041
display_id: GRB-003
slug: dijkstra-binary-heap
title: "Dijkstra with Binary Heap"
difficulty: Medium
difficulty_score: 45
topics:
  - Graphs
  - Dijkstra
  - Shortest Path
tags:
  - graphs-basics
  - dijkstra
  - shortest-path
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-003: Dijkstra with Binary Heap

## Problem Statement

You are given a directed graph with non-negative edge weights. Compute the shortest distance from a source node `s` to every node.

If a node is unreachable, its distance should be `-1`.

![Problem Illustration](../images/GRB-003/problem-illustration.png)

## Input Format

- First line: integers `n`, `m`, and `s`
- Next `m` lines: `u v w` describing a directed edge `u -> v` with weight `w`

## Output Format

- Single line: `n` integers, the distances from `s` to nodes `0..n-1`

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `0 <= w <= 10^9`
- `0 <= s < n`

## Example

**Input:**

```
3 3 0
0 1 1
1 2 2
0 2 5
```

**Output:**

```
0 1 3
```

**Explanation:**

The shortest path to node 2 is `0 -> 1 -> 2` with total cost 3.

![Example Visualization](../images/GRB-003/example-1.png)

## Notes

- Use Dijkstra with a min-heap (priority queue).
- Skip outdated heap entries using a distance check.
- Distances can exceed 32-bit; use 64-bit integers.

## Related Topics

Dijkstra, Priority Queue, Shortest Path

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long[] dijkstra(int n, List<List<int[]>> adj, int s) {
        return null;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int s = sc.nextInt();
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();
            adj.get(u).add(new int[]{v, w});
        }

        Solution solution = new Solution();
        long[] dist = solution.dijkstra(n, adj, s);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (i > 0) sb.append(' ');
            sb.append(dist[i]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
```

### Python

```python
import sys
import heapq

def dijkstra(n: int, adj: list[list[tuple[int, int]]], s: int) -> list[int]:
    return []
def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        s = int(next(iterator))
        
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            adj[u].append((v, w))
            
        dist = dijkstra(n, adj, s)
        print(" ".join(map(str, dist)))
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
    vector<long long> dijkstra(int n, const vector<vector<pair<int, int>>>& adj, int s) {
        vector<long long> dist(n, -1);
        
        // Min-priority queue: stores {distance, node}
        // Use greater to make it a min-heap
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
        
        dist[s] = 0;
        pq.push({0, s});
        
        while (!pq.empty()) {
            long long d = pq.top().first;
            int u = pq.top().second;
            pq.pop();
            
            // Lazy deletion check
            if (dist[u] != -1 && d > dist[u]) continue;
            
            for (auto& edge : adj[u]) {
                int v = edge.first;
                int w = edge.second;
                
                if (dist[v] == -1 || dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    pq.push({dist[v], v});
                }
            }
        }
        
        return dist;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s;
    if (!(cin >> n >> m >> s)) return 0;
    vector<vector<pair<int, int>>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
    }

    Solution solution;
    vector<long long> dist = solution.dijkstra(n, adj, s);
    for (int i = 0; i < n; i++) {
        if (i) cout << ' ';
        cout << dist[i];
    }
    cout << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

// Simple MinPriorityQueue implementation since JS doesn't have a built-in one
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

  isEmpty() {
    return this.heap.length === 0;
  }

  bubbleUp(idx) {
    const element = this.heap[idx];
    while (idx > 0) {
      let parentIdx = Math.floor((idx - 1) / 2);
      let parent = this.heap[parentIdx];
      if (element.priority >= parent.priority) break;
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
        if (leftChild.priority < element.priority) {
          swap = leftChildIdx;
        }
      }

      if (rightChildIdx < length) {
        let rightChild = this.heap[rightChildIdx];
        if (
          (swap === null && rightChild.priority < element.priority) ||
          (swap !== null && rightChild.priority < this.heap[swap].priority)
        ) {
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
  dijkstra(n, adj, s) {
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
  
  const tokens = data.join(" ").trim().split(/\s+/);
  if (tokens.length === 0 || tokens[0] === "") return;
  
  let ptr = 0;
  const n = parseInt(tokens[ptr++], 10);
  const m = parseInt(tokens[ptr++], 10);
  const s = parseInt(tokens[ptr++], 10);
  
  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(tokens[ptr++], 10);
    const v = parseInt(tokens[ptr++], 10);
    const w = parseInt(tokens[ptr++], 10);
    adj[u].push([v, w]);
  }

  const solution = new Solution();
  const dist = solution.dijkstra(n, adj, s);
  console.log(dist.join(" "));
});
```

