---
problem_id: HSH_TWO_STRING_CONCAT_EQUAL__4156
display_id: HSH-010
slug: two-string-concat-equal
title: "Two-String Concatenation Equal Check"
difficulty: Medium
difficulty_score: 45
topics:
  - Hashing
  - String Algorithms
tags:
  - hashing
  - concatenation
  - medium
premium: true
subscription_tier: basic
---

# HSH-010: Two-String Concatenation Equal Check

## 📋 Problem Summary

You are given four strings: `a`, `b`, `c`, and `d`. Determine if the concatenation `a + b` is equal to `c + d`.
The catch is to do this efficiently without explicitly creating the large concatenated strings (though for `N=10^5`, explicit creation is feasible, the goal is to learn the hashing technique).

## 🌍 Real-World Scenario

**Scenario Title:** Database Sharding Verification

Imagine you have a distributed database where data is split (sharded) across different servers.
- Server 1 has part `a` and part `b`.
- Server 2 has part `c` and part `d`.
- You want to verify if the combined data on Server 1 (`a+b`) is identical to the combined data on Server 2 (`c+d`) without transferring the full strings over the network.
- You can compute the hash of `a` and `b` locally, combine them mathematically, and send only the small hash value to compare with Server 2's combined hash.

![Real-World Application](../images/HSH-010/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concatenation Hash

String A: "ab" (Hash `H_A`, Len 2)
String B: "cd" (Hash `H_B`, Len 2)

Combined "abcd":
`H_AB = H_A x B^Len_B + H_B`

```text
Hash("ab") = 'a'*B + 'b'
Hash("cd") = 'c'*B + 'd'

Hash("abcd") = 'a'*B^3 + 'b'*B^2 + 'c'*B^1 + 'd'*B^0
             = ('a'*B + 'b') * B^2 + ('c'*B + 'd')
             = H_A * B^2 + H_B
```

### Key Concept: Mathematical Concatenation

We don't need to physically join strings to know their combined hash.
If we know `Hash(S_1)` and `Hash(S_2)`, then:

`Hash(S_1 + S_2) = (Hash(S_1) x Base^|S_2| + Hash(S_2)) +/-od M`


This allows `O(1)` combination if we have precomputed powers.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** Four strings `a`, `b`, `c`, `d`.
- **Output:** Boolean `true` or `false`.
- **Constraints:** Lengths up to `10^5`.
- **Note:** Standard string concatenation in Java/Python/C++ takes linear time `O(|a|+|b|)`. This is acceptable here, but the hashing approach is `O(|a|+|b|)` to compute hashes initially and then `O(1)` to check any combination.

## Naive Approach

### Intuition

Create `s1 = a + b`, `s2 = c + d`. Compare `s1.equals(s2)`.

### Time Complexity

- **O(N)**: String creation and comparison.
- **Space:** `O(N)` to store new strings.

## Optimal Approach (Hashing)

### Key Insight

Compute hashes of `a`, `b`, `c`, `d` individually.
Combine them using the formula:
`H_AB = (H_A x B^|b| + H_B) +/-od M`
`H_CD = (H_C x B^|d| + H_D) +/-od M`
Compare `H_AB` and `H_CD`.
Also check if total lengths match: `|a|+|b| == |c|+|d|`.

### Algorithm

1. Compute `H_A, H_B, H_C, H_D`.
2. Compute `P_|b| = B^|b| +/-od M`.
3. Compute `P_|d| = B^|d| +/-od M`.
4. Calculate combined hashes.
5. Compare.

### Time Complexity

- **O(N)**: To compute initial hashes.
- **Space:** `O(1)`.

![Algorithm Visualization](../images/HSH-010/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private static final long MOD = 1_000_000_007L;
    private static final long BASE = 313L;
    
    public boolean checkConcatenationEqual(String a, String b, String c, String d) {
        if (a.length() + b.length() != c.length() + d.length()) {
            return false;
        }
        
        long hA = computeHash(a);
        long hB = computeHash(b);
        long hC = computeHash(c);
        long hD = computeHash(d);
        
        long combinedAB = combine(hA, hB, b.length());
        long combinedCD = combine(hC, hD, d.length());
        
        return combinedAB == combinedCD;
    }
    
    private long computeHash(String s) {
        long h = 0;
        for (char ch : s.toCharArray()) {
            h = (h * BASE + ch) % MOD;
        }
        return h;
    }
    
    private long combine(long h1, long h2, int len2) {
        long p = 1;
        long b = BASE;
        // Modular exponentiation for B^len2
        int exp = len2;
        while (exp > 0) {
            if ((exp & 1) == 1) p = (p * b) % MOD;
            b = (b * b) % MOD;
            exp >>= 1;
        }
        
        return (h1 * p + h2) % MOD;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String a = sc.nextLine();
            String b = sc.nextLine();
            String c = sc.nextLine();
            String d = sc.nextLine();
            
            Solution solution = new Solution();
            System.out.println(solution.checkConcatenationEqual(a, b, c, d));
        }
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def check_concatenation_equal(self, a: str, b: str, c: str, d: str) -> bool:
        if len(a) + len(b) != len(c) + len(d):
            return False
            
        MOD = 10**9 + 7
        BASE = 313
        
        def compute_hash(s):
            h = 0
            for char in s:
                h = (h * BASE + ord(char)) % MOD
            return h
            
        hA = compute_hash(a)
        hB = compute_hash(b)
        hC = compute_hash(c)
        hD = compute_hash(d)
        
        # Combine: h1 * BASE^len2 + h2
        combinedAB = (hA * pow(BASE, len(b), MOD) + hB) % MOD
        combinedCD = (hC * pow(BASE, len(d), MOD) + hD) % MOD
        
        return combinedAB == combinedCD

def check_concatenation_equal(a: str, b: str, c: str, d: str) -> bool:
    solver = Solution()
    return solver.check_concatenation_equal(a, b, c, d)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    if len(input_data) >= 4:
        a = input_data[0]
        b = input_data[1]
        c = input_data[2]
        d = input_data[3]
        result = check_concatenation_equal(a, b, c, d)
        print("true" if result else "false")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <string>

using namespace std;

class Solution {
    const long long MOD = 1e9 + 7;
    const long long BASE = 313;

public:
    bool checkConcatenationEqual(string a, string b, string c, string d) {
        if (a.length() + b.length() != c.length() + d.length()) {
            return false;
        }
        
        long long hA = computeHash(a);
        long long hB = computeHash(b);
        long long hC = computeHash(c);
        long long hD = computeHash(d);
        
        long long combinedAB = combine(hA, hB, b.length());
        long long combinedCD = combine(hC, hD, d.length());
        
        return combinedAB == combinedCD;
    }
    
    long long computeHash(const string& s) {
        long long h = 0;
        for (char ch : s) {
            h = (h * BASE + ch) % MOD;
        }
        return h;
    }
    
    long long combine(long long h1, long long h2, int len2) {
        long long p = 1;
        long long b = BASE;
        int exp = len2;
        while (exp > 0) {
            if (exp & 1) p = (p * b) % MOD;
            b = (b * b) % MOD;
            exp >>= 1;
        }
        return (h1 * p + h2) % MOD;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string a, b, c, d;
    if (getline(cin, a) && getline(cin, b) && getline(cin, c) && getline(cin, d)) {
        Solution solution;
        cout << (solution.checkConcatenationEqual(a, b, c, d) ? "true" : "false") << "\n";
    }
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  checkConcatenationEqual(a, b, c, d) {
    if (a.length + b.length !== c.length + d.length) {
      return false;
    }
    
    const MOD = 1000000007n;
    const BASE = 313n;
    
    const computeHash = (s) => {
      let h = 0n;
      for (let i = 0; i < s.length; i++) {
        const code = BigInt(s.charCodeAt(i));
        h = (h * BASE + code) % MOD;
      }
      return h;
    };
    
    const power = (base, exp) => {
      let res = 1n;
      let b = base;
      let e = BigInt(exp);
      while (e > 0n) {
        if (e % 2n === 1n) res = (res * b) % MOD;
        b = (b * b) % MOD;
        e /= 2n;
      }
      return res;
    };
    
    const hA = computeHash(a);
    const hB = computeHash(b);
    const hC = computeHash(c);
    const hD = computeHash(d);
    
    const combinedAB = (hA * power(BASE, b.length) + hB) % MOD;
    const combinedCD = (hC * power(BASE, d.length) + hD) % MOD;
    
    return combinedAB === combinedCD;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length < 4) return;
  const [a, b, c, d] = data;

  const solution = new Solution();
  console.log(solution.checkConcatenationEqual(a, b, c, d) ? "true" : "false");
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
ab
cd
a
bcd
```

**Hashes:**
- `H("ab")`. `H("cd")`.
- `H("a")`. `H("bcd")`.

**Combine:**
- `H_AB = H("ab") x B^2 + H("cd")`.
- `H_CD = H("a") x B^3 + H("bcd")`.

**Result:**
- Both represent "abcd".
- Hashes match. Return `true`.

## ✅ Proof of Correctness

### Invariant
`Hash(S_1 + S_2) = Hash(S_1) x B^|S_2| + Hash(S_2)`.
This is derived directly from the polynomial definition of rolling hash.
If `H_AB == H_CD` and lengths match, strings are equal (with high probability).

## 💡 Interview Extensions

- **Extension 1:** Check if `A+B+C == D+E`.
  - *Answer:* Generalize the formula. `((H_A B^|B| + H_B) B^|C| + H_C)`.
- **Extension 2:** Given a list of strings, find two that concatenate to form a palindrome.
  - *Answer:* Use hashing to check palindrome property efficiently.

### Common Mistakes to Avoid

1. **Length Mismatch**
   - ❌ Wrong: Ignoring length check. Hash collision possible if lengths differ (though rare with polynomial hash if implemented correctly, but good practice).
   - ✅ Correct: Check `len(a)+len(b) == len(c)+len(d)` first.
2. **Power Calculation**
   - ❌ Wrong: Linear loop for power.
   - ✅ Correct: Modular exponentiation (`O(log N)`) or precomputed array.

## Related Concepts

- **Rabin-Karp:** Uses this rolling property.
- **Merkle Trees:** Combine hashes of blocks to verify data integrity.
