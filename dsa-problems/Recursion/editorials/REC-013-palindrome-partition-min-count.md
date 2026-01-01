---
title: Palindrome Partition with Minimum Count
slug: palindrome-partition-min-count
difficulty: Medium
difficulty_score: 53
tags:
- Recursion
- Backtracking
- Strings
problem_id: REC_PALINDROME_PARTITION_MIN_COUNT__3491
display_id: REC-013
topics:
- Recursion
- Backtracking
- Strings
---
# Palindrome Partition with Minimum Count - Editorial

## Problem Summary

You need to partition a string `s` into substrings such that:
1.  Every substring is a **palindrome**.
2.  The length of every substring is at most `L`.
3.  The **number of substrings** in the partition is minimized.

Return the **lexicographically smallest** partition achieving this minimum. The lexicographical order is determined by exploring palindromes in order of increasing length at each step.


## Constraints

- `1 <= |s| <= 12`
- `1 <= L <= |s|`
- `s` contains lowercase English letters
## Real-World Scenario

Think of **Data Compression**. You want to split a long message into the fewest possible chunks, but each chunk must satisfy a specific property (like being a palindrome, which might represent a reversible signal) and fit within a buffer size `L`. Minimizing the number of chunks reduces header overhead.

## Problem Exploration

### 1. Palindrome Check
A substring `s[i...j]` is a palindrome if it reads the same forwards and backwards. We can precompute this for all pairs `(i, j)` in `O(N^2)` using Dynamic Programming.
`isPal[i][j] = (s[i] == s[j]) && (j - i < 2 || isPal[i+1][j-1])`.

### 2. Minimum Cuts (DP vs BFS)
To find the *minimum number* of partitions, we can use BFS or DP.
-   **BFS**: Treat indices `0` to `N` as nodes. Edge from `i` to `j` exists if `s[i...j-1]` is a valid palindrome of length `<= L`. Find shortest path from `0` to `N`.
-   **DP**: `dp[i]` = min partitions for suffix `s[i...]`.
    `dp[i] = 1 + min(dp[j+1])` for all valid `j` where `s[i...j]` is palindrome and length `<= L`.

### 3. All Solutions
Since we need *all* partitions achieving the minimum count, we can:
1.  Compute `min_cuts` using BFS/DP.
2.  Use Backtracking (DFS) to reconstruct paths that match this `min_cuts`.

Given `N <= 12`, we can just use pure backtracking with a global minimum tracker, or iterative deepening. But BFS is cleanest for "shortest path" structure.

## Approaches

### Approach 1: BFS for Min Count + DFS for Reconstruction
1.  **BFS**: Compute `dist[i]`: minimum number of palindromes needed to cover prefix `s[0...i-1]`. Or better, `dist[i]` = min partitions for suffix `s[i...]`. Let's do suffix.
    -   `dist[N] = 0`.
    -   Work backwards or use BFS from `N` to `0` in the reversed graph?
2.  **DFS**: Reconstruct paths.
    -   `dfs(index, current_path)`
    -   If `index == N`: Add to results if `current_path.size() == min_k`.
    -   Iterate `j` from `index` to `N-1`.
    -   If `s[index...j]` is valid (palindrome & length `<= L`) AND `dist[j+1] == dist[index] - 1` (optimal substructure):
        -   Add substring to path.
        -   Recurse.
        -   Backtrack.

Then in DFS from `0`: move to `j+1` only if `dist[j+1] == dist[index] + 1`.

### Approach 2: Pure Backtracking (Small N)
With `N=12`, pure recursion is fine.
`solve(index, current_path)`
-   Track `global_min`.
-   If `current_path.size() > global_min`, prune.
-   If `index == N`:
    -   If `size < global_min`: Clear results, update `global_min`, add path.
    -   If `size == global_min`: Add path.

This is simpler to implement and sufficient for `N=12`.

## Implementations

### Java
```java
import java.util.*;

class Solution {
    int N, L;
    String S;
    boolean[][] is_pal;
    List<String> best_partition;
    int current_min;

    public String minPalindromePartitions(String s, int l) {
        S = s;
        L = l;
        N = s.length();
        
        is_pal = new boolean[N][N];
        for (int len = 1; len <= N; len++) {
            for (int i = 0; i <= N - len; i++) {
                int j = i + len - 1;
                if (S.charAt(i) == S.charAt(j)) {
                    if (len <= 2 || is_pal[i + 1][j - 1]) {
                        is_pal[i][j] = true;
                    }
                }
            }
        }

        current_min = N + 1;
        best_partition = null;
        backtrack(0, new ArrayList<>());
        
        if (best_partition == null) {
            StringBuilder sb = new StringBuilder();
            for(int i=0; i<N; i++) {
                sb.append(S.charAt(i));
                if(i < N-1) sb.append(" ");
            }
            return sb.toString();
        }
        
        return String.join(" ", best_partition);
    }

    private void backtrack(int start, List<String> current) {
        if (start == N) {
            int count = current.size();
            if (count < current_min) {
                current_min = count;
                best_partition = new ArrayList<>(current);
            }
            return;
        }

        if (current.size() >= current_min) return;

        int max_end = Math.min(start + L, N);
        for (int end = start; end < max_end; end++) {
            if (is_pal[start][end]) {
                current.add(S.substring(start, end + 1));
                backtrack(end + 1, current);
                current.remove(current.size() - 1);
            }
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if(!sc.hasNext()) return;
        String s = sc.next();
        if(!sc.hasNextInt()) return;
        int L = sc.nextInt();
        
        Solution sol = new Solution();
        System.out.println(sol.minPalindromePartitions(s, L));
        sc.close();
    }
}
```

### Python
```python
def min_palindrome_partitions(s: str, L: int) -> list[str]:
    n = len(s)
    # Precompute palindromes
    is_pal = [[False] * n for _ in range(n)]
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length <= 2 or is_pal[i + 1][j - 1]:
                    is_pal[i][j] = True

    min_count = [float('inf')]
    all_partitions = []

    def backtrack(start, current_path):
        if start == n:
            count = len(current_path)
            if count < min_count[0]:
                min_count[0] = count
                all_partitions.clear()
                all_partitions.append(list(current_path))
            elif count == min_count[0]:
                all_partitions.append(list(current_path))
            return

        # Pruning: don't explore beyond min_count
        if len(current_path) >= min_count[0]:
            return

        # Try all possible next palindromes
        for end in range(start, min(start + L, n)):
            if is_pal[start][end]:
                current_path.append(s[start : end + 1])
                backtrack(end + 1, current_path)
                current_path.pop()

    backtrack(0, [])

    if all_partitions:
        # Among all minimum partitions, select the first one found
        # The backtracking explores shorter palindromes first at each step
        best = all_partitions[0]
        return ' '.join(best)
    else:
        # Fallback: split into individual characters
        return ' '.join(list(s))

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if len(lines) < 2:
        return
    s = lines[0].strip()
    L = int(lines[1].strip())
    result = min_palindrome_partitions(s, L)
    print(result)

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
    int N;
    int L;
    string S;
    vector<vector<bool>> is_pal;
    vector<int> min_count;
    vector<string> best_partition;
    int current_min;

public:
    string minPalindromePartitions(string s, int l) {
        S = s;
        L = l;
        N = s.length();
        
        // Precompute Palindromes
        is_pal.assign(N, vector<bool>(N, false));
        for (int len = 1; len <= N; len++) {
            for (int i = 0; i <= N - len; i++) {
                int j = i + len - 1;
                if (S[i] == S[j]) {
                    if (len <= 2 || is_pal[i + 1][j - 1]) {
                        is_pal[i][j] = true;
                    }
                }
            }
        }

        current_min = N + 1;
        best_partition.clear();
        vector<string> current;
        backtrack(0, current);
        
        if(best_partition.empty()) {
            string res = "";
            for(int i=0; i<N; i++) {
                res += S[i];
                if(i < N-1) res += " ";
            }
            return res;
        }
        
        string res = "";
        for(size_t i=0; i<best_partition.size(); i++) {
            res += best_partition[i];
            if(i < best_partition.size()-1) res += " ";
        }
        return res;
    }

    void backtrack(int start, vector<string>& current) {
        if (start == N) {
            int count = current.size();
            if (count < current_min) {
                current_min = count;
                best_partition = current;
            }
            return;
        }

        // Pruning
        if (current.size() >= current_min) return;

        // Try palindromes length 1 to L
        // Python: range(start, min(start + L, n)) -> end from start to ...
        // Logic: start to end. Length = end - start + 1.
        // Python calls: start:end+1
        int max_end = min(start + L, N);
        for (int end = start; end < max_end; end++) {
            if (is_pal[start][end]) {
                current.push_back(S.substr(start, end - start + 1));
                backtrack(end + 1, current);
                if (current_min == (int)best_partition.size() && !best_partition.empty()) {
                     // Optimization: if we found best, do we stop? 
                     // Python loop continues but backtrack prunes.
                     // Python logic: if we found BETTER, Update.
                     // If we found SAME, Python keeps first found? 
                     // Python: if count < min: update. if count == min: append.
                     // Python returns all_partitions[0].
                     // To match Python traversal order, we just update if count < current_min.
                     // If count == current_min, we ignore (Keep first found).
                }
                current.pop_back();
            }
        }
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s;
    if (!(cin >> s)) return 0;
    int L; cin >> L;
    
    Solution sol;
    cout << sol.minPalindromePartitions(s, L) << endl;
    return 0;
}
```

### JavaScript
```javascript
const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const s = tokens[ptr++];
    const L = parseInt(tokens[ptr++]);
    
    const sol = new Solution();
    console.log(sol.minPalindromePartitions(s, L));
});

class Solution {
    minPalindromePartitions(s, L) {
        const n = s.length;
        const is_pal = Array.from({length: n}, () => Array(n).fill(false));
        
        for (let len = 1; len <= n; len++) {
            for (let i = 0; i <= n - len; i++) {
                let j = i + len - 1;
                if (s[i] === s[j]) {
                    if (len <= 2 || is_pal[i + 1][j - 1]) {
                        is_pal[i][j] = true;
                    }
                }
            }
        }
        
        this.current_min = n + 1;
        this.best_partition = null;
        
        const backtrack = (start, current) => {
            if (start === n) {
                const count = current.length;
                if (count < this.current_min) {
                    this.current_min = count;
                    this.best_partition = [...current];
                }
                return;
            }
            
            if (current.length >= this.current_min) return;
            
            const max_end = Math.min(start + L, n);
            for (let end = start; end < max_end; end++) {
                if (is_pal[start][end]) {
                    current.push(s.substring(start, end + 1));
                    backtrack(end + 1, current);
                    current.pop();
                }
            }
        };
        
        backtrack(0, []);
        
        if (!this.best_partition) {
            return s.split('').join(' ');
        }
        
        return this.best_partition.join(' ');
    }
}
```

## 🧪 Test Case Walkthrough (Dry Run)
**Input:** `aab`, `L=2`

1.  **Precompute Palindromes**:
    -   `a` (0,0), `a` (1,1), `b` (2,2) -> True.
    -   `aa` (0,1) -> True.
    -   `ab` (1,2) -> False.
    -   `aab` (0,2) -> False.
2.  `backtrack(0)`:
    -   Try `a` (0,0): Path `["a"]`.
        -   `backtrack(1)`:
            -   Try `a` (1,1): Path `["a", "a"]`.
                -   `backtrack(2)`:
                    -   Try `b` (2,2): Path `["a", "a", "b"]`.
                        -   Found len 3. `minCount = 3`. Results `[["a", "a", "b"]]`.
            -   Try `ab` (1,2): Invalid.
    -   Try `aa` (0,1): Path `["aa"]`.
        -   `backtrack(2)`:
            -   Try `b` (2,2): Path `["aa", "b"]`.
                -   Found len 2. `2 < 3`. `minCount = 2`. Results `[["aa", "b"]]`.
    -   Try `aab` (0,2): Length 3 > L=2. Break.

**Result:** `aa b`.

## Proof of Correctness

-   **Validity**: We only pick substrings that are palindromes and satisfy length constraint `L`.
-   **Optimality**: We track `minCount` and only keep solutions that match this minimum.
-   **Completeness**: Backtracking explores all valid partitions.

## Interview Extensions

1.  **Just the count?**
    -   Use DP: `dp[i] = 1 + min(dp[j+1])`. `O(N^2)`.
2.  **Large N?**
    -   Manacher's Algorithm for palindrome finding (`O(N)`), then DP.

### Common Mistakes

-   **Length Constraint**: Forgetting to check `end - start + 1 <= L`.
-   **Pruning**: Not pruning when `current.size() >= minCount` can lead to TLE on slightly larger inputs (though `N=12` is very forgiving).
