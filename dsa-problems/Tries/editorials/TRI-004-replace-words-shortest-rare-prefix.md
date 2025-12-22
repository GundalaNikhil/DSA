---
problem_id: TRI_REPLACE_RARE__4255
display_id: TRI-004
slug: replace-words-shortest-rare-prefix
title: "Replace Words with Shortest Rare Prefix"
difficulty: Medium
difficulty_score: 50
topics:
  - Trie
  - String
  - Greedy
  - Dictionary
tags:
  - trie
  - string
  - greedy
  - medium
premium: true
subscription_tier: basic
---

# Replace Words with Shortest Rare Prefix

![Problem Header](../images/TRI-004/header.png)

### 📋 Problem Summary

Given a dictionary of root words with rarity scores and a sentence, replace each word with the prefix from the dictionary that is both a prefix of the word and has the smallest rarity score. If multiple prefixes have the same rarity, choose the shortest one.

![Problem Concept](../images/TRI-004/problem-illustration.png)

### 🌍 Real-World Scenario

**Medical Record Compression System**

Imagine you're building a medical record system where:

- Common medical terms have standard abbreviations
- Rare, specialized terms get priority for shorter codes (lower rarity = more specialized)
- Example: "cardiologist" could be abbreviated to "card" (common) or "cardio" (rare specialty)

You have a dictionary:

- "card" (rarity: 5) - very common prefix
- "cardio" (rarity: 2) - rare, specialized

When processing "cardiologist", you choose "cardio" because:

- It has lower rarity (2 < 5)
- It's a valid prefix of "cardiologist"

This helps in:

- Efficient medical record storage
- Standardized medical coding (ICD codes)
- Insurance claim processing
- Medical research data mining

### 📚 Detailed Explanation

**Problem Components**:

1. **Dictionary**: List of root words, each with a rarity score

   - Lower rarity = more specialized/important
   - Example: {"cat": 1, "car": 2, "card": 3}

2. **Sentence**: String containing words separated by spaces

3. **Goal**: Replace each word with best matching root
   - "Best" = lowest rarity score
   - Tie-break by shortest length

**Example**:

```
Dictionary: {"cat": 1, "car": 2}
Sentence: "the cattle carried"

Processing:
- "the" → no prefix match → "the"
- "cattle" → prefix "cat" (rarity 1) → "cat"
- "carried" → prefix "car" (rarity 2) → "car"

Output: "the cat car"
```

### ❌ Naive Approach

**Idea**: For each word in sentence, check all dictionary roots linearly.

```python
def replace_naive(dictionary, sentence):
    words = sentence.split()
    result = []

    for word in words:
        best_root = word
        best_rarity = float('inf')

        for root, rarity in dictionary.items():
            if word.startswith(root):
                if rarity < best_rarity or (rarity == best_rarity and len(root) < len(best_root)):
                    best_root = root
                    best_rarity = rarity

        result.append(best_root)

    return ' '.join(result)
```

**⏱️ Time Complexity: O(N × M × L)**

Where:

- N = number of words in sentence
- M = number of dictionary roots
- L = average word length (for string prefix check)

**For realistic inputs**:

- N = 1000 words
- M = 10,000 roots
- L = 10 characters
- Total: ~100,000,000 operations

**📦 Space Complexity: O(N + M)**

### ✅ Optimal Approach

**💡 Key Insight**: Build a trie where each node stores the best (lowest rarity) root ending at that position.

**Trie with Rarity Tracking:**

```
Dictionary: {"cat": 1, "car": 2, "cattle": 5}

Trie Construction:
Root
  |
  c
  |
  a
  |
  +-- t (bestRoot="cat", rarity=1) ✓ End
  |   |
  |   t
  |   |
  |   l
  |   |
  |   e (bestRoot="cattle", rarity=5) End
  |       (but "cat" is better: rarity=1 < 5)
  |
  +-- r (bestRoot="car", rarity=2) End

Query "cattle":
  c → a → t (found "cat", rarity=1) ✓
  Continue: t → l → e (found "cattle", rarity=5)
  Best: "cat" (rarity=1 < 5)

Query "carried":
  c → a → r (found "car", rarity=2) ✓
  Continue: r → ? (no 'r' child)
  Best: "car"

Result: "the cat car"
```

**Approach**:

1. **Build trie from dictionary**:
   - Insert each root into trie
   - At each node, store the best (lowest rarity, then shortest) root seen so far
2. **Process each word in sentence**:
   - Traverse trie following word's characters
   - Track the best root encountered during traversal
   - If no root found, keep original word

**Why This Works?**

- Trie allows efficient prefix matching: O(L) per word
- Storing best root at each node eliminates redundant comparisons
- Early termination possible when traversal ends

**Example Trie Construction**:

Dictionary: {"cat": 1, "car": 2, "card": 3}

```
        root
         |
         c (best: null)
         |
         a (best: null)
        / \
       t   r (best: "car" rarity=2)
(best: "cat"  |
 rarity=1)    d (best: "car" rarity=2, not "card" because "car" is shorter)
```

**⏱️ Time Complexity: O(M × K + N × L)**

**Breakdown**:

- Building trie: O(M × K) where K = avg root length
- Processing sentence: O(N × L) where L = avg word length
- Total: Linear in input sizes!

**For realistic inputs**:

- M × K = 10,000 × 10 = 100,000
- N × L = 1,000 × 10 = 10,000
- Total: ~110,000 operations (vs 100M naive!)

**📦 Space Complexity: O(M × K)**

- Trie nodes for all dictionary roots
- Typically much smaller than M × K due to shared prefixes

### 🎨 Visual Representation

**Example: Dictionary: {"cat": 1, "car": 2}, Sentence: "cattle car"**

```
┌────────────────────────────────────────┐
│  Trie Construction                     │
└────────────────────────────────────────┘

Insert "cat" (rarity=1):
    root
     |
     c
     |
     a
     |
     t (end: "cat", rarity=1) ★

Insert "car" (rarity=2):
    root
     |
     c
     |
     a (best so far: none)
    / \
   t   r (end: "car", rarity=2) ★
(cat)

┌────────────────────────────────────────┐
│  Word Processing                       │
└────────────────────────────────────────┘

Word 1: "cattle"
Traverse: c → a → t (found "cat", rarity=1)
         → continue: t (no child)
         → stop
Best match: "cat"
Output: "cat"

Word 2: "car"
Traverse: c → a → r (found "car", rarity=2)
Best match: "car"
Output: "car"

Final: "cat car"
```

### 🧪 Test Case Walkthrough

**Input**:

```
Dictionary: {"cat": 1, "car": 2}
Sentence: "the cattle carried"
```

**Step-by-Step**:

```
Build Trie:
    root
     |
     c
     |
     a
    / \
   t   r
("cat") ("car")

Process Words:

1. "the":
   - Search: 't' → not in trie (root has child 'c' only)
   - No match
   - Output: "the"

2. "cattle":
   - Search: 'c' → exists
   - Move to 'a': exists
   - Move to 't': exists, found "cat" (rarity=1) ★
   - Move to 't': no child 't' under current node
   - Best found: "cat"
   - Output: "cat"

3. "carried":
   - Search: 'c' → 'a' → 'r': found "car" (rarity=2) ★
   - Move to 'r': no child 'r'
   - Best found: "car"
   - Output: "car"

Result: ["the", "cat", "car"]
Final Output: "the cat car"
```

### ⚠️ Common Mistakes & Pitfalls

#### 1. **Not Handling Tie-Breaking Correctly** 🔴

**Problem**:

```python
if rarity <= best_rarity:  # ❌ Wrong tie-break
    best = root
```

**Solution**:

```python
if rarity < best_rarity or (rarity == best_rarity and len(root) < len(best)):
    best = root
```

#### 2. **Forgetting to Track Best During Traversal** 🔴

**Problem**: Only checking at the end of traversal

**Solution**: Update best root at every node that marks end of a dictionary word

#### 3. **Not Handling Words Without Matches** 🔴

**Problem**:

```python
return best_root  # ❌ What if best_root is None?
```

**Solution**:

```python
return best_root if best_root else original_word
```

#### 4. **Incorrect Trie Node Structure** 🔴

**Problem**: Not storing rarity at nodes

**Solution**:

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
        self.rarity = float('inf')
```

### 🔑 Algorithm Steps

**Optimal Algorithm**:

1. **Build Trie**:

   ```
   For each (root, rarity) in dictionary:
       Insert root into trie
       At end node, store: root, rarity
   ```

2. **Process Sentence**:

   ```
   For each word in sentence.split():
       curr = trie root
       best_root = None
       best_rarity = infinity

       For each char in word:
           If char not in curr.children:
               break
           curr = curr.children[char]

           If curr has end marker:
               If curr.rarity < best_rarity OR
                  (curr.rarity == best_rarity AND len(curr.word) < len(best_root)):
                   best_root = curr.word
                   best_rarity = curr.rarity

       Append (best_root or word) to result
   ```

3. **Return** joined result

### 💻 Implementations

### Java

```java
class TrieNode {
    Map<Character, TrieNode> children;
    String word;
    int rarity;

    TrieNode() {
        children = new HashMap<>();
        word = null;
        rarity = Integer.MAX_VALUE;
    }
}

class Solution {
    private TrieNode root;

    public String replaceWords(Map<String, Integer> dictionary, String sentence) {
        root = new TrieNode();

        // Build trie
        for (Map.Entry<String, Integer> entry : dictionary.entrySet()) {
            insert(entry.getKey(), entry.getValue());
        }

        // Process sentence
        String[] words = sentence.split(" ");
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < words.length; i++) {
            if (i > 0) result.append(" ");
            result.append(findReplacement(words[i]));
        }

        return result.toString();
    }

    private void insert(String word, int rarity) {
        TrieNode curr = root;

        for (char c : word.toCharArray()) {
            curr.children.putIfAbsent(c, new TrieNode());
            curr = curr.children.get(c);
        }

        // Update only if this is better
        if (rarity < curr.rarity ||
            (rarity == curr.rarity && (curr.word == null || word.length() < curr.word.length()))) {
            curr.word = word;
            curr.rarity = rarity;
        }
    }

    private String findReplacement(String word) {
        TrieNode curr = root;
        String best = null;
        int bestRarity = Integer.MAX_VALUE;

        for (char c : word.toCharArray()) {
            if (!curr.children.containsKey(c)) break;

            curr = curr.children.get(c);

            if (curr.word != null) {
                if (curr.rarity < bestRarity ||
                    (curr.rarity == bestRarity && curr.word.length() < best.length())) {
                    best = curr.word;
                    bestRarity = curr.rarity;
                }
            }
        }

        return best != null ? best : word;
    }
}

// Time: O(M×K + N×L), Space: O(M×K)
```

### Python

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
        self.rarity = float('inf')

class Solution:
    def replace_words(self, dictionary: dict, sentence: str) -> str:
        """
        Replace words with shortest rare prefix from dictionary.

        Args:
            dictionary: Dict mapping root words to rarity scores
            sentence: Input sentence

        Returns:
            Sentence with words replaced by best matching roots
        """
        # Build trie
        root = TrieNode()

        for word, rarity in dictionary.items():
            self._insert(root, word, rarity)

        # Process sentence
        words = sentence.split()
        result = []

        for word in words:
            replacement = self._find_replacement(root, word)
            result.append(replacement)

        return ' '.join(result)

    def _insert(self, root, word, rarity):
        curr = root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        # Update if better
        if rarity < curr.rarity or (rarity == curr.rarity and (curr.word is None or len(word) < len(curr.word))):
            curr.word = word
            curr.rarity = rarity

    def _find_replacement(self, root, word):
        curr = root
        best = None
        best_rarity = float('inf')

        for char in word:
            if char not in curr.children:
                break

            curr = curr.children[char]

            if curr.word is not None:
                if curr.rarity < best_rarity or (curr.rarity == best_rarity and len(curr.word) < len(best)):
                    best = curr.word
                    best_rarity = curr.rarity

        return best if best is not None else word

# Time: O(M×K + N×L), Space: O(M×K)

if __name__ == "__main__":
    n = int(input().strip())
    dictionary = {}
    for _ in range(n):
        parts = input().strip().split()
        root = parts[0]
        rarity = int(parts[1])
        dictionary[root] = rarity
    sentence = input().strip()

    solution = Solution()
    result = solution.replace_words(dictionary, sentence)
    print(result)
```

### C++++

```cpp
struct TrieNode {
    unordered_map<char, TrieNode*> children;
    string word;
    int rarity;

    TrieNode() : word(""), rarity(INT_MAX) {}
};

class Solution {
private:
    TrieNode* root;

    void insert(const string& word, int rarity) {
        TrieNode* curr = root;

        for (char c : word) {
            if (curr->children.find(c) == curr->children.end()) {
                curr->children[c] = new TrieNode();
            }
            curr = curr->children[c];
        }

        if (rarity < curr->rarity ||
            (rarity == curr->rarity && (curr->word.empty() || word.length() < curr->word.length()))) {
            curr->word = word;
            curr->rarity = rarity;
        }
    }

    string findReplacement(const string& word) {
        TrieNode* curr = root;
        string best = "";
        int bestRarity = INT_MAX;

        for (char c : word) {
            if (curr->children.find(c) == curr->children.end()) break;

            curr = curr->children[c];

            if (!curr->word.empty()) {
                if (curr->rarity < bestRarity ||
                    (curr->rarity == bestRarity && curr->word.length() < best.length())) {
                    best = curr->word;
                    bestRarity = curr->rarity;
                }
            }
        }

        return best.empty() ? word : best;
    }

public:
    string replaceWords(unordered_map<string, int>& dictionary, string sentence) {
        root = new TrieNode();

        // Build trie
        for (auto& entry : dictionary) {
            insert(entry.first, entry.second);
        }

        // Process sentence
        stringstream ss(sentence);
        string word, result;
        bool first = true;

        while (ss >> word) {
            if (!first) result += " ";
            result += findReplacement(word);
            first = false;
        }

        return result;
    }
};

// Time: O(M×K + N×L), Space: O(M×K)
```

### JavaScript

```javascript
class TrieNode {
  constructor() {
    this.children = new Map();
    this.word = null;
    this.rarity = Infinity;
  }
}

class Solution {
  replaceWords(dictionary, sentence) {
    const root = new TrieNode();

    // Build trie
    for (const [word, rarity] of Object.entries(dictionary)) {
      this.insert(root, word, rarity);
    }

    // Process sentence
    const words = sentence.split(" ");
    const result = words.map((word) => this.findReplacement(root, word));

    return result.join(" ");
  }

  insert(root, word, rarity) {
    let curr = root;

    for (const char of word) {
      if (!curr.children.has(char)) {
        curr.children.set(char, new TrieNode());
      }
      curr = curr.children.get(char);
    }

    if (
      rarity < curr.rarity ||
      (rarity === curr.rarity &&
        (curr.word === null || word.length < curr.word.length))
    ) {
      curr.word = word;
      curr.rarity = rarity;
    }
  }

  findReplacement(root, word) {
    let curr = root;
    let best = null;
    let bestRarity = Infinity;

    for (const char of word) {
      if (!curr.children.has(char)) break;

      curr = curr.children.get(char);

      if (curr.word !== null) {
        if (
          curr.rarity < bestRarity ||
          (curr.rarity === bestRarity && curr.word.length < best.length)
        ) {
          best = curr.word;
          bestRarity = curr.rarity;
        }
      }
    }

    return best !== null ? best : word;
  }
}

// Time: O(M×K + N×L), Space: O(M×K)
```

### 📊 Comparison Table

| **Aspect**            | **Naive**        | **Trie Optimal** |
| --------------------- | ---------------- | ---------------- |
| **Time Complexity**   | O(N × M × L)     | O(M×K + N×L)     |
| **Space**             | O(N + M)         | O(M×K)           |
| **For N=1000, M=10K** | ~100M operations | ~110K operations |
| **Prefix Matching**   | Linear scan      | Trie traversal   |
| **Scalability**       | Poor             | Excellent        |

### 🎯 Key Takeaways

1. **Tries excel at prefix matching** - O(L) vs O(M×L)
2. **Store metadata at nodes** for efficient lookups
3. **Greedy choice**: Always pick lowest rarity, then shortest
4. **Early termination** when traversal fails

---

**Difficulty**: Medium  
**Topics**: Trie, String, Greedy  
**Companies**: Google, Microsoft, Amazon
