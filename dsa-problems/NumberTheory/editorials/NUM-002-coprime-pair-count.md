---
problem_id: NUM_COPRIME_PAIR_COUNT__7194
display_id: NUM-002
slug: coprime-pair-count
title: "Coprime Pair Count Up To N"
difficulty: Medium
difficulty_score: 48
topics:
  - Number Theory
  - Euler Totient
  - Counting
tags:
  - number-theory
  - totient
  - counting
  - medium
premium: true
subscription_tier: basic
---

# NUM-002: Coprime Pair Count Up To N

## 📋 Problem Summary

Count the number of pairs $(i, j)$ such that $1 \le i < j \le N$ and $\text{gcd}(i, j) = 1$.
- Input: Integer $N$.
- Output: Total count of such pairs.

## 🌍 Real-World Scenario

**Scenario Title:** The Secure Key Generator

In RSA cryptography, generating keys involves selecting two large prime numbers. However, in other cryptographic schemes or when generating parameters for Diffie-Hellman key exchange, we often need numbers that are **coprime** (share no common factors) to ensure mathematical inverses exist.
- Imagine you are building a system that tests all possible pairs of parameters up to a certain limit $N$ to find valid configurations.
- A "valid configuration" requires the two parameters to be coprime.
- To estimate the search space or the probability of finding a valid pair randomly, you need to know exactly how many such pairs exist up to $N$.

**Why This Problem Matters:**

- **Cryptography:** Ensuring modular inverses exist (which requires coprimality).
- **Number Theory:** Fundamental counting problem related to the distribution of prime numbers.
- **Algorithm Design:** Efficiently computing properties over a range using sieves.

![Real-World Application](../images/NUM-002/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Coprime Grid

Let $N=4$. We look for pairs $(i, j)$ with $1 \le i < j \le 4$.

```
j=2: (1,2) -> gcd(1,2)=1 ✅
j=3: (1,3) -> gcd(1,3)=1 ✅
     (2,3) -> gcd(2,3)=1 ✅
j=4: (1,4) -> gcd(1,4)=1 ✅
     (2,4) -> gcd(2,4)=2 ❌
     (3,4) -> gcd(3,4)=1 ✅

Total = 1 + 2 + 2 = 5 pairs.
```

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Constraints:** $N \le 100,000$. An $O(N^2)$ solution (checking every pair) will time out ($10^{10}$ ops). We need something close to $O(N)$.
- **Pairs:** Ordered pairs $(i, j)$ with $i < j$. This means for a fixed $j$, we want to count $i < j$ such that $\text{gcd}(i, j) = 1$.
- **Definition:** This count is exactly Euler's Totient Function, $\phi(j)$.

### Core Concept: Euler's Totient Function

$\phi(n)$ is defined as the number of positive integers less than or equal to $n$ that are relatively prime to $n$.
Since we require $i < j$, for a fixed $j$, the number of valid $i$'s is exactly $\phi(j)$.
The total answer is $\sum_{j=2}^{N} \phi(j)$.
(Note: The problem asks for $1 \le i < j$. Since $\text{gcd}(1, j)=1$ always, $i=1$ is included in $\phi(j)$).

## Naive Approach

### Intuition

Iterate all pairs $(i, j)$ and check GCD.

### Algorithm

```python
count = 0
for j in range(2, N + 1):
    for i in range(1, j):
        if gcd(i, j) == 1:
            count += 1
return count
```

### Time Complexity

- **O(N^2 \log N)**. Too slow.

### Space Complexity

- **O(1)**.

## Optimal Approach

### Key Insight

Use a **Linear Sieve** (or Sieve of Eratosthenes) to precompute $\phi(k)$ for all $k$ from 1 to $N$.
Then simply sum them up.

### Algorithm

1. Create an array `phi` where `phi[i] = i`.
2. Iterate `i` from 2 to $N$:
   - If `phi[i] == i`, then `i` is prime.
   - For every multiple `j` of `i` (including `i` itself), update `phi[j]`:
     - `phi[j] -= phi[j] / i`.
     - This implements the formula $\phi(n) = n \prod (1 - 1/p)$.
3. Sum `phi[j]` for $j$ from 2 to $N$.

### Time Complexity

- **O(N \log \log N)** using standard sieve.
- **O(N)** using linear sieve.
- Given $N=10^5$, $O(N \log \log N)$ is perfectly fine and easier to implement.

### Space Complexity

- **O(N)** for the `phi` array.

![Algorithm Visualization](../images/NUM-002/algorithm-visualization.png)
![Algorithm Steps](../images/NUM-002/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public long countCoprimePairs(int N) {
        if (N < 2) return 0;
        
        int[] phi = new int[N + 1];
        for (int i = 0; i <= N; i++) {
            phi[i] = i;
        }
        
        for (int i = 2; i <= N; i++) {
            if (phi[i] == i) { // i is prime
                for (int j = i; j <= N; j += i) {
                    phi[j] -= phi[j] / i;
                }
            }
        }
        
        long total = 0;
        for (int i = 2; i <= N; i++) {
            total += phi[i];
        }
        
        return total;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int N = sc.nextInt();
            Solution solution = new Solution();
            System.out.println(solution.countCoprimePairs(N));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def count_coprime_pairs(N: int) -> int:
    if N < 2:
        return 0
        
    phi = list(range(N + 1))
    
    for i in range(2, N + 1):
        if phi[i] == i:  # i is prime
            for j in range(i, N + 1, i):
                phi[j] -= phi[j] // i
                
    return sum(phi[2:])

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    N = int(data[0])
    print(count_coprime_pairs(N))

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
    long long countCoprimePairs(int N) {
        if (N < 2) return 0;
        
        vector<int> phi(N + 1);
        for (int i = 0; i <= N; i++) phi[i] = i;
        
        for (int i = 2; i <= N; i++) {
            if (phi[i] == i) { // i is prime
                for (int j = i; j <= N; j += i) {
                    phi[j] -= phi[j] / i;
                }
            }
        }
        
        long long total = 0;
        for (int i = 2; i <= N; i++) {
            total += phi[i];
        }
        
        return total;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (cin >> N) {
        Solution solution;
        cout << solution.countCoprimePairs(N) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function countCoprimePairs(N) {
  if (N < 2) return 0;
  
  const phi = new Int32Array(N + 1);
  for (let i = 0; i <= N; i++) phi[i] = i;
  
  for (let i = 2; i <= N; i++) {
    if (phi[i] === i) { // i is prime
      for (let j = i; j <= N; j += i) {
        phi[j] -= Math.floor(phi[j] / i);
      }
    }
  }
  
  let total = 0n; // Use BigInt for safety, though N=10^5 fits in number
  for (let i = 2; i <= N; i++) {
    total += BigInt(phi[i]);
  }
  
  return total.toString();
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  const N = parseInt(data[0], 10);
  console.log(countCoprimePairs(N));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `N = 5`.

1. **Init:** `phi = [0, 1, 2, 3, 4, 5]`.
2. **i=2 (Prime):**
   - Update 2: `phi[2] -= 2/2 = 1`. `phi` is `[..., 1, ...]`.
   - Update 4: `phi[4] -= 4/2 = 2`. `phi` is `[..., 1, ..., 2, ...]`.
3. **i=3 (Prime):**
   - Update 3: `phi[3] -= 3/3 = 2`. `phi` is `[..., 2, ...]`.
4. **i=4 (Not Prime):** `phi[4]=2 != 4`. Skip.
5. **i=5 (Prime):**
   - Update 5: `phi[5] -= 5/5 = 4`. `phi` is `[..., 4]`.
6. **Sum:**
   - `phi[2] + phi[3] + phi[4] + phi[5]`
   - `1 + 2 + 2 + 4 = 9`.
   - Example pairs: (1,2), (1,3), (1,4), (1,5), (2,3), (2,5), (3,4). Total 7.
   - My manual trace:
     - $\phi(2) = 1$ (1)
     - $\phi(3) = 2$ (1, 2)
     - $\phi(4) = 2$ (1, 3)
     - $\phi(5) = 4$ (1, 2, 3, 4)
     - Sum: $1+2+2+4 = 9$.
   - Why is example 7?
   - Ah, the example explanation lists:
     - (1,2) -> $\phi(2)$ counts 1.
     - (1,3), (2,3) -> $\phi(3)$ counts 2.
     - (1,4), (3,4) -> $\phi(4)$ counts 2.
     - (1,5), (2,5), (3,5), (4,5) -> $\phi(5)$ counts 4.
     - Total sum is indeed 9.
   - **Correction:** The example output in the problem file says 7.
   - Let's look at the example pairs again: `(1,2),(1,3),(1,4),(1,5),(2,3),(2,5),(3,4)`.
   - Missing from my list: `(3,5)`? Yes, gcd(3,5)=1. `(4,5)`? Yes, gcd(4,5)=1.
   - The example explanation list seems incomplete or I misread it.
   - "The coprime pairs are: (1,2),(1,3),(1,4),(1,5),(2,3),(2,5),(3,4)".
   - It missed (3,5) and (4,5).
   - "1 <= i < j <= N".
   - If N=5.
   - j=2: (1,2) [1]
   - j=3: (1,3), (2,3) [2]
   - j=4: (1,4), (3,4) [2]
   - j=5: (1,5), (2,5), (3,5), (4,5) [4]
   - Total 9.
   - If the example output is 7, maybe N=4?
   - If N=4, sum is $1+2+2 = 5$.
   - If N=5, sum is 9.
   - Is it possible the example output is wrong in the problem description? Or maybe I am misunderstanding "coprime".
   - GCD(1, 5) = 1. GCD(2, 5) = 1. GCD(3, 5) = 1. GCD(4, 5) = 1.
   - All correct.
   - Let's check the provided example again.
   - Input: 5. Output: 7.
   - Explanation lists 7 pairs.
   - It explicitly lists `(2,5)` but omits `(3,5)` and `(4,5)`.
   - This suggests the example explanation is manually constructed and might be erroneous, OR there's a constraint I missed.
   - "1 <= i < j <= N".
   - Is it possible `i` must be > 1? No, `1 <= i`.
   - Is it possible `gcd(i, j) = 1` excludes `i=1`? Usually `gcd(1, k) = 1`.
   - If `i=1` is excluded:
     - j=2: -
     - j=3: (2,3) [1]
     - j=4: (3,4) [1]
     - j=5: (2,5), (3,5), (4,5) [3]
     - Total 5. Still not 7.
   - What if the example meant N=4? Output 5.
   - What if the example meant N=5 but output 10 (sum of phi from 1 to 5)? $\phi(1)=1$. Total 10.
   - Let's assume the standard interpretation: $\sum_{k=2}^N \phi(k)$.
   - I will stick to the mathematical definition. The example output in the problem file might be illustrative or slightly off, but the definition "count pairs with gcd=1" is standard.
   - "(1,2),(1,3),(1,4),(1,5),(2,3),(2,5),(3,4)".
   - It has 4 pairs with 1.
   - It has 2 pairs with 2.
   - It has 1 pair with 3.
   - It has 0 pairs with 4.
   - It seems to be missing pairs for 5.
   - I will implement the standard solution $\sum \phi(i)$.

## ✅ Proof of Correctness

### Invariant
The number of integers $i < j$ such that $\text{gcd}(i, j) = 1$ is exactly $\phi(j)$.
Thus, the total count is $\sum_{j=2}^N \phi(j)$.

### Why the approach is correct
The sieve correctly computes $\phi(j)$ for all $j$ using the multiplicative property and the formula $\phi(n) = n \prod (1 - 1/p)$.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Sum of GCDs of all pairs.
  - *Hint:* $\sum_{g=1}^N g \cdot \text{count pairs with gcd } g$.
- **Extension 2:** $N$ up to $10^{12}$.
  - *Hint:* Use Min_25 sieve or Du Jiao sieve (advanced).
- **Extension 3:** Probability that two random numbers are coprime.
  - *Hint:* Approaches $6/\pi^2$ as $N \to \infty$.

### C++ommon Mistakes to Avoid

1. **Integer Overflow**
   - ❌ Wrong: Using `int` for the sum. For $N=10^5$, sum can be $\approx \frac{3}{\pi^2} N^2 \approx 3 \cdot 10^9$, which exceeds signed 32-bit int ($2 \cdot 10^9$).
   - ✅ Correct: Use `long` (Java/C++) or `BigInt` (JS).
2. **Sieve Complexity**
   - ❌ Wrong: Nested loops without checking primality ($O(N^2)$).
   - ✅ Correct: Only iterate multiples for primes ($O(N \log \log N)$).

## Related Concepts

- **Mobius Inversion:** Another way to count coprime pairs.
- **Sieve of Eratosthenes:** Basis for the solution.
