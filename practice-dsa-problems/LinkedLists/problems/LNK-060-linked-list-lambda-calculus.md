---
problem_id: LNK_LINKED_LIST_LAMBDA_CALCULUS__1753
display_id: NTB-LNK-1753
slug: linked-list-lambda-calculus
title: "Linked List as Lambda Calculus"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-lambda-calculus
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List as Lambda Calculus

## Problem Statement

A lambda term is encoded as a list of tokens using:

- `Lx` for lambda `\x`
- `.` for separator
- variable names as single lowercase letters
- `(` and `)` for grouping

You must perform **exactly** `K` beta-reduction steps or stop earlier if no redex remains. Output the resulting token list.

Beta-reduction rule:

```
( Lx . body ) arg  => body with free x replaced by arg
```

## Input Format

- First line: integer `K`
- Second line: list of tokens separated by spaces

## Output Format

- One line: resulting tokens separated by spaces

## Constraints

- Number of tokens <= 200
- `0 <= K <= 100`

## Clarifying Notes

- Always reduce the leftmost-outermost redex.
- Variables are single lowercase letters.

## Example Input

```
1
( Lx . x ) y
```

## Example Output

```
y
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<String> processLambda(int K, String[] tokens) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def processLambda(self, K: int, tokens: list[str]) -> list[str]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> processLambda(int K, vector<string>& tokens) {
        // Your code here
        return {};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} K
   * @param {string[]} tokens
   * @returns {string[]}
   */
  processLambda(K, tokens) {
    // Your code here
    return [];
  }
}
```
