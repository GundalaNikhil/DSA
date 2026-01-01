---
id: STR-006
title: Minimal Unique Rotation
sidebar_label: STR-006 - Minimal Unique Rotation
tags:
- strings
- rotation
- booth-algorithm
- medium
difficulty: Medium
difficulty_score: 42
problem_id: STR_MINIMAL_UNIQUE_ROTATION__1006
display_id: STR-006
slug: minimal-unique-rotation
topics:
- String Manipulation
- Booth Algorithm
- Rotation
---
# STR-006: Minimal Unique Rotation

## 📋 Problem Summary

**Input**: String `s` (lowercase letters)  
**Output**: Lexicographically smallest rotation that differs from original, or original if all rotations equal  
**Constraints**: `1 <= |s| <= 10^5`

## 🌍 Real-World Scenario

Circular data structures (like DNA sequences or circular shift registers) need canonical representations. Finding the minimal rotation ensures consistent identification across different starting positions.

## Detailed Explanation

**Rotation**: Shift characters cyclically. For "abc", rotations are "abc", "bca", "cab"

**Goal**: Among all rotations ≠ original, find the lexicographically smallest

**Special Case**: If all characters identical (e.g., "aaa"), all rotations equal → return original

**Example**: "bba"

- Rotations: "bba" (original), "bab", "abb"
- Excluding original: "bab", "abb"
- Smallest: "abb"

## Naive Approach

```
1. Generate all n rotations
2. Filter out the original
3. Find the lexicographically smallest
```

### Time Complexity: **O(n²)**

- Generating n rotations: O(n²)
- Comparing strings: O(n) per comparison

### Space Complexity: **O(n²)**

- Storing all rotations

## Optimal Approach

**Use Booth's Algorithm + Filter Original**:

Booth's algorithm finds the minimal rotation in O(n) time by analyzing the doubled string.

**Algorithm**:

```
1. Use Booth's algorithm to find minimal rotation index
2. Generate minimal rotation
3. If it equals original:
   - All rotations identical
   - Return original
4. Else:
   - Return minimal rotation
```

**Booth's Algorithm Core**:

```
1. doubled = s + s
2. failure = array of size 2n, initialized to -1
3. k = 0  # minimal rotation start index
4. For j from 1 to 2n-1:
   i = failure[j - k - 1]
   While i != -1 and doubled[j] != doubled[k + i + 1]:
      If doubled[j] < doubled[k + i + 1]:
         k = j - i - 1
      i = failure[i]

   If doubled[j] != doubled[k + i + 1]:
      If doubled[j] < doubled[k + i + 1]:
         k = j
      failure[j - k] = -1
   Else:
      failure[j - k] = i + 1
5. Return k
```

### Time Complexity

| Phase                 | Operations                    | Cost     |
| --------------------- | ----------------------------- | -------- |
| Booth's algorithm     | Linear scan of doubled string | O(n)     |
| Generate rotation     | Substring + concatenation     | O(n)     |
| Compare with original | String equality               | O(n)     |
| **Total**             |                               | **O(n)** |

### Space Complexity

| Component      | Space | Justification   |
| -------------- | ----- | --------------- |
| doubled string | O(n)  | 2n characters   |
| failure array  | O(n)  | 2n integers     |
| Result string  | O(n)  | At most n chars |
| **Total**      |       | **O(n)**        |

## 💻 Implementation

### Python


### Java


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `s = "bba"`

**Step 1: Apply Booth's Algorithm**

```
doubled = "bbabba"
n = 3
failure = [-1, -1, -1, -1, -1, -1]
k = 0 (minimal rotation start index)

j=1: doubled[1]='b', doubled[k+i+1]=doubled[0]='b' → equal
     failure[1-0]=failure[1]=0

j=2: doubled[2]='a', doubled[k+i+1]=doubled[1]='b' → 'a'<'b'
     k = 2
     failure[2-2]=failure[0]=-1

j=3: doubled[3]='b', k=2, doubled[k+i+1]=doubled[2]='a' → 'b'>'a', no update
     i = failure[0] = -1
     failure[3-2]=failure[1]=-1

j=4: doubled[4]='b', k=2, doubled[k+i+1]=doubled[2]='a' → 'b'>'a'
     i = -1
     failure[4-2]=failure[2]=-1

j=5: doubled[5]='a', k=2, doubled[k+i+1]=doubled[2]='a' → equal
     failure[5-2]=failure[3]=0

Result: k = 2
```

**Step 2: Generate Minimal Rotation**

```
minIdx = 2
minRotation = s[2:] + s[:2] = "a" + "bb" = "abb"
```

**Step 3: Compare with Original**

```
minRotation = "abb"
original = "bba"
"abb" ≠ "bba" → return "abb"
```

**Output**: `"abb"`

## ⚠️ Common Mistakes to Avoid

1. **Generating All Rotations**: O(n²) approach when O(n) exists
2. **Not Handling Identical Chars**: Forgetting special case where all chars same
3. **Wrong Booth Implementation**: Failure array logic is subtle
4. **String Comparison Overhead**: Using multiple comparisons instead of single check
5. **Off-By-One Errors**: Index calculations in Booth's algorithm

## 💡 Key Takeaways

1. **Booth's Algorithm**: Elegant O(n) solution for minimal rotation
2. **Doubled String Trick**: s+s contains all rotations as substrings
3. **Failure Function**: Adapted from KMP for rotation finding
4. **Special Case Handling**: All-identical characters need explicit check
5. **Linear Time String Algorithms**: Often exist for circular/rotation problems


## Constraints

- `1 ≤ |s| ≤ 10^5`
- `s` contains only lowercase English letters