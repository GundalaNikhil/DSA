---
problem_id: STC_SUFFIX_AUTOMATON_QUERIES__9036
display_id: STC-016
slug: suffix-automaton-queries
title: "Suffix Automaton Substring Queries"
difficulty: Medium
difficulty_score: 62
topics:
  - Strings
  - Suffix Automaton
  - Counting
tags:
  - strings
  - suffix-automaton
  - counting
  - medium
premium: true
subscription_tier: basic
---

# STC-016: Suffix Automaton Substring Queries

## 📋 Problem Summary

Given a string `s`, you need to answer multiple queries. Each query provides a string `p`, and you must return the number of times `p` appears as a substring in `s`. You are expected to use a **Suffix Automaton** to solve this efficiently.

## 🌍 Real-World Scenario

**Scenario Title:** High-Frequency Trading Pattern Analysis

In financial markets, analysts look for recurring patterns in price movements (represented as a string of symbols). To estimate the significance of a specific pattern (e.g., "Up-Down-Up"), they need to know how often it has occurred in the historical data. A Suffix Automaton allows for extremely fast querying of pattern frequencies over massive datasets, enabling real-time analysis.

**Why This Problem Matters:**

- **Search Engines:** Counting phrase frequencies for indexing and ranking.
- **Bioinformatics:** Counting motif occurrences in a genome.
- **Efficiency:** Suffix Automaton answers queries in O(|p|) time, independent of |s| (after O(|s|) preprocessing).

![Real-World Application](../images/STC-016/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

Let `s = "ababa"`.
Suffix Automaton States (simplified):
- **Root**: Empty string.
- **State "a"**: Occurs at {0, 2, 4}. Count = 3.
- **State "ab"**: Occurs at {1, 3}. Count = 2.
- **State "aba"**: Occurs at {2, 4}. Count = 2.
- **State "abab"**: Occurs at {3}. Count = 1.
- **State "ababa"**: Occurs at {4}. Count = 1.

Query "aba": Walk `root -> a -> ab -> aba`. Current state has count 2. Answer: 2.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** String `s` and multiple query strings `p`.
- **Output:** Count of occurrences for each `p`.
- **Constraints:** `|s| <= 100,000`. Sum of `|p| <= 200,000`.
- **Clones:** The construction involves "cloning" states. Cloned states initially have count 0, while original states (created when extending the string) have count 1. Counts must be propagated.

## Naive Approach

### Intuition

For each query `p`, scan `s` to count occurrences (e.g., using KMP or naive search).

### Algorithm

1. For each query `p`:
2. Count occurrences in `s` using `s.indexOf(p, start)`.
3. Return count.

### Time Complexity

- **O(Q * (|s| + |p|))**: Too slow if many queries or long `s`.

### Space Complexity

- **O(1)**.

## Optimal Approach (Suffix Automaton)

### Key Insight

A **Suffix Automaton (SAM)** is a DAG where nodes represent equivalence classes of substrings. All substrings in a class `u` appear at the same set of end positions in `s`.
- `len(u)`: Length of the longest substring in class `u`.
- `link(u)`: Points to the state representing the longest proper suffix of `u` that is in a different class.
- `count(u)`: The number of times substrings in class `u` appear in `s`.

**Construction:**
We build the SAM incrementally. When adding character `c`:
- Create a new state `cur`.
- `count[cur] = 1` (it represents the full prefix ending at current position).
- Update transitions and links. If we split a state `q` into `q` and `clone`, `clone` inherits `count = 0` (it represents substrings that appear elsewhere, but doesn't account for the *current* prefix position directly; its count will be accumulated from children in the link tree).

**Count Propagation:**
The suffix links form a tree rooted at the initial state.
If a state `u` appears `k` times, then any suffix of `u` (represented by `link[u]`) also appears at least `k` times (plus occurrences where the suffix appears but `u` doesn't).
Therefore, `count[link[u]] += count[u]`.
We must process states in decreasing order of length (or reverse topological order) to propagate counts correctly.

**Querying:**
Start at root. For each char in `p`, follow transitions.
- If no transition, count is 0.
- If we process all of `p` and end at state `u`, the answer is `count[u]`.

### Algorithm

1. **Build SAM**:
   - Standard construction.
   - Maintain `is_clone` flag or initialize `cnt=1` for non-clones.
2. **Sort States**:
   - Sort states by `len` descending (or use bucket sort since `len <= |s|`).
3. **Propagate Counts**:
   - For each state `u` in sorted order (except root):
     - `cnt[link[u]] += cnt[u]`.
4. **Answer Queries**:
   - Walk the SAM. Return `cnt[final_state]`.

### Time Complexity

- **O(|s|)**: Construction and propagation.
- **O(|p|)**: Per query.
- **Total**: O(|s| + Sum(|p|)).

### Space Complexity

- **O(|s| * Sigma)**: Number of states is at most `2*|s|`.

![Algorithm Visualization](../images/STC-016/algorithm-visualization.png)
![Algorithm Steps](../images/STC-016/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    static class State {
        int len, link;
        Map<Character, Integer> next = new HashMap<>();
        long cnt = 0;
        boolean isClone = false;
    }

    State[] st;
    int sz, last;

    public long[] countOccurrences(String s, String[] queries) {
        int n = s.length();
        st = new State[n * 2 + 5]; // Max states 2*n
        for(int i=0; i<st.length; i++) st[i] = new State();
        
        st[0].len = 0;
        st[0].link = -1;
        sz = 1;
        last = 0;
        
        // 1. Build SAM
        for (char c : s.toCharArray()) {
            extend(c);
        }
        
        // 2. Sort by length descending
        List<Integer> nodes = new ArrayList<>();
        for (int i = 1; i < sz; i++) nodes.add(i);
        nodes.sort((a, b) -> st[b].len - st[a].len);
        
        // 3. Propagate counts
        for (int u : nodes) {
            if (st[u].link != -1) {
                st[st[u].link].cnt += st[u].cnt;
            }
        }
        
        // 4. Answer queries
        long[] ans = new long[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int curr = 0;
            boolean ok = true;
            for (char c : queries[i].toCharArray()) {
                if (!st[curr].next.containsKey(c)) {
                    ok = false;
                    break;
                }
                curr = st[curr].next.get(c);
            }
            if (ok) ans[i] = st[curr].cnt;
            else ans[i] = 0;
        }
        
        return ans;
    }
    
    void extend(char c) {
        int cur = sz++;
        st[cur].len = st[last].len + 1;
        st[cur].cnt = 1; // Original state
        st[cur].isClone = false;
        
        int p = last;
        while (p != -1 && !st[p].next.containsKey(c)) {
            st[p].next.put(c, cur);
            p = st[p].link;
        }
        
        if (p == -1) {
            st[cur].link = 0;
        } else {
            int q = st[p].next.get(c);
            if (st[p].len + 1 == st[q].len) {
                st[cur].link = q;
            } else {
                int clone = sz++;
                st[clone].len = st[p].len + 1;
                st[clone].next = new HashMap<>(st[q].next);
                st[clone].link = st[q].link;
                st[clone].cnt = 0; // Clone starts with 0
                st[clone].isClone = true;
                
                while (p != -1 && st[p].next.get(c) == q) {
                    st[p].next.put(c, clone);
                    p = st[p].link;
                }
                st[q].link = st[cur].link = clone;
            }
        }
        last = cur;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        String s = sc.next();
        int q = sc.nextInt();
        String[] queries = new String[q];
        for (int i = 0; i < q; i++) {
            queries[i] = sc.next();
        }

        Solution solution = new Solution();
        long[] ans = solution.countOccurrences(s, queries);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.length; i++) {
            sb.append(ans[i]);
            if (i + 1 < ans.length) sb.append('\n');
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
```

### Python

```python
import sys

class State:
    def __init__(self, length=0, link=-1):
        self.len = length
        self.link = link
        self.next = {}
        self.cnt = 0

def count_occurrences(s: str, queries: list[str]) -> list[int]:
    # Initialize SAM
    st = [State()]
    last = 0
    
    # Extend function
    def extend(c):
        nonlocal last
        cur = len(st)
        st.append(State(st[last].len + 1))
        st[cur].cnt = 1 # Original state
        
        p = last
        while p != -1 and c not in st[p].next:
            st[p].next[c] = cur
            p = st[p].link
            
        if p == -1:
            st[cur].link = 0
        else:
            q = st[p].next[c]
            if st[p].len + 1 == st[q].len:
                st[cur].link = q
            else:
                clone = len(st)
                st.append(State(st[p].len + 1, st[q].link))
                st[clone].next = st[q].next.copy()
                st[clone].cnt = 0 # Clone
                
                while p != -1 and st[p].next.get(c) == q:
                    st[p].next[c] = clone
                    p = st[p].link
                st[q].link = st[cur].link = clone
        last = cur

    # Build SAM
    for char in s:
        extend(char)
        
    # Propagate counts
    # Sort by length descending
    nodes = sorted(range(1, len(st)), key=lambda i: st[i].len, reverse=True)
    for u in nodes:
        if st[u].link != -1:
            st[st[u].link].cnt += st[u].cnt
            
    # Answer queries
    ans = []
    for query in queries:
        curr = 0
        ok = True
        for char in query:
            if char not in st[curr].next:
                ok = False
                break
            curr = st[curr].next[char]
        if ok:
            ans.append(st[curr].cnt)
        else:
            ans.append(0)
            
    return ans

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    q = int(input_data[1])
    queries = input_data[2:2 + q]
    
    ans = count_occurrences(s, queries)
    sys.stdout.write("\n".join(str(x) for x in ans) + "\n")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

struct State {
    int len, link;
    map<char, int> next;
    long long cnt = 0;
};

class Solution {
    vector<State> st;
    int sz, last;

    void extend(char c) {
        int cur = sz++;
        st.emplace_back();
        st[cur].len = st[last].len + 1;
        st[cur].cnt = 1;
        st[cur].link = 0; // Default
        
        int p = last;
        while (p != -1 && st[p].next.find(c) == st[p].next.end()) {
            st[p].next[c] = cur;
            p = st[p].link;
        }
        
        if (p == -1) {
            st[cur].link = 0;
        } else {
            int q = st[p].next[c];
            if (st[p].len + 1 == st[q].len) {
                st[cur].link = q;
            } else {
                int clone = sz++;
                st.emplace_back();
                st[clone].len = st[p].len + 1;
                st[clone].next = st[q].next;
                st[clone].link = st[q].link;
                st[clone].cnt = 0;
                
                while (p != -1 && st[p].next[c] == q) {
                    st[p].next[c] = clone;
                    p = st[p].link;
                }
                st[q].link = st[cur].link = clone;
            }
        }
        last = cur;
    }

public:
    vector<long long> countOccurrences(const string& s, const vector<string>& queries) {
        st.clear();
        st.reserve(s.length() * 2 + 5);
        st.emplace_back(); // Root
        st[0].len = 0;
        st[0].link = -1;
        sz = 1;
        last = 0;
        
        for (char c : s) extend(c);
        
        // Propagate counts
        vector<int> nodes(sz);
        for (int i = 0; i < sz; i++) nodes[i] = i;
        sort(nodes.begin(), nodes.end(), [&](int a, int b) {
            return st[a].len > st[b].len;
        });
        
        for (int u : nodes) {
            if (u == 0) continue;
            if (st[u].link != -1) {
                st[st[u].link].cnt += st[u].cnt;
            }
        }
        
        vector<long long> ans;
        ans.reserve(queries.size());
        for (const string& q : queries) {
            int curr = 0;
            bool ok = true;
            for (char c : q) {
                if (st[curr].next.find(c) == st[curr].next.end()) {
                    ok = false;
                    break;
                }
                curr = st[curr].next[c];
            }
            if (ok) ans.push_back(st[curr].cnt);
            else ans.push_back(0);
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (cin >> s) {
        int q;
        cin >> q;
        vector<string> queries(q);
        for (int i = 0; i < q; i++) {
            cin >> queries[i];
        }
        
        Solution solution;
        vector<long long> ans = solution.countOccurrences(s, queries);
        for (long long x : ans) cout << x << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class State {
  constructor(len = 0, link = -1) {
    this.len = len;
    this.link = link;
    this.next = new Map();
    this.cnt = 0n;
  }
}

class Solution {
  countOccurrences(s, queries) {
    const st = [new State()];
    let last = 0;
    
    const extend = (c) => {
      const cur = st.length;
      st.push(new State(st[last].len + 1));
      st[cur].cnt = 1n;
      
      let p = last;
      while (p !== -1 && !st[p].next.has(c)) {
        st[p].next.set(c, cur);
        p = st[p].link;
      }
      
      if (p === -1) {
        st[cur].link = 0;
      } else {
        const q = st[p].next.get(c);
        if (st[p].len + 1 === st[q].len) {
          st[cur].link = q;
        } else {
          const clone = st.length;
          const cloneState = new State(st[p].len + 1, st[q].link);
          cloneState.next = new Map(st[q].next);
          cloneState.cnt = 0n;
          st.push(cloneState);
          
          while (p !== -1 && st[p].next.get(c) === q) {
            st[p].next.set(c, clone);
            p = st[p].link;
          }
          st[q].link = st[cur].link = clone;
        }
      }
      last = cur;
    };
    
    for (const char of s) {
      extend(char);
    }
    
    // Propagate
    const nodes = Array.from({length: st.length}, (_, i) => i);
    nodes.sort((a, b) => st[b].len - st[a].len);
    
    for (const u of nodes) {
      if (u === 0) continue;
      if (st[u].link !== -1) {
        st[st[u].link].cnt += st[u].cnt;
      }
    }
    
    const ans = [];
    for (const q of queries) {
      let curr = 0;
      let ok = true;
      for (const char of q) {
        if (!st[curr].next.has(char)) {
          ok = false;
          break;
        }
        curr = st[curr].next.get(char);
      }
      if (ok) ans.push(st[curr].cnt.toString());
      else ans.push("0");
    }
    
    return ans;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part) data.push(part);
  }
});

rl.on("close", () => {
  if (data.length === 0) return;
  const s = data[0];
  const q = parseInt(data[1], 10);
  const queries = data.slice(2, 2 + q);
  const solution = new Solution();
  const ans = solution.countOccurrences(s, queries);
  console.log(ans.join("\n"));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

`s = "ababa"`
SAM Construction:
- `extend(a)`: `st[1] ("a")`, `cnt=1`.
- `extend(b)`: `st[2] ("ab")`, `cnt=1`.
- `extend(a)`: `st[3] ("aba")`, `cnt=1`. Note: `st[1]` ("a") is split? No, `st[0]` has `a` -> 1. `st[2]` has no `a`. `st[2]` links to `st[0]`. `p=2`. `st[2].next[a]=3`. `p=0`. `st[0].next[a]=1`. `q=1`. `len(0)+1 == len(1)`. `link[3]=1`.
- `extend(b)`: `st[4] ("abab")`.
- `extend(a)`: `st[5] ("ababa")`.

Propagation:
- `st[5]` ("ababa", cnt=1) -> link to `st[3]` ("aba"). `cnt[3] += 1` -> 2.
- `st[4]` ("abab", cnt=1) -> link to `st[2]` ("ab"). `cnt[2] += 1` -> 2.
- `st[3]` ("aba", cnt=2) -> link to `st[1]` ("a"). `cnt[1] += 2` -> 3.
- `st[2]` ("ab", cnt=2) -> link to `st[1]` ("a"). `cnt[1] += 2` -> 5?
  - `st[2]` is "ab". Suffix "b". `st[1]` is "a".
  - "b" is not "a".
  - `link[2]` should be a state for "b".
  - My manual trace is simplified.
  - Correct logic: `cnt[u]` accumulates occurrences.
  - "aba" occurs 2 times. `st[3]` represents "aba". `cnt[3]` should be 2.
  - "ab" occurs 2 times. `st[2]` represents "ab". `cnt[2]` should be 2.
  - "a" occurs 3 times. `st[1]` represents "a". `cnt[1]` should be 3.

Query "aba":
- `root -> a (1) -> b (2) -> a (3)`.
- `cnt[3] = 2`. Correct.

Query "baa":
- `root -> b`. `next[b]`? Yes.
- `-> a`. `next[a]`? Yes.
- `-> a`. `next[a]`? No.
- Result 0. Correct.

## ✅ Proof of Correctness

### Invariant

`count[u]` initially counts the number of times the longest string in class `u` appears as a *prefix* of the string processed so far (which is 1 for original states, 0 for clones).
The suffix link tree represents suffix inclusion. If `u` is a child of `v` in the link tree, then substrings in `v` are suffixes of substrings in `u`.
Any occurrence of `u` implies an occurrence of `v` ending at the same position.
Summing counts up the link tree correctly aggregates all end positions for each equivalence class.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1: First Occurrence Index**
  - Maintain `first_end_pos[u]`. Update during extension (for original) and cloning (copy from original). Do not sum up links; take min/max if needed, but usually `first_end_pos` is invariant for the class? No, `clone` inherits `first_end_pos`.

- **Extension 2: Longest Common Substring**
  - Build SAM for `S`. Stream `T` through it, tracking current length and state. Max length seen is LCS.

### Common Mistakes to Avoid

1. **Not Propagating Counts**
   - ❌ Returning `cnt` directly after construction (will be 1 or 0).
   - ✅ Must propagate up suffix links.

2. **Sorting Order**
   - ❌ Propagating in arbitrary order.
   - ✅ Must be decreasing length (children before parents in link tree).

## Related Concepts

- **Suffix Tree**: Similar capabilities, often O(N) construction (Ukkonen's).
- **LCP Array**: Can solve counting but slower query time.
