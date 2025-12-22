---
problem_id: HSH_POLYNOMIAL_HASH_PREFIXES__3824
display_id: HSH-001
slug: polynomial-hash-prefixes
title: "Polynomial Hash of Prefixes"
difficulty: Easy
difficulty_score: 25
topics:
  - Hashing
  - Rolling Hash
  - String Algorithms
tags:
  - hashing
  - rolling-hash
  - polynomial-hash
  - easy
premium: true
subscription_tier: basic
---

# HSH-001: Polynomial Hash of Prefixes

## 📋 Problem Summary

You are given a string `s` and two integers `B` (base) and `M` (modulus). Your task is to compute the polynomial rolling hash for every prefix of the string.
The hash of a prefix $s[0 \dots i]$ is defined recursively:
- $H_0 = s[0] \pmod M$
- $H_i = (H_{i-1} \times B + s[i]) \pmod M$

## 🌍 Real-World Scenario

**Scenario Title:** Digital Fingerprinting

Imagine you are building a system to detect plagiarism in documents. Comparing entire documents character by character is slow. Instead, you convert each document (or sentence) into a unique number called a "fingerprint" or "hash".
- If two documents have different fingerprints, they are definitely different.
- If they have the same fingerprint, they are likely the same.

In this problem, we are computing the fingerprint for every "beginning part" (prefix) of a document. This is the first step in more complex algorithms like Rabin-Karp, which can find a specific pattern inside a massive text by comparing these fingerprints efficiently.

![Real-World Application](../images/HSH-001/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Rolling Calculation

String: "abc", Base: 10, Mod: 1000 (for simplicity)
ASCII: 'a'=97, 'b'=98, 'c'=99

```text
Step 1: Prefix "a"
Hash = 97
Result: [97]

Step 2: Prefix "ab"
Previous Hash = 97
New Char = 'b' (98)
Hash = (97 * 10 + 98) % 1000
     = (970 + 98) % 1000
     = 1068 % 1000
     = 68
Result: [97, 68]

Step 3: Prefix "abc"
Previous Hash = 68
New Char = 'c' (99)
Hash = (68 * 10 + 99) % 1000
     = (680 + 99) % 1000
     = 779 % 1000
     = 779
Result: [97, 68, 779]
```

### Key Concept: Polynomial Rolling Hash

The formula $H_i = (H_{i-1} \times B + s[i]) \pmod M$ essentially treats the string as a number in base $B$.
For string "abc":
- "a" $\approx 97$
- "ab" $\approx 97 \times B + 98$
- "abc" $\approx (97 \times B + 98) \times B + 99 = 97 \times B^2 + 98 \times B^1 + 99 \times B^0$

This allows us to compute the hash of a new prefix in $O(1)$ time using the previous result, rather than re-scanning the whole string.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** String `s`, integers `B` and `M`.
- **Output:** Array of integers where the $i$-th element is the hash of $s[0 \dots i]$.
- **Indexing:** 0-based.
- **Modulo:** All calculations must be modulo `M` to prevent overflow.

## Naive Approach

### Intuition

For each prefix $s[0 \dots i]$, loop from $0$ to $i$ to compute the polynomial value.

### Algorithm

1. Loop `i` from 0 to `n-1`.
2. Inside, loop `j` from 0 to `i`.
3. Compute $\sum s[j] \times B^{i-j} \pmod M$.
4. Store result.

### Time Complexity

- **O(N^2)**: Sum of $1 + 2 + \dots + N$ operations. Too slow for $N=2 \cdot 10^5$.

## Optimal Approach

### Key Insight

Use the recursive property:
$H_i = (H_{i-1} \times B + s[i]) \pmod M$
This is the definition of a **Rolling Hash**. We can compute the current hash using only the previous hash and the current character.

### Algorithm

1. Initialize `current_hash = 0`.
2. Create a result list.
3. Iterate through each character `c` in `s`:
   - `current_hash = (current_hash * B + ASCII(c)) % M`
   - Append `current_hash` to result.
4. Return result.

### Time Complexity

- **O(N)**: One pass through the string.

### Space Complexity

- **O(N)**: To store the output array.

![Algorithm Visualization](../images/HSH-001/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public long[] computePrefixHashes(String s, long B, long M) {
        int n = s.length();
        long[] hashes = new long[n];
        long currentHash = 0;
        
        for (int i = 0; i < n; i++) {
            // Use long to prevent overflow before modulo
            // s.charAt(i) returns char, which promotes to int/long automatically
            currentHash = (currentHash * B + s.charAt(i)) % M;
            hashes[i] = currentHash;
        }
        
        return hashes;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine();
            if (sc.hasNextLong()) {
                long B = sc.nextLong();
                long M = sc.nextLong();
                
                Solution solution = new Solution();
                long[] result = solution.computePrefixHashes(s, B, M);
                
                for (int i = 0; i < result.length; i++) {
                    System.out.print(result[i]);
                    if (i < result.length - 1) System.out.print(" ");
                }
                System.out.println();
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth just in case, though not needed for iterative
sys.setrecursionlimit(2000)

def compute_prefix_hashes(s: str, B: int, M: int) -> list:
    hashes = []
    current_hash = 0
    
    for char in s:
        # ord(char) gets the ASCII value
        current_hash = (current_hash * B + ord(char)) % M
        hashes.append(current_hash)
        
    return hashes

def main():
    # Read all input from stdin
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # First token is string s
    # Note: If string is empty or contains spaces, split() might behave differently
    # But problem constraints say lowercase English letters, so no spaces.
    
    # However, if the input format is strictly line-based:
    # Line 1: s
    # Line 2: B M
    # We should parse carefully.
    
    # Re-reading using standard input lines for safety with potential empty strings
    # or strict formatting
    import sys
    lines = sys.stdin.readlines()
    if not lines:
        return
        
    s = lines[0].strip()
    if len(lines) > 1:
        B, M = map(int, lines[1].split())
    else:
        # Fallback if B M are on same line or something (unlikely based on format)
        return

    result = compute_prefix_hashes(s, B, M)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<long long> computePrefixHashes(string s, long long B, long long M) {
        vector<long long> hashes;
        hashes.reserve(s.length());
        
        long long currentHash = 0;
        
        for (char c : s) {
            // (currentHash * B) can exceed 2^63-1 if M is large (~10^18)
            // But constraints say M <= 10^9 + 7, so long long is safe.
            currentHash = (currentHash * B + c) % M;
            hashes.push_back(currentHash);
        }
        
        return hashes;
    }
};

int main() {
    // Fast I/O
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string s;
    long long B, M;
    
    if (getline(cin, s)) {
        if (cin >> B >> M) {
            Solution solution;
            vector<long long> result = solution.computePrefixHashes(s, B, M);
            
            for (int i = 0; i < result.size(); i++) {
                cout << result[i];
                if (i < result.size() - 1) cout << " ";
            }
            cout << "\n";
        }
    }
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  computePrefixHashes(s, B, M) {
    const hashes = [];
    // Use BigInt because intermediate values (hash * B) can exceed 2^53 - 1
    // M is up to 10^9, B up to 10^9. Product is 10^18.
    // JS Number is safe up to 9*10^15. 10^18 requires BigInt.
    let currentHash = 0n;
    const bigB = BigInt(B);
    const bigM = BigInt(M);
    
    for (let i = 0; i < s.length; i++) {
      const charCode = BigInt(s.charCodeAt(i));
      currentHash = (currentHash * bigB + charCode) % bigM;
      hashes.push(Number(currentHash)); // Convert back to Number for output
    }
    
    return hashes;
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
  
  let ptr = 0;
  const s = data[ptr++];
  const [B, M] = data[ptr++].split(" ").map(Number);
  
  const solution = new Solution();
  const result = solution.computePrefixHashes(s, B, M);
  console.log(result.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
abc
911382323 1000000007
```

**Variables:**
- `s` = "abc"
- `B` = 911382323
- `M` = 1000000007

**Iteration 1 (char 'a', code 97):**
- `currentHash` = $(0 \times B + 97) \pmod M = 97$
- Output: `[97]`

**Iteration 2 (char 'b', code 98):**
- `currentHash` = $(97 \times 911382323 + 98) \pmod M$
- $97 \times 911382323 = 88404085331$
- $88404085331 + 98 = 88404085429$
- $88404085429 \pmod{1000000007} = 374134515$
- Output: `[97, 374134515]`

**Iteration 3 (char 'c', code 99):**
- `currentHash` = $(374134515 \times 911382323 + 99) \pmod M$
- Product $\approx 3.4 \times 10^{17}$ (Fits in 64-bit integer, requires BigInt in JS)
- Result modulo $M = 549818522$
- Output: `[97, 374134515, 549818522]`

## ✅ Proof of Correctness

### Invariant
At the end of iteration $i$, `currentHash` holds the polynomial hash of the prefix $s[0 \dots i]$.
Base case ($i=0$): $H_0 = s[0] \pmod M$. Correct.
Inductive step: Assume $H_{i-1}$ is correct.
$H_i = (H_{i-1} \times B + s[i]) \pmod M$.
This matches the definition of the polynomial rolling hash.

## 💡 Interview Extensions

- **Extension 1:** How to calculate the hash of any substring $s[i \dots j]$ in $O(1)$?
  - *Answer:* $H(s[i \dots j]) = (H_j - H_{i-1} \times B^{j-i+1}) \pmod M$. You need to precompute powers of $B$.
- **Extension 2:** What if collisions occur?
  - *Answer:* Use double hashing (two different pairs of $B$ and $M$).

### Common Mistakes to Avoid

1. **Integer Overflow**
   - ❌ Wrong: Using 32-bit `int` for intermediate calculations ($H \times B$).
   - ✅ Correct: Use `long long` (C++), `long` (Java), or `BigInt` (JS).

2. **Negative Modulo**
   - ❌ Wrong: In subtraction (for substrings), result might be negative.
   - ✅ Correct: Add `M` before taking modulo: `(a - b + M) % M`. (Not needed for this specific prefix problem, but good to know).

## Related Concepts

- **Rabin-Karp Algorithm:** Uses this rolling hash for pattern matching.
- **Modular Arithmetic:** Essential for preventing overflow.
