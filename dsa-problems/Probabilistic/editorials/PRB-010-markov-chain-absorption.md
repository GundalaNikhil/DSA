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
---

# PRB-010: Markov Chain Absorption

## 📋 Problem Summary

Given a Markov Chain with n states, some of which are absorbing (once entered, cannot leave).
Starting from state s, calculate:

1. The expected number of steps until absorption.
2. The probability of being absorbed into each specific absorbing state.

| | |
|---|---|
| **Input** | Transition matrix P, start state s |
| **Output** | Expected steps, List of absorption probabilities |

## 🌍 Real-World Scenario

**Scenario Title:** The Customer Conversion Funnel

You are analyzing user behavior on an e-commerce site.

- States: "Homepage", "Product Page", "Cart", "Checkout", "Purchase" (Absorbing), "Exit" (Absorbing).
- Users move between states with certain probabilities (e.g., 30% from Cart to Checkout, 10% to Exit).
- You want to know:
  - **Expected Steps:** How many pages does a user visit before either buying or leaving? (Engagement metric).
  - **Absorption Probabilities:** What is the probability a user eventually buys vs. exits? (Conversion Rate).
- This helps in optimizing the UX flow to maximize purchases.

**Why This Problem Matters:**

- **Finance:** Credit rating migration (probability of default).
- **Genetics:** Wright-Fisher model for gene fixation.
- **Board Games:** Snakes and Ladders analysis.

![Real-World Application](../images/PRB-010/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Customer Journey Visualization

Real-world example of the e-commerce funnel:

```
         0.3           0.5           0.7
Homepage ───→ Product ───→ Cart ───→ Checkout ───→ [Purchase] ✓
   │            │           │            │         (Absorbing)
   │ 0.7        │ 0.5       │ 0.3        │ 0.3
   └────────────┴───────────┴────────────┴────────→ [Exit] ✗
                                                   (Absorbing)

States:
• 0: Homepage  (Transient) ─┐
• 1: Product   (Transient)  ├─ Can move between these
• 2: Cart      (Transient)  │
• 3: Checkout  (Transient) ─┘
• 4: Purchase  (Absorbing) ─ Once here, stays forever
• 5: Exit      (Absorbing) ─ Once here, stays forever
```

### Matrix Canonical Form

States: 0 (Transient), 1 (Transient), 2 (Absorbing), 3 (Absorbing).
Rearrange matrix so transient states come first, then absorbing.

```
         Transient | Absorbing
              T1 T2 | A1 A2
            +-------+-------+
  Transient | Q     | R     |  ← Transient → Transient (Q)
         T1 |       |       |  ← Transient → Absorbing (R)
         T2 |       |       |
            +-------+-------+
  Absorbing | 0     | I     |  ← Always 0 (can't leave)
         A1 |       |       |  ← Identity (stay in place)
         A2 |       |       |
            +-------+-------+
```

**Key Submatrices:**

- **Q:** Transitions between transient states (size: t×t)
- **R:** Transitions from transient to absorbing (size: t×a)
- **0:** Zero matrix - absorbing states can't go to transient
- **I:** Identity matrix - absorbing states stay put

**Fundamental Matrix:** N = (I - Q)^{-1}$

- Element `N_ij` = Expected visits to state j starting from state i
- Each row sums to total expected steps before absorption

**Key Formulas:**

1. Expected steps vector: t = N \times \mathbf{1}$ (column of 1s)
2. Absorption probabilities: B = N \times R$

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Absorbing State:** A state i where P_ii = 1.
- **Constraints:** n \le 20$. Matrix inversion is O(n^3), perfectly fine.
- **Output Format:**
  - First line: Expected steps (scalar).
  - Second line: Probabilities for _all_ absorbing states, sorted by their original index.
  - If start state is absorbing, expected steps = 0, prob for itself = 1, others = 0.

### Core Concept: Fundamental Matrix

**What is the Fundamental Matrix N?**

For an absorbing Markov chain, the matrix N = (I - Q)^{-1}$ is called the **Fundamental Matrix**.

**Intuitive Meaning:**

- Element `N_ij` = "Starting from transient state i, how many times (on average) will I visit transient state j before getting absorbed?"
- The sum of row i in N = "Starting from state i, how many total steps until absorption?"

**Why It Works:**

Think of it as an infinite series:

- Visit state j directly: `Q_ij` (1 step)
- Visit via 2 steps: `(Q^2)_ij` (go through one intermediate)
- Visit via 3 steps: `(Q^3)_ij` (go through two intermediates)
- ...and so on

Total expected visits: N = I + Q + Q^2 + Q^3 + \dots$

This infinite geometric series sums to `(I - Q)^-1` (just like `1 + r + r^2 + dots = frac11-r`)

**Absorption Probabilities:**

Once we know N (expected visits to transient states), we multiply by R (probabilities of jumping to absorbing states from transient states) to get B = N \times R$, which gives the probability of ending in each absorbing state.

## Naive Approach

### Intuition

Simulate random walks until absorption.

### Algorithm

Monte Carlo simulation.

### Time Complexity

- **O(Trials \cdot Steps)**. Inaccurate and slow.

## Optimal Approach

### Key Insight

Use Gaussian Elimination to invert the matrix `(I - Q)` or solve the linear systems directly.
Since we only need the result for a specific start state s, we can solve the linear equations just for variable s (or all variables if we want full matrix).
Given n is small (20), full matrix operations are easiest.

### Algorithm Flowchart

```
                ┌─────────────────┐
                │  Input: P, s    │
                └────────┬─────────┘
                         ↓
            ┌────────────────────────┐
            │ Identify Absorbing     │
            │ (P[i][i] = 1.0)       │
            └────────┬────────────────┘
                     ↓
          ┌──────────────────────┐
          │ Is start state s     │────Yes──→ ┌────────────────┐
          │ absorbing?           │           │ Steps = 0      │
          └──────────┬───────────┘           │ Prob[s] = 1.0  │
                     │ No                    │ Others = 0.0   │
                     ↓                       └────────────────┘
         ┌────────────────────────┐
         │ Separate states into:  │
         │ • Transient list (T)   │
         │ • Absorbing list (A)   │
         └────────┬───────────────┘
                  ↓
      ┌───────────────────────────┐
      │ Build Q matrix (T × T)    │
      │ Build R matrix (T × A)    │
      └────────┬──────────────────┘
               ↓
      ┌───────────────────────────┐
      │ Compute I - Q             │
      └────────┬──────────────────┘
               ↓
      ┌───────────────────────────┐
      │ Invert: N = (I-Q)^(-1)    │
      │ (Gaussian Elimination)    │
      └────────┬──────────────────┘
               ↓
      ┌───────────────────────────┐
      │ Find s_idx in transient   │
      │ list                      │
      └────────┬──────────────────┘
               ↓
      ┌───────────────────────────┐
      │ Expected Steps:           │
      │ E = Σ N[s_idx][j]        │
      └────────┬──────────────────┘
               ↓
      ┌───────────────────────────┐
      │ Absorption Probs:         │
      │ B[j] = Σ N[s_idx][k]×R[k][j] │
      └────────┬──────────────────┘
               ↓
         ┌─────────────┐
         │   Output    │
         └─────────────┘
```

### Detailed Algorithm Steps

1. Identify absorbing states (P_ii == 1).
2. If start state s is absorbing:
   - Expected steps = 0.
   - Probs: 1.0 for s, 0.0 for others.
   - Return.
3. Separate states into Transient (T) and Absorbing (A).
4. Construct submatrices Q (TxT) and R (TxA).
5. Compute I - Q$.
6. Invert M = I - Q$ to get N.
7. Expected steps from s: Sum of row in N corresponding to s.
   - Note: s is an index in original matrix. Map it to index in T.
8. Absorption probs from s: Row in B = N \times R$ corresponding to s.
9. Print results.

### Time Complexity

- **O(n^3)** for inversion.

### Space Complexity

- **O(n^2)**.

![Algorithm Visualization](../images/PRB-010/algorithm-visualization.png)
![Algorithm Steps](../images/PRB-010/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    // Gaussian elimination to invert matrix
    public double[][] invert(double[][] A) {
        int n = A.length;
        double[][] B = new double[n][2 * n];

        // Augment with Identity
        for (int i = 0; i < n; i++) {
            System.arraycopy(A[i], 0, B[i], 0, n);
            B[i][n + i] = 1;
        }

        for (int i = 0; i < n; i++) {
            // Pivot
            int pivot = i;
            for (int j = i + 1; j < n; j++) {
                if (Math.abs(B[j][i]) > Math.abs(B[pivot][i])) pivot = j;
            }
            double[] temp = B[i]; B[i] = B[pivot]; B[pivot] = temp;

            double div = B[i][i];
            for (int j = i; j < 2 * n; j++) B[i][j] /= div;

            for (int k = 0; k < n; k++) {
                if (k != i) {
                    double factor = B[k][i];
                    for (int j = i; j < 2 * n; j++) B[k][j] -= factor * B[i][j];
                }
            }
        }

        double[][] res = new double[n][n];
        for (int i = 0; i < n; i++) {
            System.arraycopy(B[i], n, res[i], 0, n);
        }
        return res;
    }

    public double[] absorptionStats(double[][] P, int s) {
        int n = P.length;
        List<Integer> absorbing = new ArrayList<>();
        List<Integer> transientStates = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            boolean isAbsorbing = true;
            for (int j = 0; j < n; j++) {
                if (i != j && P[i][j] > 0) {
                    isAbsorbing = false;
                    break;
                }
            }
            // Or simpler: P[i][i] == 1.0 (assuming rows sum to 1)
            if (Math.abs(P[i][i] - 1.0) < 1e-9) isAbsorbing = true;

            if (isAbsorbing) absorbing.add(i);
            else transientStates.add(i);
        }

        // Base case: Start is absorbing
        if (absorbing.contains(s)) {
            double[] res = new double[1 + absorbing.size()];
            res[0] = 0.0;
            for (int i = 0; i < absorbing.size(); i++) {
                res[i + 1] = (absorbing.get(i) == s) ? 1.0 : 0.0;
            }
            return res;
        }

        int tSize = transientStates.size();
        int aSize = absorbing.size();

        double[][] Q = new double[tSize][tSize];
        double[][] R = new double[tSize][aSize];

        for (int i = 0; i < tSize; i++) {
            int u = transientStates.get(i);
            for (int j = 0; j < tSize; j++) {
                int v = transientStates.get(j);
                Q[i][j] = P[u][v];
            }
            for (int j = 0; j < aSize; j++) {
                int v = absorbing.get(j);
                R[i][j] = P[u][v];
            }
        }

        // I - Q
        double[][] I_minus_Q = new double[tSize][tSize];
        for (int i = 0; i < tSize; i++) {
            for (int j = 0; j < tSize; j++) {
                I_minus_Q[i][j] = (i == j ? 1.0 : 0.0) - Q[i][j];
            }
        }

        double[][] N = invert(I_minus_Q);

        // Find index of s in transient list
        int sIdx = transientStates.indexOf(s);

        // Expected steps: Sum of row sIdx in N
        double expectedSteps = 0;
        for (int j = 0; j < tSize; j++) expectedSteps += N[sIdx][j];

        // Absorption probs: Row sIdx of N * R
        double[] probs = new double[aSize];
        for (int j = 0; j < aSize; j++) {
            for (int k = 0; k < tSize; k++) {
                probs[j] += N[sIdx][k] * R[k][j];
            }
        }

        double[] result = new double[1 + aSize];
        result[0] = expectedSteps;
        System.arraycopy(probs, 0, result, 1, aSize);
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int s = sc.nextInt();
            double[][] P = new double[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    P[i][j] = sc.nextDouble();
                }
            }

            Solution solution = new Solution();
            double[] res = solution.absorptionStats(P, s);
            if (res.length > 0) {
                System.out.printf("%.6f\n", res[0]);
                for (int i = 1; i < res.length; i++) {
                    System.out.printf("%.6f", res[i]);
                    if (i + 1 < res.length) System.out.print(" ");
                }
                System.out.println();
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def invert(A):
    n = len(A)
    # Augment
    M = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(A)]

    for i in range(n):
        pivot = i
        for j in range(i + 1, n):
            if abs(M[j][i]) > abs(M[pivot][i]):
                pivot = j
        M[i], M[pivot] = M[pivot], M[i]

        div = M[i][i]
        for j in range(i, 2 * n):
            M[i][j] /= div

        for k in range(n):
            if k != i:
                factor = M[k][i]
                for j in range(i, 2 * n):
                    M[k][j] -= factor * M[i][j]

    return [row[n:] for row in M]

def absorption_stats(P, s: int):
    n = len(P)
    absorbing = []
    transient = []

    for i in range(n):
        if abs(P[i][i] - 1.0) < 1e-9:
            absorbing.append(i)
        else:
            transient.append(i)

    if s in absorbing:
        res = [0.0]
        for idx in absorbing:
            res.append(1.0 if idx == s else 0.0)
        return res

    t_size = len(transient)
    a_size = len(absorbing)

    Q = [[0.0] * t_size for _ in range(t_size)]
    R = [[0.0] * a_size for _ in range(t_size)]

    for i in range(t_size):
        u = transient[i]
        for j in range(t_size):
            v = transient[j]
            Q[i][j] = P[u][v]
        for j in range(a_size):
            v = absorbing[j]
            R[i][j] = P[u][v]

    I_minus_Q = [[(1.0 if i == j else 0.0) - Q[i][j] for j in range(t_size)] for i in range(t_size)]
    N = invert(I_minus_Q)

    s_idx = transient.index(s)

    expected_steps = sum(N[s_idx])

    probs = [0.0] * a_size
    for j in range(a_size):
        for k in range(t_size):
            probs[j] += N[s_idx][k] * R[k][j]

    return [expected_steps] + probs

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    iterator = iter(data)
    try:
        n = int(next(iterator))
        s = int(next(iterator))
        P = []
        for _ in range(n):
            row = []
            for _ in range(n):
                row.append(float(next(iterator)))
            P.append(row)

        res = absorption_stats(P, s)
        if res:
            print(f"{res[0]:.6f}")
            print(" ".join(f"{x:.6f}" for x in res[1:]))
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

using namespace std;

class Solution {
    vector<vector<double>> invert(vector<vector<double>> A) {
        int n = A.size();
        vector<vector<double>> B(n, vector<double>(2 * n));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) B[i][j] = A[i][j];
            B[i][n + i] = 1;
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

public:
    vector<double> absorptionStats(const vector<vector<double>>& P, int s) {
        int n = P.size();
        vector<int> absorbing, transient;

        for (int i = 0; i < n; i++) {
            if (abs(P[i][i] - 1.0) < 1e-9) absorbing.push_back(i);
            else transient.push_back(i);
        }

        bool startIsAbsorbing = false;
        for (int idx : absorbing) if (idx == s) startIsAbsorbing = true;

        if (startIsAbsorbing) {
            vector<double> res;
            res.push_back(0.0);
            for (int idx : absorbing) res.push_back(idx == s ? 1.0 : 0.0);
            return res;
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
        for (int i = 0; i < tSize; i++) if (transient[i] == s) sIdx = i;

        double expectedSteps = 0;
        for (int j = 0; j < tSize; j++) expectedSteps += N[sIdx][j];

        vector<double> probs(aSize, 0.0);
        for (int j = 0; j < aSize; j++) {
            for (int k = 0; k < tSize; k++) {
                probs[j] += N[sIdx][k] * R[k][j];
            }
        }

        vector<double> result;
        result.push_back(expectedSteps);
        for (double p : probs) result.push_back(p);
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, s;
    if (cin >> n >> s) {
        vector<vector<double>> P(n, vector<double>(n));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) cin >> P[i][j];
        }

        Solution solution;
        vector<double> res = solution.absorptionStats(P, s);
        if (!res.empty()) {
            cout << fixed << setprecision(6) << res[0] << "\n";
            for (int i = 1; i < (int)res.size(); i++) {
                if (i > 1) cout << " ";
                cout << fixed << setprecision(6) << res[i];
            }
            cout << "\n";
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function invert(A) {
  const n = A.length;
  const B = Array(n)
    .fill(0)
    .map(() => Array(2 * n).fill(0));

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) B[i][j] = A[i][j];
    B[i][n + i] = 1;
  }

  for (let i = 0; i < n; i++) {
    let pivot = i;
    for (let j = i + 1; j < n; j++) {
      if (Math.abs(B[j][i]) > Math.abs(B[pivot][i])) pivot = j;
    }
    [B[i], B[pivot]] = [B[pivot], B[i]];

    const div = B[i][i];
    for (let j = i; j < 2 * n; j++) B[i][j] /= div;

    for (let k = 0; k < n; k++) {
      if (k !== i) {
        const factor = B[k][i];
        for (let j = i; j < 2 * n; j++) B[k][j] -= factor * B[i][j];
      }
    }
  }

  const res = Array(n)
    .fill(0)
    .map(() => Array(n).fill(0));
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) res[i][j] = B[i][n + j];
  }
  return res;
}

function absorptionStats(P, s) {
  const n = P.length;
  const absorbing = [];
  const transient = [];

  for (let i = 0; i < n; i++) {
    if (Math.abs(P[i][i] - 1.0) < 1e-9) absorbing.push(i);
    else transient.push(i);
  }

  if (absorbing.includes(s)) {
    const res = [0.0];
    for (const idx of absorbing) res.push(idx === s ? 1.0 : 0.0);
    return res;
  }

  const tSize = transient.length;
  const aSize = absorbing.length;

  const Q = Array(tSize)
    .fill(0)
    .map(() => Array(tSize).fill(0));
  const R = Array(tSize)
    .fill(0)
    .map(() => Array(aSize).fill(0));

  for (let i = 0; i < tSize; i++) {
    const u = transient[i];
    for (let j = 0; j < tSize; j++) {
      const v = transient[j];
      Q[i][j] = P[u][v];
    }
    for (let j = 0; j < aSize; j++) {
      const v = absorbing[j];
      R[i][j] = P[u][v];
    }
  }

  const I_minus_Q = Array(tSize)
    .fill(0)
    .map((_, i) =>
      Array(tSize)
        .fill(0)
        .map((_, j) => (i === j ? 1.0 : 0.0) - Q[i][j])
    );

  const N = invert(I_minus_Q);

  const sIdx = transient.indexOf(s);

  let expectedSteps = 0;
  for (let j = 0; j < tSize; j++) expectedSteps += N[sIdx][j];

  const probs = Array(aSize).fill(0);
  for (let j = 0; j < aSize; j++) {
    for (let k = 0; k < tSize; k++) {
      probs[j] += N[sIdx][k] * R[k][j];
    }
  }

  return [expectedSteps, ...probs];
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  if (lines.length === 0) return;
  let idx = 0;
  const first = lines[idx++].split(/\s+/).map(Number);
  const n = first[0];
  const s = first[1];
  const P = [];
  for (let i = 0; i < n; i++) {
    P.push(lines[idx++].split(/\s+/).map(Number));
  }
  const res = absorptionStats(P, s);
  if (res.length > 0) {
    console.log(res[0].toFixed(6));
    if (res.length > 1) {
      console.log(
        res
          .slice(1)
          .map((x) => x.toFixed(6))
          .join(" ")
      );
    } else {
      console.log("");
    }
  }
});
```

## 🧪 Test Case Walkthrough (Dry Run)

### Example: Simple 3-State Chain

**Input:**

```
3 0
0.5 0.5 0
0 0.5 0.5
0 0 1
```

**Step-by-Step Visualization:**

```
State Diagram:
     0.5       0.5
  0 ────→ 1 ────→ [2]
  ↑       ↑       Absorbing
  │ 0.5   │ 0.5   (Stays forever)
  └───────┘
```

**Step 1: Identify States**

- Absorbing states: {2} (P[2][2] = 1.0)
- Transient states: {0, 1}
- Start state: s = 0 (transient)

**Step 2: Build Submatrices**

Original Matrix P:

```
     0    1    2
0 [0.5  0.5  0.0]
1 [0.0  0.5  0.5]
2 [0.0  0.0  1.0]
```

Extract Q (Transient → Transient):

```
Q =  0    1
  0[0.5  0.5]
  1[0.0  0.5]
```

Extract R (Transient → Absorbing):

```
R =  2
  0[0.0]
  1[0.5]
```

**Step 3: Compute I - Q**

```
I - Q =  0    1
      0[0.5 -0.5]
      1[0.0  0.5]
```

**Step 4: Invert to get N**

Using Gaussian elimination:

```
N = (I - Q)^(-1) =  0   1
                  0[2.0 2.0]
                  1[0.0 2.0]
```

**Interpretation of N:**

- N[0][0] = 2.0: Starting from state 0, visit state 0 an average of 2 times
- N[0][1] = 2.0: Starting from state 0, visit state 1 an average of 2 times
- N[1][1] = 2.0: Starting from state 1, visit state 1 an average of 2 times

**Step 5: Calculate Expected Steps**

For s = 0:

```
E[0] = Σ N[0][j] = N[0][0] + N[0][1]
     = 2.0 + 2.0
     = 4.0 steps
```

**Step 6: Calculate Absorption Probabilities**

B = N × R:

```
B[0][2] = N[0][0] × R[0][0] + N[0][1] × R[1][0]
        = 2.0 × 0.0 + 2.0 × 0.5
        = 0.0 + 1.0
        = 1.0
```

**Output:**

```
4.000000      (Expected steps)
1.000000      (Probability of absorbing into state 2)
```

**Verification:**

- Makes sense! From state 0, you can only reach state 2 eventually
- On average, you bounce between states 0 and 1 about 4 times before reaching 2
- Probability of ending in state 2 is 100% (only absorbing state reachable)

## ✅ Proof of Correctness

### Invariant

The Fundamental Matrix N correctly sums the geometric series of visits to transient states.

### Why the approach is correct

Standard linear algebra solution for Absorbing Markov Chains.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** PageRank.
  - _Hint:_ Eigenvector of transition matrix (for ergodic chains).
- **Extension 2:** Sparse Matrices.
  - _Hint:_ Use iterative methods (Power Iteration) if n is large.
- **Extension 3:** Infinite State Space.
  - _Hint:_ Random Walk on 1D line (Gambler's Ruin).

### Common Mistakes to Avoid

1. **Singular Matrix**
   - ❌ Wrong: Assuming `I-Q` is always invertible.
   - ✅ Correct: It is invertible if every transient state can eventually reach an absorbing state.
2. **Row Sums**
   - ❌ Wrong: Rows not summing to 1.
   - ✅ Correct: Verify input validity.

## Related Concepts

- **Eigenvalues:** 1 is always an eigenvalue of stochastic matrices.
- **Dynamic Programming:** Special case when graph is a DAG.
