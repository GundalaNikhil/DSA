---
problem_id: HSH_ROLLING_HASH_COLLISION__8932
display_id: HSH-011
slug: rolling-hash-collision
title: "Rolling Hash Collision Finder"
difficulty: Medium
difficulty_score: 60
topics:
  - Hashing
  - Collision
  - Brute Force
tags:
  - hashing
  - collision
  - cryptography
  - medium
premium: true
subscription_tier: basic
---

# HSH-011: Rolling Hash Collision Finder

## 📋 Problem Summary

You are given hash parameters: Base `B`, Modulus `M`, and a target length `L`.
Your task is to find **two distinct strings** of length `L` that have the same polynomial hash value.
A collision occurs when `Hash(S_1) equiv Hash(S_2) +/-od M` but `S_1 !=q S_2`.

## 🌍 Real-World Scenario

**Scenario Title:** Security Vulnerability Testing

In cybersecurity, hash collisions are dangerous. If an attacker can find two different files with the same hash, they might be able to replace a legitimate file (like a software update) with a malicious one without the system noticing.
- This problem simulates a "collision attack" on a simplified hashing algorithm.
- By finding a collision, you demonstrate the weakness of using small moduli or predictable bases.

![Real-World Application](../images/HSH-011/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: The Pigeonhole Principle

Modulus M = 5.
Possible Hash Values: {0, 1, 2, 3, 4}

Strings generated:
1. "a" -> Hash 2
2. "b" -> Hash 4
3. "c" -> Hash 0
4. "d" -> Hash 2  <-- COLLISION! ("a" and "d")

Even though there are infinitely many strings, there are only `M` possible hash values.
If we generate `M+1` strings, we are guaranteed a collision (Pigeonhole Principle).
In practice, due to the **Birthday Paradox**, we likely find a collision after generating only `~= sqrtM` strings.

### Key Concept: Birthday Attack

If we generate random strings and store their hashes, the probability of a collision increases rapidly.
For `M = 10^9`, `sqrtM ~= 31,622`.
Generating ~32,000 strings is very fast.
Since `L <= 8`, the total number of possible strings is `26^8 ~= 2 x 10^11`, which is much larger than `M`. A collision is guaranteed to exist.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** `B, M, L`.
- **Output:** Two distinct strings `S_1, S_2`.
- **Constraints:** `L <= 8`. `M <= 10^9`.
- **Strategy:** Since `L` is small, we can iterate or randomize. Given `M` can be up to `10^9`, storing `10^9` integers is impossible (4GB RAM). But we only need `sqrtM` entries. A HashMap is perfect.

## Naive Approach

### Intuition

Iterate through all strings "aaaa...", "aaab...", etc. Store hash in a map. If seen, return pair.

### Algorithm

1. Map `seen: Hash -> String`.
2. Generate strings lexicographically.
3. Compute hash.
4. If hash in `seen`, return `(seen[hash], current)`.
5. Else `seen[hash] = current`.

### Time Complexity

- **O(\sqrt{M})**: Expected iterations until collision.
- **Space:** `O(sqrtM)`.

## Optimal Approach

### Key Insight

Since `L` is very small (up to 8), we can just use **Depth First Search (DFS)** to generate strings.
We stop as soon as we find a collision.
The constraints allow `26^L` which is huge, but we will statistically hit a collision much earlier.

### Algorithm

1. `Map<Long, String> map`.
2. `dfs(current_string)`:
   - If `len == L`:
     - `h = computeHash(current_string)`
     - If `map` has `h`: return `(map[h], current_string)`
     - `map[h] = current_string`
     - Return null
   - For `c` in 'a'...'z':
     - `res = dfs(current_string + c)`
     - If `res` found, return it.

### Time Complexity

- **O(\sqrt{M})**: On average. Worst case is bounded by `26^L` or `M`, whichever is smaller.

### Space Complexity

- **O(\sqrt{M})**: To store hashes.

![Algorithm Visualization](../images/HSH-011/algorithm-visualization.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    private long B, M;
    private int L;
    private Map<Long, String> seen;
    
    public String[] findCollision(long B, long M, int L) {
        this.B = B;
        this.M = M;
        this.L = L;
        this.seen = new HashMap<>();
        
        return dfs(new StringBuilder());
    }
    
    private String[] dfs(StringBuilder sb) {
        if (sb.length() == L) {
            String s = sb.toString();
            long h = computeHash(s);
            if (seen.containsKey(h)) {
                return new String[]{seen.get(h), s};
            }
            seen.put(h, s);
            return null;
        }
        
        for (char c = 'a'; c <= 'z'; c++) {
            sb.append(c);
            String[] res = dfs(sb);
            if (res != null) return res;
            sb.setLength(sb.length() - 1);
            
            // For M=10^9, expected map size is approximately sqrt(M) ≈ 32k.
            // With L≤8, we have 26^8 possible strings, far exceeding M.
            // By the pigeonhole principle, collisions must exist for these inputs.
        }
        return null;
    }
    
    private long computeHash(String s) {
        long h = 0;
        for (char c : s.toCharArray()) {
            h = (h * B + c) % M;
        }
        return h;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long B = sc.nextLong();
            long M = sc.nextLong();
            int L = sc.nextInt();
            
            Solution solution = new Solution();
            String[] result = solution.findCollision(B, M, L);
            
            if (result != null) {
                System.out.println(result[0]);
                System.out.println(result[1]);
            }
        }
        sc.close();
    }
}
```

### Python
```python
import sys

# Increase recursion depth
sys.setrecursionlimit(20000)

class Solution:
    def find_collision(self, B: int, M: int, L: int) -> tuple:
        seen = {}
        
        def compute_hash(s):
            h = 0
            for char in s:
                h = (h * B + ord(char)) % M
            return h
            
        def dfs(current_s):
            if len(current_s) == L:
                h = compute_hash(current_s)
                if h in seen:
                    return (seen[h], current_s)
                seen[h] = current_s
                return None
            
            for char_code in range(ord('a'), ord('z') + 1):
                res = dfs(current_s + chr(char_code))
                if res:
                    return res
            return None

        # Optimization: Iterative approach might be safer for stack depth
        # Or just use random generation if L is large.
        # Given L <= 8, DFS is fine.
        return dfs("")

def find_collision(B: int, M: int, L: int) -> tuple:
    solver = Solution()
    return solver.find_collision(B, M, L)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    B = int(input_data[0])
    M = int(input_data[1])
    L = int(input_data[2])
    
    s1, s2 = find_collision(B, M, L)
    print(s1)
    print(s2)

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
    long long B, M;
    int L;
    unordered_map<long long, string> seen;

public:
    pair<string, string> findCollision(long long B, long long M, int L) {
        this->B = B;
        this->M = M;
        this->L = L;
        seen.clear();
        
        string current = "";
        return dfs(current);
    }
    
    pair<string, string> dfs(string& current) {
        if (current.length() == L) {
            long long h = computeHash(current);
            if (seen.count(h)) {
                return {seen[h], current};
            }
            seen[h] = current;
            return {"", ""};
        }
        
        for (char c = 'a'; c <= 'z'; c++) {
            current.push_back(c);
            pair<string, string> res = dfs(current);
            if (res.first != "") return res;
            current.pop_back();
        }
        return {"", ""};
    }
    
    long long computeHash(const string& s) {
        long long h = 0;
        for (char c : s) {
            h = (h * B + c) % M;
        }
        return h;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    long long B, M;
    int L;
    if (cin >> B >> M >> L) {
        Solution solution;
        auto result = solution.findCollision(B, M, L);
        cout << result.first << "\n" << result.second << "\n";
    }
    
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class Solution {
  findCollision(B, M, L) {
    const seen = new Map();
    const MOD = BigInt(M);
    const BASE = BigInt(B);
    
    const computeHash = (s) => {
      let h = 0n;
      for (let i = 0; i < s.length; i++) {
        const code = BigInt(s.charCodeAt(i));
        h = (h * BASE + code) % MOD;
      }
      return h;
    };
    
    // Using iterative DFS (stack) to avoid recursion limits if needed
    // But L <= 8 is small enough for recursion.
    
    const dfs = (current) => {
      if (current.length === L) {
        const h = computeHash(current);
        if (seen.has(h)) {
          return [seen.get(h), current];
        }
        seen.set(h, current);
        return null;
      }
      
      for (let i = 97; i <= 122; i++) {
        const char = String.fromCharCode(i);
        const res = dfs(current + char);
        if (res) return res;
      }
      return null;
    };
    
    return dfs("") || ["", ""];
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
  const [B, M, L] = data[0].split(" ").map(Number);

  const solution = new Solution();
  const [s1, s2] = solution.findCollision(B, M, L);

  console.log(s1);
  console.log(s2);
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:** `3 7 3` (B=3, M=7, L=3)

**DFS:**
1. "aaa": Hash `0`. Store `{0: "aaa"}`.
2. "aab": Hash `1`. Store `{1: "aab"}`.
3. ...
4. "dac": Hash `1`.
   - Collision found with "aab"!
   - Return "aab", "dac".

## ✅ Proof of Correctness

### Invariant
The algorithm explores distinct strings.
Since `26^L > M` (for typical inputs), by Pigeonhole Principle, a collision must occur.
The map stores the first string found for each hash. The second time a hash is seen, we have a pair.

## 💡 Interview Extensions

- **Extension 1:** Find a collision for SHA-256?
  - *Answer:* Impossible computationally. That's why it's secure.
- **Extension 2:** What if we want strings with specific characters?
  - *Answer:* Modify the DFS generation loop.

### Common Mistakes to Avoid

1. **Memory Limit**
   - ❌ Wrong: Storing all strings if `L` is large.
   - ✅ Correct: We only need to store up to `M` (or `sqrtM`) strings.
2. **Infinite Loop**
   - ❌ Wrong: Not checking base case `L`.

## Related Concepts

- **Birthday Attack:** Probability of collision.
- **Floyd's Cycle Finding:** Can be used to find collision with `O(1)` space (Pollard's Rho), but requires a function `f(x)` mapping hash to next string.
