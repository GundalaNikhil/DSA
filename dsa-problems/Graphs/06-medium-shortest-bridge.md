# Emergency Response Route

**Difficulty:** Medium
**Topic:** Graphs, BFS, Shortest Path
**License:** Free to use for commercial purposes

## Problem Statement

An emergency response system manages a city grid where intersections are nodes and roads are edges. Each road segment takes 1 minute to traverse. An ambulance needs to get from a `dispatch_center` to an `incident_location` as quickly as possible.

Given `n` intersections, a list of `roads`, the `dispatch_center` ID, and the `incident_location` ID, find the minimum time (in minutes) required to reach the scene.

If the location is unreachable, return -1.

## Constraints

- `1 <= number of intersections <= 1000`
- `0 <= roads.length <= 5000`
- `0 <= dispatch_center, incident_location < n`
- Roads are bidirectional

## Examples

### Example 1
```
Input: n = 8, roads = [[0, 2], [2, 4], [4, 6], [6, 7], [1, 3], [3, 5], [5, 7], [0, 1]], dispatch_center = 0, incident_location = 7

Routes:
- 0->2->4->6->7 (4 minutes)
- 0->1->3->5->7 (4 minutes)

Output: 4
```

### Example 2
```
Input: n = 6, roads = [[0, 1], [2, 3], [4, 5]], dispatch_center = 0, incident_location = 5
Output: -1
Explanation: 0 is connected to 1. 5 is connected to 4. No path between them.
```

### Example 3
```
Input: n = 5, roads = [[0, 4], [4, 3], [3, 2], [2, 1], [0, 1]], dispatch_center = 0, incident_location = 2
Output: 2
Explanation: Path 0->1->2 is length 2. (0->4->3->2 is length 3).
```

## Function Signature

### Python
```python
def min_response_time(n: int, roads: list[list[int]], dispatch_center: int, incident_location: int) -> int:
    pass
```

### JavaScript
```javascript
function minResponseTime(n, roads, dispatchCenter, incidentLocation) {
    // Your code here
}
```

### Java
```java
public int minResponseTime(int n, int[][] roads, int dispatchCenter, int incidentLocation) {
    // Your code here
}
```

## Hints

1. Use BFS (breadth-first search) for shortest path in unweighted graphs
2. Start from the start city and explore level by level
3. Track distance for each city as you visit it
4. When you reach destination, return its distance
5. Time complexity: O(n + e), Space complexity: O(n)

## Tags
`graph` `bfs` `shortest-path` `unweighted` `medium`
