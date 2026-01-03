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
time_limit: 2000
memory_limit: 256
---

# Replace Words with Shortest Rare Prefix

## Problem Statement

Given a dictionary of root words with rarity scores and a sentence, replace each word in the sentence with the prefix from the dictionary that:

1. Is a prefix of the word
2. Has the smallest rarity score
3. If multiple prefixes have the same rarity, choose the shortest one
4. If no prefix exists, keep the original word

![Problem Illustration](../images/TRI-004/problem-illustration.png)

## Input Format

- First line: Integer `n` (1 ≤ n ≤ 10^5) - number of dictionary roots
- Next `n` lines: Each contains a string `root` and integer `rarity` separated by space
- Last line: String `sentence` containing words separated by spaces

## Output Format

Print the modified sentence with words replaced according to the rules.

## Constraints

- 1 ≤ n ≤ 10^5
- 1 ≤ word length ≤ 30
- 1 ≤ rarity ≤ 10^9
- 1 ≤ sentence length ≤ 10^5

## Examples

### Example 1

**Input:**

```
2
cat 1
car 2
the cattle carried
```

**Output:**

```
the cat car
```

**Explanation:**

- "the" has no prefix match → remains "the"
- "cattle" has prefix "cat" (rarity 1) → becomes "cat"
- "carried" has prefix "car" (rarity 2) → becomes "car"

![Example 1 Visualization](../images/TRI-004/example-1.png)

### Example 2

**Input:**

```
3
a 3
aa 2
aaa 1
aaaa
```

**Output:**

```
aaa
```

**Explanation:**

Word "aaaa" has three prefix matches:

- "a" (rarity 3)
- "aa" (rarity 2)
- "aaa" (rarity 1) ← lowest rarity, chosen

## Notes

- Lower rarity score means more specialized/important
- Tie-break by shortest length if rarity is equal
- Words are separated by single spaces
- All words and roots consist of lowercase English letters only

## Related Topics

Trie, String, Greedy, Dictionary Lookup

---

## Solution Template

### Java

```java
import java.util.*;

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
    private TrieNode root = new TrieNode();

    public String replaceWords(Map<String, Integer> dictionary, String sentence) {
        //Implement here
        return "";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        Map<String, Integer> dictionary = new HashMap<>();
        
        for (int i = 0; i < n; i++) {
            String word = sc.next();
            int rarity = sc.nextInt();
            dictionary.put(word, rarity);
        }
        
        sc.nextLine(); // consume newline
        String sentence = sc.nextLine();
        
        Solution sol = new Solution();
        System.out.println(sol.replaceWords(dictionary, sentence));
        sc.close();
    }
}
```

### Python

```python
class Solution:
    def __init__(self):
        self.root = TrieNode()

    def replace_words(self, dictionary: dict, sentence: str) -> str:
        # //Implement here
        return ""

def main():
    import sys
    input_data = sys.stdin.read().strip().split('\n')

    n = int(input_data[0])
    dictionary = {}
    for i in range(1, n + 1):
        parts = input_data[i].rsplit(' ', 1)
        root = parts[0]
        rarity = int(parts[1])
        dictionary[root] = rarity

    sentence = input_data[n + 1]
    solution = Solution()
    result = solution.replace_words(dictionary, sentence)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <unordered_map>
#include <sstream>
#include <string>
#include <climits>
#include <limits>

using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    string word;
    int rarity;

    TrieNode() : word(""), rarity(INT_MAX) {}
};

class Solution {
private:
    TrieNode* root;

public:
    Solution() : root(new TrieNode()) {}

    string replaceWords(unordered_map<string, int>& dictionary, const string& sentence) {
        //Implement here
        return "";
    }
};

int main() {
    int n;
    if (!(cin >> n)) {
        return 0;
    }

    unordered_map<string, int> dictionary;
    for (int i = 0; i < n; i++) {
        string root;
        int rarity;
        cin >> root >> rarity;
        dictionary[root] = rarity;
    }
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string sentence;
    getline(cin, sentence);

    Solution solution;
    string result = solution.replaceWords(dictionary, sentence);

    cout << result << '\n';
    return 0;
}
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
  constructor() {
    this.root = new TrieNode();
  }

  replaceWords(dictionary, sentence) {
    //Implement here
    return "";
  }
}

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

const lines = [];
rl.on('line', (line) => lines.push(line.trim()));
rl.on('close', () => {
    const n = parseInt(lines[0]);
    const dictionary = {};
    
    for (let i = 1; i <= n; i++) {
        const parts = lines[i].split(' ');
        const word = parts[0];
        const rarity = parseInt(parts[1]);
        dictionary[word] = rarity;
    }
    
    const sentence = lines[n + 1];
    
    const sol = new Solution();
    console.log(sol.replaceWords(dictionary, sentence));
});
```
