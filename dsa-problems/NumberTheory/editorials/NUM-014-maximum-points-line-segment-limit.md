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

Given `n` points on a 2D plane and a maximum length `L`, find the maximum number of collinear points that can be covered by a single line segment of length at most `L`.
- Input: Points `(x_i, y_i)`, Length `L`.
- Output: Max count.

## 🌍 Real-World Scenario

**Scenario Title:** The Sensor Alignment

You are deploying a linear sensor array (like a LIDAR strip or a directional antenna) that has a physical length limit `L`.
- You have a map of potential signal sources (points).
- To maximize signal reception, you want to align your sensor array such that it covers the maximum number of sources simultaneously.
- The sources must lie on the line defined by the sensor, and the distance between the first and last covered source must not exceed `L`.

**Why This Problem Matters:**

- **Computational Geometry:** Finding patterns in spatial data.
- **Computer Vision:** Line detection (Hough Transform variants).
- **Data Mining:** Finding linear clusters with density constraints.

![Real-World Application](../images/NUM-014/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Sliding Window

Points: A(0,0), B(1,1), C(2,2), D(3,3). `L=2`.
All are collinear on `y=x`.
Distances from A:
A: 0
B: `sqrt2 ~= 1.41`
C: `2sqrt2 ~= 2.82`
D: `3sqrt2 ~= 4.24`

Window `[0, 2]`:
- A (0), B (1.41). Count 2.
- C is at 2.82 > 2. Not included.

Window shifts:
- B (1.41), C (2.82). Dist `2.82 - 1.41 = 1.41 <= 2`. Count 2.
- C (2.82), D (4.24). Dist `1.41 <= 2`. Count 2.

`2.82 > 2`. So A and C cannot be covered together.
Correct.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Constraints:** `n <= 2000`. `O(n^2 log n)` is acceptable.
- **Collinearity:** Three points are collinear if slopes match.
- **Length:** Euclidean distance.
- **Single Point:** A segment of length 0 covers 1 point. Max is at least 1.

### Core Concept: Slope Grouping & Sliding Window

1. **Fix an anchor point `P_i`.**
2. Calculate the slope from `P_i` to every other point `P_j`.
3. Group points by slope.
4. For each group (points collinear with `P_i`), sort them by distance from `P_i`.
5. Use a **sliding window** on the sorted distances to find the max subset with range `<= L`.

## Naive Approach

### Intuition

For every pair of points, define a line. Project all points onto this line. Sort and slide window.

### Algorithm

- Iterate all pairs `(i, j)`.
- Define line.
- Check all `k`.
- `O(n^3)`. Too slow.

## Optimal Approach

### Key Insight

Instead of checking all lines, iterate each point as a "center" or "anchor".
For a fixed anchor `i`, any line passing through `i` is determined by its angle/slope.
We collect all `j` relative to `i`, store as `(slope, distance)`.
Sort by slope. Points with same slope are collinear with `i`.
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
- `2000^2 x 11 ~= 4.4 * 10^7` ops. Fits in 2s.

### Space Complexity

- **O(n)**.

![Algorithm Visualization](../images/NUM-014/algorithm-visualization.png)
![Algorithm Steps](../images/NUM-014/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private long gcd(long a, long b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    public int maxPointsOnSegment(int[][] points, int L) {
        int n = points.length;
        if (n <= 1) return n;
        
        // Count frequencies of each point
        Map<String, Integer> pointCounts = new HashMap<>();
        for (int[] p : points) {
            String key = p[0] + "," + p[1];
            pointCounts.put(key, pointCounts.getOrDefault(key, 0) + 1);
        }
        
        List<int[]> uniquePoints = new ArrayList<>();
        List<Integer> counts = new ArrayList<>();
        for (String key : pointCounts.keySet()) {
            String[] parts = key.split(",");
            uniquePoints.add(new int[]{Integer.parseInt(parts[0]), Integer.parseInt(parts[1])});
            counts.add(pointCounts.get(key));
        }
        
        int maxPts = 0;
        for (int c : counts) maxPts = Math.max(maxPts, c);
        
        int m = uniquePoints.size();
        for (int i = 0; i < m; i++) {
            Map<String, Integer> slopeMap = new HashMap<>();
            int[] p1 = uniquePoints.get(i);
            
            for (int j = 0; j < m; j++) {
                if (i == j) continue;
                int[] p2 = uniquePoints.get(j);
                
                long dx = (long)p2[0] - p1[0];
                long dy = (long)p2[1] - p1[1];
                double dist = Math.sqrt((double)dx * dx + (double)dy * dy);
                
                if (dist > L + 1e-9) continue;
                
                long g = gcd(Math.abs(dx), Math.abs(dy));
                String slope = (dx / g) + "," + (dy / g);
                
                slopeMap.put(slope, slopeMap.getOrDefault(slope, 0) + counts.get(j));
            }
            
            for (int count : slopeMap.values()) {
                maxPts = Math.max(maxPts, counts.get(i) + count);
            }
        }
        
        return maxPts;
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
    
    point_counts = {}
    for p in points:
        point_counts[p] = point_counts.get(p, 0) + 1
        
    unique_pts = list(point_counts.keys())
    counts = [point_counts[p] for p in unique_pts]
    m = len(unique_pts)
    
    max_pts = max(counts)
    
    for i in range(m):
        slope_map = {}
        x1, y1 = unique_pts[i]
        
        for j in range(m):
            if i == j: continue
            x2, y2 = unique_pts[j]
            
            dx = x2 - x1
            dy = y2 - y1
            dist = sqrt(dx*dx + dy*dy)
            
            if dist > L + 1e-9:
                continue
                
            g = gcd(abs(dx), abs(dy))
            slope = (dx // g, dy // g)
            
            slope_map[slope] = slope_map.get(slope, 0) + counts[j]
            
        for count in slope_map.values():
            max_pts = max(max_pts, counts[i] + count)
            
    return max_pts

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        L = int(next(it))
        points = []
        for _ in range(n):
            x = int(next(it))
            y = int(next(it))
            points.append((x, y))
            
        print(max_points_on_segment(points, L))
    except (StopIteration, ValueError):
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
    long long gcd(long long a, long long b) {
        return b == 0 ? a : gcd(b, a % b);
    }

public:
    int maxPointsOnSegment(const vector<vector<int>>& points, int L) {
        int n = points.size();
        if (n <= 1) return n;
        
        map<pair<int, int>, int> pointCounts;
        for (const auto& p : points) {
            pointCounts[{p[0], p[1]}]++;
        }
        
        vector<pair<int, int>> uniquePts;
        vector<int> counts;
        for (auto const& [pt, count] : pointCounts) {
            uniquePts.push_back(pt);
            counts.push_back(count);
        }
        
        int maxPts = 0;
        for (int c : counts) maxPts = max(maxPts, c);
        
        int m = uniquePts.size();
        for (int i = 0; i < m; i++) {
            map<pair<long long, long long>, int> slopeMap;
            long long x1 = uniquePts[i].first;
            long long y1 = uniquePts[i].second;
            
            for (int j = 0; j < m; j++) {
                if (i == j) continue;
                long long x2 = uniquePts[j].first;
                long long y2 = uniquePts[j].second;
                
                long long dx = x2 - x1;
                long long dy = y2 - y1;
                double dist = sqrt((double)dx * dx + (double)dy * dy);
                
                if (dist > L + 1e-9) continue;
                
                long long g = gcd(abs(dx), abs(dy));
                slopeMap[{dx / g, dy / g}] += counts[j];
            }
            
            for (auto const& [slope, count] : slopeMap) {
                maxPts = max(maxPts, counts[i] + count);
            }
        }
        
        return maxPts;
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
  
  const pointCounts = new Map();
  for (const p of points) {
    const key = `${p[0]},${p[1]}`;
    pointCounts.set(key, (pointCounts.get(key) || 0) + 1);
  }
  
  const uniquePts = [];
  const counts = [];
  for (const [key, count] of pointCounts.entries()) {
    const [x, y] = key.split(",").map(Number);
    uniquePts.push([x, y]);
    counts.push(count);
  }
  
  let maxPts = 0;
  for (const c of counts) {
    if (c > maxPts) maxPts = c;
  }
  
  for (let i = 0; i < uniquePts.length; i++) {
    const slopeMap = new Map();
    const [x1, y1] = uniquePts[i];
    
    for (let j = 0; j < uniquePts.length; j++) {
      if (i === j) continue;
      const [x2, y2] = uniquePts[j];
      
      let dx = x2 - x1;
      let dy = y2 - y1;
      const dist = Math.sqrt(dx * dx + dy * dy);
      
      const g = gcd(dx, dy);
      dx /= g;
      dy /= g;
      
      if (dx < 0 || (dx === 0 && dy < 0)) {
        dx = -dx;
        dy = -dy;
      }
      
      const key = `${dx},${dy}`;
      if (!slopeMap.has(key)) slopeMap.set(key, []);
      
      const origDx = x2 - x1;
      const origDy = y2 - y1;
      const signedDist = (origDx * dx + origDy * dy < 0) ? -dist : dist;
      
      slopeMap.get(key).push({dist: signedDist, count: counts[j]});
    }
    
    for (const group of slopeMap.values()) {
      group.push({dist: 0, count: counts[i]});
      group.sort((a, b) => a.dist - b.dist);
      
      let left = 0;
      let currentPts = 0;
      for (let right = 0; right < group.length; right++) {
        currentPts += group[right].count;
        while (group[right].dist - group[left].dist > L + 1e-9) {
          currentPts -= group[left].count;
          left++;
        }
        if (currentPts > maxPts) maxPts = currentPts;
      }
    }
  }
  
  return maxPts;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (let i = 0; i < parts.length; i++) {
    if (parts[i].length > 0) data.push(parts[i]);
  }
});

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

### Common Mistakes to Avoid

1. **Slope Representation**
   - ❌ Wrong: Using `double` slope (precision issues).
   - ✅ Correct: Use reduced fraction `(dx, dy)`.
2. **Line Direction**
   - ❌ Wrong: Treating `(1,1)` and `(-1,-1)` as different lines.
   - ✅ Correct: Normalize to canonical form.

## Related Concepts

- **Hough Transform:** Line detection.
- **Angular Sweep:** Processing points by angle.
