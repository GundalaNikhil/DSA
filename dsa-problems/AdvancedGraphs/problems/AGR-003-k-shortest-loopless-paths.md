---
problem_id: AGR_K_SHORTEST_LOOPLESS_PATHS__2749
display_id: AGR-003
slug: k-shortest-loopless-paths
title: "K Shortest Paths (Loopless)"
difficulty: Medium
difficulty_score: 62
topics:
  - Graphs
  - Shortest Path
  - Yen Algorithm
tags:
  - advanced-graphs
  - k-shortest
  - yen
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-003: K Shortest Paths (Loopless)

## Problem Statement

Given a directed weighted graph, find the `k` shortest **simple** paths from source `s` to target `t` (no repeated vertices). Output the path lengths in ascending order.

If fewer than `k` simple paths exist, output all of them.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767187126/dsa-problems/AGR-003/problem/ycidx4enufuhzccowmgb.jpg)

## Input Format

- First line: integers `n`, `m`, `s`, `t`, and `k`
- Next `m` lines: `u v w` describing a directed edge `u -> v` with weight `w`

## Output Format

- Line 1: integer `r`, the number of paths found
- Line 2: `r` integers, the path lengths in ascending order

## Constraints

- `1 <= n <= 500`
- `0 <= m <= 5000`
- `1 <= k <= 50`
- `0 <= w <= 10^9`
- `0 <= s, t < n`

## Example

**Input:**

```
3 3 0 2 2
0 1 1
1 2 1
0 2 3
```

**Output:**

```
2
2 3
```

**Explanation:**

The two shortest simple paths are `0-1-2` (length 2) and `0-2` (length 3).

![Example Visualization](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767187128/dsa-problems/AGR-003/problem/wvacrhnvixycwwqlk1md.jpg)

## Notes

- Use Yen's algorithm with Dijkstra for spur paths.
- Distances can exceed 32-bit; use 64-bit integers.
- If no path exists, output `0` and an empty second line.

## Related Topics

K Shortest Paths, Dijkstra, Yen's Algorithm

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    static class Edge {
        int to;
        int weight;
        Edge(int to, int weight) { this.to = to; this.weight = weight; }
    }

    static class Path implements Comparable<Path> {
        List<Integer> nodes;
        long cost;

        Path(List<Integer> nodes, long cost) {
            this.nodes = new ArrayList<>(nodes);
            this.cost = cost;
        }

        @Override
        public int compareTo(Path other) {
        return 0;
    }
    }

    public long[] kShortestPaths(int n, List<List<int[]>> adjList, int s, int t, int k) {
        return null;
    }

    private Path getShortestPath(int n, List<List<Edge>> adj, int s, int t, 
                                 Set<Integer> forbiddenNodes, Set<String> forbiddenEdges) {
        long[] dist = new long[n];
        Arrays.fill(dist, Long.MAX_VALUE);
        int[] parent = new int[n];
        Arrays.fill(parent, -1);
        dist[s] = 0;

        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        pq.add(new long[]{0, s});

        while (!pq.isEmpty()) {
            long[] top = pq.poll();
            long d = top[0];
            int u = (int) top[1];

            if (d > dist[u]) continue;
            if (u == t) break;

            for (Edge e : adj.get(u)) {
                if (forbiddenNodes.contains(e.to)) continue;
                if (forbiddenEdges.contains(u + "," + e.to)) continue;

                if (dist[u] + e.weight < dist[e.to]) {
                    dist[e.to] = dist[u] + e.weight;
                    parent[e.to] = u;
                    pq.add(new long[]{dist[e.to], e.to});
                }
            }
        }

        if (dist[t] == Long.MAX_VALUE) return null;

        List<Integer> nodes = new ArrayList<>();
        int curr = t;
        while (curr != -1) {
            nodes.add(curr);
            curr = parent[curr];
        }
        Collections.reverse(nodes);
        return new Path(nodes, dist[t]);
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int s = sc.nextInt();
        int t = sc.nextInt();
        int k = sc.nextInt();
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();
            adj.get(u).add(new int[]{v, w});
        }

        Solution solution = new Solution();
        long[] paths = solution.kShortestPaths(n, adj, s, t, k);
        StringBuilder sb = new StringBuilder();
        sb.append(paths.length).append('\n');
        for (int i = 0; i < paths.length; i++) {
            if (i > 0) sb.append(' ');
            sb.append(paths[i]);
        }
        System.out.print(sb.toString());
        sc.close();
    }
}
```

### Python

```python
import sys
import heapq

def k_shortest_paths(n: int, adj: list[list[tuple[int, int]]], s: int, t: int, k: int) -> list[int]:
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
        t = int(next(iterator))
        k = int(next(iterator))
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            adj[u].append((v, w))
            
        paths = k_shortest_paths(n, adj, s, t, k)
        print(len(paths))
        print(" ".join(map(str, paths)))
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
#include <set>
#include <algorithm>
#include <map>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int to;
    int weight;
};

struct Path {
    vector<int> nodes;
    long long cost;

    bool operator<(const Path& other) const {
        if (cost != other.cost) return cost < other.cost;
        return nodes < other.nodes;
    }
    bool operator>(const Path& other) const {
        return other < *this;
    }
    bool operator==(const Path& other) const {
        return cost == other.cost && nodes == other.nodes;
    }
};

class Solution {
    vector<vector<Edge>> adj;
    int N;

    Path getShortestPath(int s, int t, const set<int>& forbiddenNodes, const set<pair<int, int>>& forbiddenEdges) {
        return 0;
    }

public:
    vector<long long> kShortestPaths(int n, const vector<vector<pair<int, int>>>& adjList, int s, int t, int k) {
        N = n;
        adj.assign(n, vector<Edge>());
        for (int u = 0; u < n; u++) {
            for (auto& p : adjList[u]) {
                adj[u].push_back({p.first, p.second});
            }
        }

        vector<Path> A;
        set<Path> B; // Use set to keep sorted and unique candidates

        Path p0 = getShortestPath(s, t, {}, {});
        if (p0.cost == -1) return {};
        A.push_back(p0);

        for (int i = 1; i < k; i++) {
            Path prevPath = A.back();

            for (size_t j = 0; j < prevPath.nodes.size() - 1; j++) {
                int spurNode = prevPath.nodes[j];
                vector<int> rootPathNodes(prevPath.nodes.begin(), prevPath.nodes.begin() + j + 1);
                
                long long rootCost = 0;
                for (size_t x = 0; x < j; x++) {
                    int u = prevPath.nodes[x];
                    int v = prevPath.nodes[x+1];
                    for (auto& e : adj[u]) if (e.to == v) { rootCost += e.weight; break; }
                }

                set<int> forbiddenNodes(rootPathNodes.begin(), rootPathNodes.end());
                forbiddenNodes.erase(spurNode);

                set<pair<int, int>> forbiddenEdges;
                for (const auto& p : A) {
                    if (p.nodes.size() > j && 
                        vector<int>(p.nodes.begin(), p.nodes.begin() + j + 1) == rootPathNodes) {
                        forbiddenEdges.insert({p.nodes[j], p.nodes[j+1]});
                    }
                }

                Path spurPath = getShortestPath(spurNode, t, forbiddenNodes, forbiddenEdges);

                if (spurPath.cost != -1) {
                    vector<int> totalNodes = rootPathNodes;
                    totalNodes.pop_back();
                    totalNodes.insert(totalNodes.end(), spurPath.nodes.begin(), spurPath.nodes.end());
                    
                    Path totalPath = {totalNodes, rootCost + spurPath.cost};
                    B.insert(totalPath);
                }
            }

            if (B.empty()) break;
            
            // Move best from B to A
            // Since B is a set, begin() is the smallest
            A.push_back(*B.begin());
            B.erase(B.begin());
        }

        vector<long long> result;
        for (const auto& p : A) result.push_back(p.cost);
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s, t, k;
    if (!(cin >> n >> m >> s >> t >> k)) return 0;
    vector<vector<pair<int, int>>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
    }

    Solution solution;
    vector<long long> paths = solution.kShortestPaths(n, adj, s, t, k);
    cout << paths.size() << "\n";
    for (int i = 0; i < (int)paths.size(); i++) {
        if (i) cout << ' ';
        cout << paths[i];
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class PriorityQueue {
  constructor(comparator = (a, b) => a - b) {
    this.heap = [];
    this.comparator = comparator;
  }
  push(val) {
    this.heap.push(val);
    this.bubbleUp(this.heap.length - 1);
  }
  pop() {
    if (this.heap.length === 0) return null;
    const top = this.heap[0];
    const bottom = this.heap.pop();
    if (this.heap.length > 0) {
      this.heap[0] = bottom;
      this.bubbleDown(0);
    }
    return top;
  }
  isEmpty() { return this.heap.length === 0; }
  bubbleUp(idx) {
    while (idx > 0) {
      const pIdx = Math.floor((idx - 1) / 2);
      if (this.comparator(this.heap[idx], this.heap[pIdx]) < 0) {
        [this.heap[idx], this.heap[pIdx]] = [this.heap[pIdx], this.heap[idx]];
        idx = pIdx;
      } else break;
    }
  }
  bubbleDown(idx) {
    while (true) {
      const lIdx = 2 * idx + 1;
      const rIdx = 2 * idx + 2;
      let swapIdx = null;
      if (lIdx < this.heap.length && this.comparator(this.heap[lIdx], this.heap[idx]) < 0) swapIdx = lIdx;
      if (rIdx < this.heap.length && this.comparator(this.heap[rIdx], swapIdx === null ? this.heap[idx] : this.heap[swapIdx]) < 0) swapIdx = rIdx;
      if (swapIdx !== null) {
        [this.heap[idx], this.heap[swapIdx]] = [this.heap[swapIdx], this.heap[idx]];
        idx = swapIdx;
      } else break;
    }
  }
}

class Solution {
  kShortestPaths(n, adj, s, t, k) {
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => { const parts = line.trim().split(/\s+/); for (const p of parts) if (p) data.push(p); });
rl.on("close", () => {
  if (data.length === 0) return;
  
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const m = parseInt(data[idx++], 10);
  const s = parseInt(data[idx++], 10);
  const t = parseInt(data[idx++], 10);
  const k = parseInt(data[idx++], 10);
  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const w = parseInt(data[idx++], 10);
    if (u >= n || u < 0) { console.error(`Error: u=${u} n=${n} idx=${idx-3} len=${data.length}`); }
    if (!adj[u]) { console.error(`Error: adj[${u}] undefined. n=${n}`); }
    adj[u].push([v, w]);
  }

  const solution = new Solution();
  const paths = solution.kShortestPaths(n, adj, s, t, k);
  console.log(paths.length.toString());
  console.log(paths.join(" "));
});
```

