---
problem_id: NUM_LATTICE_POINTS_ON_SEGMENT__6330
display_id: NUM-008
slug: lattice-points-on-segment
title: "Counting Lattice Points On Segment"
difficulty: Easy
difficulty_score: 28
topics:
  - Number Theory
  - Geometry
  - GCD
tags:
  - number-theory
  - geometry
  - gcd
  - easy
premium: true
subscription_tier: basic
---

# NUM-008: Counting Lattice Points On Segment

## 📋 Problem Summary

Given two points $(x_1, y_1)$ and $(x_2, y_2)$ on a 2D grid, count the number of integer coordinates (lattice points) that lie exactly on the line segment connecting them.
- Input: Coordinates $x_1, y_1, x_2, y_2$.
- Output: Integer count.

## 🌍 Real-World Scenario

**Scenario Title:** The Streetlight Planner

You are an urban planner designing a new straight road connecting two intersections at coordinates $(x_1, y_1)$ and $(x_2, y_2)$.
- To ensure proper illumination, you want to place streetlights at regular intervals along this road.
- However, for structural stability and grid alignment, streetlights can only be placed at integer grid coordinates.
- You need to know how many valid spots exist on this segment (including the endpoints) to order the correct number of lamp posts.

**Why This Problem Matters:**

- **Computer Graphics:** Rasterizing lines (Bresenham's algorithm steps).
- **Pick's Theorem:** Calculating the area of a polygon on a grid requires counting boundary lattice points.
- **Diophantine Equations:** Solving linear equations with integer constraints.

![Real-World Application](../images/NUM-008/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Line Segment

Points: $(0, 0)$ to $(6, 4)$.
$\Delta x = 6, \Delta y = 4$.

```
(0,0) * . . . . .
      . . . . . .
      . . . * . . (3,2)
      . . . . . .
      . . . . . * (6,4)
```

The slope is $4/6 = 2/3$.
This means for every 3 steps right, we go 2 steps up to hit an integer point.
Steps:
1. $(0, 0)$
2. $(0+3, 0+2) = (3, 2)$
3. $(3+3, 2+2) = (6, 4)$
Total points: 3.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Constraints:** Coordinates up to $10^9$.
- **Negative Coordinates:** The formula works with absolute differences $|\Delta x|$ and $|\Delta y|$.
- **Vertical/Horizontal Lines:**
  - If $x_1=x_2$, count is $|y_1 - y_2| + 1$.
  - If $y_1=y_2$, count is $|x_1 - x_2| + 1$.
  - This is consistent with the general formula.

### Core Concept: GCD and Slope

The number of steps to get from $(x_1, y_1)$ to $(x_2, y_2)$ hitting integer points is determined by reducing the slope $\frac{\Delta y}{\Delta x}$ to its simplest form.
Let $g = \text{gcd}(|\Delta x|, |\Delta y|)$.
The reduced step size is $(\frac{\Delta x}{g}, \frac{\Delta y}{g})$.
The number of intervals is exactly $g$.
The number of points is $g + 1$ (since we include both endpoints).

## Naive Approach

### Intuition

Iterate through all x-coordinates between $x_1$ and $x_2$, calculate corresponding $y$, and check if it's an integer.

### Algorithm

```python
count = 0
for x in range(min(x1, x2), max(x1, x2) + 1):
    y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
    if is_integer(y):
        count += 1
```

### Time Complexity

- **O(|\Delta x|)**. With coordinates up to $10^9$, this is too slow.

### Space Complexity

- **O(1)**.

## Optimal Approach

### Key Insight

Use the GCD formula directly.
Count = $\text{gcd}(|x_1 - x_2|, |y_1 - y_2|) + 1$.

### Algorithm

1. Compute $dx = |x_1 - x_2|$.
2. Compute $dy = |y_1 - y_2|$.
3. Return $\text{gcd}(dx, dy) + 1$.

### Time Complexity

- **O(\log(\min(dx, dy)))** for GCD. Extremely fast.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/NUM-008/algorithm-visualization.png)
![Algorithm Steps](../images/NUM-008/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private long gcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public long latticePoints(long x1, long y1, long x2, long y2) {
        long dx = Math.abs(x1 - x2);
        long dy = Math.abs(y1 - y2);
        return gcd(dx, dy) + 1;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long x1 = sc.nextLong();
            long y1 = sc.nextLong();
            long x2 = sc.nextLong();
            long y2 = sc.nextLong();
            
            Solution solution = new Solution();
            System.out.println(solution.latticePoints(x1, y1, x2, y2));
        }
        sc.close();
    }
}
```

### Python

```python
import sys
from math import gcd

def lattice_points(x1: int, y1: int, x2: int, y2: int) -> int:
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return gcd(dx, dy) + 1

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    x1, y1, x2, y2 = map(int, data)
    print(lattice_points(x1, y1, x2, y2))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <numeric>
#include <cmath>

using namespace std;

class Solution {
    long long gcd(long long a, long long b) {
        while (b) {
            a %= b;
            swap(a, b);
        }
        return a;
    }

public:
    long long latticePoints(long long x1, long long y1, long long x2, long long y2) {
        long long dx = abs(x1 - x2);
        long long dy = abs(y1 - y2);
        return gcd(dx, dy) + 1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long x1, y1, x2, y2;
    if (cin >> x1 >> y1 >> x2 >> y2) {
        Solution solution;
        cout << solution.latticePoints(x1, y1, x2, y2) << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

function gcd(a, b) {
  while (b !== 0) {
    let temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

function latticePoints(x1, y1, x2, y2) {
  const dx = Math.abs(x1 - x2);
  const dy = Math.abs(y1 - y2);
  return gcd(dx, dy) + 1;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const x1 = parseInt(data[0], 10);
  const y1 = parseInt(data[1], 10);
  const x2 = parseInt(data[2], 10);
  const y2 = parseInt(data[3], 10);
  console.log(latticePoints(x1, y1, x2, y2));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `0 0 6 4`.
1. `dx = |0 - 6| = 6`.
2. `dy = |0 - 4| = 4`.
3. `gcd(6, 4) = 2`.
4. Result: `2 + 1 = 3`.

Input: `1 1 1 5`.
1. `dx = 0`.
2. `dy = 4`.
3. `gcd(0, 4) = 4`.
4. Result: `4 + 1 = 5`.
Points: `(1,1), (1,2), (1,3), (1,4), (1,5)`. Correct.

## ✅ Proof of Correctness

### Invariant
The segment is divided into $g$ equal integer-length segments.
The endpoints of these sub-segments are exactly the lattice points.
There are $g$ segments, so $g+1$ points.

### Why the approach is correct
Derived from the property of linear Diophantine equations.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Pick's Theorem.
  - *Question:* Given a polygon vertices, find Area.
  - *Answer:* $A = I + \frac{B}{2} - 1$. We can find $B$ by summing lattice points on each edge using this GCD formula.
- **Extension 2:** Count points strictly inside the segment.
  - *Answer:* $\text{gcd}(dx, dy) - 1$.
- **Extension 3:** 3D Segment.
  - *Answer:* $\text{gcd}(dx, \text{gcd}(dy, dz)) + 1$.

### C++ommon Mistakes to Avoid

1. **Zero Handling**
   - ❌ Wrong: `gcd(0, 0)` crashing.
   - ✅ Correct: If points are same, `gcd(0, 0) = 0`, result 1. Correct.
2. **Negative Differences**
   - ❌ Wrong: Passing negative values to GCD.
   - ✅ Correct: Use `abs()`.

## Related Concepts

- **Pick's Theorem:** Area of lattice polygons.
- **Bresenham's Line Algorithm:** Drawing lines on pixels.
