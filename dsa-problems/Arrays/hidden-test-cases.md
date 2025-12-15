# Hidden Test Cases for Array Problems

JSON-style hidden cases per problem. Each block uses a consistent schema:
- `problem_id`: matches array set IDs ARR-001 … ARR-016
- `tests`: list of cases with `id`, `category`, `input`, `output`, `notes`

---

## Snack Restock Snapshot (ARR-001)

```json
{
  "problem_id": "ARR-001",
  "tests": [
    { "id": "base_1", "category": "base", "input": { "arr": [4] }, "output": [4], "notes": "Single element" },
    { "id": "base_2", "category": "base", "input": { "arr": [4, 6, 6, 0] }, "output": [4, 5, 5, 4], "notes": "From prompt example" },
    { "id": "edge_1", "category": "edge", "input": { "arr": [0] }, "output": [0], "notes": "All zeros minimal n" },
    { "id": "corner_1", "category": "corner", "input": { "arr": [1000000, 0, 1000000, 0] }, "output": [1000000, 500000, 666666, 500000], "notes": "Alternating min/max" },
    { "id": "boundary_1", "category": "boundary", "input": { "arr": [999999, 999999, 999999] }, "output": [999999, 999999, 999999], "notes": "Near upper value, stable average" },
    { "id": "stress_1", "category": "stress", "input": { "arr": [1, 1000000, 1, 1000000, 1, 1000000] }, "output": [1, 500000, 333334, 500000, 400000, 500000], "notes": "Oscillating extremes" },
    { "id": "boundary_2", "category": "boundary", "input": { "arr": [1, 2, 3, 4, 5, 6] }, "output": [1, 1, 2, 2, 3, 3], "notes": "Sequential growth with integer floor" },
    { "id": "large_1", "category": "large", "input": { "arr": [500000, 500000, 500000, 500000, 500000, 500000] }, "output": [500000, 500000, 500000, 500000, 500000, 500000], "notes": "Representative constant large array" },
    { "id": "large_2", "category": "large", "input": { "arr": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] }, "output": [1, 1, 2, 2, 3, 3, 4, 4, 5, 5], "notes": "Longer prefix average rounding" }
  ]
}
```

---

## Bench Flip With Locked Ends (ARR-002)

```json
{
  "problem_id": "ARR-002",
  "tests": [
    { "id": "base_1", "category": "base", "input": { "arr": [1, 2] }, "output": [1, 2], "notes": "No middle to reverse" },
    { "id": "base_2", "category": "base", "input": { "arr": [1, 2, 3] }, "output": [1, 2, 3], "notes": "Single middle element unchanged" },
    { "id": "corner_1", "category": "corner", "input": { "arr": [5, 3, 8, 1, 9] }, "output": [5, 1, 8, 3, 9], "notes": "Typical reversal" },
    { "id": "edge_1", "category": "edge", "input": { "arr": [-1000000000, 0, 1000000000] }, "output": [-1000000000, 0, 1000000000], "notes": "Extreme values, center fixed" },
    { "id": "stress_1", "category": "stress", "input": { "arr": [100, 1, 2, 3, 4, 5, 100] }, "output": [100, 5, 4, 3, 2, 1, 100], "notes": "Longer middle reversal" },
    { "id": "boundary_1", "category": "boundary", "input": { "arr": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] }, "output": [10, 2, 3, 4, 5, 6, 7, 8, 9, 1], "notes": "Locks ends on longer array" },
    { "id": "large_1", "category": "large", "input": { "arr": [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5] }, "output": [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5], "notes": "Middle is palindromic, reversal no-ops" }
  ]
}
```

---

## Shuttle Shift With Blackout (ARR-003)

```json
{
  "problem_id": "ARR-003",
  "tests": [
    { "id": "base_1", "category": "base", "input": { "arr": [1, 2, 3], "k": 1, "blackout": [] }, "output": [2, 3, 1], "notes": "Simple left rotation" },
    { "id": "base_2", "category": "base", "input": { "arr": [1, 2, 3], "k": 0, "blackout": [] }, "output": [1, 2, 3], "notes": "Zero rotation" },
    { "id": "corner_1", "category": "corner", "input": { "arr": [1, 2, 3, 4, 5], "k": 2, "blackout": [1] }, "output": [4, 2, 5, 1, 3], "notes": "Single blackout index" },
    { "id": "edge_1", "category": "edge", "input": { "arr": [1], "k": 1000000000, "blackout": [] }, "output": [1], "notes": "Single element, huge k" },
    { "id": "edge_2", "category": "edge", "input": { "arr": [1, 2, 3, 4, 5], "k": 5, "blackout": [0, 2, 4] }, "output": [1, 4, 3, 2, 5], "notes": "Movable subset rotates by k % movable_count" },
    { "id": "corner_2", "category": "corner", "input": { "arr": [1, 2, 3, 4, 5], "k": 3, "blackout": [0, 1, 2, 3, 4] }, "output": [1, 2, 3, 4, 5], "notes": "All indices fixed" },
    { "id": "stress_1", "category": "stress", "input": { "arr": [5, 5, 5, 5, 5, 5], "k": 4, "blackout": [1, 3, 4] }, "output": [5, 5, 5, 5, 5, 5], "notes": "All values equal, mix of fixed/movable" },
    { "id": "boundary_1", "category": "boundary", "input": { "arr": [1, 2, 3, 4, 5, 6, 7, 8], "k": 10, "blackout": [1, 4] }, "output": [6, 2, 7, 8, 5, 1, 3, 4], "notes": "Rotation reduced by movable count after blackout removal" },
    { "id": "large_1", "category": "large", "input": { "arr": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], "k": 25, "blackout": [0, 5, 9] }, "output": [10, 70, 80, 90, 20, 60, 30, 40, 50, 100], "notes": "Mixed fixed endpoints and internal blackout with big k" }
  ]
}
```

---

## Lab Temperature Offline Ranges (ARR-004)

```json
{
  "problem_id": "ARR-004",
  "tests": [
    { "id": "base_1", "category": "base", "input": { "temps": [5, 5, 5], "queries": [["sum", 0, 2]] }, "output": [15], "notes": "Only sum query" },
    { "id": "base_2", "category": "base", "input": { "temps": [1, 2, 3], "queries": [["add", 0, 2, 1], ["sum", 0, 2]] }, "output": [9], "notes": "Single add then sum" },
    { "id": "edge_1", "category": "edge", "input": { "temps": [0], "queries": [["add", 0, 0, 1000000000], ["sum", 0, 0]] }, "output": [1000000000], "notes": "Max add on single element" },
    { "id": "edge_2", "category": "edge", "input": { "temps": [1000000000, 1000000000, 1000000000], "queries": [["sum", 0, 2]] }, "output": [3000000000], "notes": "Large initial values" },
    { "id": "corner_1", "category": "corner", "input": { "temps": [-1000000000, -1000000000], "queries": [["add", 0, 1, -1000000000], ["sum", 0, 1]] }, "output": [-4000000000], "notes": "Negative extremes" },
    { "id": "corner_2", "category": "corner", "input": { "temps": [0, 0, 0, 0, 0], "queries": [["add", 0, 1, 10], ["add", 1, 3, -5], ["add", 2, 4, 3], ["sum", 0, 4]] }, "output": [14], "notes": "Overlapping updates" },
    { "id": "stress_1", "category": "stress", "input": { "temps": [1, 2, 3], "queries": [["add", 0, 1, 5], ["sum", 0, 2], ["add", 2, 2, -1], ["sum", 1, 2]] }, "output": [16, 9], "notes": "Multiple adds and sums" },
    { "id": "boundary_1", "category": "boundary", "input": { "temps": [1000000000, -1000000000], "queries": [["add", 0, 1, 1], ["sum", 0, 1]] }, "output": [2], "notes": "Large magnitude cancellation after add" },
    { "id": "large_1", "category": "large", "input": { "temps": [1, 2, 3, 4, 5, 6], "queries": [["add", 0, 5, 1], ["add", 2, 4, -2], ["sum", 1, 4], ["add", 0, 0, 5], ["sum", 0, 5]] }, "output": [12, 26], "notes": "Multiple cumulative updates across wider ranges" }
  ]
}
```

---

## Weighted Balance Point (ARR-005)

```json
{
  "problem_id": "ARR-005",
  "tests": [
    { "id": "base_1", "category": "base", "input": { "a": [2, 3, -1, 3, 2], "L": 2, "R": 1 }, "output": 1, "notes": "Prompt example" },
    { "id": "base_2", "category": "base", "input": { "a": [1, -1, 1], "L": 1, "R": 1 }, "output": 0, "notes": "Balance at first index" },
    { "id": "edge_1", "category": "edge", "input": { "a": [5], "L": 3, "R": 3 }, "output": 0, "notes": "Single element always balances" },
    { "id": "corner_1", "category": "corner", "input": { "a": [1, 1, 1], "L": 1, "R": 2 }, "output": -1, "notes": "No feasible balance" },
    { "id": "stress_1", "category": "stress", "input": { "a": [10, -5, -5, 0, 0], "L": 1, "R": 1 }, "output": 3, "notes": "Balance late in array" },
    { "id": "boundary_1", "category": "boundary", "input": { "a": [1000000000, -1000000000, 1000000000], "L": 1, "R": 1 }, "output": 1, "notes": "Large magnitude with symmetry" },
    { "id": "large_1", "category": "large", "input": { "a": [5, -1, 3, -2, 5, -10, 5], "L": 2, "R": 3 }, "output": 0, "notes": "First index balances when left sum is zero" }
  ]
}
```

---

## Zero Slide With Limit (ARR-006)

```json
{
  "problem_id": "ARR-006",
  "tests": [
    { "id": "base_1", "category": "base", "input": { "arr": [0, 4, 0, 5, 7], "m": 1 }, "output": [4, 0, 5, 7, 0], "notes": "Stops after limited swaps" },
    { "id": "base_2", "category": "base", "input": { "arr": [0, 1, 0, 2], "m": 10 }, "output": [1, 2, 0, 0], "notes": "Plenty of swaps to move all non-zeros" },
    { "id": "edge_1", "category": "edge", "input": { "arr": [1, 2, 3], "m": 0 }, "output": [1, 2, 3], "notes": "No swaps allowed" },
    { "id": "corner_1", "category": "corner", "input": { "arr": [0, 0, 0], "m": 5 }, "output": [0, 0, 0], "notes": "All zeros" },
    { "id": "stress_1", "category": "stress", "input": { "arr": [1, 0, 2, 0, 3, 0, 4], "m": 3 }, "output": [1, 2, 3, 4, 0, 0, 0], "notes": "Swaps just enough to bubble non-zeros forward" },
    { "id": "boundary_1", "category": "boundary", "input": { "arr": [0, 0, 1, 2, 3], "m": 5 }, "output": [1, 2, 3, 0, 0], "notes": "Enough swaps to move each non-zero across multiple zeros" },
    { "id": "large_1", "category": "large", "input": { "arr": [0, 1, 0, 2, 0, 3, 0, 4, 0, 5], "m": 100 }, "output": [1, 2, 3, 4, 5, 0, 0, 0, 0, 0], "notes": "Plenty of swaps on a longer array" }
  ]
}
```

---

## Hostel Roster Merge With Gap (ARR-007)

```json
{
  "problem_id": "ARR-007",
  "tests": [
    { "id": "base_1", "category": "base", "input": { "A": [1, 3, 3], "B": [3, 4] }, "output": [1, 3, 3, 3, 4], "notes": "Prompt example" },
    { "id": "base_2", "category": "base", "input": { "A": [], "B": [1, 2, 3] }, "output": [1, 2, 3], "notes": "Empty first array" },
    { "id": "edge_1", "category": "edge", "input": { "A": [2, 2], "B": [2] }, "output": [2, 2, 2], "notes": "Tie break keeps A elements first but values same" },
    { "id": "corner_1", "category": "corner", "input": { "A": [-5, -1, 0], "B": [-3, -1, 2] }, "output": [-5, -3, -1, -1, 0, 2], "notes": "Negative numbers and duplicates" },
    { "id": "stress_1", "category": "stress", "input": { "A": [1, 4, 7, 10], "B": [2, 3, 5, 6, 8, 9] }, "output": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "notes": "Interleaving merge" },
    { "id": "boundary_1", "category": "boundary", "input": { "A": [1, 1, 2], "B": [1, 2, 2] }, "output": [1, 1, 1, 2, 2, 2], "notes": "Tie rule keeps A duplicates before B duplicates" },
    { "id": "large_1", "category": "large", "input": { "A": [0, 2, 4, 6, 8], "B": [1, 3, 5, 7, 9, 11] }, "output": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11], "notes": "Alternating parity merge on longer arrays" }
  ]
}
```

---

## Partner Pair Sum With Forbidden (ARR-008)

```json
{
  "problem_id": "ARR-008",
  "tests": [
    { "id": "base_1", "category": "base", "input": { "arr": [1, 4, 6, 7], "target": 11, "forbidden": [0] }, "output": true, "notes": "Uses 4 + 7" },
    { "id": "base_2", "category": "base", "input": { "arr": [1, 2, 3, 4], "target": 5, "forbidden": [1] }, "output": true, "notes": "Pair 1 (idx0) + 4 (idx3)" },
    { "id": "edge_1", "category": "edge", "input": { "arr": [2, 3], "target": 5, "forbidden": [0, 1] }, "output": false, "notes": "All indices forbidden" },
    { "id": "corner_1", "category": "corner", "input": { "arr": [-2, 0, 3, 9], "target": 7, "forbidden": [2, 3] }, "output": false, "notes": "No usable pair" },
    { "id": "stress_1", "category": "stress", "input": { "arr": [1, 2, 3, 4, 6, 8, 9], "target": 10, "forbidden": [2, 5] }, "output": true, "notes": "Pair 1 (idx0) + 9 (idx6)" },
    { "id": "boundary_1", "category": "boundary", "input": { "arr": [1, 3, 5, 7], "target": 8, "forbidden": [] }, "output": true, "notes": "Simple pair with no restrictions" },
    { "id": "large_1", "category": "large", "input": { "arr": [1, 2, 3, 4, 5, 6, 7, 8], "target": 13, "forbidden": [2, 3, 4, 5] }, "output": false, "notes": "Remaining indices cannot reach target" }
  ]
}
```

---

## Best Streak With One Smoothing (ARR-009)

```json
{
  "problem_id": "ARR-009",
  "tests": [
    { "id": "base_1", "category": "base", "input": { "a": [-2, 3, -4, 5] }, "output": 9, "notes": "Prompt example smoothing -4 to 1" },
    { "id": "base_2", "category": "base", "input": { "a": [3, -2, 4] }, "output": 8, "notes": "Smooth middle -> 1, best subarray 3 + 1 + 4" },
    { "id": "edge_1", "category": "edge", "input": { "a": [5, 5, 5] }, "output": 15, "notes": "Smoothing unnecessary, all positive" },
    { "id": "corner_1", "category": "corner", "input": { "a": [1, -10, 2, 3] }, "output": 6, "notes": "Matches prompt extra example" },
    { "id": "stress_1", "category": "stress", "input": { "a": [-5, -1, -5, -1, -5] }, "output": -1, "notes": "Best after smoothing still single -1" },
    { "id": "boundary_1", "category": "boundary", "input": { "a": [-1, -2, -3] }, "output": -1, "notes": "All negative, smoothing cannot exceed best single" },
    { "id": "large_1", "category": "large", "input": { "a": [10, -20, 5, 5, 5] }, "output": 23, "notes": "Smoothing deep dip lifts full-array sum" }
  ]
}
```

---

## Early Discount With Stay Window and Ceiling (ARR-010)

```json
{
  "problem_id": "ARR-010",
  "tests": [
    { "id": "base_1", "category": "base", "input": { "prices": [7, 2, 5, 1, 9], "dMin": 1, "dMax": 3, "C": 6 }, "output": 5, "notes": "Prompt example" },
    { "id": "base_2", "category": "base", "input": { "prices": [3, 8, 5, 10], "dMin": 1, "dMax": 2, "C": 20 }, "output": 7, "notes": "Buy 3 sell 10 after 2 days" },
    { "id": "edge_1", "category": "edge", "input": { "prices": [9, 8, 7], "dMin": 1, "dMax": 2, "C": 100 }, "output": 0, "notes": "No profitable window" },
    { "id": "corner_1", "category": "corner", "input": { "prices": [2, 10, 12], "dMin": 1, "dMax": 2, "C": 8 }, "output": 6, "notes": "Ceiling clamps sell price" },
    { "id": "stress_1", "category": "stress", "input": { "prices": [5, 1, 5, 1, 5, 1, 10], "dMin": 2, "dMax": 3, "C": 9 }, "output": 8, "notes": "Best buy at 1, sell at min(10,9)=9 after hold" },
    { "id": "boundary_1", "category": "boundary", "input": { "prices": [5, 3, 6], "dMin": 1, "dMax": 1, "C": 10 }, "output": 3, "notes": "Hold window fixed to one day" },
    { "id": "large_1", "category": "large", "input": { "prices": [1, 3, 2, 8, 4, 9, 2, 5], "dMin": 2, "dMax": 4, "C": 7 }, "output": 6, "notes": "Ceiling-limited sells within sliding window" }
  ]
}
```

---

## Leaky Roof Reinforcement (ARR-011)

```json
{
  "problem_id": "ARR-011",
  "tests": [
    { "id": "base_1", "category": "base", "input": { "height": [4, 1, 3, 1, 5] }, "output": 7, "notes": "Prompt example" },
    { "id": "base_2", "category": "base", "input": { "height": [2, 2, 2] }, "output": 0, "notes": "Already single-peak" },
    { "id": "edge_1", "category": "edge", "input": { "height": [0] }, "output": 0, "notes": "Single cell roof" },
    { "id": "corner_1", "category": "corner", "input": { "height": [0, 1, 0] }, "output": 0, "notes": "Naturally peaked" },
    { "id": "stress_1", "category": "stress", "input": { "height": [3, 1, 2, 1, 2, 1, 3] }, "output": 5, "notes": "Symmetric peaks; pick center for minimal fill" },
    { "id": "boundary_1", "category": "boundary", "input": { "height": [1, 0, 1] }, "output": 1, "notes": "Raise middle to form single peak" },
    { "id": "large_1", "category": "large", "input": { "height": [3, 1, 1, 1, 3] }, "output": 6, "notes": "Raise middle section to flat peak at height 3" }
  ]
}
```

---

## Longest Zero-Sum Even Length (ARR-012)

```json
{
  "problem_id": "ARR-012",
  "tests": [
    { "id": "base_1", "category": "base", "input": { "a": [1, -1, 3, -3, 2] }, "output": 4, "notes": "Prompt example length 4" },
    { "id": "base_2", "category": "base", "input": { "a": [2, -2, 2, -2] }, "output": 4, "notes": "Entire array qualifies" },
    { "id": "edge_1", "category": "edge", "input": { "a": [5] }, "output": 0, "notes": "No even-length subarray" },
    { "id": "corner_1", "category": "corner", "input": { "a": [1, 2, -3, 4, -4] }, "output": 0, "notes": "Only odd-length zero sums exist" },
    { "id": "stress_1", "category": "stress", "input": { "a": [1, -1, 1, -1, 1, -1, 1, -1] }, "output": 8, "notes": "Alternating zeros out, entire length even" },
    { "id": "boundary_1", "category": "boundary", "input": { "a": [0, 0, 0, 0] }, "output": 4, "notes": "All zeros even length" },
    { "id": "large_1", "category": "large", "input": { "a": [1, -1, 1, -1, 1, -1, 1, -1, 1, -1] }, "output": 10, "notes": "Longer alternating pattern" }
  ]
}
```

---

## Tool Frequency Top K with Recency Decay (ARR-013)

```json
{
  "problem_id": "ARR-013",
  "tests": [
    { "id": "base_1", "category": "base", "input": { "values": [[3, 0], [1, 0], [3, 5], [2, 6], [1, 9]], "now": 10, "D": 5, "k": 2 }, "output": [3, 1], "notes": "Prompt-style example" },
    { "id": "base_2", "category": "base", "input": { "values": [[5, 0], [5, 0], [2, 0]], "now": 0, "D": 10, "k": 1 }, "output": [5], "notes": "Same timestamp, frequency driven" },
    { "id": "edge_1", "category": "edge", "input": { "values": [[1, 1]], "now": 1000000000, "D": 1, "k": 1 }, "output": [1], "notes": "Single value, heavy decay but still top" },
    { "id": "corner_1", "category": "corner", "input": { "values": [[1, 0], [2, 0], [3, 0]], "now": 0, "D": 1, "k": 2 }, "output": [1, 2], "notes": "Tie on scores, choose smaller values" },
    { "id": "stress_1", "category": "stress", "input": { "values": [[1, 0], [1, 5], [2, 5], [2, 6], [3, 9]], "now": 10, "D": 2, "k": 2 }, "output": [3, 2], "notes": "Most recent event for value 3 dominates decay weights" },
    { "id": "boundary_1", "category": "boundary", "input": { "values": [[1, 0], [2, 0]], "now": 0, "D": 1, "k": 2 }, "output": [1, 2], "notes": "k equals number of distinct values" },
    { "id": "large_1", "category": "large", "input": { "values": [[5, 0], [4, 1], [4, 2], [3, 3], [3, 7], [2, 8], [1, 9]], "now": 10, "D": 3, "k": 3 }, "output": [1, 2, 3], "notes": "Later timestamps outweigh higher raw counts" }
  ]
}
```

---

## Boarding Order With Fixed Ones (ARR-014)

```json
{
  "problem_id": "ARR-014",
  "tests": [
    { "id": "base_1", "category": "base", "input": { "arr": [2, 1, 0, 2, 0, 1] }, "output": [0, 1, 0, 1, 2, 2], "notes": "Prompt example" },
    { "id": "base_2", "category": "base", "input": { "arr": [1, 1, 0, 2] }, "output": [0, 1, 1, 2], "notes": "Ones remain anchored" },
    { "id": "edge_1", "category": "edge", "input": { "arr": [1] }, "output": [1], "notes": "Only anchor elements" },
    { "id": "corner_1", "category": "corner", "input": { "arr": [0, 2, 0, 2] }, "output": [0, 0, 2, 2], "notes": "No ones to anchor" },
    { "id": "stress_1", "category": "stress", "input": { "arr": [2, 0, 1, 2, 1, 0, 2, 0, 1] }, "output": [0, 0, 1, 0, 1, 2, 2, 2, 1], "notes": "Anchored ones interleaved; zeros fill earliest non-one slots" },
    { "id": "boundary_1", "category": "boundary", "input": { "arr": [2, 0, 2, 0] }, "output": [0, 0, 2, 2], "notes": "No anchors, pure 0/2 sorting" },
    { "id": "large_1", "category": "large", "input": { "arr": [2, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1] }, "output": [0, 1, 0, 0, 1, 2, 2, 1, 2, 2, 1], "notes": "Multiple anchored ones force staggered placement" }
  ]
}
```

---

## Seat Gap After Removals (ARR-015)

```json
{
  "problem_id": "ARR-015",
  "tests": [
    { "id": "base_1", "category": "base", "input": { "seats": [2, 5, 9, 10], "remove_indices": [1] }, "output": 7, "notes": "Prompt example removes seat 5" },
    { "id": "base_2", "category": "base", "input": { "seats": [1, 4, 6, 9], "remove_indices": [0, 3] }, "output": 2, "notes": "Remaining [4,6]" },
    { "id": "edge_1", "category": "edge", "input": { "seats": [1, 3], "remove_indices": [] }, "output": 2, "notes": "No removals" },
    { "id": "corner_1", "category": "corner", "input": { "seats": [1, 3, 6, 10], "remove_indices": [1, 2] }, "output": 9, "notes": "Large gap after removing middle seats" },
    { "id": "stress_1", "category": "stress", "input": { "seats": [1, 2, 4, 7, 11, 16], "remove_indices": [0, 4] }, "output": 9, "notes": "Remaining seats [2,4,7,16]; largest gap 9" },
    { "id": "boundary_1", "category": "boundary", "input": { "seats": [1, 5, 9], "remove_indices": [1] }, "output": 8, "notes": "Removing middle leaves extreme gap" },
    { "id": "large_1", "category": "large", "input": { "seats": [1, 2, 3, 5, 8, 13, 21], "remove_indices": [2, 5] }, "output": 13, "notes": "Remaining [1,2,5,8,21]; largest gap 13" }
  ]
}
```

---

## Power Window With Drop (ARR-016)

```json
{
  "problem_id": "ARR-016",
  "tests": [
    { "id": "base_1", "category": "base", "input": { "arr": [2, 1, 5, 3, 2], "k": 3 }, "output": 10, "notes": "Prompt example, keep window 5,3,2" },
    { "id": "base_2", "category": "base", "input": { "arr": [5, 1, 4], "k": 2 }, "output": 9, "notes": "Drop 1 to use window 5 + 4" },
    { "id": "edge_1", "category": "edge", "input": { "arr": [3, 2, 1], "k": 2 }, "output": 5, "notes": "Dropping hurts; best is full window 3+2" },
    { "id": "corner_1", "category": "corner", "input": { "arr": [1, 1, 1, 1], "k": 4 }, "output": 3, "notes": "Dropping any one element in full window" },
    { "id": "stress_1", "category": "stress", "input": { "arr": [10, 2, 9, 1, 8, 3, 7], "k": 3 }, "output": 21, "notes": "Max window sum 21 from [10,2,9]; dropping is unnecessary" },
    { "id": "boundary_1", "category": "boundary", "input": { "arr": [5, 4, 3], "k": 1 }, "output": 5, "notes": "Window size one, optional drop unused" },
    { "id": "large_1", "category": "large", "input": { "arr": [9, 1, 8, 1, 7, 1, 6, 1], "k": 5 }, "output": 26, "notes": "Best window [9,1,8,1,7] keeps all elements" }
  ]
}
```
