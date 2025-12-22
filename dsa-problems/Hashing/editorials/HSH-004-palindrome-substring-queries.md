---
problem_id: HSH_PALINDROME_SUBSTRING_QUERIES__2639
display_id: HSH-004
slug: palindrome-substring-queries
title: "Palindrome Substring Queries"
difficulty: Medium
difficulty_score: 50
topics:
  - Hashing
  - Palindrome
  - String Algorithms
tags:
  - hashing
  - palindrome
  - queries
  - medium
premium: true
subscription_tier: basic
---

# HSH-004: Palindrome Substring Queries

## 📋 Problem Summary

You are given a string `s` and multiple queries. Each query consists of a range `[l, r]`. You need to determine if the substring `s[l..r]` is a palindrome (reads the same forwards and backwards).

## 🌍 Real-World Scenario

**Scenario Title:** DNA Palindrome Detection

In genetics, palindromic sequences in DNA (like `GAATTC` which pairs with `CTTAAG` on the opposite strand, reading the same 5' to 3') are crucial. They often serve as binding sites for restriction enzymes.
- A researcher might want to scan millions of specific regions to check if they are palindromic.
- Doing this naively for every region is slow.
- Hashing allows us to check any region in constant time.

![Real-World Application](../images/HSH-004/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Forward vs Reverse Hash

String: "banana"
Reverse: "ananab"

Query: `s[1..3]` ("ana")

```text
Original (s):
Index: 0 1 2 3 4 5
Char:  b a n a n a

Reverse (rev_s):
Index: 0 1 2 3 4 5
Char:  a n a n a b
(Note: rev_s[0] corresponds to s[5])

To check if s[l..r] is a palindrome:
1. Compute Hash(s[l..r]) using prefix hashes of s.
2. Compute Hash(Reverse of s[l..r]).
   - The reverse of s[l..r] corresponds to a substring in rev_s.
   - Specifically, index i in s maps to index (N-1-i) in rev_s.
   - So s[l..r] reversed is rev_s[N-1-r ... N-1-l].
3. If Hash(Forward) == Hash(Backward), it's a palindrome.
```

### Key Concept: Reverse String Hashing

A string is a palindrome if it equals its reverse.
Instead of reversing the substring explicitly (which takes $O(Len)$), we can precompute hashes for the **entire reversed string**.
Then, the hash of the "reversed substring" can be retrieved in $O(1)$ from the reversed string's hash array.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** String `s`, queries `(l, r)`.
- **Output:** Boolean for each query.
- **Constraints:** $N, Q \le 2 \cdot 10^5$. $O(1)$ per query is required.
- **Double Hashing:** Highly recommended to avoid collisions.

## Naive Approach

### Intuition

For each query `(l, r)`, extract the substring, reverse it, and compare.

### Algorithm

1. For each query:
   - Extract `sub = s.substring(l, r+1)`.
   - Check if `sub == reverse(sub)`.

### Time Complexity

- **O(Q * N)**: Extracting and reversing takes linear time relative to substring length. Too slow.

## Optimal Approach

### Key Insight

Use **Rolling Hash** on both `s` and `reverse(s)`.
- Let `h1` be the prefix hash array for `s`.
- Let `h2` be the prefix hash array for `reverse(s)`.
- For query `(l, r)`:
  - Forward Hash = Hash of `s[l..r]` using `h1`.
  - Backward Hash = Hash of `reverse(s)[(n-1-r)..(n-1-l)]` using `h2`.
  - If they match, it's a palindrome.

### Algorithm

1. Construct `rev_s` by reversing `s`.
2. Compute prefix hashes and powers for `s` (Forward Hash).
3. Compute prefix hashes for `rev_s` (Reverse Hash).
4. For each query `(l, r)`:
   - Get forward hash of `s[l..r]`.
   - Get reverse hash of `rev_s` corresponding to range `[n-1-r, n-1-l]`.
   - Compare.

### Time Complexity

- **O(N + Q)**: Preprocessing takes $O(N)$, queries take $O(1)$.

### Space Complexity

- **O(N)**: Storing hash arrays.

![Algorithm Visualization](../images/HSH-004/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private static final long MOD = 1_000_000_007L;
    private static final long BASE = 313L;
    
    // Using single hash for simplicity in template, but double hash is safer
    // Ideally, implement double hashing as in HSH-002
    
    public boolean[] checkPalindromes(String s, int[][] queries) {
        int n = s.length();
        long[] hForward = new long[n + 1];
        long[] hReverse = new long[n + 1];
        long[] power = new long[n + 1];
        
        power[0] = 1;
        String revS = new StringBuilder(s).reverse().toString();
        
        for (int i = 0; i < n; i++) {
            hForward[i + 1] = (hForward[i] * BASE + s.charAt(i)) % MOD;
            hReverse[i + 1] = (hReverse[i] * BASE + revS.charAt(i)) % MOD;
            power[i + 1] = (power[i] * BASE) % MOD;
        }
        
        boolean[] results = new boolean[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int l = queries[i][0];
            int r = queries[i][1];
            
            long fwdHash = getHash(hForward, power, l, r);
            
            // Map indices to reversed string
            // s[l...r] corresponds to revS[n-1-r ... n-1-l]
            int revL = n - 1 - r;
            int revR = n - 1 - l;
            long revHash = getHash(hReverse, power, revL, revR);
            
            results[i] = (fwdHash == revHash);
        }
        return results;
    }
    
    private long getHash(long[] h, long[] p, int l, int r) {
        int len = r - l + 1;
        long val = (h[r + 1] - (h[l] * p[len]) % MOD + MOD) % MOD;
        return val;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine();
            if (sc.hasNextInt()) {
                int q = sc.nextInt();
                int[][] queries = new int[q][2];
                for (int i = 0; i < q; i++) {
                    queries[i][0] = sc.nextInt();
                    queries[i][1] = sc.nextInt();
                }
                Solution solution = new Solution();
                boolean[] result = solution.checkPalindromes(s, queries);
                for (boolean ans : result) {
                    System.out.println(ans);
                }
            }
        }
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

class Solution:
    def check_palindromes(self, s: str, queries: list) -> list:
        n = len(s)
        MOD = 10**9 + 7
        BASE = 313
        
        h_fwd = [0] * (n + 1)
        h_rev = [0] * (n + 1)
        power = [1] * (n + 1)
        
        rev_s = s[::-1]
        
        for i in range(n):
            h_fwd[i+1] = (h_fwd[i] * BASE + ord(s[i])) % MOD
            h_rev[i+1] = (h_rev[i] * BASE + ord(rev_s[i])) % MOD
            power[i+1] = (power[i] * BASE) % MOD
            
        def get_hash(h, l, r):
            length = r - l + 1
            return (h[r+1] - h[l] * power[length]) % MOD
            
        results = []
        for l, r in queries:
            fwd_hash = get_hash(h_fwd, l, r)
            
            rev_l = n - 1 - r
            rev_r = n - 1 - l
            rev_hash = get_hash(h_rev, rev_l, rev_r)
            
            results.append(fwd_hash == rev_hash)
            
        return results

def check_palindromes(s: str, queries: list) -> list:
    solver = Solution()
    return solver.check_palindromes(s, queries)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        s = next(iterator)
        q = int(next(iterator))
        queries = []
        for _ in range(q):
            l = int(next(iterator))
            r = int(next(iterator))
            queries.append([l, r])
            
        result = check_palindromes(s, queries)
        for ans in result:
            print("true" if ans else "false")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
    const long long MOD = 1e9 + 7;
    const long long BASE = 313;

public:
    vector<bool> checkPalindromes(string s, vector<pair<int,int>>& queries) {
        int n = s.length();
        string revS = s;
        reverse(revS.begin(), revS.end());
        
        vector<long long> hFwd(n + 1, 0), hRev(n + 1, 0), power(n + 1, 1);
        
        for (int i = 0; i < n; i++) {
            hFwd[i + 1] = (hFwd[i] * BASE + s[i]) % MOD;
            hRev[i + 1] = (hRev[i] * BASE + revS[i]) % MOD;
            power[i + 1] = (power[i] * BASE) % MOD;
        }
        
        vector<bool> results;
        results.reserve(queries.size());
        
        for (const auto& q : queries) {
            int l = q.first;
            int r = q.second;
            
            long long fwdHash = getHash(hFwd, power, l, r);
            
            int revL = n - 1 - r;
            int revR = n - 1 - l;
            long long revHash = getHash(hRev, power, revL, revR);
            
            results.push_back(fwdHash == revHash);
        }
        
        return results;
    }
    
    long long getHash(const vector<long long>& h, const vector<long long>& p, int l, int r) {
        int len = r - l + 1;
        long long val = (h[r + 1] - (h[l] * p[len]) % MOD + MOD) % MOD;
        return val;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string s;
    if (!(cin >> s)) return 0;
    
    int q;
    if (!(cin >> q)) return 0;
    
    vector<pair<int,int>> queries(q);
    for (int i = 0; i < q; i++) {
        cin >> queries[i].first >> queries[i].second;
    }
    
    Solution solution;
    vector<bool> result = solution.checkPalindromes(s, queries);
    
    for (bool ans : result) {
        cout << (ans ? "true" : "false") << "\n";
    }
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  checkPalindromes(s, queries) {
    const n = s.length;
    const MOD = 1000000007n;
    const BASE = 313n;
    
    const hFwd = new BigInt64Array(n + 1);
    const hRev = new BigInt64Array(n + 1);
    const power = new BigInt64Array(n + 1);
    
    power[0] = 1n;
    const revS = s.split('').reverse().join('');
    
    for (let i = 0; i < n; i++) {
      const codeFwd = BigInt(s.charCodeAt(i));
      const codeRev = BigInt(revS.charCodeAt(i));
      
      hFwd[i + 1] = (hFwd[i] * BASE + codeFwd) % MOD;
      hRev[i + 1] = (hRev[i] * BASE + codeRev) % MOD;
      power[i + 1] = (power[i] * BASE) % MOD;
    }
    
    const getHash = (h, p, l, r) => {
      const len = r - l + 1;
      let val = (h[r + 1] - (h[l] * p[len]) % MOD) % MOD;
      if (val < 0n) val += MOD;
      return val;
    };
    
    const results = [];
    for (const [l, r] of queries) {
      const fwdHash = getHash(hFwd, power, l, r);
      
      const revL = n - 1 - r;
      const revR = n - 1 - l;
      const revHash = getHash(hRev, power, revL, revR);
      
      results.push(fwdHash === revHash);
    }
    
    return results;
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
  const q = parseInt(data[ptr++]);
  
  const queries = [];
  for (let i = 0; i < q; i++) {
    const [l, r] = data[ptr++].split(" ").map(Number);
    queries.push([l, r]);
  }
  
  const solution = new Solution();
  const result = solution.checkPalindromes(s, queries);
  
  result.forEach((ans) => console.log(ans ? "true" : "false"));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
abccba
1
1 4
```
Query: `s[1..4]` ("bccb").

**Preprocessing:**
- `s` = "abccba"
- `hFwd` and `hRev` will be identical arrays.

**Query Processing:**
- `l=1, r=4`. Substring "bccb".
- `fwdHash` = Hash of `s[1..4]` ("bccb").
- `revL` = $6 - 1 - 4 = 1$.
- `revR` = $6 - 1 - 1 = 4$.
- `revHash` = Hash of `rev_s[1..4]` ("bccb").
- `fwdHash == revHash`? Yes.
- Ah, `s[1..4]` is "bccb".
- Is "bccb" a palindrome? Yes.
- Let's check the example input carefully.
- Example Input: `abccba`.
- Query 2: `1 4`.
- `s[1]`='b', `s[2]`='c', `s[3]`='c', `s[4]`='b'.
- "bccb" IS a palindrome.
- Why does example output say `false`?
- Let's re-read the example explanation.
- "Query 2: s[1..4] = "bccb" -> not a palindrome -> false"
- Is there a mistake in my reading or the example?
- Maybe indices are different?
- "0-indexed".
- `s`: a(0) b(1) c(2) c(3) b(4) a(5).
- `s[1..4]` is `b c c b`.
- Reverse is `b c c b`.
- It IS a palindrome.
- **Correction:** The example explanation in the problem description might be wrong, OR I am misinterpreting "palindrome".
- Or maybe the input string in example is different?
- "abccba".
- Let's look at Query 3: `2 3`. `s[2..3]` = "cc". True.
- Query 1: `0 5`. "abccba". True.
- Why would `1 4` be false?
- Maybe the example output in the problem file is actually correct and I'm missing something?
- Or maybe the problem file has a typo.
- "Query 2: s[1..4] = "bccb" -> not a palindrome -> false".
- This statement "bccb -> not a palindrome" is factually incorrect.
- I will assume the code logic (checking if palindrome) is correct and the example description might have a typo, OR the string is different.
- Wait! Look at the example input again.
- `abccba`.
- Maybe the query is `1 3`? "bcc". Not palindrome.
- But input says `1 4`.
- I will implement the correct logic for "Is Palindrome". If "bccb" is passed, it should return true.



## ✅ Proof of Correctness

### Invariant
A string $S$ is a palindrome iff $S == \text{reverse}(S)$.
Hash($S$) == Hash($\text{reverse}(S)$) is a necessary condition. With double hashing, it is sufficient with high probability.
The mapping `s[l..r]` $\leftrightarrow$ `rev_s[n-1-r .. n-1-l]` correctly identifies the reversed substring.

## 💡 Interview Extensions

- **Extension 1:** Count all palindromic substrings.
  - *Answer:* Manacher's Algorithm ($O(N)$). Hashing is $O(N \log N)$ or $O(N^2)$.
- **Extension 2:** Longest Palindromic Substring.
  - *Answer:* Binary search on length + Hashing check ($O(N \log N)$). Or Manacher's ($O(N)$).

### Common Mistakes to Avoid

1. **Index Mapping**
   - ❌ Wrong: `rev_s[l..r]`.
   - ✅ Correct: `rev_s[n-1-r .. n-1-l]`. The indices flip.
2. **Off-by-one**
   - ❌ Wrong: `len = r - l`.
   - ✅ Correct: `len = r - l + 1`.

## Related Concepts

- **Manacher's Algorithm:** Specialized for palindromes.
- **Rolling Hash:** General purpose string tool.
