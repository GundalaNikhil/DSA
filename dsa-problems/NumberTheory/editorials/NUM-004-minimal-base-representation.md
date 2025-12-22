---
problem_id: NUM_MINIMAL_BASE_REPRESENTATION__6628
display_id: NUM-004
slug: minimal-base-representation
title: "Minimal Base Representation"
difficulty: Medium
difficulty_score: 50
topics:
  - Number Theory
  - Bases
  - Optimization
tags:
  - number-theory
  - bases
  - optimization
  - medium
premium: true
subscription_tier: basic
---

# NUM-004: Minimal Base Representation

## 📋 Problem Summary

Given an integer $x$, find the base $b$ ($2 \le b \le 36$) that minimizes the sum of digits of $x$ in that base.
- Input: Integer $x$.
- Output: The optimal base $b$ and the minimal digit sum.
- Tie-breaking: If multiple bases yield the same sum, choose the smallest base.

## 🌍 Real-World Scenario

**Scenario Title:** The Efficient Data Encoder

In data transmission, you often want to encode numbers in a way that minimizes the "weight" or "cost" of the signal.
- Suppose transmitting a digit $d$ costs $d$ units of energy (e.g., amplitude modulation).
- You want to represent a large number $x$ in a base $b$ such that the total energy required to transmit its digits is minimized.
- However, the receiver hardware only supports bases up to 36 (digits 0-9 and A-Z).
- Your task is to find the optimal base configuration for each packet to save battery life on IoT devices.

**Why This Problem Matters:**

- **Information Theory:** Representing data efficiently.
- **Hardware Design:** Choosing radices for arithmetic units (e.g., binary vs. ternary logic).
- **Numerology:** Digital roots and properties of numbers in different bases.

![Real-World Application](../images/NUM-004/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Base Conversion

Let $x = 31$.

**Base 2:**
$31 = 11111_2$
Sum = $1+1+1+1+1 = 5$.

**Base 3:**
$31 = 1011_3$ ($1 \cdot 27 + 0 \cdot 9 + 1 \cdot 3 + 1 \cdot 1$)
Sum = $1+0+1+1 = 3$.

**Base 5:**
$31 = 111_5$ ($1 \cdot 25 + 1 \cdot 5 + 1 \cdot 1$)
Sum = $1+1+1 = 3$.

**Base 10:**
$31 = 31_{10}$
Sum = $3+1 = 4$.

Minimal sum is 3. Smallest base achieving this is 3.
Let's recheck Base 3.
$31 = 1011_3 \implies 27 + 3 + 1 = 31$. Sum = 3.
Base 5: $111_5 \implies 25 + 5 + 1 = 31$. Sum = 3.
Since 3 < 5, the answer should be Base 3.
**Correction:** The example output in the problem description says `5 3`.
Let's check if I missed something.
Problem: "Smallest base b (2 <= b <= 36)".
My calculation: Base 3 sum is 3. Base 5 sum is 3.
Smallest base is 3.
Why does the example say 5?
Maybe I calculated Base 3 wrong?
$31 / 3 = 10$ rem $1$.
$10 / 3 = 3$ rem $1$.
$3 / 3 = 1$ rem $0$.
$1 / 3 = 0$ rem $1$.
Digits: $1, 0, 1, 1$. $1011_3$. Sum = 3.
Is it possible the example output is just illustrative or I am misinterpreting "smallest base"?
"If multiple bases yield the same minimal digit sum, choose the smallest base."
Okay, let's check Base 2 again. $11111_2 \to 5$.
Base 4: $31 = 133_4$ ($16 + 12 + 3$). Sum = 7.
Base 6: $31 = 51_6$ ($30 + 1$). Sum = 6.
Base 30: $31 = 11_{30}$. Sum = 2.
$31 = 1 \cdot 30 + 1$. Digits 1, 1. Sum 2.
So for $x=31$, the minimal sum is actually 2 (at base 30).
The example output `5 3` is definitely strange if the range is up to 36.
Maybe the example meant $x=31$ with a restricted range? Or maybe my manual calculation of Base 30 is correct and the example is just wrong?
Or maybe the example input is NOT 31?
Input: `31`. Output: `5 3`.
Let's assume the constraints are correct ($2 \le b \le 36$) and the example might be a specific case or I should just implement the logic correctly.
"Given an integer x (>= 2), find the smallest base b (2 <= b <= 36)..."
If $x=31$, Base 30 gives sum 2. Base 3 gives sum 3. Base 5 gives sum 3.
So the answer should be `30 2`.
However, if the example says `5 3`, maybe the input was different?
Let's ignore the specific values in the example output if they contradict the logic, and focus on the correct algorithm. The algorithm is simply to iterate $b$ from 2 to 36.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Constraints:** $x \le 10^{12}$.
- **Base Range:** $2 \le b \le 36$.
- **Digit Sum:** Sum of values of digits. E.g., in base 16, 'A' counts as 10.

### Core Concept: Base Conversion

To find the sum of digits of $x$ in base $b$:
1. Initialize `sum = 0`, `temp = x`.
2. While `temp > 0`:
   - `sum += temp % b`
   - `temp //= b`
3. Return `sum`.

## Naive Approach

### Intuition

Iterate through all bases from 2 to 36.

### Algorithm

1. Initialize `minSum = infinity`, `bestBase = -1`.
2. For `b` from 2 to 36:
   - Calculate `currentSum` for `x` in base `b`.
   - If `currentSum < minSum`:
     - `minSum = currentSum`
     - `bestBase = b`
   - Else if `currentSum == minSum`:
     - Do nothing (since we iterate from smallest base, we already have the smallest `b`).
3. Return `bestBase, minSum`.

### Time Complexity

- **O(36 \cdot \log_2 x)**.
- With $x=10^{12}$, $\log_2 x \approx 40$.
- Total operations $\approx 36 \times 40 \approx 1440$. Extremely fast.

### Space Complexity

- **O(1)**.

## Optimal Approach

### Key Insight

Since the number of bases is very small (35), the "naive" approach IS the optimal approach. There's no need for anything fancier.

### Algorithm

Same as above.

### Time Complexity

- **O(\log x)**.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/NUM-004/algorithm-visualization.png)
![Algorithm Steps](../images/NUM-004/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private long getDigitSum(long x, int b) {
        long sum = 0;
        while (x > 0) {
            sum += x % b;
            x /= b;
        }
        return sum;
    }

    public long[] minimalBase(long x) {
        long minSum = Long.MAX_VALUE;
        long bestBase = 2;
        
        for (int b = 2; b <= 36; b++) {
            long currentSum = getDigitSum(x, b);
            if (currentSum < minSum) {
                minSum = currentSum;
                bestBase = b;
            }
        }
        
        return new long[]{bestBase, minSum};
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long x = sc.nextLong();
            Solution solution = new Solution();
            long[] res = solution.minimalBase(x);
            System.out.println(res[0] + " " + res[1]);
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def get_digit_sum(x: int, b: int) -> int:
    total = 0
    while x > 0:
        total += x % b
        x //= b
    return total

def minimal_base(x: int):
    min_sum = float('inf')
    best_base = 2
    
    for b in range(2, 37):
        current_sum = get_digit_sum(x, b)
        if current_sum < min_sum:
            min_sum = current_sum
            best_base = b
            
    return best_base, min_sum

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    x = int(data[0])
    b, s = minimal_base(x)
    print(f"{b} {s}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
    long long getDigitSum(long long x, int b) {
        long long sum = 0;
        while (x > 0) {
            sum += x % b;
            x /= b;
        }
        return sum;
    }

public:
    pair<long long, long long> minimalBase(long long x) {
        long long minSum = LLONG_MAX;
        long long bestBase = 2;
        
        for (int b = 2; b <= 36; b++) {
            long long currentSum = getDigitSum(x, b);
            if (currentSum < minSum) {
                minSum = currentSum;
                bestBase = b;
            }
        }
        
        return {bestBase, minSum};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long x;
    if (cin >> x) {
        Solution solution;
        auto res = solution.minimalBase(x);
        cout << res.first << " " << res.second << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function getDigitSum(x, b) {
  let sum = 0;
  let temp = x;
  while (temp > 0) {
    sum += temp % b;
    temp = Math.floor(temp / b);
  }
  return sum;
}

function minimalBase(x) {
  let minSum = Infinity;
  let bestBase = 2;
  
  for (let b = 2; b <= 36; b++) {
    const currentSum = getDigitSum(x, b);
    if (currentSum < minSum) {
      minSum = currentSum;
      bestBase = b;
    }
  }
  
  return [bestBase, minSum];
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  const x = parseInt(data[0], 10);
  const res = minimalBase(x);
  console.log(res[0] + " " + res[1]);
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `x = 10`.
1. **b=2:** $10 = 1010_2$. Sum = 2. `minSum=2, bestBase=2`.
2. **b=3:** $10 = 101_3$. Sum = 2. `currentSum == minSum`, no update.
3. **b=4:** $10 = 22_4$. Sum = 4.
4. ...
5. **b=9:** $10 = 11_9$. Sum = 2.
6. **b=11:** $10 = A_{11}$ (digit 10). Sum = 10.
7. Result: `2 2`.

Input: `x = 31`.
1. **b=2:** $11111_2 \to 5$. `min=5, base=2`.
2. **b=3:** $1011_3 \to 3$. `min=3, base=3`.
3. ...
4. **b=5:** $111_5 \to 3$. No update.
5. ...
6. **b=30:** $11_{30} \to 2$. `min=2, base=30`.
7. Result: `30 2`.

## ✅ Proof of Correctness

### Invariant
We exhaustively check every valid base.
The digit sum calculation is mathematically correct.

### Why the approach is correct
Since the search space is small and constant (35 bases), brute force is optimal.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Unbounded Base.
  - *Question:* What if $b$ can be up to $x$?
  - *Answer:* For large $b > \sqrt{x}$, $x$ has at most 2 digits. $x = a \cdot b + c$. We want to minimize $a+c$. This becomes an optimization problem.
- **Extension 2:** Negative Bases.
  - *Question:* How to handle base -2?
  - *Answer:* Digits are still $0, 1$, but positions have alternating signs.
- **Extension 3:** Base Conversion String.
  - *Question:* Return the string representation.
  - *Answer:* Map digits 0-35 to 0-9, A-Z.

### C++ommon Mistakes to Avoid

1. **Loop Bounds**
   - ❌ Wrong: `b < 36`.
   - ✅ Correct: `b <= 36`.
2. **Tie-Breaking**
   - ❌ Wrong: `currentSum <= minSum`.
   - ✅ Correct: `currentSum < minSum` ensures we keep the smallest base for ties.

## Related Concepts

- **Radix Sort:** Uses base properties.
- **Digital Root:** Recursive digit sum.
