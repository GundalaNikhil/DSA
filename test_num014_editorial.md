
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
                double dist = Math.sqrt(dx * dx + dy * dy);
                
                if (dist > L + 1e-9) continue;
                
                // Only consider points in one direction from p1
                // Actually, if we want to catch all segments starting at p1,
                // we just look at ANY point p2 with dist(p1, p2) <= L.
                // But we must group by line. So we need slope.
                // But p2 could be in the "negative" direction? 
                // No, a segment [p1, p1 + L*v] only covers points in the "forward" direction v.
                
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
    n = int(next(it))
    L = int(next(it))
    points = []
    for _ in range(n):
        x = int(next(it))
        y = int(next(it))
        points.append((x, y))
        
    print(max_points_on_segment(points, L))

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
  a = Math.abs(a);
  b = Math.abs(b);
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
  
  let maxPts = Math.max(...counts);
  
  const m = uniquePts.size; // Wait, uniquePts is an array
  for (let i = 0; i < uniquePts.length; i++) {
    const slopeMap = new Map();
    const [x1, y1] = uniquePts[i];
    
    for (let j = 0; j < uniquePts.length; j++) {
      if (i === j) continue;
      const [x2, y2] = uniquePts[j];
      
      const dx = x2 - x1;
      const dy = y2 - y1;
      const dist = Math.sqrt(dx * dx + dy * dy);
      
      if (dist > L + 1e-9) continue;
      
      const g = gcd(dx, dy);
      const slope = `${dx / g},${dy / g}`;
      slopeMap.set(slope, (slopeMap.get(slope) || 0) + counts[j]);
    }
    
    for (const count of slopeMap.values()) {
      maxPts = Math.max(maxPts, counts[i] + count);
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
