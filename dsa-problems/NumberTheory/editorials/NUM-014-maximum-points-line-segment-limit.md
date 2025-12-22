---
problem_id: NUM_MAXIMUM_POINTS_LINE_SEGMENT_LIMIT__2904
display_id: NUM-014
slug: maximum-points-line-segment-limit
title: "Maximum Points on a Line Segment Length Limit"
difficulty: Medium
difficulty_score: 58
topics:
  - Number Theory
  - Geometry
  - Sorting
tags:
  - number-theory
  - geometry
  - sorting
  - medium
premium: true
subscription_tier: basic
---

# NUM-014: Maximum Points on a Line Segment Length Limit

## 📋 Problem Summary

Given $n$ points on a 2D plane and a maximum length $L$, find the maximum number of collinear points that can be covered by a single line segment of length at most $L$.
- Input: Points $(x_i, y_i)$, Length $L$.
- Output: Max count.

## 🌍 Real-World Scenario

**Scenario Title:** The Sensor Alignment

You are deploying a linear sensor array (like a LIDAR strip or a directional antenna) that has a physical length limit $L$.
- You have a map of potential signal sources (points).
- To maximize signal reception, you want to align your sensor array such that it covers the maximum number of sources simultaneously.
- The sources must lie on the line defined by the sensor, and the distance between the first and last covered source must not exceed $L$.

**Why This Problem Matters:**

- **Computational Geometry:** Finding patterns in spatial data.
- **Computer Vision:** Line detection (Hough Transform variants).
- **Data Mining:** Finding linear clusters with density constraints.

![Real-World Application](../images/NUM-014/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Sliding Window

Points: A(0,0), B(1,1), C(2,2), D(3,3). $L=2$.
All are collinear on $y=x$.
Distances from A:
A: 0
B: $\sqrt{2} \approx 1.41$
C: $2\sqrt{2} \approx 2.82$
D: $3\sqrt{2} \approx 4.24$

Window $[0, 2]$:
- A (0), B (1.41). Count 2.
- C is at 2.82 > 2. Not included.

Window shifts:
- B (1.41), C (2.82). Dist $2.82 - 1.41 = 1.41 \le 2$. Count 2.
- C (2.82), D (4.24). Dist $1.41 \le 2$. Count 2.

Max count is 2. Wait, example output says 2.
Wait, distance between A and C is $\sqrt{(2-0)^2 + (2-0)^2} = \sqrt{8} \approx 2.82$.
$2.82 > 2$. So A and C cannot be covered together.
Correct.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Constraints:** $n \le 2000$. $O(n^2 \log n)$ is acceptable.
- **Collinearity:** Three points are collinear if slopes match.
- **Length:** Euclidean distance.
- **Single Point:** A segment of length 0 covers 1 point. Max is at least 1.

### Core Concept: Slope Grouping & Sliding Window

1. **Fix an anchor point $P_i$.**
2. Calculate the slope from $P_i$ to every other point $P_j$.
3. Group points by slope.
4. For each group (points collinear with $P_i$), sort them by distance from $P_i$.
5. Use a **sliding window** on the sorted distances to find the max subset with range $\le L$.

## Naive Approach

### Intuition

For every pair of points, define a line. Project all points onto this line. Sort and slide window.

### Algorithm

- Iterate all pairs $(i, j)$.
- Define line.
- Check all $k$.
- $O(n^3)$. Too slow.

## Optimal Approach

### Key Insight

Instead of checking all lines, iterate each point as a "center" or "anchor".
For a fixed anchor $i$, any line passing through $i$ is determined by its angle/slope.
We collect all $j$ relative to $i$, store as `(slope, distance)`.
Sort by slope. Points with same slope are collinear with $i$.
Process each slope group: sort by distance, then sliding window.

### Algorithm

1. `max_points = 1`.
2. For each point `i` from 0 to `n-1`:
   - Create a list of `(dx, dy, dist)` for all `j != i`.
   - Simplify `(dx, dy)` by dividing by `gcd(|dx|, |dy|)` to represent slope uniquely.
   - Sort the list by `(dx, dy)`.
   - Group by `(dx, dy)`.
   - For each group:
     - We have a list of distances from `i`. Note: `i` itself is at distance 0.
     - Add 0 to the list (representing `i`).
     - Sort distances.
     - Sliding window: `left = 0`. For `right` from 0 to `size-1`:
       - While `dists[right] - dists[left] > L`: `left++`.
       - `max_points = max(max_points, right - left + 1)`.
3. Return `max_points`.

### Time Complexity

- **O(n^2 \log n)** due to sorting.
- $2000^2 \times 11 \approx 4.4 \cdot 10^7$ ops. Fits in 2s.

### Space Complexity

- **O(n)**.

![Algorithm Visualization](../images/NUM-014/algorithm-visualization.png)
![Algorithm Steps](../images/NUM-014/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    public int maxPointsOnSegment(int[][] points, int L) {
        int n = points.length;
        if (n <= 1) return n;
        
        int maxCount = 1;
        
        for (int i = 0; i < n; i++) {
            Map<String, List<Double>> slopeMap = new HashMap<>();
            
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                int dx = points[j][0] - points[i][0];
                int dy = points[j][1] - points[i][1];
                int g = gcd(Math.abs(dx), Math.abs(dy));
                dx /= g;
                dy /= g;
                
                // Canonical form for slope
                // Ensure dx is non-negative, or if dx=0, dy is positive
                // Actually, since we want lines through i, (dx, dy) and (-dx, -dy) are same line but opposite directions.
                // But for sliding window, we treat them as a single line.
                // We can project onto the line.
                // Easier: Normalize so that we cover the full line.
                // If we normalize (dx, dy) to be unique for the line, we can store signed distances.
                
                if (dx < 0 || (dx == 0 && dy < 0)) {
                    dx = -dx;
                    dy = -dy;
                }
                
                String key = dx + "," + dy;
                slopeMap.putIfAbsent(key, new ArrayList<>());
                double dist = Math.sqrt(Math.pow(points[j][0] - points[i][0], 2) + Math.pow(points[j][1] - points[i][1], 2));
                
                // Determine sign relative to i.
                // Since we normalized slope, we can just use dot product or check original dx/dy sign relative to normalized.
                // Actually, simpler: just use signed distance based on coordinate comparison.
                // If original dx matches normalized dx, positive. Else negative.
                // Wait, if dx=0, check dy.
                
                int origDx = points[j][0] - points[i][0];
                int origDy = points[j][1] - points[i][1];
                boolean sameDir = (origDx == 0 && origDy == 0) || (origDx * dx >= 0 && origDy * dy >= 0); 
                // Wait, if normalized is (1, 1) and original is (-1, -1), dist should be negative.
                // If normalized is (1, 1) and original is (2, 2), dist positive.
                
                // Let's re-verify normalization.
                // If we normalize (dx, dy) strictly, then (-dx, -dy) becomes (dx, dy).
                // We need to know if j is "forward" or "backward" from i.
                
                // Check dot product of (origDx, origDy) and (dx, dy).
                if (origDx * dx + origDy * dy < 0) {
                    dist = -dist;
                }
                
                slopeMap.get(key).add(dist);
            }
            
            for (List<Double> dists : slopeMap.values()) {
                dists.add(0.0); // Add point i itself
                Collections.sort(dists);
                
                int left = 0;
                for (int right = 0; right < dists.size(); right++) {
                    while (dists.get(right) - dists.get(left) > L + 1e-9) {
                        left++;
                    }
                    maxCount = Math.max(maxCount, right - left + 1);
                }
            }
        }
        
        return maxCount;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int L = sc.nextInt();
            int[][] points = new int[n][2];
            for (int i = 0; i < n; i++) {
                points[i][0] = sc.nextInt();
                points[i][1] = sc.nextInt();
            }

            Solution solution = new Solution();
            System.out.println(solution.maxPointsOnSegment(points, L));
        }
        sc.close();
    }
}
```

### Python

```python
import sys
from math import gcd, sqrt

def max_points_on_segment(points, L):
    n = len(points)
    if n <= 1: return n
    
    max_count = 1
    
    for i in range(n):
        slope_groups = {}
        
        for j in range(n):
            if i == j: continue
            
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            g = gcd(abs(dx), abs(dy))
            dx //= g
            dy //= g
            
            # Normalize slope to unique line representation
            if dx < 0 or (dx == 0 and dy < 0):
                dx = -dx
                dy = -dy
                
            key = (dx, dy)
            if key not in slope_groups:
                slope_groups[key] = []
                
            dist = sqrt((points[j][0] - points[i][0])**2 + (points[j][1] - points[i][1])**2)
            
            # Check sign
            orig_dx = points[j][0] - points[i][0]
            orig_dy = points[j][1] - points[i][1]
            
            if orig_dx * dx + orig_dy * dy < 0:
                dist = -dist
                
            slope_groups[key].append(dist)
            
        for dists in slope_groups.values():
            dists.append(0.0)
            dists.sort()
            
            left = 0
            for right in range(len(dists)):
                while dists[right] - dists[left] > L + 1e-9:
                    left += 1
                max_count = max(max_count, right - left + 1)
                
    return max_count

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    iterator = iter(data)
    try:
        n = int(next(iterator))
        L = int(next(iterator))
        points = []
        for _ in range(n):
            x = int(next(iterator))
            y = int(next(iterator))
            points.append((x, y))
            
        print(max_points_on_segment(points, L))
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
#include <algorithm>
#include <map>
#include <numeric>

using namespace std;

class Solution {
    int gcd(int a, int b) {
        while (b) {
            a %= b;
            swap(a, b);
        }
        return a;
    }

public:
    int maxPointsOnSegment(const vector<vector<int>>& points, int L) {
        int n = points.size();
        if (n <= 1) return n;
        
        int maxCount = 1;
        
        for (int i = 0; i < n; i++) {
            map<pair<int, int>, vector<double>> slopeGroups;
            
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                
                int dx = points[j][0] - points[i][0];
                int dy = points[j][1] - points[i][1];
                int g = gcd(abs(dx), abs(dy));
                dx /= g;
                dy /= g;
                
                if (dx < 0 || (dx == 0 && dy < 0)) {
                    dx = -dx;
                    dy = -dy;
                }
                
                double dist = sqrt(pow(points[j][0] - points[i][0], 2) + pow(points[j][1] - points[i][1], 2));
                
                int origDx = points[j][0] - points[i][0];
                int origDy = points[j][1] - points[i][1];
                
                if (origDx * dx + origDy * dy < 0) {
                    dist = -dist;
                }
                
                slopeGroups[{dx, dy}].push_back(dist);
            }
            
            for (auto& entry : slopeGroups) {
                vector<double>& dists = entry.second;
                dists.push_back(0.0);
                sort(dists.begin(), dists.end());
                
                int left = 0;
                for (int right = 0; right < dists.size(); right++) {
                    while (dists[right] - dists[left] > L + 1e-9) {
                        left++;
                    }
                    maxCount = max(maxCount, right - left + 1);
                }
            }
        }
        
        return maxCount;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, L;
    if (cin >> n >> L) {
        vector<vector<int>> points(n, vector<int>(2));
        for (int i = 0; i < n; i++) {
            cin >> points[i][0] >> points[i][1];
        }

        Solution solution;
        cout << solution.maxPointsOnSegment(points, L) << "\n";
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

function maxPointsOnSegment(points, L) {
  const n = points.length;
  if (n <= 1) return n;
  
  let maxCount = 1;
  
  for (let i = 0; i < n; i++) {
    const slopeGroups = new Map();
    
    for (let j = 0; j < n; j++) {
      if (i === j) continue;
      
      let dx = points[j][0] - points[i][0];
      let dy = points[j][1] - points[i][1];
      const g = gcd(Math.abs(dx), Math.abs(dy));
      dx /= g;
      dy /= g;
      
      if (dx < 0 || (dx === 0 && dy < 0)) {
        dx = -dx;
        dy = -dy;
      }
      
      const key = `${dx},${dy}`;
      if (!slopeGroups.has(key)) slopeGroups.set(key, []);
      
      let dist = Math.sqrt(Math.pow(points[j][0] - points[i][0], 2) + Math.pow(points[j][1] - points[i][1], 2));
      
      const origDx = points[j][0] - points[i][0];
      const origDy = points[j][1] - points[i][1];
      
      if (origDx * dx + origDy * dy < 0) {
        dist = -dist;
      }
      
      slopeGroups.get(key).push(dist);
    }
    
    for (const dists of slopeGroups.values()) {
      dists.push(0.0);
      dists.sort((a, b) => a - b);
      
      let left = 0;
      for (let right = 0; right < dists.length; right++) {
        while (dists[right] - dists[left] > L + 1e-9) {
          left++;
        }
        maxCount = Math.max(maxCount, right - left + 1);
      }
    }
  }
  
  return maxCount;
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
  const L = parseInt(data[idx++], 10);
  const points = [];
  for (let i = 0; i < n; i++) {
    const x = parseInt(data[idx++], 10);
    const y = parseInt(data[idx++], 10);
    points.push([x, y]);
  }
  console.log(maxPointsOnSegment(points, L));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Input: `(0,0), (1,1), (2,2), (0,1)`, `L=2`.
1. Anchor `(0,0)`:
   - `(1,1)`: Slope `(1,1)`, Dist `1.41`.
   - `(2,2)`: Slope `(1,1)`, Dist `2.82`.
   - `(0,1)`: Slope `(0,1)`, Dist `1.0`.
   - Group `(1,1)`: `[0, 1.41, 2.82]`.
     - Window `[0, 1.41]`: Len 1.41 <= 2. Count 2.
     - Window `[1.41, 2.82]`: Len 1.41 <= 2. Count 2.
     - Window `[0, 2.82]`: Len 2.82 > 2.
   - Group `(0,1)`: `[0, 1.0]`. Count 2.
2. Max 2.

## ✅ Proof of Correctness

### Invariant
By iterating every point as an anchor, we consider every possible line.
By sorting signed distances, we correctly handle points on both sides of the anchor.
Sliding window finds the optimal segment on that line.

### Why the approach is correct
Exhaustive coverage of all lines defined by pairs of points.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Max points on ANY line (no length limit).
  - *Hint:* Just max group size.
- **Extension 2:** Circle of radius R.
  - *Hint:* Angular sweep.
- **Extension 3:** 3D Points.
  - *Hint:* Slope becomes `(dx, dy, dz) / gcd`.

## Common Mistakes to Avoid

1. **Slope Representation**
   - ❌ Wrong: Using `double` slope (precision issues).
   - ✅ Correct: Use reduced fraction `(dx, dy)`.
2. **Line Direction**
   - ❌ Wrong: Treating `(1,1)` and `(-1,-1)` as different lines.
   - ✅ Correct: Normalize to canonical form.

## Related Concepts

- **Hough Transform:** Line detection.
- **Angular Sweep:** Processing points by angle.
