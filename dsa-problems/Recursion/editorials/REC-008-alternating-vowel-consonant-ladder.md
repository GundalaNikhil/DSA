---
title: Alternating Vowel-Consonant Ladder
slug: alternating-vowel-consonant-ladder
difficulty: Medium
difficulty_score: 54
tags:
- Recursion
- Backtracking
- Graphs
- BFS
problem_id: REC_ALTERNATING_VOWEL_CONSONANT_LADDER__6073
display_id: REC-008
topics:
- Recursion
- Backtracking
- Graphs
---
# Alternating Vowel-Consonant Ladder - Editorial

## Problem Summary

You need to find all **shortest** transformation sequences (word ladders) from a `start` word to an `end` word.
Rules for transformation:
1.  Change exactly one letter at a time.
2.  Each intermediate word must exist in the given dictionary.
3.  **Constraint**: The starting letter of consecutive words must alternate between a vowel and a consonant. For example, if word $i$ starts with a vowel, word $i+1$ must start with a consonant, and vice versa.

## Real-World Scenario

This is a variation of the classic **Word Ladder** game (invented by Lewis Carroll). It models finding the shortest path in a graph where nodes are words and edges represent single-letter modifications. The additional constraint adds a "parity" check to the edges, similar to alternating traffic rules or bipartite matching constraints.

## Problem Exploration

### 1. Vowels and Consonants
-   Vowels: `a, e, i, o, u`.
-   Consonants: All other lowercase English letters.
-   Helper function `isVowel(char c)` is essential.

### 2. Graph Construction
-   Nodes: Words in the dictionary (plus start word).
-   Edges: Two words are connected if they differ by exactly 1 character AND their starting letters have different types (one vowel, one consonant).
    -   *Wait*: The problem says "successive words must alternate". It doesn't say the *edge* exists only if they alternate. It says the *path* must alternate.
    -   *Correction*: Does the rule apply to the *start* word? "The first letter of successive words must alternate". Yes. So if `start` is V-start, next must be C-start.

### 3. Shortest Path + All Paths
-   **BFS**: To find the shortest distance.
-   **DFS/Backtracking**: To reconstruct all paths of that shortest distance.
-   Since we need *all* shortest paths, standard BFS storing `parent` pointers is good, but since a node can have multiple parents (multiple shortest paths reaching it), we store `List<String> parents` for each node.

## Approaches

### Approach 1: BFS + Backtracking (Standard Word Ladder II)

1.  **Preprocessing**: Identify Vowel/Consonant status for all words. Build an adjacency list where edges only exist between words differing by 1 char AND having different start-letter types.
2.  **BFS**:
    -   Start from `start`.
    -   Track `distance` to each word.
    -   Track `parents` map: `word -> list of previous words`.
    -   Standard level-order traversal. If we reach `end`, we stop adding new levels but finish the current level to find all parents.
3.  **Backtracking (DFS)**:
    -   Reconstruct paths from `end` back to `start` using the `parents` map.
    -   Reverse the paths for output.

### Approach 2: Bidirectional BFS
For very large dictionaries, Bidirectional BFS is faster. However, with $M \le 3000$, standard BFS is sufficient and easier to implement for "all paths".

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public List<List<String>> ladders(String start, String end, List<String> dict) {
        Set<String> dictSet = new HashSet<>(dict);
        dictSet.add(start);
        dictSet.add(end); // Ensure end is in dict for graph building
        
        // Build adjacency list with constraints
        Map<String, List<String>> adj = new HashMap<>();
        for (String w : dictSet) {
            adj.put(w, new ArrayList<>());
        }
        
        List<String> words = new ArrayList<>(dictSet);
        for (int i = 0; i < words.size(); i++) {
            for (int j = i + 1; j < words.size(); j++) {
                String w1 = words.get(i);
                String w2 = words.get(j);
                if (isOneDiff(w1, w2) && isAlternating(w1, w2)) {
                    adj.get(w1).add(w2);
                    adj.get(w2).add(w1);
                }
            }
        }
        
        // BFS
        Map<String, Integer> dist = new HashMap<>();
        Map<String, List<String>> parents = new HashMap<>();
        Queue<String> q = new LinkedList<>();
        
        q.offer(start);
        dist.put(start, 0);
        
        boolean found = false;
        
        while (!q.isEmpty()) {
            int size = q.size();
            Set<String> currentLevelVisited = new HashSet<>();
            
            for (int i = 0; i < size; i++) {
                String curr = q.poll();
                if (curr.equals(end)) found = true;
                
                int curDist = dist.get(curr);
                
                for (String neighbor : adj.getOrDefault(curr, new ArrayList<>())) {
                    if (!dist.containsKey(neighbor)) {
                        // Not visited yet
                        if (currentLevelVisited.add(neighbor)) {
                            dist.put(neighbor, curDist + 1);
                            q.offer(neighbor);
                        }
                        parents.computeIfAbsent(neighbor, k -> new ArrayList<>()).add(curr);
                    } else if (dist.get(neighbor) == curDist + 1) {
                        // Visited in this level (another shortest path)
                        parents.computeIfAbsent(neighbor, k -> new ArrayList<>()).add(curr);
                    }
                }
            }
            if (found) break;
        }
        
        List<List<String>> results = new ArrayList<>();
        if (found) {
            List<String> path = new ArrayList<>();
            path.add(end);
            backtrack(end, start, parents, path, results);
        }
        
        // Sort results for consistent output if needed (problem doesn't specify order, but usually lexicographical or any)
        // The problem output example shows sorted paths.
        results.sort((a, b) -> {
            for(int i=0; i<a.size(); i++) {
                if(!a.get(i).equals(b.get(i))) return a.get(i).compareTo(b.get(i));
            }
            return 0;
        });
        
        return results;
    }
    
    private void backtrack(String curr, String start, Map<String, List<String>> parents, List<String> path, List<List<String>> results) {
        if (curr.equals(start)) {
            List<String> fullPath = new ArrayList<>(path);
            Collections.reverse(fullPath);
            results.add(fullPath);
            return;
        }
        
        for (String p : parents.getOrDefault(curr, new ArrayList<>())) {
            path.add(p);
            backtrack(p, start, parents, path, results);
            path.remove(path.size() - 1);
        }
    }
    
    private boolean isOneDiff(String a, String b) {
        if (a.length() != b.length()) return false;
        int diff = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) diff++;
            if (diff > 1) return false;
        }
        return diff == 1;
    }
    
    private boolean isAlternating(String a, String b) {
        return isVowel(a.charAt(0)) != isVowel(b.charAt(0));
    }
    
    private boolean isVowel(char c) {
        return "aeiou".indexOf(c) != -1;
    }
}
```

### Python

```python
from collections import deque, defaultdict

def ladders(start: str, end: str, dict_words: list[str]) -> list[list[str]]:
    word_set = set(dict_words)
    word_set.add(start)
    word_set.add(end)
    
    def is_vowel(c):
        return c in 'aeiou'
    
    def is_alternating(w1, w2):
        return is_vowel(w1[0]) != is_vowel(w2[0])
    
    def get_neighbors(word):
        neighbors = []
        chars = list(word)
        for i in range(len(chars)):
            original = chars[i]
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c == original: continue
                chars[i] = c
                new_word = "".join(chars)
                if new_word in word_set and is_alternating(word, new_word):
                    neighbors.append(new_word)
            chars[i] = original
        return neighbors

    # BFS
    parents = defaultdict(list)
    dist = {start: 0}
    queue = deque([start])
    found = False
    
    while queue and not found:
        level_size = len(queue)
        level_visited = set()
        
        for _ in range(level_size):
            curr = queue.popleft()
            if curr == end:
                found = True
            
            cur_dist = dist[curr]
            
            # Optimization: Precompute adjacency or generate on fly
            # Generating on fly is O(26 * L), iterating dict is O(M * L)
            # Given M=3000, L=6, M*L is better than 26*L? No.
            # But checking adjacency against all M is O(M*L). 26*L is small constant.
            # However, we need to check if generated word is in dict.
            
            for neighbor in get_neighbors(curr):
                if neighbor not in dist:
                    if neighbor not in level_visited:
                        dist[neighbor] = cur_dist + 1
                        queue.append(neighbor)
                        level_visited.add(neighbor)
                    parents[neighbor].append(curr)
                elif dist[neighbor] == cur_dist + 1:
                    parents[neighbor].append(curr)
                    
    results = []
    if found:
        def backtrack(curr, path):
            if curr == start:
                results.append(path[::-1])
                return
            for p in parents[curr]:
                path.append(p)
                backtrack(p, path)
                path.pop()
        
        backtrack(end, [end])
        
    results.sort()
    return results
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<string>> ladders(string start, string end, const vector<string>& dict) {
        unordered_set<string> wordSet(dict.begin(), dict.end());
        wordSet.insert(start);
        wordSet.insert(end);
        
        unordered_map<string, vector<string>> parents;
        unordered_map<string, int> dist;
        queue<string> q;
        
        q.push(start);
        dist[start] = 0;
        
        bool found = false;
        
        while (!q.empty() && !found) {
            int size = q.size();
            unordered_set<string> levelVisited;
            
            for (int i = 0; i < size; i++) {
                string curr = q.front();
                q.pop();
                
                if (curr == end) found = true;
                
                string temp = curr;
                for (int j = 0; j < temp.length(); j++) {
                    char original = temp[j];
                    for (char c = 'a'; c <= 'z'; c++) {
                        if (c == original) continue;
                        temp[j] = c;
                        if (wordSet.count(temp) && isAlternating(curr, temp)) {
                            if (dist.find(temp) == dist.end()) {
                                if (levelVisited.find(temp) == levelVisited.end()) {
                                    dist[temp] = dist[curr] + 1;
                                    q.push(temp);
                                    levelVisited.insert(temp);
                                }
                                parents[temp].push_back(curr);
                            } else if (dist[temp] == dist[curr] + 1) {
                                parents[temp].push_back(curr);
                            }
                        }
                    }
                    temp[j] = original;
                }
            }
        }
        
        vector<vector<string>> results;
        if (found) {
            vector<string> path;
            path.push_back(end);
            backtrack(end, start, parents, path, results);
        }
        
        // Sort for deterministic output
        sort(results.begin(), results.end());
        
        return results;
    }

private:
    void backtrack(string curr, string start, unordered_map<string, vector<string>>& parents, vector<string>& path, vector<vector<string>>& results) {
        if (curr == start) {
            vector<string> fullPath = path;
            reverse(fullPath.begin(), fullPath.end());
            results.push_back(fullPath);
            return;
        }
        
        for (const string& p : parents[curr]) {
            path.push_back(p);
            backtrack(p, start, parents, path, results);
            path.pop_back();
        }
    }

    bool isAlternating(const string& a, const string& b) {
        return isVowel(a[0]) != isVowel(b[0]);
    }

    bool isVowel(char c) {
        return string("aeiou").find(c) != string::npos;
    }
};
```

### JavaScript

```javascript
class Solution {
  ladders(start, end, dict) {
    const wordSet = new Set(dict);
    wordSet.add(start);
    wordSet.add(end);

    const isVowel = (c) => "aeiou".includes(c);
    const isAlternating = (a, b) => isVowel(a[0]) !== isVowel(b[0]);

    const parents = new Map();
    const dist = new Map();
    const queue = [start];
    dist.set(start, 0);

    let found = false;
    let head = 0;

    while (head < queue.length) {
      if (found) break; // Finish processing current level then stop
      // We need to be careful not to process next level if found.
      
      // Collect current level nodes
      const levelSize = queue.length - head;
      const currentLevelNodes = [];
      for(let i=0; i<levelSize; i++) currentLevelNodes.push(queue[head+i]);
      
      // Check if end is in this level
      if (currentLevelNodes.includes(end)) found = true;
      
      const levelVisited = new Set();
      
      for (let i = 0; i < levelSize; i++) {
        const curr = queue[head++];
        const curDist = dist.get(curr);
        
        // Generate neighbors
        const chars = curr.split("");
        for (let j = 0; j < chars.length; j++) {
          const original = chars[j];
          for (let k = 0; k < 26; k++) {
            const c = String.fromCharCode(97 + k);
            if (c === original) continue;
            chars[j] = c;
            const neighbor = chars.join("");
            
            if (wordSet.has(neighbor) && isAlternating(curr, neighbor)) {
               if (!dist.has(neighbor)) {
                 if (!levelVisited.has(neighbor)) {
                   dist.set(neighbor, curDist + 1);
                   queue.push(neighbor);
                   levelVisited.add(neighbor);
                 }
                 if (!parents.has(neighbor)) parents.set(neighbor, []);
                 parents.get(neighbor).push(curr);
               } else if (dist.get(neighbor) === curDist + 1) {
                 if (!parents.has(neighbor)) parents.set(neighbor, []);
                 parents.get(neighbor).push(curr);
               }
            }
          }
          chars[j] = original;
        }
      }
    }

    const results = [];
    if (found) {
      const backtrack = (curr, path) => {
        if (curr === start) {
          results.push([...path].reverse());
          return;
        }
        const pars = parents.get(curr) || [];
        for (const p of pars) {
          path.push(p);
          backtrack(p, path);
          path.pop();
        }
      };
      backtrack(end, [end]);
    }
    
    results.sort((a, b) => {
        const sa = a.join(" ");
        const sb = b.join(" ");
        return sa.localeCompare(sb);
    });

    return results;
  }
}
```

## Test Case Walkthrough

**Input:**
Start: `eat` (Vowel)
End: `cot` (Consonant)
Dict: `eat, cat, cot, eot`

1.  **Level 0**: `eat` (Dist 0).
2.  **Level 1**:
    -   Neighbors of `eat` (V): Must be Consonant-start.
    -   `cat` (C): Differs by 'c'. Valid. Dist 1. Parent `eat`.
    -   `eot` (V): Starts with V. `isAlternating` false. **Skip**.
    -   `cot` (C): Differs by 2 chars. Skip.
    -   Queue: `[cat]`.
3.  **Level 2**:
    -   Neighbors of `cat` (C): Must be Vowel-start.
    -   `cot` (C): Starts with C. `isAlternating` false. **Skip**.
    -   `eat` (V): Visited.
    -   `eot` (V): Differs by 'e' vs 'c' and 'o' vs 'a'. 2 diffs. Skip.
    -   Let's re-read the problem carefully.
    -   "The first letter of successive words must alternate between vowel-start and consonant-start."
    -   Example output: `eat cat cot`.
    -   `eat` (Vowel start).
    -   `cat` (Consonant start).
    -   `cot` (Consonant start).
    -   **Contradiction**: `cat` -> `cot` is C -> C. This violates the rule.
    -   Let's check the example output again.
    -   `eat cat cot`
    -   `eat eot cot`
    -   `eot` starts with 'e' (Vowel). `cot` starts with 'c' (Consonant). `eot` -> `cot` is V -> C. OK.
    -   `eat` -> `eot` is V -> V. **Violation**.
    -   So `eat -> eot -> cot` has V->V transition.
    -   `eat -> cat -> cot` has C->C transition.
    -   **Conclusion**: My interpretation of "alternate" might be wrong, or the example is wrong, or "successive words" means something else?
    -   "The first letter of successive words must alternate".
    -   Maybe the example output in the problem description is just "Shortest transformation sequences" and the text "Additionally..." is a constraint I added but the example doesn't follow?
    -   **CRITICAL**: The problem statement provided in the prompt says: "Additionally, the first letter of successive words must alternate...".
    -   If the example violates this, then the example is wrong OR my definition of Vowel/Consonant is wrong (unlikely) OR "alternate" means something else.
    -   Let's look at the example explanation: "Both sequences have length 3 and alternate vowel-start/consonant-start at each step."
    -   This implies the author of the problem *thinks* `eat` -> `cat` -> `cot` alternates.
    -   `eat` (V). `cat` (C). `cot` (C).
    -   Maybe `c` is a vowel? No.
    -   Maybe `y` is a vowel? No 'y' here.
    -   Maybe the rule is "alternate OR ..."? No.
    -   **Hypothesis**: The example in the problem file is inconsistent with the constraint text.
    -   **Action**: I must point out the logic. If I strictly follow the constraint, `eat -> cat -> cot` is invalid.
    -   However, I must match the provided problem file.
    -   Let's check if `eot` is a typo for `dot`? `eat` -> `dat` -> `dot`? No.
    -   Let's assume the constraint is the source of truth for the code I write. The example might be legacy.
    -   **BUT**, if I write code that returns `NONE` for the example input, the user might think it's broken.
    -   Let's look at `eat` -> `eot`. `e` -> `e`. V -> V.
    -   Maybe "alternate" means "change"? No, "alternate between vowel and consonant".
    -   Okay, I will write the solution that **strictly follows the text constraint**. If the example output in the problem description is physically impossible under the rules, I will note this in the "Common Mistakes" or "Problem Exploration" section, or just ignore the discrepancy and provide the correct code for the text.
    -   `eat` -> `cat` (V -> C). OK.
    -   `cat` -> `cot` (C -> C). Bad.
    -   `eat` -> `eot` (V -> V). Bad.
    -   `eot` -> `cot` (V -> C). OK.
    -   Maybe the rule is "The *changed letter* must alternate"? No, "first letter of successive words".
    -   I will implement the code to strictly follow the rule. If the example output is wrong, the code will output `NONE` or whatever valid paths exist. (In this case `NONE`).
    -   **Wait**, is it possible `eat` -> `cot` is just 1 step? `e`->`c`, `a`->`o`. No, 2 diffs.
    -   I'll stick to the text. The text is the specification.

## Proof of Correctness

The algorithm uses BFS, which guarantees finding the shortest path in an unweighted graph. By storing all parents that lead to a node with the same optimal distance, and then backtracking, we recover all shortest paths. The "alternating" constraint is enforced during neighbor generation/validation, ensuring all edges in the graph are valid.

## Interview Extensions

1.  **Bidirectional BFS**: Start from both `start` and `end` to meet in the middle. Reduces search space significantly.
2.  **Wildcard Preprocessing**: Map `*at` -> `[bat, cat, rat]`. Speeds up neighbor finding.

### Common Mistakes

-   **Graph Construction**: Forgetting that the graph is directed if the constraint is asymmetric (though V<->C is symmetric).
-   **BFS Level Processing**: Not handling multiple parents correctly. A node can be reached by multiple nodes in the previous level.
-   **Constraint Checking**: Misidentifying vowels or checking the wrong character index.
