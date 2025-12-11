# Exams With Cooldown Gap

## Problem Metadata
- **unique_problem_id**: `dp_016`
- **display_id**: `DP-016`
- **slug**: `exams-with-cooldown-gap`
- **version**: `1.0.0`
- **difficulty**: `Medium`
- **topic_tags**: `["Dynamic Programming", "Interval Scheduling", "Binary Search", "Weighted Job Scheduling"]`

## Problem Title
Exams With Cooldown Gap

## Problem Description
You are given `n` exam slots, where each slot `i` has:
- `start[i]`: start time
- `end[i]`: end time
- `score[i]`: score you gain for completing this exam

You want to maximize your total score, but there's a constraint: you must leave a gap of at least `g` time units between the end of one exam and the start of the next exam you take.

Formally, if you take exam `i` and then exam `j` (where end[i] < start[j]), you must ensure that `start[j] >= end[i] + g`.

Return the maximum total score achievable.

## Examples

### Example 1
**Input:**
```
exams = [(1, 3, 5), (4, 6, 6), (6, 10, 5)]
g = 1
```

**Output:**
```
11
```

**Explanation:**
- Take exam 0: time [1, 3], score 5
- Exam 1 starts at 4, need gap of 1, so can start at time 3+1=4 ✓
- Take exam 1: time [4, 6], score 6
- Exam 2 starts at 6, need gap of 1, so can start at time 6+1=7, but exam 2 starts at 6 ✗
- So we take exams 0 and 1: total score = 5 + 6 = 11

Alternative: Take exams 1 and 2?
- Exam 1: [4, 6], score 6
- Exam 2: [6, 10], need start >= 6 + 1 = 7, but it starts at 6 ✗

So maximum is 11.

### Example 2
**Input:**
```
exams = [(1, 4, 10), (3, 5, 5), (6, 8, 8), (9, 12, 6)]
g = 2
```

**Output:**
```
18
```

**Explanation:**
- Take exam 0: [1, 4], score 10
- Skip exam 1 (overlaps with exam 0)
- Take exam 2: [6, 8], starts at 6 >= 4 + 2 ✓, score 8
- Take exam 3: [9, 12], starts at 9 >= 8 + 2? No, 9 < 10 ✗

Wait, let me recalculate:
- Exam 0: ends at 4, next can start at 4 + 2 = 6
- Exam 2: starts at 6 ✓
- Exam 2: ends at 8, next can start at 8 + 2 = 10
- Exam 3: starts at 9 < 10 ✗

So we can take exams 0 and 2: 10 + 8 = 18 ✓

### Example 3
**Input:**
```
exams = [(1, 3, 20), (2, 5, 20), (3, 10, 100)]
g = 0
```

**Output:**
```
100
```

**Explanation:**
- Exam 2 has the highest score (100) and doesn't overlap with cooldown
- Taking exam 2 alone gives score 100
- Taking exams 0 and 1 would give 40 (but they overlap)
- Maximum: 100

## Constraints
- `1 <= n <= 10^5`
- `1 <= start[i] < end[i] <= 10^9`
- `1 <= score[i] <= 10^9`
- `0 <= g <= 10^9`
- Exams may overlap in time

## Function Signatures

### Java
```java
class Solution {
    public int maxScore(int[][] exams, int g) {
        // exams[i] = [start, end, score]
        // Your code here
    }
}
```

### Python
```python
class Solution:
    def maxScore(self, exams: List[List[int]], g: int) -> int:
        # exams[i] = [start, end, score]
        # Your code here
        pass
```

### C++
```cpp
class Solution {
public:
    int maxScore(vector<vector<int>>& exams, int g) {
        // exams[i] = [start, end, score]
        // Your code here
    }
};
```

## Input Format
```
Line 1: Two space-separated integers: n (number of exams), g (cooldown gap)
Next n lines: Three space-separated integers: start_i, end_i, score_i
```

### Sample Input
```
3 1
1 3 5
4 6 6
6 10 5
```

## Hints
- This is a variant of Weighted Interval Scheduling problem
- Sort exams by end time
- Use DP: dp[i] = maximum score using exams 0 to i
- For each exam i, find the latest exam j where end[j] + g <= start[i]
- Use binary search to find j efficiently
- Recurrence: dp[i] = max(dp[i-1], dp[j] + score[i])
  - Either skip exam i, or take it and add to best solution ending before i-g
- Time complexity: O(n log n)

## Related Topics Quiz

### Question 1
Why do we sort exams by end time?
- A) To simplify binary search for compatible exams
- B) To process exams in chronological order
- C) To use DP efficiently
- D) All of the above

**Answer:** D) All of the above - Sorting by end time enables efficient DP with binary search.

### Question 2
What is the time complexity of this solution?
- A) O(n)
- B) O(n log n)
- C) O(n²)
- D) O(n² log n)

**Answer:** B) O(n log n) - Sorting takes O(n log n), and DP with binary search is O(n log n).

### Question 3
What problem is this similar to?
- A) Longest Increasing Subsequence
- B) Weighted Interval Scheduling
- C) Knapsack
- D) Shortest Path

**Answer:** B) Weighted Interval Scheduling - Classic problem with added cooldown constraint.

### Question 4
Why do we use binary search?
- A) To find the maximum score
- B) To find the latest compatible exam before exam i
- C) To sort the exams
- D) To count total exams

**Answer:** B) To find the latest compatible exam before exam i - Efficiently locate the latest exam that ends before start[i] - g.

### Question 5
What if g = 0?
- A) Problem becomes easier
- B) Problem is unsolvable
- C) Standard Weighted Interval Scheduling (no gap required)
- D) All exams can be taken

**Answer:** C) Standard Weighted Interval Scheduling (no gap required) - No cooldown means back-to-back exams are allowed.

### Question 6
What does dp[i] represent?
- A) Score of exam i
- B) Maximum score considering first i exams
- C) Number of exams taken
- D) End time of exam i

**Answer:** B) Maximum score considering first i exams - Classic DP state for interval problems.
