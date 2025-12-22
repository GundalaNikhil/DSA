---
problem_id: HSH_MAX_REPEATED_BLOCK_LENGTH__5827
display_id: HSH-008
slug: max-repeated-block-length
title: "Maximum Repeated Block Length"
difficulty: Medium
difficulty_score: 55
topics:
  - Hashing
  - Binary Search
  - String Algorithms
tags:
  - hashing
  - binary-search
  - substring
  - medium
premium: true
subscription_tier: basic
---

# HSH-008: Maximum Repeated Block Length

## 📋 Problem Summary

You are given a string `s`. Find the maximum length `L` such that there are two **non-overlapping** substrings of length `L` that are identical.
Non-overlapping means if the first substring is at indices `[i, i+L-1]` and the second at `[j, j+L-1]`, then the intervals must not intersect (i.e., `i+L <= j` assuming `i < j`).

## 🌍 Real-World Scenario

**Scenario Title:** Audio Sample Looping

Imagine you are editing a music track. You want to find the longest "loop" or repeated beat that occurs in the song to use it as a sample.
- However, the loop must be distinct; you can't just pick a sound that overlaps with itself (like a continuous "aaaaa" sound).
- You need two separate occurrences of the same sound pattern to create a clean transition or echo effect.

![Real-World Application](../images/HSH-008/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Overlapping vs Non-Overlapping

String: "aaaaa"

**Length 2:**
- "aa" at index 0 (0-1)
- "aa" at index 2 (2-3)
- Indices: [0,1] and [2,3]. No overlap. Valid.

**Length 3:**
- "aaa" at index 0 (0-2)
- "aaa" at index 1 (1-3) -> Overlap!
- "aaa" at index 2 (2-4) -> Overlap with index 0?
  - [0,2] and [2,4]. Overlap at index 2?
  - Indices are inclusive. 0,1,2 vs 2,3,4. Overlap at 2.
  - Usually means `end1 < start2`.
  - `0+3 = 3`. Next start must be $\ge 3$.
  - Can we find "aaa" starting at $\ge 3$? No. String length 5.
  - So Length 3 is invalid.

Max Length: 2.

### Key Concept: Binary Search on Answer

If a non-overlapping repeated substring of length `L` exists, does one of length `L-1` exist?
Yes. Just trim the last character of both occurrences. They remain equal and non-overlapping.
This monotonicity allows **Binary Search**.
- Range: `[0, N/2]`. (Max possible length is N/2).
- Check `possible(len)`:
  - Use Rolling Hash.
  - Store the **first occurrence index** of each hash in a Map.
  - For current substring at `i`, if hash exists in Map at `first_pos`:
    - Check if `first_pos + len <= i`.
    - If yes, return true.
    - If no, keep the `first_pos` (don't update it, we want the earliest start to maximize gap).

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** String `s`.
- **Output:** Integer `L`.
- **Constraints:** $|s| \le 10^5$.
- **Non-overlapping:** `end1 < start2`.

## Naive Approach

### Intuition

Check all pairs of substrings.

### Algorithm

1. Loop length `len` from `N/2` down to 1.
2. Loop `i` from 0 to `N - 2*len`.
3. Loop `j` from `i + len` to `N - len`.
4. Compare `s[i..i+len]` with `s[j..j+len]`.
5. If match, return `len`.

### Time Complexity

- **O(N^3)**: Three nested loops. Too slow.

## Optimal Approach

### Key Insight

Combine **Binary Search** and **Rolling Hash**.
- Binary search for length `L`.
- For a fixed `L`, compute rolling hashes.
- Store `Map<Long, Integer>` mapping `hash -> first_start_index`.
- When seeing a hash again at `curr_start_index`:
  - If `curr_start_index >= map.get(hash) + L`, valid! Return true.
  - Else, ignore (don't update map, keeping the earliest occurrence gives best chance for non-overlap).

### Algorithm

1. `low = 0`, `high = n / 2`.
2. While `low <= high`:
   - `mid = (low + high) / 2`.
   - If `check(mid)`: `ans = mid`, `low = mid + 1`.
   - Else: `high = mid - 1`.
3. Return `ans`.

**Check(len):**
1. Map `first_occurrence`.
2. Compute rolling hash for window size `len`.
3. For each window starting at `i`:
   - If hash not in map, `put(hash, i)`.
   - Else if `i >= map.get(hash) + len`, return true.
4. Return false.

### Time Complexity

- **O(N \log N)**.

### Space Complexity

- **O(N)**: Map storage.

![Algorithm Visualization](../images/HSH-008/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private static final long MOD = 1_000_000_007L;
    private static final long BASE = 313L;
    
    public int maxRepeatedBlockLength(String s) {
        int n = s.length();
        int low = 0, high = n / 2;
        int ans = 0;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (mid == 0) {
                low = mid + 1;
                continue;
            }
            
            if (check(s, mid)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }
    
    private boolean check(String s, int len) {
        int n = s.length();
        Map<Long, Integer> firstOccurrence = new HashMap<>();
        
        long currentHash = 0;
        long power = 1;
        
        // Precompute BASE^(len-1)
        for (int i = 0; i < len - 1; i++) {
            power = (power * BASE) % MOD;
        }
        
        // Initial window
        for (int i = 0; i < len; i++) {
            currentHash = (currentHash * BASE + s.charAt(i)) % MOD;
        }
        firstOccurrence.put(currentHash, 0);
        
        // Slide window
        for (int i = 1; i <= n - len; i++) {
            // Remove char at i-1
            long remove = (s.charAt(i - 1) * power) % MOD;
            currentHash = (currentHash - remove + MOD) % MOD;
            
            // Add char at i+len-1
            currentHash = (currentHash * BASE + s.charAt(i + len - 1)) % MOD;
            
            if (firstOccurrence.containsKey(currentHash)) {
                int firstIdx = firstOccurrence.get(currentHash);
                if (i >= firstIdx + len) {
                    return true;
                }
            } else {
                firstOccurrence.put(currentHash, i);
            }
        }
        
        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine();
            Solution solution = new Solution();
            System.out.println(solution.maxRepeatedBlockLength(s));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def max_repeated_block_length(self, s: str) -> int:
        n = len(s)
        MOD = 10**9 + 7
        BASE = 313
        
        def check(length):
            if length == 0: return True
            
            first_occurrence = {}
            current_hash = 0
            power = pow(BASE, length - 1, MOD)
            
            # Initial window
            for i in range(length):
                current_hash = (current_hash * BASE + ord(s[i])) % MOD
            first_occurrence[current_hash] = 0
            
            # Slide window
            for i in range(1, n - length + 1):
                remove = (ord(s[i - 1]) * power) % MOD
                current_hash = (current_hash - remove + MOD) % MOD
                current_hash = (current_hash * BASE + ord(s[i + length - 1])) % MOD
                
                if current_hash in first_occurrence:
                    if i >= first_occurrence[current_hash] + length:
                        return True
                else:
                    first_occurrence[current_hash] = i
            return False

        low, high = 0, n // 2
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            if mid == 0:
                low = mid + 1
                continue
            
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans

def max_repeated_block_length(s: str) -> int:
    solver = Solution()
    return solver.max_repeated_block_length(s)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    print(max_repeated_block_length(s))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
    const long long MOD = 1e9 + 7;
    const long long BASE = 313;

public:
    int maxRepeatedBlockLength(string s) {
        int n = s.length();
        int low = 0, high = n / 2;
        int ans = 0;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (mid == 0) {
                low = mid + 1;
                continue;
            }
            
            if (check(s, mid)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }
    
    bool check(const string& s, int len) {
        int n = s.length();
        unordered_map<long long, int> firstOccurrence;
        
        long long currentHash = 0;
        long long power = 1;
        
        for (int i = 0; i < len - 1; i++) {
            power = (power * BASE) % MOD;
        }
        
        for (int i = 0; i < len; i++) {
            currentHash = (currentHash * BASE + s[i]) % MOD;
        }
        firstOccurrence[currentHash] = 0;
        
        for (int i = 1; i <= n - len; i++) {
            long long remove = (s[i - 1] * power) % MOD;
            currentHash = (currentHash - remove + MOD) % MOD;
            currentHash = (currentHash * BASE + s[i + len - 1]) % MOD;
            
            if (firstOccurrence.count(currentHash)) {
                if (i >= firstOccurrence[currentHash] + len) {
                    return true;
                }
            } else {
                firstOccurrence[currentHash] = i;
            }
        }
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string s;
    if (getline(cin, s)) {
        Solution solution;
        cout << solution.maxRepeatedBlockLength(s) << "\n";
    }
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxRepeatedBlockLength(s) {
    const n = s.length;
    const MOD = 1000000007n;
    const BASE = 313n;
    
    const check = (len) => {
      if (len === 0) return true;
      
      const firstOccurrence = new Map();
      let currentHash = 0n;
      let power = 1n;
      
      for (let i = 0; i < len - 1; i++) {
        power = (power * BASE) % MOD;
      }
      
      for (let i = 0; i < len; i++) {
        const code = BigInt(s.charCodeAt(i));
        currentHash = (currentHash * BASE + code) % MOD;
      }
      firstOccurrence.set(currentHash, 0);
      
      for (let i = 1; i <= n - len; i++) {
        const removeCode = BigInt(s.charCodeAt(i - 1));
        const addCode = BigInt(s.charCodeAt(i + len - 1));
        
        let remove = (removeCode * power) % MOD;
        currentHash = (currentHash - remove + MOD) % MOD;
        currentHash = (currentHash * BASE + addCode) % MOD;
        
        if (firstOccurrence.has(currentHash)) {
          if (i >= firstOccurrence.get(currentHash) + len) {
            return true;
          }
        } else {
          firstOccurrence.set(currentHash, i);
        }
      }
      return false;
    };
    
    let low = 0, high = Math.floor(n / 2);
    let ans = 0;
    
    while (low <= high) {
      const mid = Math.floor((low + high) / 2);
      if (mid === 0) {
        low = mid + 1;
        continue;
      }
      
      if (check(mid)) {
        ans = mid;
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }
    return ans;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  const s = data[0];

  const solution = new Solution();
  console.log(solution.maxRepeatedBlockLength(s));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
abcabc
```
$N=6$. Range `[0, 3]`.

**Check 1 (Mid=1):**
- "a" at 0. "a" at 3. Gap $\ge 1$. Valid.
- Ans = 1. Range `[2, 3]`.

**Check 2 (Mid=2):**
- "ab" at 0. "ab" at 3. Gap $\ge 2$. Valid.
- Ans = 2. Range `[3, 3]`.

**Check 3 (Mid=3):**
- "abc" at 0. "abc" at 3. Gap $\ge 3$. Valid.
- Ans = 3. Range `[4, 3]`. Loop ends.

**Result:** 3.

## ✅ Proof of Correctness

### Invariant
If we find a valid pair of length $L$, we record it.
Since we search for the *maximum* $L$, and the property is monotonic, binary search works.
The non-overlapping condition `start2 >= start1 + L` is strictly enforced.

## 💡 Interview Extensions

- **Extension 1:** Allow overlapping?
  - *Answer:* Just check `firstOccurrence.containsKey(hash)`. Don't check indices.
- **Extension 2:** Find the actual substring?
  - *Answer:* Return the substring corresponding to the hash when found.

### C++ommon Mistakes to Avoid

1. **Overlapping Check**
   - ❌ Wrong: `start2 > start1`.
   - ✅ Correct: `start2 >= start1 + len`.
2. **Updating Map**
   - ❌ Wrong: Always updating `firstOccurrence` to the latest index.
   - ✅ Correct: Only set it if it's the *first* time seeing the hash. We want the maximum gap.

## Related Concepts

- **Longest Repeated Substring:** Usually allows overlap.
- **Suffix Tree:** Can solve this in $O(N)$.
