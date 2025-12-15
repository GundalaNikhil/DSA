# Original Computational Geometry Practice Set (16 Questions)

## 1) Orientation of Triplets
- Slug: orientation-triplets
- Difficulty: Easy
- Problem: Given three points, determine if they are collinear, clockwise, or counterclockwise.
- Constraints: Coordinates in [-10^9,10^9].
- Example:
  - Input: (0,0),(1,1),(2,0)
  - Output: clockwise

## 2) Point in Polygon (Winding)
- Slug: point-in-polygon-winding
- Difficulty: Medium
- Problem: Determine if a point lies inside, outside, or on the boundary of a simple polygon using winding number.
- Constraints: n <= 10^5.
- Example:
  - Input: polygon [(0,0),(2,0),(2,2),(0,2)], point (1,1)
  - Output: inside

## 3) Segment Intersection Count
- Slug: segment-intersection-count
- Difficulty: Medium
- Problem: Given `m` line segments, count how many pairs intersect (including touching).
- Constraints: m <= 2*10^5.
- Hint: Sweep line with balanced tree.
- Example:
  - Input: segments [(0,0)-(2,2),(0,2)-(2,0)]
  - Output: 1

## 4) Closest Pair of Points
- Slug: closest-pair-points
- Difficulty: Medium
- Problem: Given points in 2D, find squared distance of closest pair.
- Constraints: n <= 2*10^5.
- Hint: Divide and conquer.
- Example:
  - Input: [(0,0),(3,4),(1,1)]
  - Output: 2

## 5) Convex Hull with Interior Caps
- Slug: convex-hull-capped
- Difficulty: Medium
- Problem: Compute convex hull of a set of points, but discard any hull vertex whose interior angle is less than a given threshold `theta` (in degrees). Return the capped hull in CCW order.
- Constraints: n <= 10^5, 0 < theta < 180.
- Example:
  - Input: points [(0,0),(1,1),(2,0),(1,-1)], theta=60
  - Output: capped hull (may remove sharp vertices if below threshold)

## 6) Polygon Area (Shoelace)
- Slug: polygon-area-shoelace
- Difficulty: Easy-Medium
- Problem: Compute signed area of a simple polygon.
- Constraints: n <= 10^5.
- Example:
  - Input: [(0,0),(2,0),(2,2),(0,2)]
  - Output: 4

## 7) Rotating Calipers Diameter
- Slug: rotating-calipers-diameter
- Difficulty: Medium
- Problem: Given convex polygon, find farthest pair of vertices (diameter squared).
- Constraints: n <= 10^5.
- Example:
  - Input: square (0,0),(1,0),(1,1),(0,1)
  - Output: 2

## 8) Minimum Enclosing Circle
- Slug: minimum-enclosing-circle
- Difficulty: Medium
- Problem: Find the smallest circle enclosing all points.
- Constraints: n <= 2*10^5.
- Hint: Randomized incremental algorithm.
- Example:
  - Input: [(0,0),(1,0),(0,1)]
  - Output: center (0.5,0.5), radius ~0.707

## 9) Half-Plane Intersection
- Slug: half-plane-intersection
- Difficulty: Hard
- Problem: Given half-planes, compute intersection polygon or report empty.
- Constraints: up to 10^5 half-planes.
- Example:
  - Input: bounding square half-planes x>=0,x<=1,y>=0,y<=1
  - Output: polygon of the square

## 10) Line Sweep Weighted Union Area
- Slug: weighted-union-area-rectangles
- Difficulty: Medium
- Problem: Given axis-aligned rectangles each with an integer weight, compute the area covered by rectangles where the cumulative weight is at least `W` (threshold). Rectangles can overlap; count area only where sum of weights >= W.
- Constraints: up to 10^5 rectangles, |weight| <= 10^6, `1 <= W <= 10^6`.
- Hint: Sweep x; segment tree tracks coverage weight and length above threshold.
- Example:
  - Input: rectangles [(0,0)-(2,2,w=1),(1,1)-(3,3,w=2)], W=2
  - Output: 4 (area where weights overlap)

## 11) Maximum Overlap of Rectangles
- Slug: max-overlap-rectangles
- Difficulty: Medium
- Problem: Given axis-aligned rectangles, find maximum number overlapping at any point.
- Constraints: up to 10^5 rectangles.
- Hint: Similar sweep; track coverage.
- Example:
  - Input: rectangles [(0,0)-(2,2),(1,1)-(3,3),(2,0)-(4,2)]
  - Output: 2

## 12) Largest Empty Circle Inside Rectangle
- Slug: largest-empty-circle-rect
- Difficulty: Medium
- Problem: Given points inside a bounding rectangle, find the largest empty circle fully contained in the rectangle and not covering any point.
- Constraints: n <= 2000.
- Hint: Voronoi edges or brute force candidate centers from circumcenters and rectangle edges.
- Example:
  - Input: rect (0,0)-(4,4), points (1,1),(3,1)
  - Output: radius 1.5

## 13) Point-Line Distance
- Slug: point-line-distance
- Difficulty: Easy
- Problem: Compute shortest distance from point to line segment.
- Constraints: coordinates in [-10^9,10^9].
- Example:
  - Input: segment (0,0)-(2,0), point (1,1)
  - Output: 1

## 14) Angle Sorting for Polar Order
- Slug: angle-sorting-polar
- Difficulty: Easy-Medium
- Problem: Sort points by polar angle around origin; tie by distance.
- Constraints: n <= 10^5.
- Example:
  - Input: [(1,0),(1,1),(0,1)]
  - Output: [(1,0),(1,1),(0,1)]

## 15) Segment-Rectangle Intersection
- Slug: segment-rectangle-intersection
- Difficulty: Medium
- Problem: Determine if a line segment intersects or lies within an axis-aligned rectangle.
- Constraints: coordinates in [-10^9,10^9].
- Example:
  - Input: segment ( -1,1)-(1,1), rect (0,0)-(2,2)
  - Output: true

## 16) Minimum Spanning Tree on Complete Graph by Geometry
- Slug: mst-complete-geometry
- Difficulty: Hard
- Problem: Given points, MST of complete graph with edge weight as Manhattan distance. Compute MST weight efficiently.
- Constraints: n <= 2*10^5.
- Hint: Use 4-directional transforms with sweep + DSU (Manhattan MST trick).
- Example:
  - Input: [(0,0),(2,2),(3,0)]
  - Output: 6
