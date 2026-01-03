---
problem_id: PRB_MIN_CUT_RANDOM_CONTRACTION__8305
display_id: PRB-006
slug: min-cut-random-contraction
title: "Min-Cut with Randomized Contraction"
difficulty: Medium
difficulty_score: 52
topics:
  - Probability
  - Graphs
  - Randomized Algorithms
tags:
  - probability
  - karger
  - min-cut
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-006: Min-Cut with Randomized Contraction

## Problem Statement

Karger's randomized contraction algorithm succeeds in finding the global min-cut with probability at least:

```
P_success = 2 / (n * (n - 1))
```

Given `n` and a target confidence `P`, compute the minimum number of independent trials needed so that the overall success probability is at least `P`.

![Problem Illustration](../images/PRB-006/problem-illustration.png)

## Input Format

- Single line: integer `n` and real `P`

## Output Format

- Single integer: minimum number of trials

## Constraints

- `2 <= n <= 10^9`
- `0 < P < 1`

## Example

**Input:**

```
4 0.9
```

**Output:**

```
13
```

**Explanation:**

For n=4, P_success = 1/6. The smallest t with 1 - (1 - 1/6)^t >= 0.9 is 13.

![Example Visualization](../images/PRB-006/example-1.png)

## Notes

- Use t = ceil(log(1-P) / log(1-P_success))
- Handle floating-point precision carefully
- Time complexity: O(1)

## Related Topics

Randomized Algorithms, Min-Cut, Probability

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int kargerMinCut(int n, List<Edge> edges, Random rng) {
        //Implement here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            List<Solution.Edge> edges = new ArrayList<>();
            for (int i = 0; i < m; i++) {
                edges.add(new Solution.Edge(sc.nextInt(), sc.nextInt()));
            }

            int trials;
            if (n <= 20) trials = 100;
            else trials = (int) (n * n * 0.5);

            Solution sol = new Solution();
            Random rng = new Random(42); // Fixed seed for determinism
            
            int minCut = m + 1;
            for (int i = 0; i < trials; i++) {
                int cut = sol.kargerMinCut(n, edges, rng);
                if (cut < minCut) minCut = cut;
            }
            
            System.out.println(minCut);
        }
        sc.close();
    }
}
```

### Python

```python
import sys
import random
from collections import defaultdict

def karger_min_cut(n: int, edges):
    # //Implement here
    return 0

def main():
    input_data = sys.stdin.read
    lines = input_data().strip().split('\n')

    if not lines:
        return

    n, m = map(int, lines[0].split())
    edges = []

    for i in range(1, m + 1):
        u, v = map(int, lines[i].split())
        edges.append((u, v))

    # Run Karger's algorithm multiple times and return minimum
    min_cut = float('inf')

    # Number of trials - Karger's algorithm may need many runs for accuracy
    # but we need to balance with performance
    # Number of trials - Karger's algorithm succeeds with probability >= 2/(n(n-1))
    # We need enough trials to ensure high probability of finding min cut.
    # For small n, we can run many trials.
    # Theoretical bound for failure < 1/n is O(n^2 log n) trials.
    if n <= 20:
        trials = 100
    else:
        trials = int(n * n * 0.5)  # Heuristic for larger n

    for _ in range(trials):
        cut = karger_min_cut(n, edges)
        min_cut = min(min_cut, cut)

    print(min_cut)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <numeric>

using namespace std;

struct Edge {
    int u, v;
};

struct DSU {
    vector<int> parent;
    int components;

    DSU(int n) {
        parent.resize(n + 1);
        iota(parent.begin(), parent.end(), 0);
        components = n;
    }

    int find(int i) {
        if (parent[i] == i)
            return i;
        return parent[i] = find(parent[i]);
    }

    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
            components--;
        }
    }
};

int kargerMinCut(int n, vector<Edge>& edges, mt19937& rng) {
    DSU dsu(n);
    vector<Edge> current_edges = edges;
    shuffle(current_edges.begin(), current_edges.end(), rng);

    for (const auto& edge : current_edges) {
        if (dsu.components <= 2) break;
        dsu.unite(edge.u, edge.v);
    }

    int cut_size = 0;
    for (const auto& edge : edges) {
        if (dsu.find(edge.u) != dsu.find(edge.v)) {
            cut_size++;
        }
    }
    return cut_size;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (cin >> n >> m) {
        vector<Edge> edges;
        for (int i = 0; i < m; ++i) {
            int u, v;
            cin >> u >> v;
            edges.push_back({u, v});
        }

        int trials;
        if (n <= 20) trials = 100;
        else trials = (int)(n * n * 0.5);

        // Seed with a fixed value or device if needed, but python uses random
        // Using a fixed seed ensures determinism across runs of this binary
        mt19937 rng(42); 

        int min_cut = m + 1;

        for (int i = 0; i < trials; ++i) {
            int cut = kargerMinCut(n, edges, rng);
            if (cut < min_cut) min_cut = cut;
        }

        cout << min_cut << "\n";
    }
    return 0;
}

class Solution {
public:
     DSU(int n) {
        //Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (cin >> n >> m) {
        vector<Edge> edges;
        for (int i = 0; i < m; ++i) {
            int u, v;
            cin >> u >> v;
            edges.push_back({u, v});
        }

        int trials;
        if (n <= 20) trials = 100;
        else trials = (int)(n * n * 0.5);

        // Seed with a fixed value or device if needed, but python uses random
        // Using a fixed seed ensures determinism across runs of this binary
        mt19937 rng(42); 

        int min_cut = m + 1;

        for (int i = 0; i < trials; ++i) {
            int cut = kargerMinCut(n, edges, rng);
            if (cut < min_cut) min_cut = cut;
        }

        cout << min_cut << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class DSU {
  constructor(n) {
    this.parent = Array.from({ length: n + 1 }, (_, i) => i);
    this.components = n;
  }
  find(i) {
    if (this.parent[i] === i) return i;
    return (this.parent[i] = this.find(this.parent[i]));
  }
  unite(i, j) {
    const rootI = this.find(i);
    const rootJ = this.find(j);
    if (rootI !== rootJ) {
      this.parent[rootI] = rootJ;
      this.components--;
    }
  }
}

function kargerMinCut(n, edges) {
  //Implement here
  return 0;
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
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    edges.push([u, v]);
  }

  let trials;
  if (n <= 20) trials = 100;
  else trials = Math.floor(n * n * 0.5);

  let minCut = m + 1;
  for (let i = 0; i < trials; i++) {
    const cut = kargerMinCut(n, edges);
    if (cut < minCut) minCut = cut;
  }
  console.log(minCut);
});
```

