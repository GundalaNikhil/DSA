---
problem_id: ARR_ZIGZAG_SUB__9912
display_id: ARR-023
slug: longest-zigzag-subarray
title: "Longest Zigzag Subarray"
difficulty: Easy
difficulty_score: 18
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - coding-interviews
  - data-structures
  - greedy
  - iteration
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
---

# ARR-023: Longest Zigzag Subarray

## 📋 Problem Summary

Find the length of the longest contiguous subarray where consecutive differences strictly **alternate in sign**. The differences must be non-zero (no plateaus) and follow a pattern like: positive, negative, positive, negative... or negative, positive, negative, positive...

**Key Requirements:**

- Consecutive differences must alternate signs
- Zero differences break the zigzag pattern
- Return the maximum length found

**Examples:**

```
[1, 3, 2, 4] → Diffs: [+2, -1, +2] → Alternating → Length 4
[1, 2, 3] → Diffs: [+1, +1] → NOT alternating → Length 2
[5, 1, 3, 1, 3] → Diffs: [-4, +2, -2, +2] → Alternating → Length 5
```

## 🌍 Real-World Scenarios

**Scenario 1:** ⛰️ **Mountain Path Elevation Analysis**

You're hiking a trail and recording elevation at regular intervals. A "good hiking trail" alternates between uphill and downhill segments (zigzag pattern). Find the longest stretch of trail that maintains this alternating pattern - it's considered the most scenic and balanced workout.

**Scenario 2:** 📈 **Stock Price Oscillation Detection**

In trading, certain oscillating price patterns (up-down-up-down) indicate specific market conditions. Detect the longest period where stock prices alternate between rising and falling days, signaling high volatility or consolidation patterns.

**Scenario 3:** 🏃 **Heart Rate Variability Training**

During interval training, ideal heart rate follows a zigzag: increase during exercise, decrease during rest, increase again. Find the longest period where your heart rate properly alternates between increasing and decreasing phases.

**Scenario 4:** 🌊 **Wave Pattern Recognition**

Ocean wave sensors record wave heights. A "good surfing condition" has waves that alternate between rising (crest forming) and falling (trough). Identify the longest sequence of alternating wave movements.

**Scenario 5:** 🔊 **Audio Signal Quality**

In audio processing, certain desirable waveforms exhibit alternating positive and negative slopes. Detect the longest segment where an audio signal maintains this zigzag pattern, indicating clean oscillation without distortion (plateaus).

### Real-World Relevance

- **Signal Processing:** Detecting alternating patterns in time series
- **Technical Trading:** Identifying oscillation patterns in price charts
- **Sports Science:** Analyzing interval training effectiveness
- **Quality Control:** Detecting periodic variations in manufacturing
- **Seismology:** Analyzing earthquake wave patterns

## 🚀 Detailed Explanation

### 1. Understanding Zigzag Patterns

A zigzag pattern means the **direction changes** at every step.

**Visual Example:**

```
Array: [1, 3, 2, 4, 3, 5, 6]
         ↓  ↓  ↓  ↓  ↓  ↓
Diffs:   +2 -1 +2 -1 +2 +1
Signs:   +  -  +  -  +  +  ← Breaks here!

Zigzag continues: 1→3→2→4→3→5 (length 6)
Breaks at 5→6 because +2 followed by +1 (both positive)
```

**Pattern Types:**

1. **Up-Down**: +, -, +, -, ... (starts going up)
2. **Down-Up**: -, +, -, +, ... (starts going down)

### 2. Difference-Based Approach

**Key Insight:** Instead of looking at values, look at **differences** and their **signs**.

```
For array [a₀, a₁, a₂, ..., aₙ₋₁]:
diff[i] = a[i+1] - a[i]  for i = 0 to n-2

Zigzag condition:
- diff[i] and diff[i+1] must have opposite signs
- diff[i] ≠ 0 (no plateaus)
```

**Example Walkthrough:**

```
Input: [1, 3, 2, 4, 3]

Calculate differences:
diff[0] = 3 - 1 = +2 (positive)
diff[1] = 2 - 3 = -1 (negative)
diff[2] = 4 - 2 = +2 (positive)
diff[3] = 3 - 4 = -1 (negative)

Check alternation:
diff[0] vs diff[1]: +2 vs -1 → opposite signs ✓
diff[1] vs diff[2]: -1 vs +2 → opposite signs ✓
diff[2] vs diff[3]: +2 vs -1 → opposite signs ✓

All consecutive pairs alternate → length = 5 (all elements)
```

### 3. Sign-Based State Machine

We can track the **current sign** and **length** as we iterate:

**States:**

- `NONE`: Haven't started (initial or after reset)
- `POSITIVE`: Last difference was positive (+)
- `NEGATIVE`: Last difference was negative (-)

**Transitions:**

```
Current State | Current Diff | Action
--------------|--------------|---------------------------
NONE          | d > 0        | Set POSITIVE, length = 2
NONE          | d < 0        | Set NEGATIVE, length = 2
NONE          | d = 0        | Stay NONE, length = 1
POSITIVE      | d < 0        | Continue alternating, length++
POSITIVE      | d > 0        | Reset to POSITIVE, length = 2
POSITIVE      | d = 0        | Reset to NONE, length = 1
NEGATIVE      | d > 0        | Continue alternating, length++
NEGATIVE      | d < 0        | Reset to NEGATIVE, length = 2
NEGATIVE      | d = 0        | Reset to NONE, length = 1
```

### 4. Greedy Algorithm

**Algorithm:**

```
1. Initialize: currentLength = 1, maxLength = 1, lastSign = 0
2. For each adjacent pair (i, i+1):
   a. Calculate diff = arr[i+1] - arr[i]
   b. Determine sign = sign(diff)

   c. If diff == 0:
      - Reset: currentLength = 1, lastSign = 0

   d. Else if lastSign == 0:
      - Start new sequence: currentLength = 2, lastSign = sign

   e. Else if sign == -lastSign:
      - Continue zigzag: currentLength++

   f. Else (sign == lastSign):
      - Break zigzag, start new: currentLength = 2, lastSign = sign

   g. Update maxLength = max(maxLength, currentLength)

3. Return maxLength
```

**Detailed Example:**

```
Input: [5, 1, 3, 1, 3]

i=0: diff = 1-5 = -4, sign = -1
     lastSign = 0 → Start sequence
     currentLength = 2, lastSign = -1, maxLength = 2

i=1: diff = 3-1 = +2, sign = +1
     sign (+1) == -lastSign (-(-1)=+1) → Continue
     currentLength = 3, maxLength = 3

i=2: diff = 1-3 = -2, sign = -1
     sign (-1) == -lastSign (-(+1)=-1) → Continue
     currentLength = 4, maxLength = 4

i=3: diff = 3-1 = +2, sign = +1
     sign (+1) == -lastSign (-(-1)=+1) → Continue
     currentLength = 5, maxLength = 5

Result: 5 (entire array is zigzag)
```

### 🔄 Algorithm Flow Diagram

```mermaid
flowchart TD
    A[Start] --> B[maxLen = 1, curLen = 1, lastSign = 0]
    B --> C[Loop i from 0 to N-2]
    C --> D[diff = arr[i+1] - arr[i]]
    D --> E{diff == 0?}
    E -- Yes --> F[curLen = 1, lastSign = 0]
    E -- No --> G[sign = diff > 0 ? +1 : -1]
    G --> H{lastSign == 0?}
    H -- Yes --> I[curLen = 2, lastSign = sign]
    H -- No --> J{sign == -lastSign?}
    J -- Yes Alternate --> K[curLen++]
    J -- No Same Sign --> L[curLen = 2, lastSign = sign]
    F --> M[maxLen = max maxLen, curLen]
    I --> M
    K --> M
    L --> M
    M --> C
    C -- End --> N[Return maxLen]
```

                    currentLength++;
                } else {
                    // Same sign: break and restart
                    currentLength = 2;
                    lastSign = sign;
                }
            }

            maxLength = max(maxLength, currentLength);
        }

        return maxLength;
    }
};
```

**C++ Note:** Use `long long` for diff calculation to prevent overflow.

### JavaScript Implementation

```javascript
class Solution {
  longestZigzagSubarray(arr) {
    const n = arr.length;
    if (n <= 1) return n;

    let maxLength = 1;
    let currentLength = 1;
    let lastSign = 0; // 0: none, 1: positive, -1: negative

    for (let i = 0; i < n - 1; i++) {
      const diff = arr[i + 1] - arr[i];

      if (diff === 0) {
        // Plateau: reset
        currentLength = 1;
        lastSign = 0;
      } else {
        const sign = diff > 0 ? 1 : -1;

        if (lastSign === 0) {
          // Starting new sequence
          currentLength = 2;
          lastSign = sign;
        } else if (sign === -lastSign) {
          // Alternating: continue zigzag
          currentLength++;
        } else {
          // Same sign: break and restart
          currentLength = 2;
          lastSign = sign;
        }
      }

      maxLength = Math.max(maxLength, currentLength);
    }

    return maxLength;
  }
}
```

## 🔍 Complexity Analysis

### Time Complexity: O(N)

- Single pass through array: N-1 iterations
- Each iteration: O(1) operations (diff, comparison, updates)
- **Total: O(N)**

### Space Complexity: O(1)

- Only using variables: `maxLength`, `currentLength`, `lastSign`, `diff`, `sign`
- No additional data structures
- **Total: O(1)** auxiliary space

### Optimality

This is **optimal**:

- Must examine every element at least once: Ω(N)
- Cannot use better than O(1) space for this greedy approach

## 🧪 Edge Cases & Testing

### Edge Case 1: Single Element

```
Input: [5]
Output: 1
Explanation: Any single element is trivially a zigzag
```

### Edge Case 2: Two Elements - Different

```
Input: [1, 3]
Output: 2
Explanation: One difference, automatically zigzag
```

### Edge Case 3: Two Elements - Same

```
Input: [5, 5]
Output: 1
Explanation: Difference is 0, plateau breaks zigzag
```

### Edge Case 4: All Equal (Plateau)

```
Input: [7, 7, 7, 7]
Output: 1
Explanation: All differences are 0, no zigzag possible
```

### Edge Case 5: Strictly Monotonic Increasing

```
Input: [1, 2, 3, 4, 5]
Differences: [+1, +1, +1, +1]
Output: 2
Explanation: All differences positive, max zigzag is 2 (any adjacent pair)
```

### Edge Case 6: Strictly Monotonic Decreasing

```
Input: [10, 8, 6, 4, 2]
Differences: [-2, -2, -2, -2]
Output: 2
Explanation: All differences negative, max zigzag is 2
```

### Edge Case 7: Perfect Zigzag

```
Input: [1, 5, 2, 6, 3, 7]
Differences: [+4, -3, +4, -3, +4]
Output: 6
Explanation: Entire array is zigzag
```

### Edge Case 8: Multiple Separate Zigzags

```
Input: [1, 3, 2, 5, 6, 4, 6, 4]
Differences: [+2, -1, +3, +1, -2, +2, -2]
Segments: [1,3,2,5] [5,6] [6,4,6,4]
Lengths:     4        2       4
Output: 4
```

### Edge Case 9: Plateau in Middle

```
Input: [1, 3, 3, 2, 4]
Differences: [+2, 0, -1, +2]
Breaks at index 1 (0 difference)
Output: 3 (either [1,3,3] or [3,2,4])
```

> [!TIP]
> Always test with: single element, all equal, strictly monotonic, perfect zigzag, and plateaus.

## ⚠️ Common Pitfalls & Debugging

### Pitfall 1: Forgetting to Handle diff = 0

```python
# ❌ Wrong: Doesn't handle plateaus
if sign == -last_sign:
    current_length += 1
else:
    current_length = 2

# ✓ Correct: Explicit plateau handling
if diff == 0:
    current_length = 1
    last_sign = 0
elif sign == -last_sign:
    current_length += 1
```

### Pitfall 2: Not Resetting Properly

```java
// ❌ Wrong: Doesn't restart correctly
if (sign != -lastSign) {
    currentLength = 1;  // Wrong! Should be 2
}

// ✓ Correct: New sequence has 2 elements
if (sign != -lastSign) {
    currentLength = 2;  // Current pair is valid
    lastSign = sign;
}
```

### Pitfall 3: Integer Overflow in Difference

```cpp
// ❌ Wrong: May overflow
int diff = arr[i + 1] - arr[i];  // If values near INT_MAX/INT_MIN

// ✓ Correct: Use long long
long long diff = (long long)arr[i + 1] - arr[i];
```

### Pitfall 4: Off-by-One in Loop

```javascript
// ❌ Wrong: Misses last element
for (let i = 0; i < n - 2; i++) {
  // Only processes n-2 pairs!
}

// ✓ Correct: Process all n-1 pairs
for (let i = 0; i < n - 1; i++) {
  // Compares arr[i+1] with arr[i]
}
```

## 🎯 Variations & Extensions

### Variation 1: Count All Zigzag Subarrays

Count the **number** of zigzag subarrays (not just max length):

```python
def countZigzagSubarrays(arr):
    # For each valid zigzag of length L, it contains L subarrays
    # Track all valid lengths and sum
    pass
```

### Variation 2: Return the Zigzag Subarray

Instead of length, return the actual subarray:

```java
public int[] longestZigzagSubarrayElements(int[] arr) {
    // Track start index of max zigzag
    int maxStart = 0, maxEnd = 0;
    // ... algorithm
    return Arrays.copyOfRange(arr, maxStart, maxEnd + 1);
}
```

### Variation 3: K-Tolerance Zigzag

Allow up to K consecutive non-alternating pairs:

```python
def zigzagWithTolerance(arr, K):
    violations = 0
    # Continue zigzag even if sign doesn't alternate
    # But track violations, reset if > K
    pass
```

### Variation 4: Weighted Zigzag

Each element has a weight, find zigzag with maximum total weight:

```python
def maxWeightZigzag(arr, weights):
    # Track not just length but accumulated weight
    pass
```

### Variation 5: 2D Zigzag Path

In a 2D grid, find longest path where vertical and horizontal moves alternate:

```
Grid path: (0,0) → (0,1) → (1,1) → (1,2) → (2,2)
Directions: right, down, right, down (alternating)
```

## 🎓 Key Takeaways

1. **Difference arrays** simplify pattern detection problems
2. **Sign-based logic** reduces complex conditions to simple comparisons
3. **Greedy approach** works when we can locally decide whether to extend or reset
4. **State machines** (NONE/POSITIVE/NEGATIVE) model transition logic clearly
5. **Edge case testing** is critical: empty, single, plateau, perfect zigzag

## 📚 Related Problems

- **Longest Mountain in Array:** Similar but requires specific min length of up/down segments
- **Wiggle Subsequence:** Non-contiguous version of zigzag
- **Stock Buy Sell Multiple Transactions:** Detect alternating buy/sell opportunities
- **Zig Zag Conversion:** String manipulation with zigzag pattern
- **Peak Valley Pattern:** Related signal processing problem

## 🔗 Additional Resources

- **Dynamic Programming:** When greedy doesn't suffice
- **State Machines:** Modeling transitions in sequential data
- **Signal Analysis:** Detecting oscillations in time series
- **Pattern Recognition:** Algorithmic approaches to sequence patterns
