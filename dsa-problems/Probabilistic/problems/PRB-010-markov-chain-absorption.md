---
problem_id: PRB_MARKOV_CHAIN_ABSORPTION__9031
display_id: PRB-010
slug: markov-chain-absorption
title: "Markov Chain Absorption"
difficulty: Medium
difficulty_score: 55
topics:
  - Probability
  - Markov Chains
  - Linear Algebra
tags:
  - probability
  - markov
  - absorption
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-010: Markov Chain Absorption

## Problem Statement

You are given a Markov chain with some absorbing states (a state with probability 1 of staying in itself). From a given start state, compute:

- Expected number of steps to absorption
- Absorption probabilities for each absorbing state

![Problem Illustration](../images/PRB-010/problem-illustration.png)

## Input Format

- First line: integer `n` and integer `s` (start state, 0-based)
- Next `n` lines: `n` real numbers (transition matrix rows)

## Output Format

- First line: expected steps to absorption
- Second line: absorption probabilities for absorbing states in increasing index order

## Constraints

- `1 <= n <= 20`
- Matrix rows sum to 1

## Example

**Input:**

```
3 0
0.5 0.5 0
0 0.5 0.5
0 0 1
```

**Output:**

```
4.000000
1.000000
```

**Explanation:**

State 2 is absorbing. Starting at 0, absorption is certain and expected steps are 4.

![Example Visualization](../images/PRB-010/example-1.png)

## Notes

- Use standard absorbing Markov chain formulas with (I-Q)^{-1}
- Accept answers with absolute error <= 1e-6
- Time complexity: O(n^3)

## Related Topics

Markov Chains, Linear Algebra, Absorption

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double[][] invert(double[][] A) {
        return null;
    }

    static class Result {
        double expectedSteps;
        double[] probs;
        Result(double e, double[] p) { expectedSteps = e; probs = p; }
    }

    public Result absorptionStats(double[][] P, int s) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            double[][] P = new double[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) P[i][j] = sc.nextDouble();
            }

            int numQueries = sc.nextInt();
            List<Integer> queryStates = new ArrayList<>();
            for (int i = 0; i < numQueries; i++) queryStates.add(sc.nextInt());

            int numAbsorbing = sc.nextInt();
            List<Integer> absorbingIndices = new ArrayList<>();
            for (int i = 0; i < numAbsorbing; i++) absorbingIndices.add(sc.nextInt());

            Solution sol = new Solution();
            
            // Reconstruct absorbing list used in logic to map indices
            List<Integer> funcAbsorbing = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if (Math.abs(P[i][i] - 1.0) < 1e-9) funcAbsorbing.add(i);
            }

            List<String> finalProbs = new ArrayList<>();
            List<String> finalSteps = new ArrayList<>();

            for (int s : queryStates) {
                Solution.Result res = sol.absorptionStats(P, s);
                finalSteps.add(String.format("%.6f", res.expectedSteps));
                
                for (int aIdx : absorbingIndices) {
                    int pos = funcAbsorbing.indexOf(aIdx);
                    if (pos != -1) {
                        finalProbs.add(String.format("%.6f", res.probs[pos]));
                    }
                }
            }

            System.out.println(String.join(" ", finalProbs));
            System.out.println(String.join(" ", finalSteps));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def invert(A):
    return 0
def absorption_stats(P, s: int):
    return 0
def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    iterator = iter(data)
    try:
        n = int(next(iterator))
        P = []
        for _ in range(n):
            row = []
            for _ in range(n):
                row.append(float(next(iterator)))
            P.append(row)

        num_queries = int(next(iterator))
        query_states = []
        for _ in range(num_queries):
            query_states.append(int(next(iterator)))

        num_absorbing = int(next(iterator))
        absorbing_indices = []
        for _ in range(num_absorbing):
            absorbing_indices.append(int(next(iterator)))

        # Get absorption states from matrix
        all_absorbing_states = []
        for i in range(n):
            if abs(P[i][i] - 1.0) < 1e-9:
                all_absorbing_states.append(i)

        # Collect absorption probabilities and expected steps for each query
        absorption_probs = []
        expected_steps = []

        for s in query_states:
            res = absorption_stats(P, s)
            if res:
                expected_steps.append(f"{res[0]:.6f}")
                # For each absorbing state in absorbing_indices, get probability
                for a_idx in absorbing_indices:
                    if a_idx in all_absorbing_states:
                        pos = all_absorbing_states.index(a_idx)
                        if pos + 1 < len(res):
                            absorption_probs.append(f"{res[pos + 1]:.6f}")

        print(" ".join(absorption_probs))
        print(" ".join(expected_steps))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <sstream>

using namespace std;

// Matrix Inversion
vector<vector<double>> invert(vector<vector<double>>& A) {
    int n = A.size();
    vector<vector<double>> B(n, vector<double>(2 * n));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) B[i][j] = A[i][j];
        B[i][n + i] = 1.0;
    }

    for (int i = 0; i < n; i++) {
        int pivot = i;
        for (int j = i + 1; j < n; j++) {
            if (abs(B[j][i]) > abs(B[pivot][i])) pivot = j;
        }
        swap(B[i], B[pivot]);

        double div = B[i][i];
        for (int j = i; j < 2 * n; j++) B[i][j] /= div;

        for (int k = 0; k < n; k++) {
            if (k != i) {
                double factor = B[k][i];
                for (int j = i; j < 2 * n; j++) B[k][j] -= factor * B[i][j];
            }
        }
    }

    vector<vector<double>> res(n, vector<double>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) res[i][j] = B[i][n + j];
    }
    return res;
}

struct Result {
    double expectedSteps;
    vector<double> probs;
};

Result absorptionStats(const vector<vector<double>>& P, int s) {
    int n = P.size();
    vector<int> absorbing;
    vector<int> transient;

    for (int i = 0; i < n; i++) {
        if (abs(P[i][i] - 1.0) < 1e-9) absorbing.push_back(i);
        else transient.push_back(i);
    }

    bool sIsAbsorbing = false;
    for (int idx : absorbing) if (idx == s) sIsAbsorbing = true;

    if (sIsAbsorbing) {
        vector<double> probs;
        for (int idx : absorbing) probs.push_back(idx == s ? 1.0 : 0.0);
        return {0.0, probs};
    }

    int tSize = transient.size();
    int aSize = absorbing.size();

    vector<vector<double>> Q(tSize, vector<double>(tSize));
    vector<vector<double>> R(tSize, vector<double>(aSize));

    for (int i = 0; i < tSize; i++) {
        int u = transient[i];
        for (int j = 0; j < tSize; j++) {
            int v = transient[j];
            Q[i][j] = P[u][v];
        }
        for (int j = 0; j < aSize; j++) {
            int v = absorbing[j];
            R[i][j] = P[u][v];
        }
    }

    vector<vector<double>> I_minus_Q(tSize, vector<double>(tSize));
    for (int i = 0; i < tSize; i++) {
        for (int j = 0; j < tSize; j++) {
            I_minus_Q[i][j] = (i == j ? 1.0 : 0.0) - Q[i][j];
        }
    }

    vector<vector<double>> N = invert(I_minus_Q);

    int sIdx = -1;
    for (int i = 0; i < tSize; i++) {
        if (transient[i] == s) {
            sIdx = i;
            break;
        }
    }

    double expectedSteps = 0;
    for (int j = 0; j < tSize; j++) expectedSteps += N[sIdx][j];

    vector<double> probs(aSize, 0.0);
    for (int j = 0; j < aSize; j++) {
        probs[j] = 0.0;
        for (int k = 0; k < tSize; k++) {
            probs[j] += N[sIdx][k] * R[k][j];
        }
    }

    return {expectedSteps, probs};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<double>> P(n, vector<double>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) cin >> P[i][j];
    }

    int num_queries;
    cin >> num_queries;
    vector<int> query_states(num_queries);
    for (int i = 0; i < num_queries; i++) cin >> query_states[i];

    int num_absorbing;
    cin >> num_absorbing;
    vector<int> absorbing_indices(num_absorbing);
    for (int i = 0; i < num_absorbing; i++) cin >> absorbing_indices[i];

    vector<int> all_absorbing_states;
    for (int i = 0; i < n; i++) {
        if (abs(P[i][i] - 1.0) < 1e-9) all_absorbing_states.push_back(i);
    }

    vector<string> final_probs;
    vector<string> final_steps;

    cout << fixed << setprecision(6);

    for (int s : query_states) {
        Result res = absorptionStats(P, s);
        
        stringstream ssSteps;
        ssSteps << fixed << setprecision(6) << res.expectedSteps;
        final_steps.push_back(ssSteps.str());

        // Map probs back to requested indices
        // res.probs corresponds to 'absorbing' list in order
        // We need for each 'absorbing_indices'
        
        // Reconstruct absorbing list order used in function
        vector<int> func_absorbing;
        for (int i = 0; i < n; i++) {
            if (abs(P[i][i] - 1.0) < 1e-9) func_absorbing.push_back(i);
        }

        for (int a_idx : absorbing_indices) {
            // Find a_idx in func_absorbing
            auto it = find(func_absorbing.begin(), func_absorbing.end(), a_idx);
            if (it != func_absorbing.end()) {
                int pos = distance(func_absorbing.begin(), it);
                stringstream ssProb;
                ssProb << fixed << setprecision(6) << res.probs[pos];
                final_probs.push_back(ssProb.str());
            }
        }
    }

    for (int i = 0; i < final_probs.size(); i++) {
        cout << final_probs[i] << (i == final_probs.size() - 1 ? "" : " ");
    }
    cout << "\n";
    for (int i = 0; i < final_steps.size(); i++) {
        cout << final_steps[i] << (i == final_steps.size() - 1 ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function invert(A) {
    return 0;
  }

function absorptionStats(P, s) {
    return 0;
  }

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part !== "") data.push(part);
  }
});

rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const P = [];
  for (let i = 0; i < n; i++) {
    const row = [];
    for (let j = 0; j < n; j++) row.push(parseFloat(data[idx++]));
    P.push(row);
  }

  const numQueries = parseInt(data[idx++], 10);
  const queryStates = [];
  for (let i = 0; i < numQueries; i++) queryStates.push(parseInt(data[idx++], 10));

  const numAbsorbing = parseInt(data[idx++], 10);
  const absorbingIndices = [];
  for (let i = 0; i < numAbsorbing; i++) absorbingIndices.push(parseInt(data[idx++], 10));

  const funcAbsorbing = [];
  for (let i = 0; i < n; i++) {
    if (Math.abs(P[i][i] - 1.0) < 1e-9) funcAbsorbing.push(i);
  }

  const finalProbs = [];
  const finalSteps = [];

  for (const s of queryStates) {
    const res = absorptionStats(P, s);
    finalSteps.push(res.expectedSteps.toFixed(6));
    
    for (const aIdx of absorbingIndices) {
      const pos = funcAbsorbing.indexOf(aIdx);
      if (pos !== -1) {
        finalProbs.push(res.probs[pos].toFixed(6));
      }
    }
  }

  console.log(finalProbs.join(" "));
  console.log(finalSteps.join(" "));
});
```

