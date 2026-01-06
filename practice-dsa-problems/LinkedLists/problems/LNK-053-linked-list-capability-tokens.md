---
problem_id: LNK_LINKED_LIST_CAPABILITY_TOKENS__6893
display_id: NTB-LNK-6893
slug: linked-list-capability-tokens
title: "Linked List with Capability Tokens"
difficulty: Medium
difficulty_score: 50
topics:
  - Linked Lists
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - linked-list-capability-tokens
  - linkedlists
  - memory-management
  - pointers
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Linked List with Capability Tokens

## Problem Statement

Operations on the list require capability tokens. Each token grants access to a range of positions `[l, r]` and expires at time `t_expire`.

Operations:

- `INS token pos x t`
- `DEL token pos t`
- `GET pos t`

An operation is valid only if `t <= t_expire` and `pos` lies in the token's range. Invalid operations are ignored.

## Input Format

- First line: integer `n`
- Second line: `n` integers: initial list values
- Third line: integer `k` (tokens)
- Next `k` lines: `token_id l r t_expire`
- Next line: integer `q`
- Next `q` lines: operations

## Output Format

- For each `GET`, output value or `-1`

## Constraints

- `1 <= n, q <= 200000`
- Token ids are unique
- Timestamps are non-decreasing

## Clarifying Notes

- `GET` does not require a token.

## Example Input

```
3
1 2 3
1
5 1 2 10
3
INS 5 2 9 1
GET 2 1
DEL 5 3 2
```

## Example Output

```
9
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    static class Token {
        int id, l, r;
        long tExpire;
        Token(int id, int l, int r, long tExpire) {
            this.id = id;
            this.l = l;
            this.r = r;
            this.tExpire = tExpire;
        }
    }

    public List<Integer> processCapabilityTokens(int n, int[] initialList, List<Token> tokens, String[] operations) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Token:
    def __init__(self, id, l, r, t_expire):
        self.id = id
        self.l = l
        self.r = r
        self.t_expire = t_expire

class Solution:
    def processCapabilityTokens(self, n: int, initial_list: list[int], tokens: list[Token], operations: list[str]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <string>

using namespace std;

struct Token {
    int id, l, r;
    long long tExpire;
};

class Solution {
public:
    vector<int> processCapabilityTokens(int n, vector<int>& initialList, vector<Token>& tokens, vector<string>& operations) {
        // Your code here
        return {};
    }
};
```

```javascript
class Token {
  constructor(id, l, r, tExpire) {
    this.id = id;
    this.l = l;
    this.r = r;
    this.tExpire = tExpire;
  }
}

class Solution {
  /**
   * @param {number} n
   * @param {number[]} initialList
   * @param {Token[]} tokens
   * @param {string[]} operations
   * @returns {number[]}
   */
  processCapabilityTokens(n, initialList, tokens, operations) {
    // Your code here
    return [];
  }
}
```
