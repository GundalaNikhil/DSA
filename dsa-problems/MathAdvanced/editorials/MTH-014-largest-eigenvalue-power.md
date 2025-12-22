---
problem_id: MTH_LARGEST_EIGENVALUE_POWER__2197
display_id: MTH-014
slug: largest-eigenvalue-power
title: "Largest Eigenvalue Power Method"
difficulty: Medium
difficulty_score: 58
topics:
  - MathAdvanced
  - Largest
tags:
  - math-advanced
  - eigenvalue
  - medium
premium: true
subscription_tier: basic
---

# MTH-014: Largest Eigenvalue Power Method

## 📋 Problem Summary

Find the **largest eigenvalue** (by absolute value) of a square matrix $A$ using the **Power Iteration** method.
- Start with a random vector $v$.
- Repeatedly apply $v_{new} = A v_{old}$.
- Normalize $v$ at each step to prevent overflow.
- The Rayleigh Quotient $\frac{v^T A v}{v^T v}$ converges to the largest eigenvalue $\lambda_{max}$.

## 🌍 Real-World Scenario

**Scenario Title:** The Search Engine Ranker

Google's original **PageRank** algorithm is essentially finding the principal eigenvector of the web graph's transition matrix.
- The web is a graph where pages are nodes and links are edges.
- A "random surfer" moves from page to page.
- The probability distribution of the surfer's location after infinite steps is the **stationary distribution**.
- This stationary distribution is the eigenvector corresponding to the eigenvalue 1 (which is the largest for stochastic matrices).
- By computing this, search engines determine the "importance" of a webpage.

**Why This Problem Matters:**

- **Data Science:** Principal Component Analysis (PCA) finds directions of maximum variance (eigenvectors of covariance matrix).
- **Structural Engineering:** Resonance frequencies are eigenvalues of the stiffness matrix.
- **Quantum Mechanics:** Energy levels are eigenvalues of the Hamiltonian.

![Real-World Application](../images/MTH-014/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Convergence

Imagine a vector $v$ as a mix of all eigenvectors $e_1, e_2, \dots$.
$v = c_1 e_1 + c_2 e_2 + \dots$
Applying $A$:
$Av = c_1 \lambda_1 e_1 + c_2 \lambda_2 e_2 + \dots$
Applying $A^k$:
$A^k v = c_1 \lambda_1^k e_1 + c_2 \lambda_2^k e_2 + \dots$

If $|\lambda_1| > |\lambda_2|$, then for large $k$, the term $\lambda_1^k$ dominates.
$A^k v \approx c_1 \lambda_1^k e_1$.
The vector aligns with the direction of $e_1$.

```
       /
      /  e1 (Strong pull)
     /
    /
   v_0 -> v_1 -> v_2 -> ... -> v_inf (Aligned with e1)
```

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** Matrix $A$, max iterations, tolerance $\epsilon$.
- **Output:** A single float.
- **Normalization:** Divide vector by its norm (Euclidean or Max-norm) at each step. Max-norm ($L_\infty$) is cheaper and sufficient.
- **Convergence Check:** If $|\lambda_{new} - \lambda_{old}| < \epsilon$, stop.

### Core Concept: Rayleigh Quotient

Once $v$ is close to the eigenvector $e$, $Av \approx \lambda v$.
We can find $\lambda$ by projecting $Av$ onto $v$:
$\lambda \approx \frac{v \cdot Av}{v \cdot v}$.
If $v$ is normalized ($v \cdot v = 1$), then $\lambda \approx v \cdot Av$.

## Naive Approach

### Intuition

Analytic solution (Characteristic Polynomial).

### Algorithm

Compute $\det(A - \lambda I)$, solve polynomial roots.
- **Impossible** for $N > 4$ analytically (Abel-Ruffini).
- Numerical root finding is complex.

## Optimal Approach

### Key Insight

Power Iteration is simple, robust, and effective for the largest eigenvalue.

### Algorithm

1. Initialize $v$ to a random vector (e.g., all 1s).
2. Loop `iter` from 1 to `maxIter`:
   - Compute $w = A v$.
   - Find $\lambda = \frac{v \cdot w}{v \cdot v}$ (Rayleigh Quotient).
   - Normalize $w$: $v = w / \|w\|_\infty$ (divide by element with max absolute value).
   - Check convergence: If $|\lambda - \lambda_{old}| < \epsilon$, break.
   - Update $\lambda_{old} = \lambda$.
3. Return $\lambda$.

### Time Complexity

- **O(k \cdot n^2)** where $k$ is iterations.

### Space Complexity

- **O(n^2)** to store matrix.

![Algorithm Visualization](../images/MTH-014/algorithm-visualization.png)
![Algorithm Steps](../images/MTH-014/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public double largest_eigenvalue_power(int n, int maxIter, double[][] matrix, double epsilon) {
        double[] v = new double[n];
        Arrays.fill(v, 1.0); // Initial guess
        
        double lambda = 0.0;
        
        for (int iter = 0; iter < maxIter; iter++) {
            // w = A * v
            double[] w = new double[n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    w[i] += matrix[i][j] * v[j];
                }
            }
            
            // Rayleigh Quotient: num = v dot w, den = v dot v
            double num = 0.0;
            double den = 0.0;
            for (int i = 0; i < n; i++) {
                num += v[i] * w[i];
                den += v[i] * v[i];
            }
            
            double newLambda = (den == 0) ? 0 : num / den;
            
            if (Math.abs(newLambda - lambda) < epsilon) {
                return newLambda;
            }
            lambda = newLambda;
            
            // Normalize w
            double maxVal = 0.0;
            for (double val : w) maxVal = Math.max(maxVal, Math.abs(val));
            
            if (maxVal < 1e-9) break; // Zero vector
            
            for (int i = 0; i < n; i++) {
                v[i] = w[i] / maxVal;
            }
        }
        
        return lambda;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        int maxIter = sc.nextInt();
        
        double[][] matrix = new double[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = sc.nextDouble();
            }
        }
        
        double epsilon = sc.nextDouble();
        
        Solution solution = new Solution();
        double res = solution.largest_eigenvalue_power(n, maxIter, matrix, epsilon);
        
        System.out.printf("%.6f\n", res);
        sc.close();
    }
}
```

### Python

```python
import sys
import math

class Solution:
    def largest_eigenvalue_power(self, n: int, maxIter: int, matrix: list[list[float]], epsilon: float) -> float:
        v = [1.0] * n
        lambda_val = 0.0
        
        for _ in range(maxIter):
            # w = A * v
            w = [0.0] * n
            for i in range(n):
                for j in range(n):
                    w[i] += matrix[i][j] * v[j]
            
            # Rayleigh Quotient
            num = sum(v[i] * w[i] for i in range(n))
            den = sum(v[i] * v[i] for i in range(n))
            
            new_lambda = 0.0 if den == 0 else num / den
            
            if abs(new_lambda - lambda_val) < epsilon:
                return new_lambda
            
            lambda_val = new_lambda
            
            # Normalize
            max_val = max(abs(x) for x in w)
            if max_val < 1e-9: break
            
            v = [x / max_val for x in w]
            
        return lambda_val

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        maxIter = int(next(iterator))
        
        matrix = []
        for _ in range(n):
            row = [float(next(iterator)) for _ in range(n)]
            matrix.append(row)
            
        epsilon = float(next(iterator))
        
        sol = Solution()
        res = sol.largest_eigenvalue_power(n, maxIter, matrix, epsilon)
        print(f"{res:.6f}")
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
using namespace std;

class Solution {
public:
    double largest_eigenvalue_power(int n, int maxIter, vector<vector<double>>& matrix, double epsilon) {
        vector<double> v(n, 1.0);
        double lambda = 0.0;

        for (int iter = 0; iter < maxIter; iter++) {
            vector<double> w(n, 0.0);
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    w[i] += matrix[i][j] * v[j];
                }
            }

            double num = 0.0;
            double den = 0.0;
            for (int i = 0; i < n; i++) {
                num += v[i] * w[i];
                den += v[i] * v[i];
            }

            double newLambda = (den == 0) ? 0 : num / den;

            if (abs(newLambda - lambda) < epsilon) {
                return newLambda;
            }
            lambda = newLambda;

            double maxVal = 0.0;
            for (double val : w) maxVal = max(maxVal, abs(val));

            if (maxVal < 1e-9) break;

            for (int i = 0; i < n; i++) {
                v[i] = w[i] / maxVal;
            }
        }

        return lambda;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, maxIter;
    if (!(cin >> n >> maxIter)) return 0;

    vector<vector<double>> matrix(n, vector<double>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> matrix[i][j];
        }
    }

    double epsilon;
    cin >> epsilon;

    Solution solution;
    double res = solution.largest_eigenvalue_power(n, maxIter, matrix, epsilon);

    cout << fixed << setprecision(6) << res << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  largest_eigenvalue_power(n, maxIter, matrix, epsilon) {
    let v = new Array(n).fill(1.0);
    let lambda = 0.0;

    for (let iter = 0; iter < maxIter; iter++) {
      let w = new Array(n).fill(0.0);
      for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
          w[i] += matrix[i][j] * v[j];
        }
      }

      let num = 0.0;
      let den = 0.0;
      for (let i = 0; i < n; i++) {
        num += v[i] * w[i];
        den += v[i] * v[i];
      }

      let newLambda = (den === 0) ? 0 : num / den;

      if (Math.abs(newLambda - lambda) < epsilon) {
        return newLambda;
      }
      lambda = newLambda;

      let maxVal = 0.0;
      for (let val of w) maxVal = Math.max(maxVal, Math.abs(val));

      if (maxVal < 1e-9) break;

      for (let i = 0; i < n; i++) {
        v[i] = w[i] / maxVal;
      }
    }

    return lambda;
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
  let ptr = 0;
  
  const n = parseInt(data[ptr++]);
  const maxIter = parseInt(data[ptr++]);
  
  const matrix = [];
  for(let i=0; i<n; i++) {
      const row = [];
      for(let j=0; j<n; j++) row.push(parseFloat(data[ptr++]));
      matrix.push(row);
  }
  
  const epsilon = parseFloat(data[ptr++]);
  
  const solution = new Solution();
  const res = solution.largest_eigenvalue_power(n, maxIter, matrix, epsilon);
  
  console.log(res.toFixed(6));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `A = [[2, 0], [0, 1]]`.
1. `v = [1, 1]`.
2. `w = A v = [2, 1]`.
3. `RQ = (1*2 + 1*1) / (1*1 + 1*1) = 3/2 = 1.5`.
4. `Norm w`: max is 2. `v = [1, 0.5]`.
5. `w = A v = [2, 0.5]`.
6. `RQ = (1*2 + 0.5*0.5) / (1*1 + 0.5*0.5) = 2.25 / 1.25 = 1.8`.
7. `Norm w`: max is 2. `v = [1, 0.25]`.
8. Converges to `v = [1, 0]`, `lambda = 2`.

![Example Visualization](../images/MTH-014/example-1.png)

## ✅ Proof of Correctness

### Invariant
The vector $v$ aligns closer to the principal eigenvector with each iteration.
The Rayleigh Quotient provides an increasingly accurate estimate of the eigenvalue.

### Why the approach is correct
- Assuming a unique largest eigenvalue, the component of $v$ in the direction of the principal eigenvector grows as $(\lambda_1 / \lambda_2)^k$.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Inverse Iteration.
  - *Hint:* Apply power method to $(A - \mu I)^{-1}$ to find eigenvalue closest to $\mu$.
- **Extension 2:** Deflation.
  - *Hint:* Find largest, remove it, find next largest.
- **Extension 3:** QR Algorithm.
  - *Hint:* Finds all eigenvalues.

### Common Mistakes to Avoid

1. **Normalization**
   - ❌ Wrong: Forgetting to normalize leads to overflow/underflow.
   - ✅ Correct: Divide by norm at each step.

2. **Convergence**
   - ❌ Wrong: Assuming it always works.
   - ✅ Correct: Fails if $\lambda_1 = -\lambda_2$ (oscillation).

## Related Concepts

- **PageRank:** A variant for stochastic matrices.
- **SVD:** Uses power method on $A^T A$.
