---
problem_id: STR_RABIN_KARP_COLLISION_DETECTION__2313
display_id: NTB-STR-2313
slug: rabin-karp-collision-detection
title: "Rabin-Karp with Collision Detection"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - pattern-matching
  - rabin-karp-collision-detection
  - string-manipulation
  - strings
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Rabin-Karp with Collision Detection

## Problem Statement

You are given a text string `T` and a pattern string `P`. Use Rabin-Karp with **double hashing** to find all occurrences of `P` in `T`. Whenever the two hashes match for an alignment, you must verify the substring to detect collisions.

Report:

1. The number of exact matches of `P` in `T`.
2. The number of **false hash matches** (hashes equal but substring different).

Hashing must use the following deterministic constants:

- `mod1 = 1000000007`
- `mod2 = 1000000009`
- `base = 911382323`

Character mapping: `'a' -> 1`, `'b' -> 2`, ..., `'z' -> 26`.

## Input Format

- First line: string `T`
- Second line: string `P`

## Output Format

- Two integers: `exact_matches false_hash_matches`

## Constraints

- `1 <= |T|, |P| <= 200000`
- Strings contain only lowercase English letters

## Clarifying Notes

- If `|P| > |T|`, output `0 0`.
- A false hash match is counted only when **both** hashes match but the substring is not equal to `P`.
- Double hashing is required to make collisions detectable and deterministic.

## Example Input

```
ababa
aba
```

## Example Output

```
2 0
```

## Solution Stubs

### Java

```java
import java.util.*;

public class Solution {
    public int[] solveRabinKarp(String t, String p) {
        // Your code here
        return new int[]{0, 0};
    }
}
```

### Python

```python
class Solution:
    def solveRabinKarp(self, t: str, p: str) -> list[int]:
        # Your code here
        pass
```

### C++

```cpp
#include <string>
#include <vector>

class Solution {
public:
    std::pair<int, int> solveRabinKarp(std::string t, std::string p) {
        // Your code here
        return {0, 0};
    }
};
```

### JavaScript

```javascript
class Solution {
  solveRabinKarp(t, p) {
    // Your code here
    return [0, 0];
  }
}
```
