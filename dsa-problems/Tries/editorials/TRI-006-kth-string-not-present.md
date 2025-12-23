---
problem_id: TRI_KTH_MISSING__4257
display_id: TRI-006
slug: kth-string-not-present
title: "Lexicographic k-th String Not Present"
difficulty: Medium
difficulty_score: 50
topics:
  - Trie
  - String
  - Combinatorics
  - DFS
tags:
  - trie
  - string
  - combinatorics
  - dfs
  - medium
premium: true
subscription_tier: basic
---

# Lexicographic k-th String Not Present

![Problem Header](../images/TRI-006/header.png)

### 📋 Problem Summary

Given a trie with inserted strings, find the k-th lexicographically smallest string of length ≤ L that is NOT in the trie.

![Problem Concept](../images/TRI-006/problem-illustration.png)

### 🌍 Real-World Scenario

**Username Generation System**

Imagine you're building a user registration system for a social media platform. Certain usernames are already taken (stored in a trie), and you need to suggest available alternatives.

- Taken: "alice", "bob", "carol"
- User wants a short username (length ≤ 5)
- System suggests: 1st available = "aa", 2nd = "ab", 3rd = "ac", etc.

This helps in:

- Auto-generating available usernames
- Domain name suggestion tools
- License plate generation systems
- Product ID creation
- Session token generation

### 📚 Detailed Explanation

**Total Possible Strings of Length ≤ L**:

For alphabet size 26 (a-z):

- Length 1: 26 strings (a, b, ..., z)
- Length 2: 26² = 676 strings (aa, ab, ..., zz)
- ...
- Length L: 26^L strings

Total = 26 + 26² + ... + 26^L = 26(26^L - 1)/(26-1)

**Example with L=2**:

- Total possible: 26 + 676 = 702 strings
- If 2 are inserted ("a", "b"), 700 are missing
- Find the k-th missing in lexicographic order

**Lexicographic Order**:

```
a, aa, ab, ac, ..., az, b, ba, bb, ..., zz
```

### ❌ Naive Approach

**Idea**: Generate all possible strings up to length L, filter out inserted ones, sort, and pick k-th.

```python
def naive(inserted, L, k):
    all_strings = []
    # Generate all strings of length 1 to L
    for length in range(1, L+1):
        for combo in all_combinations_of_length(length):
            if combo not in inserted:
                all_strings.append(combo)

    all_strings.sort()
    return all_strings[k-1] if k <= len(all_strings) else ""
```

**⏱️ Time Complexity: O(26^L × L + n × L)**

- Generating all: O(26^L)
- Checking membership: O(n × L) per string
- Sorting: O(26^L × log(26^L))

**For L=6**: 26^6 ≈ 300 million strings!

**📦 Space Complexity: O(26^L)**

### ✅ Optimal Approach

**💡 Key Insight**: Use DFS on trie to count and find missing strings without generating all possibilities.

**Trie with Missing Counts:**

```
Example: inserted = ["a", "ab"], L = 2, k = 3

Trie of inserted strings:
Root
  |
  a (marked end)  ← "a" present
  |
  b (marked end)  ← "ab" present

Missing strings analysis (lexicographical order):
Length 1: Missing = {b,c,d,...,z} = 25 strings
Length 2:
  - Starting with 'a': aa,ac,ad,...,az (missing ab) = 25 strings
  - Starting with 'b': ba,bb,bc,...,bz = 26 strings
  - Starting with 'c': ca,cb,...,cz = 26 strings
  - ...

Lexicographical order of missing strings:
1. "aa" ← k=1
2. "ac" ← k=2
3. "ad" ← k=3 ✓

DFS Traversal to find k=3:
Root
  |
  a → Has "a" and "ab"
      Count missing under 'a': aa,ac,ad,...,az (25 strings)
      k=3 ≤ 25, so answer is under 'a'
      |
      +-- a (missing) ← k=1: "aa"
      +-- b (present) → skip
      +-- c (missing) ← k=2: "ac"
      +-- d (missing) ← k=3: "ad" ✓

Result: "ad"
```

**Approach**:

1. Build trie from inserted strings
2. DFS through trie, tracking:
   - Current depth (≤ L)
   - Count of missing strings in current subtree
3. At each node, calculate missing children
4. Navigate to k-th missing string

**Counting Missing Strings**:

At depth d with L remaining levels:

- If current node doesn't exist: All 26^(L-d+1) - 1 strings rooted here are missing
- If exists but not marked as end: Count this string as missing
- Recurse for each of 26 possible children

**DFS Navigation**:

1. For each child 'a' to 'z':

   - Count missing strings if we take this path
   - If count >= k, go down this path
   - Else, k -= count, try next child

2. If current depth < L and node not marked as end:
   - This position itself is a missing string

**⏱️ Time Complexity: O(26 × L × k)**

- Each DFS step: O(26) children check
- Maximum depth: L
- In worst case, traverse k nodes

**Practical**: Much better than O(26^L)

**📦 Space Complexity: O(n × avgLen)**

- Trie storage for inserted strings

### 🎨 Visual Representation

**Example: inserted=["a","b"], L=2, k=1**

```
Trie after insertion:
    root
   /    \
  a*     b*    (* = end marker)

All possible strings length ≤ 2:
Length 1: a*, b*, c, d, ..., z (24 missing)
Length 2: aa, ab, ..., zz (676 missing)

Lexicographic order:
a* (taken), aa (missing #1) ← ANSWER
```

**DFS Process**:

```
Start at root, depth=0, k=1

Try child 'a':
  - Node exists and is end (string "a")
  - Count missing in 'a' subtree:
    - 'a' itself is taken (not counted)
    - Children: aa, ab, ..., az (26 missing)
  - Total under 'a': 26 missing
  - 26 >= 1, so answer is in 'a' subtree
  - Go to 'a'

At 'a', depth=1, k=1:
  Try child 'a':
    - Node doesn't exist
    - This represents string "aa"
    - k=1, found it!

Answer: "aa"
```

### 🧪 Test Case Walkthrough

**Input**: inserted=["a","b"], L=2, k=3

**Step-by-Step**:

```
Trie:
    root
   /    \
  a*     b*

Missing strings in order:
1. aa
2. ab
3. ac ← ANSWER (k=3)
4. ad
...

DFS Process for k=3:

At root:
  Try 'a':
    - Subtree 'a': 26 missing (aa, ab, ..., az)
    - 26 >= 3, enter subtree

  At 'a', k=3:
    Try 'a':
      - "aa" missing, count=1
      - 1 < 3, skip, k=3-1=2

    Try 'b':
      - "ab" missing, count=1
      - 1 < 2, skip, k=2-1=1

    Try 'c':
      - "ac" missing, count=1
      - 1 >= 1, found!

Answer: "ac"
```

### ⚠️ Common Mistakes & Pitfalls

#### 1. **Not Marking String Endings** 🔴

**Problem**: Can't distinguish between "cat" and "catch" prefix
**Solution**: Use isEnd flag

#### 2. **Incorrect Counting** 🔴

**Problem**: Counting strings at depth > L
**Solution**: Stop recursion at depth L

#### 3. **Off-by-One in k** 🔴

**Problem**: Using 0-indexed when k is 1-indexed
**Solution**: Careful with k decrements

#### 4. **Ignoring Empty String** 🔴

**Problem**: Counting empty string as valid
**Solution**: Start from length 1

### 🔑 Algorithm Steps

**Optimal Algorithm**:

1. **Build Trie** from inserted strings

2. **DFS Function**(node, depth, k, current_string):

   ```
   If depth > L: return null

   For each char c from 'a' to 'z':
       child = node.children[c]

       If depth < L and (not child or not child.isEnd):
           If k == 1:
               return current_string + c
           k -= 1

       If child and depth < L:
           result = DFS(child, depth+1, k, current_string+c)
           If result: return result

   return null
   ```

3. **Call** DFS(root, 0, k, "")

### 💻 Implementations

### Java

```java
class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    boolean isEnd = false;
}

class Solution {
    private int L;

    public String kthMissingString(List<String> inserted, int L, int k) {
        this.L = L;
        TrieNode root = new TrieNode();

        // Build trie
        for (String word : inserted) {
            insert(root, word);
        }

        return dfs(root, 0, new int[]{k}, new StringBuilder());
    }

    private void insert(TrieNode root, String word) {
        TrieNode curr = root;
        for (char c : word.toCharArray()) {
            curr.children.putIfAbsent(c, new TrieNode());
            curr = curr.children.get(c);
        }
        curr.isEnd = true;
    }

    private String dfs(TrieNode node, int depth, int[] k, StringBuilder current) {
        if (depth > L) return null;

        for (char c = 'a'; c <= 'z'; c++) {
            TrieNode child = node.children.get(c);

            // Check if this string is missing
            if (depth < L && (child == null || !child.isEnd)) {
                if (k[0] == 1) {
                    return current.toString() + c;
                }
                k[0]--;
            }

            // Recurse to children
            if (child != null && depth < L) {
                current.append(c);
                String result = dfs(child, depth + 1, k, current);
                if (result != null) return result;
                current.deleteCharAt(current.length() - 1);
            }
        }

        return null;
    }
}

// Time: O(26×L×k), Space: O(n×avgLen)
```

### Python

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def kth_missing_string(self, inserted: list, L: int, k: int) -> str:
        """Find k-th missing string of length <= L."""
        root = TrieNode()

        # Build trie
        for word in inserted:
            self._insert(root, word)

        # DFS to find k-th missing
        result = self._dfs(root, 0, L, [k], "")
        return result if result else ""

    def _insert(self, root, word):
        curr = root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def _dfs(self, node, depth, L, k, current):
        if depth > L:
            return None

        for c in 'abcdefghijklmnopqrstuvwxyz':
            child = node.children.get(c)

            # Check if current string is missing
            if depth < L and (child is None or not child.is_end):
                if k[0] == 1:
                    return current + c
                k[0] -= 1

            # Recurse
            if child and depth < L:
                result = self._dfs(child, depth + 1, L, k, current + c)
                if result:
                    return result

        return None

# Time: O(26×L×k), Space: O(n×avgLen)

if __name__ == "__main__":
    first_line = input().strip().split()
    n = int(first_line[0])
    L = int(first_line[1])
    k = int(first_line[2])

    inserted = []
    for _ in range(n):
        inserted.append(input().strip())

    solution = Solution()
    result = solution.kth_missing_string(inserted, L, k)
    print(result)
```

### C++++

```cpp
struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool isEnd = false;
};

class Solution {
private:
    int L;

    void insert(TrieNode* root, const string& word) {
        TrieNode* curr = root;
        for (char c : word) {
            if (!curr->children[c]) {
                curr->children[c] = new TrieNode();
            }
            curr = curr->children[c];
        }
        curr->isEnd = true;
    }

    string dfs(TrieNode* node, int depth, int& k, string current) {
        if (depth > L) return "";

        for (char c = 'a'; c <= 'z'; c++) {
            TrieNode* child = node->children[c];

            if (depth < L && (!child || !child->isEnd)) {
                if (k == 1) {
                    return current + c;
                }
                k--;
            }

            if (child && depth < L) {
                string result = dfs(child, depth + 1, k, current + c);
                if (!result.empty()) return result;
            }
        }

        return "";
    }

public:
    string kthMissingString(vector<string>& inserted, int L, int k) {
        this->L = L;
        TrieNode* root = new TrieNode();

        for (const string& word : inserted) {
            insert(root, word);
        }

        return dfs(root, 0, k, "");
    }
};

// Time: O(26×L×k), Space: O(n×avgLen)
```

### JavaScript

```javascript
class TrieNode {
  constructor() {
    this.children = new Map();
    this.isEnd = false;
  }
}

class Solution {
  kthMissingString(inserted, L, k) {
    const root = new TrieNode();

    // Build trie
    for (const word of inserted) {
      this.insert(root, word);
    }

    // DFS
    const kRef = { value: k };
    return this.dfs(root, 0, L, kRef, "") || "";
  }

  insert(root, word) {
    let curr = root;
    for (const char of word) {
      if (!curr.children.has(char)) {
        curr.children.set(char, new TrieNode());
      }
      curr = curr.children.get(char);
    }
    curr.isEnd = true;
  }

  dfs(node, depth, L, kRef, current) {
    if (depth > L) return null;

    for (let i = 0; i < 26; i++) {
      const c = String.fromCharCode(97 + i); // 'a' to 'z'
      const child = node.children.get(c);

      if (depth < L && (!child || !child.isEnd)) {
        if (kRef.value === 1) {
          return current + c;
        }
        kRef.value--;
      }

      if (child && depth < L) {
        const result = this.dfs(child, depth + 1, L, kRef, current + c);
        if (result) return result;
      }
    }

    return null;
  }
}

// Time: O(26×L×k), Space: O(n×avgLen)
```

### 📊 Comparison Table

| **Aspect**      | **Naive**     | **Trie DFS**   |
| --------------- | ------------- | -------------- |
| **Time**        | O(26^L × L)   | O(26×L×k)      |
| **Space**       | O(26^L)       | O(n×avgLen)    |
| **For L=6**     | ~300M strings | ~thousands ops |
| **Scalability** | Impractical   | Efficient      |

### 🎯 Key Takeaways

1. **Combinatorial counting** in tries avoids generating all possibilities
2. **DFS with pruning** efficiently navigates to k-th element
3. **L constraint** keeps problem tractable (L ≤ 6)
4. **Lexicographic order** naturally follows trie structure

### 🔗 Related Problems

- Kth Smallest in Lexicographical Order
- Missing Number
- First Missing Positive
- Shortest Unique Prefix

---

**Difficulty**: Medium  
**Topics**: Trie, String, Combinatorics, DFS  
**Companies**: Google, Facebook, Amazon


## Constraints

- 1 ≤ n ≤ 10^5
- 1 ≤ L ≤ 6
- 1 ≤ k ≤ 10^9
- All strings consist of lowercase English letters (a-z)