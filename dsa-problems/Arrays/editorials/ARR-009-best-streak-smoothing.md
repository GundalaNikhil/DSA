---
problem_id: ARR_KADANE_SMOOTH__4460
display_id: ARR-009
slug: best-streak-smoothing
title: "Best Streak With One Smoothing"
difficulty: Medium
difficulty_score: 60
topics:
  - Array
  - Dynamic Programming
  - Kadane's Algorithm
  - Optimization
tags:
  - arrays
  - dynamic-programming
  - kadane
  - medium
premium: true
subscription_tier: pro
---

# Best Streak With One Smoothing

![Problem Header](../images/ARR-009/header.png)

### 📋 Problem Summary

Find maximum subarray sum with option to replace one element with 1.

### 🌍 Real-World Scenario

**Student Performance Tracker with Grade Forgiveness**

Imagine tracking daily study scores:

- Most days: positive progress [3, -2, 4]
- Bad day (-2): Had an exam, didn't study
- **Grade smoothing**: Replace ONE score with average of itself and neighbors
- Goal: Find best continuous study streak

Without smoothing: max = 3+(-2)+4 = 5
With smoothing (-2→floor((3-2+4)/3)=1): max = 3+1+4 = 8 ✓

**Real Applications**:

- Portfolio optimization (replace one bad investment)
- Health tracking (one "cheat day" allowed)
- Performance metrics with outlier removal

### 📚 Detailed Explanation

**Kadane's Algorithm Review**:
Classic max subarray: Track running sum, reset if negative

```
maxEndingHere = max(arr[i], maxEndingHere + arr[i])
```

**With Smoothing Twist**:
Need to track TWO states:

1. **No smoothing used yet**: Classic Kadane
2. **Smoothing already used**: Extended with replacement

### ✅ Optimal Approach - Modified Kadane

**Key Insight**: Track maximum sum ending at position i in two scenarios:

- `maxNoSmooth`: Best sum without using smoothing
- `maxWithSmooth`: Best sum having used smoothing once

**At each position**:

```
Option 1: Don't use smoothing
  - Extend previous no-smooth: prevNoSmooth + arr[i]
  - Start fresh: arr[i]

Option 2: Smooth current element to floor((a[i-1]+a[i]+a[i+1])/3)
  - Extend previous no-smooth: prevNoSmooth + smoothedValue
  - Start fresh: smoothedValue

Option 3: Extend previous smoothed
  - prevWithSmooth + arr[i]
```

**Important**: Smoothing replaces a[i] with `floor((a[i-1] + a[i] + a[i+1]) / 3)`, using the actual neighbors.

**⏱️ Time Complexity: O(n)**

- Single pass through array
- Constant work per element

**📦 Space Complexity: O(1)**

- Only track 3 variables

### 🎨 Visual Representation

**Example**: `arr = [-2, 3, -4, 5]`

```
State Tracking at Each Position:

i=0: arr[0]=-2
  maxNoSmooth = -2
  maxWithSmooth = 1 (smooth -2 to 1)
  globalMax = 1

i=1: arr[1]=3
  Previous: noSmooth=-2, withSmooth=1

  New maxNoSmooth:
    - Extend: -2+3=1
    - Fresh: 3
    → max(1, 3) = 3 ✓

  New maxWithSmooth:
    - Smooth current: -2+1=-1
    - Extend smoothed: 1+3=4 ✓
    → max(-1, 4, 1) = 4

  globalMax = 4

i=2: arr[2]=-4
  Previous: noSmooth=3, withSmooth=4

  New maxNoSmooth:
    - Extend: 3+(-4)=-1
    - Fresh: -4
    → max(-1, -4) = -1

  New maxWithSmooth:
    - Smooth current: 3+1=4 ✓
    - Extend smoothed: 4+(-4)=0
    → max(4, 0, 1) = 4

  globalMax = 4

i=3: arr[3]=5
  Previous: noSmooth=-1, withSmooth=4

  New maxNoSmooth:
    - Extend: -1+5=4
    - Fresh: 5
    → max(4, 5) = 5

  New maxWithSmooth:
    - Smooth current: -1+1=0
    - Extend smoothed: 4+5=9 ✓
    → max(0, 9, 1) = 9

  globalMax = 9 ✓

Best: Smooth -4 to 1, take [-2,3,1,5] = 9
```

### 🧪 Test Case Walkthrough

**Input**: `arr = [1, -10, 2, 3]`

```
Try smoothing each valid middle index:

- Smooth index 1: floor((1 + (-10) + 2) / 3) = floor(-7/3) = -3  
  New array: [1, -3, 2, 3] → max subarray = 2 + 3 = 5
- Smooth index 2: floor(((-10) + 2 + 3) / 3) = floor(-5/3) = -2  
  New array: [1, -10, -2, 3] → max subarray = 3

Best possible after exactly one smoothing = **5**.
```

### 💻 Implementations

### Java

```java
class Solution {
    public int maxSubarrayWithSmoothing(int[] a) {
        int n = a.length;
        long[] pref = new long[n];
        long[] suff = new long[n];

        // Kadane prefix (ending at i)
        pref[0] = a[0];
        for (int i = 1; i < n; i++) {
            pref[i] = Math.max(pref[i - 1] + a[i], a[i]);
        }

        // Kadane suffix (starting at i)
        suff[n - 1] = a[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suff[i] = Math.max(suff[i + 1] + a[i], a[i]);
        }

        long ans = pref[0];
        for (int i = 1; i < n; i++) ans = Math.max(ans, pref[i]);

        for (int i = 1; i <= n - 2; i++) {
            long smooth = (long)Math.floor((a[i - 1] + (long)a[i] + a[i + 1]) / 3.0);
            long candidate = pref[i - 1] + smooth + suff[i + 1];
            ans = Math.max(ans, candidate);
        }
        return ans;
    }
}
```

### Python

```python
from math import floor

def max_subarray_with_smoothing(a: list[int]) -> int:
    n = len(a)
    pref = [0] * n
    suff = [0] * n

    pref[0] = a[0]
    for i in range(1, n):
        pref[i] = max(pref[i-1] + a[i], a[i])

    suff[-1] = a[-1]
    for i in range(n-2, -1, -1):
        suff[i] = max(suff[i+1] + a[i], a[i])

    ans = max(pref)
    for i in range(1, n-1):
        smooth = floor((a[i-1] + a[i] + a[i+1]) / 3)
        candidate = pref[i-1] + smooth + suff[i+1]
        ans = max(ans, candidate)
    return ans
```

### C++++

```cpp
class Solution {
public:
    int maxSubarrayWithSmoothing(vector<int>& a) {
        int n = a.size();
        vector<long long> pref(n);
        vector<long long> suff(n);

        // Kadane prefix (ending at i)
        pref[0] = a[0];
        for (int i = 1; i < n; i++) {
            pref[i] = max(pref[i - 1] + a[i], (long long)a[i]);
        }

        // Kadane suffix (starting at i)
        suff[n - 1] = a[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suff[i] = max(suff[i + 1] + a[i], (long long)a[i]);
        }

        long long ans = pref[0];
        for (int i = 1; i < n; i++) ans = max(ans, pref[i]);

        for (int i = 1; i <= n - 2; i++) {
            long long smooth = floor((a[i - 1] + (long long)a[i] + a[i + 1]) / 3.0);
            long long candidate = pref[i - 1] + smooth + suff[i + 1];
            ans = max(ans, candidate);
        }
        return (int)ans;
    }
};

// Time: O(n), Space: O(n)
```

### JavaScript

```javascript
/**
 * @param {number[]} a
 * @return {number}
 */
var maxSubarrayWithSmoothing = function(a) {
    const n = a.length;
    const pref = new Array(n);
    const suff = new Array(n);

    // Kadane prefix (ending at i)
    pref[0] = a[0];
    for (let i = 1; i < n; i++) {
        pref[i] = Math.max(pref[i - 1] + a[i], a[i]);
    }

    // Kadane suffix (starting at i)
    suff[n - 1] = a[n - 1];
    for (let i = n - 2; i >= 0; i--) {
        suff[i] = Math.max(suff[i + 1] + a[i], a[i]);
    }

    let ans = pref[0];
    for (let i = 1; i < n; i++) ans = Math.max(ans, pref[i]);

    for (let i = 1; i <= n - 2; i++) {
        const smooth = Math.floor((a[i - 1] + a[i] + a[i + 1]) / 3);
        const candidate = pref[i - 1] + smooth + suff[i + 1];
        ans = Math.max(ans, candidate);
    }
    return ans;
};

// Time: O(n), Space: O(n)
```

### ⚠️ Common Mistakes

1. **Forgetting to track both states**: Must maintain both smoothed and non-smoothed
2. **Starting fresh with smoothing**: maxWithSmooth can start at 1
3. **Not considering all transitions**: Each state has multiple update paths
4. **Integer overflow**: Use appropriate data types
