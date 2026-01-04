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

class Solution {
    public String replaceWords(Map<String, Integer> dictionary, String sentence) {
        // Implement here
        return sentence;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        Map<String, Integer> dictionary = new HashMap<>();
        for (int i = 0; i < n; i++) {
            String root = sc.next();
            int rarity = sc.nextInt();
            dictionary.put(root, rarity);
        }
        sc.nextLine(); // consume newline
        if (!sc.hasNextLine()) return;
        String sentence = sc.nextLine();

        Solution solution = new Solution();
        String result = solution.replaceWords(dictionary, sentence);
        System.out.println(result);
    }
}
```

### Python

```python
from typing import Dict

class Solution:
    def replace_words(self, dictionary: Dict[str, int], sentence: str) -> str:
        # Implement here
        return sentence

def main():
    import sys
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    n = int(input_data[0])
    dictionary = {}
    for i in range(1, n + 1):
        parts = input_data[i].split()
        if len(parts) == 2:
            dictionary[parts[0]] = int(parts[1])

    sentence = input_data[n + 1] if len(input_data) > n + 1 else ""

    solution = Solution()
    result = solution.replace_words(dictionary, sentence)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <sstream>
#include <limits>

using namespace std;

class Solution {
public:
    string replaceWords(unordered_map<string, int>& dictionary, const string& sentence) {
        // Implement here
        return sentence;
    }
};

int main() {
    int n;
    if (!(cin >> n)) return 0;

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

    cout << result << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  replaceWords(dictionary, sentence) {
    // Implement here
    return sentence;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const lines = [];
rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  if (lines.length === 0) return;
  const n = parseInt(lines[0]);
  const dictionary = new Map();
  for (let i = 1; i <= n; i++) {
    const [root, rarity] = lines[i].split(/\s+/);
    dictionary.set(root, parseInt(rarity));
  }
  const sentence = lines[n + 1] || "";

  const solution = new Solution();
  const result = solution.replaceWords(dictionary, sentence);

  console.log(result);
});
```
